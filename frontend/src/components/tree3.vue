<template>
    <div>
        <div class="des">
            <a-form>
                <a-form-item label="描述">
                    <a-textarea v-model:value="description"
                    placeholder="description" 
                    :auto-size="{ minRows: 2, maxRows: 5 }" 
                    style="width: 400px;"/>
                </a-form-item>
            </a-form>
        </div>

        <a-button type="primary" @click="addComp" v-if="!treeData.length">添加根节点</a-button>
        <a-tree v-if="treeData && treeData.length > 0" :autoExpandParent="true" :tree-data="treeData"
            :defaultExpandAll="true" showLine blockNode>
            
            <template v-slot:title="nodeData">
                <div style="display: flex; flex-direction : row; justify-content: space-between;">
                    <treeTitle :msg="nodeData.type" :expression="nodeData.expression"></treeTitle>
                
                    <div style="padding-left: 40px;">
                        <a-button-group style="float:right">
                            <a-button size="small" @click="addComp(nodeData)" title="添加下级">
                                <plus-square-outlined />
                            </a-button>
                            <a-button size="small" @click="slotModify(nodeData)" title="修改">
                                <form-outlined />
                            </a-button>
                            <a-popconfirm title="确定删除该节点吗？" ok-text="确定" cancel-text="取消" @confirm="confirmDel">
                                <a-button size="small" @click="slotDelete(nodeData)" title="删除">
                                    <delete-outlined />
                                </a-button>
                            </a-popconfirm>
                        </a-button-group>
                    </div>
                    
                </div>
            </template>
        </a-tree>

        <a-modal v-model:visible="visible" :title="isUpdate ? '修改节点' : '新建节点'" @ok="handleOk"
        cancelText="取消" okText="确定" >
            <div v-if="isUpdate === false" class = "drawer-right">
                <div style="display: flex; flex-direction: row;">
                    <a-textarea v-model:value="value_exp"
                    placeholder="Input"
                    auto-size />

                    <div style="padding-left: 15px;">
                        <a-button @click="exp_to_obj"> 应用 </a-button>
                    </div>
                </div>

                <div style="padding-top: 20px; font-size: 18px; font-weight: 300;">
                    <span> 类型: </span>
                    <div style="padding-top: 15px;">
                        <a-radio-group v-model:value="value_type" button-style="solid"
                        style="font-weight: 400;">
                            <div>
                                <a-radio-button value="=>"> => </a-radio-button>
                                <a-radio-button value="<=>"> {{ "<=>" }} </a-radio-button>
                                <a-radio-button value="OR"> OR </a-radio-button>
                                <a-radio-button value="AND"> AND </a-radio-button>
                                <a-radio-button value="="> = </a-radio-button>
                                <a-radio-button value="!="> != </a-radio-button>
                                <a-radio-button value="not"> {{ "not" }} </a-radio-button>
                            </div>

                            <div>
                                <a-radio-button value=">="> >= </a-radio-button>
                                <a-radio-button value="<="> {{ "<=" }} </a-radio-button>
                                <a-radio-button value=">"> > </a-radio-button>
                                <a-radio-button value="<"> {{ "<" }} </a-radio-button>
                                <a-radio-button value="opt"> option </a-radio-button>
                                <a-radio-button value="const"> const </a-radio-button>
                            </div>
                            
                        </a-radio-group>    
                    </div>
                </div>
                
                <div v-if="value_type === '>=' || value_type === '<=' || value_type === '>' || value_type === '<'">
                    <div style="padding-top: 20px; font-size: 18px; font-weight: 300;">
                        <span> Node 1: </span>
                    </div>

                    <div style="padding-top: 20px; font-size: 18px; font-weight: 300;">
                        <div style="display: flex; flex-direction: row;">
                            <a-select
                                show-search
                                v-model:value="select_value_left"
                                :options = "select_options"
                                placeholder="Select a Option"
                                style="width: 200px" >
                            </a-select>
                            <div style="padding-left: 15px;">
                                <a-button @click="handleChange_left"> 应用 </a-button>
                            </div>
                        </div>
                    </div>

                    <a-list style="padding-top: 10px;">
                        <a-list-item>
                            <a-list-item-meta
                                :description = left_opt.description>
                                <template #title>
                                    {{ left_opt.name + " ( " + left_opt.type + " ) " }}
                                </template>

                                <template #avatar>
                                    <a-avatar v-if="left_opt.type === 'Boolean'" class="boolean-avatar">01</a-avatar>
                                    <a-avatar v-else-if="left_opt.type === 'Integer'" class="integer-avatar">Z</a-avatar>
                                    <a-avatar v-else-if="left_opt.type === 'Float'" class="float-avatar">R</a-avatar>
                                    <a-avatar v-else-if="left_opt.type === 'Category'" class="category-avatar">C</a-avatar>
                                    <a-avatar v-else> ~ </a-avatar>
                                </template>
                            </a-list-item-meta>
                            
                            <div v-if="left_opt.possible.length === 1">
                                <a-tag v-for="it in left_opt.possible">
                                    {{ it }}
                                </a-tag>
                            </div>
                            <div v-if="left_opt.possible.length > 1">
                                <a-tag> ... </a-tag>
                            </div>
                            
                        </a-list-item>
                    </a-list>

                    <div style="padding-top: 10px; font-size: 18px; font-weight: 300;">
                        <span> Node 2: </span>
                    </div>

                    <div style="padding-top: 20px; width: 50%;">
                        <a-input v-model:value = "const_input"></a-input>
                    </div>

                    <!-- <div style="padding-top: 20px; font-size: 18px; font-weight: 300;">
                        <div style="display: flex; flex-direction: row;">
                            <a-select
                                show-search
                                v-model:value="select_value_right"
                                :options = "select_options"
                                placeholder="Select a Option"
                                style="width: 200px" >
                            </a-select>
                            <div style="padding-left: 15px;">
                                <a-button @click="handleChange_right"> 应用 </a-button>
                            </div>
                        </div>
                    </div> -->

                    <!-- <a-list style="padding-top: 10px;">
                        <a-list-item>
                            <a-list-item-meta
                                :description = right_opt.description>
                                <template #title>
                                    {{ right_opt.name + " ( " + right_opt.type + " ) " }}
                                </template>

                                <template #avatar>
                                    <a-avatar v-if="right_opt.type === 'Boolean'" class="boolean-avatar">01</a-avatar>
                                    <a-avatar v-else-if="right_opt.type === 'Integer'" class="integer-avatar">Z</a-avatar>
                                    <a-avatar v-else-if="right_opt.type === 'Float'" class="float-avatar">R</a-avatar>
                                    <a-avatar v-else-if="right_opt.type === 'Category'" class="category-avatar">C</a-avatar>
                                    <a-avatar v-else> ~ </a-avatar>
                                </template>
                            </a-list-item-meta>
                            
                            <div v-if="right_opt.possible.length === 1">
                                <a-tag v-for="it in right_opt.possible">
                                    {{ it }}
                                </a-tag>
                            </div>
                            <div v-if="right_opt.possible.length > 1">
                                <a-tag> ... </a-tag>
                            </div>
                            
                        </a-list-item>
                    </a-list> -->
                </div>
                
                <div v-else-if="value_type === 'opt'" >
                    <div style="padding-top: 20px; font-size: 18px; font-weight: 300;">
                        <div style="display: flex; flex-direction: row;">
                            <a-select
                                show-search
                                v-model:value="select_value_left"
                                :options = "select_options"
                                placeholder="Select a Option"
                                style="width: 200px" >
                            </a-select>
                            <div style="padding-left: 15px;">
                                <a-button @click="handleChange_left"> 应用 </a-button>
                            </div>
                        </div>
                    </div>

                    <a-list style="padding-top: 10px;">
                        <a-list-item>
                            <a-list-item-meta
                                :description = left_opt.description>
                                <template #title>
                                    {{ left_opt.name + " ( " + left_opt.type + " ) " }}
                                </template>

                                <template #avatar>
                                    <a-avatar v-if="left_opt.type === 'Boolean'" class="boolean-avatar">01</a-avatar>
                                    <a-avatar v-else-if="left_opt.type === 'Integer'" class="integer-avatar">Z</a-avatar>
                                    <a-avatar v-else-if="left_opt.type === 'Float'" class="float-avatar">R</a-avatar>
                                    <a-avatar v-else-if="left_opt.type === 'Category'" class="category-avatar">C</a-avatar>
                                    <a-avatar v-else> ~ </a-avatar>
                                </template>
                            </a-list-item-meta>
                            
                            <div v-if="left_opt.possible.length === 1">
                                <a-tag v-for="it in left_opt.possible">
                                    {{ it }}
                                </a-tag>
                            </div>
                            <div v-if="left_opt.possible.length > 1">
                                <a-tag> ... </a-tag>
                            </div>
                            
                        </a-list-item>
                    </a-list>
                </div>

                <div v-else-if="value_type === 'const'">
                    <div style="padding-top: 20px; width: 50%;">
                        <a-input v-model:value = "const_input"></a-input>
                    </div>
                    
                </div>

                <!-- <div style="padding-top: 20px; font-size: 18px; font-weight: 300;">
                    <a-button> 确定 </a-button>
                </div> -->
            </div>

            <div v-else class = "drawer-right">
                <div style="display: flex; flex-direction: row;">
                    <a-textarea v-model:value="value_exp"
                    placeholder="Input"
                    auto-size />

                    <div style="padding-left: 15px;">
                        <a-button @click="exp_to_obj"> 应用 </a-button>
                    </div>
                </div>

                <div style="padding-top: 20px; font-size: 18px; font-weight: 300;">
                    <span> 类型: </span>
                    <div style="padding-top: 15px;">
                        <a-radio-group v-model:value="value_type" button-style="solid"
                        style="font-weight: 400;">
                            <div>
                                <a-radio-button v-if="value_type === '=>' || value_type === '<=>'" value="=>"> => </a-radio-button>
                                <a-radio-button v-if="value_type === '=>' || value_type === '<=>'" value="<=>"> {{ "<=>" }} </a-radio-button>

                                <a-radio-button v-if="value_type === 'OR' || value_type === 'AND'" value="OR"> OR </a-radio-button>
                                <a-radio-button v-if="value_type === 'OR' || value_type === 'AND'" value="AND"> AND </a-radio-button>
                                
                                <a-radio-button v-if="value_type === '=' || value_type === '!='" value="="> = </a-radio-button>
                                <a-radio-button v-if="value_type === '=' || value_type === '!='" value="!="> != </a-radio-button>
                                
                                <a-radio-button v-if="value_type === '>=' || value_type === '<=' || value_type === '>' || value_type === '<'" value=">="> >= </a-radio-button>
                                <a-radio-button v-if="value_type === '>=' || value_type === '<=' || value_type === '>' || value_type === '<'" value="<="> {{ "<=" }} </a-radio-button>
                                <a-radio-button v-if="value_type === '>=' || value_type === '<=' || value_type === '>' || value_type === '<'" value=">"> > </a-radio-button>
                                <a-radio-button v-if="value_type === '>=' || value_type === '<=' || value_type === '>' || value_type === '<'" value="<"> {{ "<" }} </a-radio-button>
                                
                                <a-radio-button v-if="value_type === 'opt' || value_type === 'const' || value_type === 'final'" value="opt"> option </a-radio-button>
                                <a-radio-button v-if="value_type === 'opt' || value_type === 'const' || value_type === 'final'" value="const"> const </a-radio-button>
                            </div>
                        </a-radio-group>
                    </div>
                </div>
            </div>
        </a-modal>
        <a-button class="get-btn" type="primary" @click="getTreeData" v-if="treeData.length">获取树的值</a-button>
    </div>
