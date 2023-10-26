<template>
    <div class="main">
        <!-- <h1>Meow Meow !</h1> -->
    </div>
    <div class="content">
        <Menu></Menu>
        <div class="right-content">
            <div class="right">
                <a-steps :current="state - 1">
                    <a-step>
                        <!-- <span slot="title">Finished</span> -->
                        <template #title>设置选项</template>
                        <template #description>
                            <span>This is a description.</span>
                        </template>
                    </a-step>
                    <!-- <a-step title="Set Constraints" sub-title="Left 00:00:08" description="This is a description." /> -->
                    <a-step title="设置约束关系" description="Set Constraints" />
                    <a-step title="开始生成" description="Start Generation" />
                    <a-step title="查看结果" description="Result" />
                </a-steps>

                <div class="bread">
                    <a-breadcrumb>
                        <!-- <a-breadcrumb-item>Step 1</a-breadcrumb-item>
                        <a-breadcrumb-item>Step 2</a-breadcrumb-item>
                        <a-breadcrumb-item>Step 3</a-breadcrumb-item>
                        <a-breadcrumb-item>Step 4</a-breadcrumb-item> -->
                        <a-breadcrumb-item v-for="index in state" @click="setState(index)">
                            {{ "Step " + index }}
                        </a-breadcrumb-item>
                    </a-breadcrumb>
                    
                    <div style="padding-left: 20px;">
                        <a-button type="link" :disabled="state === 1" @click="LastState">
                            <StepBackwardOutlined />
                            上一步
                        </a-button>
                    </div>

                    <div>
                        <a-button type="link" :disabled="state === 4" @click="NextState">
                            <StepForwardOutlined />
                            下一步
                        </a-button>
                    </div>
                </div>

                <div v-if="state === 1" class="down-content">
                    <div class="buttons">
                        <a-button @click="clean_opt">
                            <DeleteOutlined />
                            重置
                        </a-button>
                        <div style="padding-left: 20px;">
                            <a-upload
                            v-model:file="file"
                            name="file"
                            :multiple="false"
                            action="http://124.71.183.200:5000/api/uploader_get_json"
                            
                            :on-success="upload_back"
                            @change="handleChangeFile" >
                                <a-button>
                                    <upload-outlined></upload-outlined>
                                    上传文件
                                </a-button>
                            </a-upload>
                        </div>
                        <div style="padding-left: 20px;">
                            <a-button @click="add_option">
                                <PlusOutlined />
                                添加选项
                            </a-button>
                        </div>
                    </div>
                    
                    <div class="down">
                        <div class="down-left">
                            <OptionList ref="childComponent"
                            @notifyChild2 = "callFunctionInChild2" 
                            @addOption = "addOption">
                            </OptionList>
                        </div>
                        <div class="down-right">
                            <OptionCard ref="child2"
                            @deleteOpt = "delete_option"
                            @editOpt = "edit_option"
                            ></OptionCard>
                        </div>
                    </div>
                    
                </div>

                <div v-if="state === 2" class="down-content">
                    <div class="buttons">
                        <a-button @click="clean_conList">
                            <DeleteOutlined />
                            重置
                        </a-button>
                        <div style="padding-left: 20px;">
                            <a-button @click="Download_Model">
                                <!-- <upload-outlined></upload-outlined>
                                上传文件 -->
                                <DownloadOutlined />
                                下载模型
                            </a-button>
                        </div>
                        <div style="padding-left: 20px;">
                            <a-button @click="add_constraint">
                                <PlusOutlined />
                                添加约束
                            </a-button>
                        </div>
                    </div>

                    <div class="buttons" style="align-items: center;">
                        <a-checkbox v-model:checked="screen" @change="change_screen">
                            筛选
                        </a-checkbox>
                        
                        <div style="padding-left: 20px;">
                            <a-select
                                show-search
                                v-model:value="screen_new"
                                :options = "select_options"
                                placeholder="选择已有选项"
                                style="width: 150px" >
                            </a-select>
                        </div>
                        
                        <div style="padding-left: 20px;">
                            <a-button :disabled = "screen_new === undefined"
                                @click="add_screen">
                                <PlusOutlined />
                                添加
                            </a-button>
                        </div>
                    </div>
                    
                    <div class="buttons">
                        <div v-for="(tag, index) in screen_list" :key="tag">
                            <a-tag closable 
                                @close="closeTag(tag)">
                                {{ tag }}
                            </a-tag>
                        </div>
                        
                    </div>

                    <div class="down">
                        <div>
                            <!-- <ConstraintList ref="conList"
                            @notifyConCard="callFunctionInConCard">
                            </ConstraintList> -->

                            <ConstraintList2 ref="conList"
                            @notifyConCard = "callFunctionInConCard">
                            </ConstraintList2>
                        </div>

                        <div class="conCard">

                            <!-- <ConstraintCard ref="conCard"
                            @deleteCon="delete_constraint"></ConstraintCard> -->
                            
                            <ConstraintCard2 ref="conCard"
                            @deleteCon="delete_constraint"
                            @editCon="edit_constraint"></ConstraintCard2>
                        </div>
                        <!-- <div>
                            <tmpCard></tmpCard>
                        </div> -->
                    </div>
                </div>

                <!-- 算法设置 -->
                <div v-if="state === 3" style="padding-top: 100px">
                    <div style="display: flex; flex-direction: column;">
                        <div v-if="loading" style="padding-bottom: 30px;">
                            <a-spin size="large" />
                        </div>
                        <div>
                            <a-button type="primary" size="large" @click="get_testcases">Start</a-button>
                        </div>
                    </div>
                </div>

                <!-- 结果展示 -->
                <div v-if="state === 4" class="down-content">
                    <div class="buttons">
                        <a-button @click="clean_tc">
                            <DeleteOutlined />
                            重置
                        </a-button>
                        <div style="padding-left: 20px;">
                            <a-button @click="download_tc">
                                <DownloadOutlined />
                                下载
                            </a-button>
                        </div>
                    </div>
                    
                    <div class="down">
                        <!-- <div>
                            <TestcaseList ref="tcList"
                            @notifyTcCard="callFunctionInTcCard"></TestcaseList>
                        </div>
                        <div style="width: 500px; padding-left: 50px;">
                            <TestcaseCard ref="tcCard"></TestcaseCard>
                        </div> -->

                        <TestcaseList2 ref="tcList"></TestcaseList2>
                    </div>
                </div>

                <div v-if="state === 0" style="padding-top: 50px">
                    <a-empty />
                </div>
                
            </div>
        </div>
    </div>
    
    <a-modal v-model:open="visible" title="添加选项" @ok="handleOk"
    cancelText="取消" okText="确定">
        <!-- <p>Some contents...</p>
        <p>Some contents...</p>
        <p>Some contents...</p> -->
        <a-form style="padding: 30px">
            
            <a-form-item label="名称">
                <a-input v-model:value="formState.name" />
            </a-form-item>

            <a-form-item label="类型">
                <a-select v-model:value="formState.type" placeholder="请选择选项类型">
                    <a-select-option value="Boolean"> Boolean </a-select-option>
                    <a-select-option value="Integer"> Integer </a-select-option>
                    <!-- <a-select-option value="Float"> Float </a-select-option> -->
                    <a-select-option value="Category"> Category </a-select-option>
                </a-select>
            </a-form-item>

            <a-form-item label="描述">
                <a-textarea v-model:value="formState.description"
                    placeholder=""
                    :auto-size="{ minRows: 2, maxRows: 5 }" />
            </a-form-item>
            
            <!-- Category -->
            <a-form-item v-if="formState.type === 'Category'" label="值域">
                <div class="category-add">
                    <a-input v-model:value="new_possible" />
                    <div style="padding-left: 10px;">
                        <a-button @click="add_possible">
                            <PlusOutlined />
                            添加
                        </a-button>
                    </div>
                </div>
            </a-form-item>
            <a-form-item v-if="formState.type === 'Category'">
                <div style="display: flex; flex-wrap: wrap;">
                    <div v-for="it in formState.possible" :key="it">
                        <a-tag closable @close=close_value_Tag(it) >
                            {{ it }}
                        </a-tag>
                    </div>
                </div>
            </a-form-item>

            <!-- Integer -->
            <a-form-item v-if="formState.type === 'Integer'">
                <div class="integer-float-value">
                    <div>最小值: </div>
                    <a-input-number id="inputNumber" v-model:value="formState.min_value" :min="-10000" :max="10000" />
                    <div>最大值: </div>
                    <a-input-number id="inputNumber" v-model:value="formState.max_value" :min="-10000" :max="10000" />
                </div>
            </a-form-item>

            <!-- Float -->
            <!-- <a-form-item v-if="formState.type === 'Float'">
                <div class="integer-float-value">
                    <div>Minimum Value: </div>
                    <a-input-number id="inputNumber" v-model:value="formState.min_value" :min="-10" :max="10" :step="0.01"/>
                    <div>Maximum Value: </div>
                    <a-input-number id="inputNumber" v-model:value="formState.max_value" :min="-10" :max="10" :step="0.01"/>
                </div>
            </a-form-item> -->
        </a-form>
    </a-modal>

    <a-drawer :title="isUpdate === true ? '修改约束' : '添加约束'" width="500px"
    placement="right" :closable="false" :destroyOnClose="true" @close="close_drawer"
    v-model:open="visible_con" :after-visible-change="afterVisibleChange" >
        <div class = "drawer">
            <div class = "drawer-left">
                <div style="display: flex; flex-direction: row;">
                    <a-popconfirm title="确定重置吗？" ok-text="确定" cancel-text="取消" @confirm="Reset_New_Con">
                        <a-button>
                            <DeleteOutlined />
                            重置
                        </a-button>
                    </a-popconfirm>
                    
                    <div style="padding-left: 20px">
                        <a-button @click="notify_tree_add_con">
                            <PlusOutlined />
                            {{ isUpdate === true ? '确认修改' : '确认添加' }}
                        </a-button>
                    </div>
                </div>
                
                <div class="drawer-left-down">
                    <!-- <Tree2 ref = "tree2"
                    @add_con_node = "add_con_node"
                    @delete_con_node = "delete_con_node"
                    @edit_con_node = "edit_con_node">
                    </Tree2> -->
                    
                    <Tree3 ref="tree3"
                    @notify_conList_add="notify_conList_add"
                    @notify_conList_edit="notify_conList_edit"></Tree3>
                </div>
            </div>
        </div>
    </a-drawer>
</template>
  
<script>
import Menu from "@/components/menu.vue"

import OptionList from "@/components/option-list.vue"
import OptionCard from "@/components/option-card.vue"

// import ConstraintList from "@/components/constraint-list.vue"
// import ConstraintCard from "@/components/constraint-card.vue"

import ConstraintList2 from "@/components/constraint-list-2.vue"
import ConstraintCard2 from "@/components/constraint-card-2.vue"

import tmpCard from "@/components/tmpCard.vue"

import TestcaseList from "@/components/testcase-list.vue"
import TestcaseList2 from "@/components/testcase-list-2.vue"
import TestcaseCard from "@/components/testcase-card.vue"

import { UploadOutlined, DownloadOutlined } from '@ant-design/icons-vue'
import { PlusOutlined, DeleteOutlined } from '@ant-design/icons-vue'
import { StepForwardOutlined, StepBackwardOutlined } from '@ant-design/icons-vue'
import { defineComponent, ref } from 'vue'
import { message } from 'ant-design-vue'

import Axios from "axios"
import { test_api, get_testcases, get_constraint_obj } from "@/utils/api"

import Tree2 from "@/components/tree2.vue"
import Tree3 from "@/components/tree3.vue"

export default {
	name: "main",
	components: { 
        Menu, OptionList, OptionCard,
        // ConstraintList, ConstraintCard,
        ConstraintList2, ConstraintCard2,
        TestcaseList, TestcaseList2, TestcaseCard,

        UploadOutlined, DownloadOutlined,
        PlusOutlined, DeleteOutlined,
        StepForwardOutlined, StepBackwardOutlined,

        defineComponent, ref,
        message,

        tmpCard, Tree2, Tree3,
    },
	data() {
		return {

            loading: false,

            file: undefined,

            isUpdate: false,
            visible_con: false,
            select_options: [],


            screen: false,
            // screen_list: ["Meow", "QAQ"],
            screen_list: [],
            screen_new: undefined,
            
            visible: false,
            state: 1,
            Steps: ["Step 1", "Step 2", "Step 3", "Step 4"],
            formState: {
                name: '',
                type: undefined,
                description: '',
                possible: [],
                max_value: 0,
                min_value: 0,
            },
            new_possible: '',

            options: [],

            tree_node_data: undefined,
        }
	},
    watch: {
        'formState.type': function (newType, oldType) {
            this.formState.possible = []
            this.formState.max_value = 0
            this.formState.min_value = 0
        },
        state : function (newState, oldState) {
            sessionStorage.setItem("main-state", JSON.stringify(this.state))
        },
    },
    created() {
        // 在组件创建时加载数据
        this.loadDataFromSessionStorage()
    },
    methods: {
        close_drawer() {
            this.isUpdate = false
        },

        test_api() {
            console.log("test api")
            const now_options = this.options
            const now_constraints = JSON.parse(sessionStorage.getItem("constraint_list_data"))
            test_api({
                test: "Meow",
                options: now_options,
                constraints: now_constraints,
            }).then((response) => {
                let ret = response.data
                console.log(ret)
            }).catch(error => {
                console.error(error);
            });
        },

        Download_Model() {
            this.$refs.conList.Download_Model()
        },

        get_testcases() {
            this.loading = true

            const now_options = this.options
            const now_constraints = JSON.parse(sessionStorage.getItem("constraint_list_data"))
            
            let now_constraints_exp = []
            for (let i = 0; i < now_constraints.length; i ++)
                now_constraints_exp.push(now_constraints[i].expression)

            get_testcases({
                options: now_options,
                // constraints: now_constraints_exp
                constraints: now_constraints
            }).then((response) => {
                let ret = response.data
                // const testcases = ret
                // console.log(testcases)
                // sessionStorage.setItem("testcases", JSON.stringify(testcases))
                
                console.log(ret)
                const columns = ret.columns
                const data = ret.data
                console.log(columns)
                console.log(data)
                sessionStorage.setItem("testcases_columns", JSON.stringify(columns))
                sessionStorage.setItem("testcases_data", JSON.stringify(data))

                this.loading = false
                this.setState(4)
            }).catch(error => {
                // console.error(error);
                message.error("约束非法")
                this.loading = false
            });
        },

        Reset_New_Con() {
            this.$refs.tree3.Reset_New_Con()
        },

        notify_tree_add_con() {
            if(this.isUpdate) {
                this.$refs.tree3.edit_con()
                this.visible_con = false
                this.isUpdate = false
            }
            else {
                this.$refs.tree3.add_con()
                this.visible_con = false
            }
        },
        notify_conList_add(Args) {

            const new_con = Args[0]
            const description = Args[1]

            // console.log(new_con)
            // this.$refs.conList.add_constraint(new_con)
            const options = this.options
            get_constraint_obj({
                constraint : new_con,
                options : options
            }).then((response) => {
                let ret = response.data

                const success = ret.success
                const new_item = ret.new_constraint
                if(description !== undefined && description.length !== "")
                    new_item.description = description
                // console.log(new_item)

                if(success === false) {
                    message.error("添加失败不是合法的表达式")
                    return
                }
                this.$refs.conList.add_constraint(new_item)

            }).catch(error => {
                // console.error(error);
                message.error("添加失败")
            });

            // this.setState(2)
        },

        add_con_node(index_list) {
            console.log('add', index_list)
        },

        delete_con_node(index_list) {
            console.log('delete', index_list)
            
            if (index_list.length === 0) {
                this.new_constraint = []
            }
            else if(index_list.length === 1) {
                this.new_constraint.children.splice(index_list[0], 1)
            }
            else if(index_list.length === 2) {
                this.new_constraint.children[index_list[0]].children.splice(index_list[1], 1)
            }
            else if(index_list.length === 3) {
                let i = index_list[0], j = index_list[1]
                this.new_constraint.children[i].children[j].splice(index_list[2], 1)
            }
            else if(index_list.length === 4) {
                let i = index_list[0], j = index_list[1], k = index_list[2]
                this.new_constraint.children[i].children[j].children[k].splice(index_list[3], 1)
            }
            else if(index_list.length === 5) {
                let i = index_list[0], j = index_list[1], k = index_list[2], p = index_list[3]
                this.new_constraint.children[i].children[j].children[k].children[p].splice(index_list[4], 1)
            }

            const obj = this.new_constraint
            this.$refs.tree2.get_item(obj)
            console.log(this.new_constraint)
        },

        edit_con_node(index_list) {
            console.log('edit', index_list)
        },

        delete_constraint(removedItem) {
            console.log(removedItem)
            this.$refs.conList.delete_constraint(removedItem)
        },

        set_tree_value() {
            console.log(this.$refs.tree3)
            this.$refs.tree3.set_tree_value(this.tree_node_data)
        },
        edit_constraint(item) {
            this.isUpdate = true
            this.visible_con = true

            this.tree_node_data = item
            setTimeout(this.set_tree_value, 100)
        },

        download_tc() {
            this.$refs.tcList.download_tc()
        },

        loadDataFromSessionStorage() {
            // 在组件创建时尝试从 sessionStorage 中加载数据
            const storedData_options = sessionStorage.getItem("main-options")
            if (storedData_options)
                this.options = JSON.parse(storedData_options)

            this.select_options = []
            for (let i = 0; i < this.options.length; i ++)
                this.select_options.push({
                    value: this.options[i].name,
                    lable: this.options[i].name
                })

            const stateDate = sessionStorage.getItem("main-state")
            if(stateDate)
                this.state = JSON.parse(stateDate)
        },

        clean_tc() {
            sessionStorage.setItem("testcases", JSON.stringify([]))
            this.setState(3)
        },
        
        handleChangeFile(info) {
            if (info.file.status !== 'uploading')
                console.log(info.file, info.fileList)
            
            if (info.file.status === 'done')
                message.success(`${info.file.name} file uploaded successfully`)
            
            else if (info.file.status === 'error')
                message.error(`${info.file.name} file upload failed.`)
        },

        upload_back(feedback) {
            const options = feedback.options
            const constraints = feedback.constraints

            this.options = options
            this.select_options = []
            for (let i = 0; i < this.options.length; i ++)
                this.select_options.push({
                    value: this.options[i].name,
                    lable: this.options[i].name
                })
            
            sessionStorage.setItem("main-options", JSON.stringify(options))
            sessionStorage.setItem("option_list_data", JSON.stringify(options))
            sessionStorage.setItem("constraint_list_data", JSON.stringify(constraints))

            this.setState(2)
            // console.log(options)
            // console.log(constraints)
            this.file = []
        },

        clean_opt() {
            this.$refs.childComponent.cleanUp()
            
            this.options = []

            this.select_options = []
            this.screen = false
            this.screen_list = []
            this.screen_new = undefined
            
            sessionStorage.setItem("main-options", JSON.stringify([]))
            sessionStorage.setItem("option_list_data", JSON.stringify([]))
            sessionStorage.setItem("constraint_list_data", JSON.stringify([]))
            // console.log(this.$refs.conList)
        },

        clean_conList() {
            this.$refs.conList.cleanUp()
        },

        change_screen() {
            if(this.screen)
                this.$refs.conList.set_screen(this.screen_list)
            else
                this.$refs.conList.cancel_screen()
        },
        
        add_screen() {
            if(this.screen_new != undefined) {
                let flag = false
                for(let i = 0; i < this.screen_list.length; i ++)
                    if(this.screen_new === this.screen_list[i]) {
                        flag = true
                        break
                    }
                if(flag)
                    message.error('This is an error message')
                else {
                    this.screen_list.push(this.screen_new)
                    this.screen_new = undefined
                }

                if(this.screen)
                    this.$refs.conList.set_screen(this.screen_list)
            }
        },

        delete_option(removedItem) {
            const options = this.options.filter(item => item !== removedItem)
            this.options = options
            sessionStorage.setItem("main-options", JSON.stringify(this.options))
        
            const select_options = this.select_options.filter(item => item !== removedItem.name)
            this.select_options = select_options

            // this.cleanSelected()

            this.$refs.childComponent.delete_option(removedItem)

            sessionStorage.setItem("constraint_list_data", JSON.stringify([]))
        },

        notify_conList_edit(Args) {
            console.log(Args)
            const old_constraint = Args[0]
            const new_constraint = Args[1]
            const description = Args[2]

            const options = this.options
            get_constraint_obj({
                constraint : new_constraint,
                options : options
            }).then((response) => {
                let ret = response.data

                const success = ret.success
                const new_constraint_std = ret.new_constraint
                new_constraint_std.description = description

                console.log(new_constraint_std.expression)
                if(success === false) {
                    message.error("修改失败不是合法的表达式")
                    return
                }
                this.$refs.conList.edit_con(old_constraint, new_constraint_std)

            }).catch(error => {
                // console.error(error);
                message.error("修改失败不是合法的表达式")
            });
        },

        edit_option(opts) {
            const old_option = opts[0]
            const new_option = opts[1]

            // console.log(old_option)
            // console.log(new_option)

            let options = []
            for (let i = 0; i < this.options.length; i ++) {
                if(this.options[i] !== old_option)
                    options.push(this.options[i])
                else options.push(new_option)
            }
            this.options = options
            sessionStorage.setItem("main-options", JSON.stringify(this.options))

            let select_options = []
            for (let i = 0; i < this.options.length; i ++) {
                if(this.select_options[i].name !== old_option.name)
                    select_options.push({
                        value: this.options[i].name,
                        lable: this.options[i].name,
                    })
                else select_options.push({
                    value: new_option.name,
                    lable: new_option.name
                })
            }
            this.select_options = select_options

            this.$refs.childComponent.edit_option(old_option, new_option)

            sessionStorage.setItem("constraint_list_data", JSON.stringify([]))
        },

        closeTag(removedTag) {
            // const tags = state.tags.filter(tag => tag !== removedTag);
            const tags = this.screen_list.filter(tag => tag !== removedTag)
            console.log(tags);
            this.screen_list = tags

            if(this.screen)
                this.$refs.conList.set_screen(this.screen_list)
        },

        close_value_Tag(removedTag) {
            // formState.possible
            const tags = this.formState.possible.filter(tag => tag !== removedTag)
            this.formState.possible = tags
        },

        addOption(new_option) {
            this.options.push(new_option)
            this.select_options.push(
                {value: new_option.name, lable: new_option.name}
            )
            // sessionStorage.setItem("options", this.options)
            sessionStorage.setItem("main-options", JSON.stringify(this.options))
        },

        LastState() {
            if(this.state > 1)
                this.state = this.state - 1
        },
        NextState() {
            if(this.state < 4)
                this.state = this.state + 1
        },
        setState(index) {
            this.state = index
        },

        callFunctionInChild2(new_item) {
            this.$refs.child2.executeFunctionInChild2(new_item)
        },
        callFunctionInConCard(new_item) {
            this.$refs.conCard.executeFunctionInConCard(new_item)
        },
        callFunctionInTcCard(new_item) {
            this.$refs.tcCard.executeFunctionInTcCard(new_item)
        },

        add_constraint() {
            this.visible_con = true

            // console.log(this.$refs.tree2)
            // this.$refs.tree2.test()
            // this.$refs.tree2.get_item(this.new_constraint)
        },
        
        add_option() {
            this.visible = true
        },
        handleOk(e) {
            console.log(e)
            const messagef = this.formState

            if(messagef.name === '') {
                message.error('名称不能为空')
                return 
            }
            if(messagef.name[0] >= '0' && messagef.name[0] <= '9') {
                message.error('首字母不能为数字')
                return
            }
            if(messagef.type === undefined) {
                message.error('请选择类型')
                return
            }
            if(messagef.type === "Category" && messagef.possible.length === 0) {
                message.error('请至少设置一个值域')
                return
            }

            this.visible = false
            this.$refs.childComponent.executeFunctionInChild(messagef)

            this.new_possible = ''
            this.formState = {
                name: '',
                type: undefined,
                description: '',
                possible: [],
                max_value: 0,
                min_value: 0,
            }
            
        },
        add_possible() {
            if(this.formState.possible.includes(this.new_possible)) {
                message.error('已添加过同名取值')
                return 
            }

            if(this.new_possible.length > 0) {
                if(this.new_possible[0] >= '0' && this.new_possible[0] <= '9') {
                    message.error('首字符不能为数字')
                    return
                }
                this.formState.possible.push(this.new_possible)
                this.new_possible = ''
            }
            
        },
    },
}
</script>