</template>

<script>
import { PlusSquareOutlined, FormOutlined, DeleteOutlined } from '@ant-design/icons-vue';
import { notification } from 'ant-design-vue';
import { ref, onMounted, onCreated, toRaw } from 'vue'
import treeTitle from "@/components/tree-title.vue"
import { message } from 'ant-design-vue'
import { get_object } from "@/utils/api"

export default {
    name: 'Tree3',
    components: {
        PlusSquareOutlined, FormOutlined, DeleteOutlined,
        notification, ref, onMounted, onCreated, toRaw,

        treeTitle,

        message,
    },
    data() {
        return {
            description: "",
            origin_item: undefined,
            isEdit: false,

            treeData: ref([]),

            parentNode: ref({}),
            visible: ref(false),
            compName: ref(''),
            isUpdate: ref(false),

            value_type: undefined,
            value_exp: "",
            left_opt: {
                name: "Unknown",
                type: "Unknown",
                description: "Unknown .",
                possible: ["Unknown"],
            },
            // right_opt: {
            //     name: "Unknown",
            //     type: "Unknown",
            //     description: "Unknown .",
            //     possible: ["Unknown"],
            // },

            options : [],
            select_options : [],
            options_map: {},
            select_value_left: undefined,
            // select_value_right: undefined,
            const_input: "",
        };
    },
    mounted() {
        // Your mounted logic here
        this.isEdit = false
        this.Reset_New_Con()
    },
    created() {
        // 在组件创建时加载数据
        this.loadDataFromSessionStorage()
    },
    methods: {
        set_tree_value(item) {
            this.isEdit = false
            const item_str = JSON.stringify(item)
            this.Reset_New_Con()
            this.description = item.description
            this.treeData.push(JSON.parse(item_str))

            // /JSON.stringify和JSON.parse
            this.isEdit = true
            this.origin_item = JSON.stringify(item)
        },

        Reset_New_Con() {
            // console.log("Reset_New_Con")
            // console.log(this.isEdit)
            // this.treeData = JSON.parse(JSON.stringify([]))
            this.treeData = ref([])
            // console.log(this.treeData.length)
            // console.log(this.treeData)
            this.parentNode = JSON.parse(JSON.stringify({}))
            this.compName = ref('')
            this.isUpdate = ref(false)

            this.value_type = undefined
            this.value_exp = ""
            this.left_opt = {
                name: "Unknown",
                type: "Unknown",
                description: "Unknown .",
                possible: ["Unknown"],
            }

            this.select_value_left = undefined
            this.const_input = ""
            this.description = ""

            if(this.isEdit) {
                this.description = JSON.parse(this.origin_item).description
                this.treeData.push(JSON.parse(this.origin_item))
            }
            else {
                this.origin_item = undefined
            }
        },

        reset() {
            this.select_value_left = undefined
            // this.select_value_right = undefined
            this.const_input = ""
            this.left_opt = {
                name: "Unknown",
                type: "Unknown",
                description: "Unknown .",
                possible: ["Unknown"],
            }
            // this.right_opt = {
            //     name: "Unknown",
            //     type: "Unknown",
            //     description: "Unknown .",
            //     possible: ["Unknown"],
            // }
            this.value_type = undefined
            this.value_exp = ""
        },

        loadDataFromSessionStorage() {
            const storedData = sessionStorage.getItem("option_list_data")
            if (storedData) {
                this.options = JSON.parse(storedData)
                for (let i = 0; i < this.options.length; i ++) {
                    this.select_options.push({
                        value: this.options[i].name,
                        label: this.options[i].name
                    })
                    this.options_map[this.options[i].name] = this.options[i]
                }
            }

        },

        handleChange_left() {
            if(this.value_type === "<=" || this.value_type === ">="
            || this.value_type === "<" || this.value_type === ">") {
                if (this.options_map[this.select_value_left].type !== "Integer") {
                    message.error('只能选择 Integer 类型')
                    return
                }
            }
            this.left_opt = this.options_map[this.select_value_left]
        },
        // handleChange_right() {
        //     if(this.value_type === "<=" || this.value_type === ">="
        //     || this.value_type === "<" || this.value_type === ">") {
        //         if (this.options_map[this.select_value_right].type !== "Integer") {
        //             message.error('只能选择 Integer 类型')
        //             return
        //         }
        //     }

        //     this.right_opt = this.options_map[this.select_value_right]
        // },

        showModal() {
            this.visible = true;
        },

        exp_to_obj() {
            console.log(this.value_exp)
            if(this.value_exp === "") {
                message.error("不能添加空表达式")
                return 
            }
            get_object({
                expression : this.value_exp
            }).then((response) => {
                let ret = response.data
                
                const new_node = ret.obj
                // console.log("des: ")
                // console.log(this.description)
                if(this.description !== undefined && this.description.length !== "")
                    new_node.description = this.description
                console.log(new_node)

                if(this.isUpdate) {
                    if (!this.parentNode.expression) {
                        const tmp_isedit = this.isEdit
                        this.isEdit = false
                        this.Reset_New_Con()
                        this.isEdit = tmp_isedit

                        this.treeData.push(new_node)
                    }
                    else
                        Object.assign(this.parentNode.dataRef, new_node)
                }
                
                else {
                    if (!this.parentNode.expression)
                        this.treeData.push(new_node)
                    else
                        this.parentNode.children.push(new_node)
                }
                

                this.reset()
                this.visible = false
            
            }).catch(error => {
                // console.error(error)
                message.error("表达式非法")
            });
        },

        handleOk() {
            console.log(this.parentNode.expression)

            if (this.value_type === undefined) {
                message.error('请选择类型')
                return
            }
            if (this.isUpdate) {
                Object.assign(this.parentNode.dataRef, {
                    // expression: this.compName
                    expression : this.value_type,
                    type : this.value_type
                });
            }

            else {
                let exp = this.value_type
                let children = []

                if (this.value_type === "opt") {
                    // console.log(this.left_opt.type)
                    if(this.left_opt.type === "Unknown") {
                        message.error('请选择一个选项')
                        return
                    }
                    exp = this.select_value_left
                }
                else if(this.value_type === "const") {
                    if(this.const_input === "") {
                        message.error('请输入')
                        return
                    }
                    exp = this.const_input
                }
                else if( this.value_type === ">=" || this.value_type === "<="
                || this.value_type === ">" || this.value_type === "<") {
                    exp = this.select_value_left + " " + this.value_type + " " + this.const_input
                    
                    if(this.left_opt.type === "Unknown") {
                        message.error('请选择 Node 1')
                        return
                    }
                    // if(this.right_opt.type === "Unknown") {
                    //     message.error('请选择 Node 2')
                    //     return
                    // }
                    if(this.const_input === "") {
                        message.error('请输入 Node 2')
                        return
                    }
                    let isNum = true
                    for (let i = 0; i < this.const_input.length; i ++)
                        if(this.const_input[i] < '0' || this.const_input[i] > '9') {
                            isNum = false
                            break
                        }
                    if(isNum === false) {
                        message.error('Node 2只能为数字')
                        return
                    }

                    let left_son = {
                        expression: this.select_value_left,
                        type: "opt",
                        children: [],
                        key: Math.random() 
                    }

                    let right_son = {
                        expression: this.const_input,
                        type: "const",
                        children: [],
                        key: Math.random() 
                    }
                    
                    children = [ left_son, right_son ]
                }

                if (!this.parentNode.expression) {
                    this.treeData.push({ 
                        expression: exp,
                        type: this.value_type,
                        children: children, 
                        key: 0 
                    });
                }
                else {

                    let parType = this.parentNode.type
                    if (parType === "=>" || parType === "<=>" 
                    || parType === "OR" || parType === "AND" 
                    || parType === "not") {

                        if( (this.value_type === "opt")
                        && (this.left_opt.type != "Boolean")) {
                            console.log(this.left_opt.type === "opt")
                            message.error('只能添加 Boolean 类的子节点')
                            return
                        }

                        if( (this.left_opt.type === "const")
                        && (this.left_opt.exp != "True") && (this.left_opt.exp != "False")) {
                            message.error('只能添加 Boolean 类的子节点')
                            return
                        }
                    }

                    this.parentNode.children.push({
                        expression: exp, 
                        type: this.value_type,
                        children: children, 
                        key: Math.random() 
                    });
                }
            }
            this.reset()
            this.visible = false
        },
        addComp(nodeData) {

            if(this.treeData.length) {
                if ( nodeData.type === "not" && nodeData.children.length === 1 ) {
                    message.error('子节点数量已达到上限')
                    return
                }
                if (nodeData.children.length === 2) {
                    if( nodeData.type === "=>" || nodeData.type === "<=>"
                    || nodeData.type === "==" || nodeData.type === "!="
                    || nodeData.type === ">=" || nodeData.type === "<=" 
                    || nodeData.type === ">" || nodeData.type === "<" ) {
                        message.error('子节点数量已达到上限')
                        return
                    }
                }
                if ( nodeData.type === "opt" || nodeData.type === "const" ) {
                    message.error('子节点数量已达到上限')
                    return
                }
            }

            this.isUpdate = false
            this.compName = ''
            this.parentNode = nodeData
            this.showModal()
        },
        slotModify(nodeData) {
            this.isUpdate = true
            this.parentNode = nodeData
            this.compName = nodeData.dataRef.name
            this.showModal()

            this.value_type = nodeData.type
            // console.log(this.value_type)
            // this.value_exp = nodeData.expression

            // this.value_type = undefined
            // this.value_exp = ""
            // this.left_opt = {
            //     name: "Unknown",
            //     type: "Unknown",
            //     description: "Unknown .",
            //     possible: ["Unknown"],
            // }

            // this.select_value_left = undefined
            // this.const_input = ""
        },
        slotDelete(nodeData) {
            this.parentNode = nodeData
        },
        confirmDel() {
            console.log(this.parentNode.expression)
            Object.assign(this.parentNode.dataRef, null)
            this.searchOption(this.parentNode.dataRef, this.treeData)
        },
        searchOption(option, arr, obj = {}) {
            for (let s = 0; s < arr.length; s++) {
                if (arr[s].key === option.key) {
                    arr.splice(s, 1);
                    break;
                } 
                else if (arr[s].children && arr[s].children.length > 0) {
                    this.searchOption(option, arr[s].children, obj);
                } 
                else {
                    continue;
                }
            }
        },
        openNotification(msg) {
            notification.open({
                message: 'tree value',
                description: msg,
                onClick: () => {
                    console.log('Notification Clicked!');
                },
                duration: 3,
            });
        },
        getTreeData() {
            let details = toRaw(this.treeData);
            console.log(details);
            this.openNotification(JSON.stringify(details));
        },

        add_con() {
            if(! this.treeData.length) {
                message.error('不能添加空指令')
                return
            }

            let args = []
            args.push(this.treeData[0])
            args.push(this.description)
            this.$emit('notify_conList_add', args)

            this.isEdit = false
            this.Reset_New_Con()
            // console.log(this.treeData[0])
        },

        edit_con() {
            if(! this.treeData.length) {
                message.error('不能修改为空指令')
                return
            }

            let args = []
            // console.log(JSON.parse(this.origin_item))
            args.push(JSON.parse(this.origin_item))
            console.log(this.treeData[0].expression)
            args.push(this.treeData[0])
            
            args.push(this.description)
            this.$emit('notify_conList_edit', args)

            this.isEdit = false
            this.Reset_New_Con()
        },
    },
};

</script>

<style scoped>
.des {
    display: flex;
    flex-direction: row;
    padding-bottom: 30px;
    /* width: 500px;
    background-color: black; */
}
header {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    font-weight: 600;
}
main {
    margin: 100px 400px;
}
.get-btn {
    margin-top: 50px;
}
</style>