<style scoped>

.drawer {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.drawer-left {
    display: flex;
    flex-direction: column;
    padding-right: 40px;
}

.drawer-right {
    /* background-color: blanchedalmond; */
    width: 360px;
    padding-right: 30px;
}

.drawer-left-down {
    padding-top: 30px;
}

.bodyStyle {
    width: 1000px !important;
    background-color: black !important;
}

::-webkit-scrollbar {
  width: 5px; /* 设置滚动条宽度 */
}

.Set-Values {
    display: flex;
    flex-direction: column;
    padding-top: 10px;
    align-items: start;
    width: 80%;

    font-size: 16px;
    font-weight: 350;
}

.new-con-option {
    padding-top: 30px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    padding-top: 20px;
    width: 80%;
}

.boolean-avatar {
    background-color: #ACB1D6;
    color: white;
    font-weight: 400;
}

.integer-avatar {
    background-color: #8294C4;
    color: white;
    font-weight: 600;
}

.float-avatar {
    background-color: #8294C4;
    color: white;
    font-weight: 600;
}

.category-avatar {
    background-color: #ACB1D6;
    color: white;
    font-weight: 600;
}

.add-constraint {
    display: flex;
    flex-direction: row;
    height: 450px;
}
.add-constraint-left {
    width: 600px;
    /* background-color: black; */
}
.add-constraint-right {
    width: 350px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.category-add {
    display: flex;
    flex-direction: row;
}

.integer-float-value {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
}

.content {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.right-content {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: center;
}

.right {
    width: 95%;
    display: flex;
    justify-content: center;
    padding-top: 10px;
    flex-direction: column;
    /* padding: 20px; */
}

.bread {
    display: flex;
    flex-direction: row;
    justify-content: start;
    align-items: center;
    padding-top: 30px;
}

.down-content {
    display: flex;
    flex-direction: column;
    width: 100%;
}

.buttons {
    display: flex;
    flex-direction: row;
    justify-content: start;
    padding-top: 20px;
}

.down {
    padding-top: 30px;
    width: 100%;
    display: flex;
    flex-direction: row;
}

.down-left {
    width: 60%;
}

.down-right {
    right: 160px;
    position: fixed;
    /* background-color: black; */
}

.down-right-2 {
    right: 50px;
    position: fixed;
    /* background-color: black; */
}

.conCard {
    padding-left: 50px;
    width: 500px; 

    /* right: 0px;
    bottom: 20px; 
    max-height: 700px;
    overflow-y: auto;
    position: fixed; */
}
</style>