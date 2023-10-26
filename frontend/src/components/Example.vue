<template>
    <div class="content">
        <Menu></Menu>
        <div class="right-content">
            <h2> 快速开始（示例） </h2>
            <div class="text">
                下面将通过一个例子，简单介绍本平台的使用方法。
            </div>
            <div style="display: flex; flex-direction: row; justify-items: flex-start;">
                <div style="display: flex; flex-direction: column; align-items: start;">
                    <div class="text">
                        假设需要被测试的系统有三个选项：
                    </div>
                    <div>
                        <a-table :columns="columns" :data-source="data" size="middle">
                            <template #action>
                                <a @click="delete_tc">删除</a>
                            </template>
                        </a-table>
                    </div>
                </div>

                <div style="display: flex; flex-direction: column; align-items: start;
                padding-left: 40px;">
                    <div class="text">
                        这些约束之间存在两个约束：
                    </div>
                    
                    <div class="format">
                        <div class="text-border">
                            <code class="text-3"> (Par0 = True) OR (Par2 > 10) </code>
                            <code class="text-3"> {{ "(Par1 != value1) OR (Par2 <= 18)" }} </code>
                        </div>
                    </div>
                </div>
            </div>
            
            <a-divider />
            <h3> 第一步：设置选项信息 </h3>
            <div style="display: flex; flex-direction: row;">
                <div class="text">
                    点击添加选项按钮，将三个选项的信息依次录入。
                </div>
                <div style="padding-left: 20px;">
                    <a-button>
                        <PlusOutlined />
                        添加选项
                    </a-button>
                </div>
            </div>

            <div style="display: flex; flex-direction: row;">
                <div class="option-form">
                    <a-form style="padding-right: 30px">
                        <a-form-item label="名称">
                            <a-input value="Par0"/>
                        </a-form-item>
                        <a-form-item label="类型">
                            <a-input value="Boolean"/>
                        </a-form-item>
                        <a-form-item label="描述">
                            <a-textarea value="这是一个示例 Parameter 0"
                                placeholder="" :auto-size="{ minRows: 2, maxRows: 5 }" />
                        </a-form-item>
                    </a-form>
                </div>

                <div class="option-form">
                    <a-form style="padding-right: 30px">
                        <a-form-item label="名称">
                            <a-input value="Par1"/>
                        </a-form-item>
                        <a-form-item label="类型">
                            <a-input value="Category"/>
                        </a-form-item>
                        <a-form-item label="描述">
                            <a-textarea value="这是一个示例 Parameter 1"
                                placeholder="" :auto-size="{ minRows: 2, maxRows: 5 }" />
                        </a-form-item>
                        <a-form-item label="值域">
                            <div style="display: flex; flex-direction: row;">
                                <a-input disabled />
                                <div style="padding-left: 10px;">
                                    <a-button disabled>
                                        <PlusOutlined />
                                        添加
                                    </a-button>
                                </div>
                            </div>
                        </a-form-item>
                        <a-form-item>
                            <div style="display: flex; flex-wrap: wrap;">
                                <a-tag>value1</a-tag>
                                <a-tag>value2</a-tag>
                                <a-tag>value3</a-tag>
                            </div>
                        </a-form-item>
                    </a-form>
                </div>

                <div class="option-form">
                    <a-form style="padding-right: 30px">
                        <a-form-item label="名称">
                            <a-input value="Par2"/>
                        </a-form-item>
                        <a-form-item label="类型">
                            <a-input value="Integer"/>
                        </a-form-item>
                        <a-form-item label="描述">
                            <a-textarea value="这是一个示例 Parameter 2"
                                placeholder="" :auto-size="{ minRows: 2, maxRows: 5 }" />
                        </a-form-item>
                        <a-form-item>
                            <div class="integer-float-value">
                                <div>最小值: </div>
                                <a-input-number :value="-10" />
                                <div>最大值: </div>
                                <a-input-number :value="20" />
                            </div>
                        </a-form-item>
                    </a-form>
                </div>
            </div>

            <div class="text">
                得到如下选项列表：
            </div>

            <div>
                <div class="checkboxs">
                    <a-checkbox-group 
                    v-model:value="display_type" 
                    name="checkboxgroup" 
                    :options="plainOptions"
                    @change="change_checkbox" />
                </div>

                <div class="list-tutorial">
                    <a-list item-layout="horizontal" :data-source="all_options"
                    style="width: 530px; padding-right: 30px;">
                        <template #renderItem="{ item, index }">
                            <a-list-item :class="index === chosen_id ? 'chosen' : 'narmal' "
                            @click="set_chosen_id(index)" >
                                <a-list-item-meta
                                :description = item.description>
                                <template #title>
                                    {{ item.name + " ( " + item.type + " ) " }}
                                </template>
                                
                                <template #avatar>
                                    <a-avatar v-if="item.type === 'Boolean'" class="boolean-avatar">01</a-avatar>
                                    <a-avatar v-if="item.type === 'Integer'" class="integer-avatar">Z</a-avatar>
                                    <a-avatar v-if="item.type === 'Float'" class="float-avatar">R</a-avatar>
                                    <a-avatar v-if="item.type === 'Category'" class="category-avatar">C</a-avatar>
                                </template>
                            </a-list-item-meta>
                            
                            <div class="Tag">
                                <div v-for="(it, index) in item.possible_org">
                                    <a-tag v-if="index  < 2"> {{ it }} </a-tag>
                                </div>
                                <a-popover v-if="item.possible_org.length > 2">
                                    <template #content>
                                        <div v-for="(it, index) in item.possible_org">
                                            <a-tag v-if="index  >= 2"> {{ it }} </a-tag>
                                        </div>
                                    </template>
                                    <a-tag>...</a-tag>
                                </a-popover>
                            </div>
                            </a-list-item>
                        </template>
                    </a-list>

                    <a-card v-if="item !== undefined" 
                    style="width: 300px; height: 188px; 
                    background-color: #f2f6ff;">
                
                        <template class="ant-card-actions" #actions>
                            <!-- <setting-outlined key="setting" /> -->
                            <a-popconfirm
                                title="是否确定删除该选项"
                                ok-text="确定" cancel-text="取消"
                                @confirm="confirm" @cancel="cancel" >
                                <a href="#">
                                    <DeleteOutlined key="delete"/>
                                </a>
                            </a-popconfirm>
                            <edit-outlined key="edit" @click="edit_option" />
                            <ellipsis-outlined key="ellipsis" @click="get_detail" />
                        </template>

                        <a-card-meta :title="item.name + ' ( ' + item.type + ' ) '" 
                            :description=item.description>
                            <template #avatar>
                                <!-- <a-avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" /> -->
                                <a-avatar v-if="item.type === 'Boolean'" class="boolean-avatar">01</a-avatar>
                                <a-avatar v-if="item.type === 'Integer'" class="integer-avatar">Z</a-avatar>
                                <a-avatar v-if="item.type === 'Float'" class="float-avatar">R</a-avatar>
                                <a-avatar v-if="item.type === 'Category'" class="category-avatar">C</a-avatar>
                            </template>
                        </a-card-meta>

                        <div class="details">
                            <a-tag v-for="it in item.possible_org">
                                {{ it }}
                            </a-tag>
                        </div>
                    </a-card>

                    <div v-else>
                        <a-empty></a-empty>
                    </div>
                </div>
                
            </div>

            <a-divider />
            <h3> 第二步：设置约束信息 </h3>
            <div style="display: flex; flex-direction: row;">
                <div class="text">
                    点击添加约束按钮，将两个约束的信息依次录入。
                </div>
                <div style="padding-left: 20px;">
                    <a-button>
                        <PlusOutlined />
                        添加约束
                    </a-button>
                </div>
            </div>

            <div class="text">
                得到如下约束列表：
            </div>
            <div style="display: flex; flex-direction: row; 
            align-items: start; justify-items: start; height: 220px;">
                <div style="width: 600px;">
                    <a-list item-layout="horizontal" :data-source="constraints">
                        <template #renderItem="{ item, index }">
                            <a-list-item>
                                <a-list-item-meta :description = "item.expression">
                                    <template #title>
                                        {{ item.description }}
                                    </template>
                                </a-list-item-meta>

                                <div class="list-right">
                                    <a-avatar-group :max-count="3" :max-style="{ color: '#f56a00', backgroundColor: '#fde3cf' }"
                                    style="width: 130px;">
                                        <optAvatar v-for="it in item.component" :msg="it.type"></optAvatar>
                                    </a-avatar-group>

                                    <div style="padding-top: 5px; display: flex; flex-direction: row; width: 130px; ">
                                        <div v-for="(it, index) in item.component">
                                            <a-tag v-if="index  < 2"> {{ it.name }} </a-tag>
                                        </div>
                                        <a-popover v-if="item.component.length > 2">
                                            <template #content>
                                                <div v-for="(it, index) in item.component">
                                                    <a-tag v-if="index  >= 2"> {{ it.name }} </a-tag>
                                                </div>
                                            </template>
                                            <a-tag>...</a-tag>
                                        </a-popover>
                                    </div>
                                </div>
                            </a-list-item>
                        </template>
                    </a-list>
                </div>

                <div style="padding-left: 10px;">
                    <a-tree show-line=true show-icon=true 
                    :default-expanded-keys="['0-0-0', '0-0-1', '0-0-2']">
                        <a-tree-node key="0-0">
                            <template #title>
                                <div style="display: flex; flex-direction : row;">
                                    <treeTitle :msg="'OR'" :expression="'(Par0 = true) OR (Par2 > 10)'"></treeTitle>
                                </div>
                            </template>

                            <a-tree-node key="0-0-0">
                                <template #title>
                                    <div style="display: flex; flex-direction : row;">
                                        <treeTitle :msg="'='" :expression="'Par0 = true'"></treeTitle>
                                    </div>
                                </template>
                                
                                <a-tree-node key="0-0-0-0">
                                    <template #title>
                                        <div style="display: flex; flex-direction : row;">
                                            <treeTitle :msg="'final'" :expression="'Par0'"></treeTitle>
                                        </div>
                                    </template>
                                </a-tree-node>

                                <a-tree-node key="0-0-0-1">
                                    <template #title>
                                        <div style="display: flex; flex-direction : row;">
                                            <treeTitle :msg="'final'" :expression="'true'"></treeTitle>
                                        </div>
                                    </template>
                                </a-tree-node>

                            </a-tree-node>
                            
                            <a-tree-node key="0-0-1">
                                <template #title>
                                    <div style="display: flex; flex-direction : row;">
                                        <treeTitle :msg="'>'" :expression="'Par2 > 10'"></treeTitle>
                                    </div>
                                </template>

                                <a-tree-node key="0-0-1-0">
                                    <template #title>
                                        <div style="display: flex; flex-direction : row;">
                                            <treeTitle :msg="'final'" :expression="'Par2'"></treeTitle>
                                        </div>
                                    </template>
                                </a-tree-node>

                                <a-tree-node key="0-0-1-1">
                                    <template #title>
                                        <div style="display: flex; flex-direction : row;">
                                            <treeTitle :msg="'final'" :expression="'10'"></treeTitle>
                                        </div>
                                    </template>
                                </a-tree-node>
                            </a-tree-node>
                        </a-tree-node>
                    </a-tree>
                </div>

                <div style="padding-left: 20px;">
                    <a-tree show-line=true show-icon=true 
                    :default-expanded-keys="['0-0-0', '0-0-1', '0-0-2']">
                        <a-tree-node key="0-0">
                            <template #title>
                                <div style="display: flex; flex-direction : row;">
                                    <treeTitle :msg="'OR'" :expression="'(Par1 != value1) OR (Par2 <= 18)'"></treeTitle>
                                </div>
                            </template>

                            <a-tree-node key="0-0-0">
                                <template #title>
                                    <div style="display: flex; flex-direction : row;">
                                        <treeTitle :msg="'!='" :expression="'Par1 != value1'"></treeTitle>
                                    </div>
                                </template>
                                
                                <a-tree-node key="0-0-0-0">
                                    <template #title>
                                        <div style="display: flex; flex-direction : row;">
                                            <treeTitle :msg="'final'" :expression="'Par1'"></treeTitle>
                                        </div>
                                    </template>
                                </a-tree-node>

                                <a-tree-node key="0-0-0-1">
                                    <template #title>
                                        <div style="display: flex; flex-direction : row;">
                                            <treeTitle :msg="'final'" :expression="'value1'"></treeTitle>
                                        </div>
                                    </template>
                                </a-tree-node>

                            </a-tree-node>
                            
                            <a-tree-node key="0-0-1">
                                <template #title>
                                    <div style="display: flex; flex-direction : row;">
                                        <treeTitle :msg="'<='" :expression="'Par2 <= 18'"></treeTitle>
                                    </div>
                                </template>

                                <a-tree-node key="0-0-1-0">
                                    <template #title>
                                        <div style="display: flex; flex-direction : row;">
                                            <treeTitle :msg="'final'" :expression="'Par2'"></treeTitle>
                                        </div>
                                    </template>
                                </a-tree-node>

                                <a-tree-node key="0-0-1-1">
                                    <template #title>
                                        <div style="display: flex; flex-direction : row;">
                                            <treeTitle :msg="'final'" :expression="'18'"></treeTitle>
                                        </div>
                                    </template>
                                </a-tree-node>
                            </a-tree-node>
                        </a-tree-node>
                    </a-tree>
                </div>
            </div>
            

            <a-divider />
            <h3> 第一步 & 第二步：使用文件 </h3>
            <div style="display: flex; flex-direction: row;">
                <div class="text">
                    创建以下文件，点击上传文件按钮上传。
                </div>
                <div style="padding-left: 20px;">
                    <a-button>
                        <upload-outlined></upload-outlined>
                        上传文件
                    </a-button>
                </div>
            </div>
            
            <div class="format">
                <div class="text-border">
                    <code class="text-3"> Model Example </code>
                    <code class="text-3"> Parameters : </code>
                    <code class="text-3"> <span class="name">Par0</span> : <span class="highlight">Boolean</span> </code>
                    <code class="text-3"> <span class="name">Par1</span> : <span class="highlight">{ value0, value1, value2 }</span> </code>
                    <code class="text-3"> <span class="name">Par2</span> : <span class="highlight">[ -10 .. 20 ]</span></code>
                    
                    <code class="text-3"></code>
                    <code class="text-3"> Constraints: </code>
                    <code class="text-3 highlight"> # (Par0 = true) OR (Par2 > 10) # </code>
                    <code class="text-3 highlight"> {{ "# (Par1 != value1) OR (Par2 <= 18) #" }} </code>
                </div>
            </div>


            <a-divider />
            <h3> 第三步：生成覆盖阵列 </h3>
            <div style="display: flex; flex-direction: row;">
                <div class="text">
                    点击开始按钮，开始生成测试数据，可能需要等待少量时间。
                </div>
                <div style="padding-left: 20px;">
                    <a-button type="primary" size="large">Start</a-button>
                </div>
            </div>

            <a-divider />
            <h3> 第四步：查看结果 </h3>
            <div style="display: flex; flex-direction: row;">
                <div class="text">
                    查看结果，可选择点击下载按钮，下载 xls 格式的测试数据（以下只展示结果的一部分）。
                </div>
                <div style="padding-left: 20px;">
                    <a-button>
                        <DownloadOutlined />
                        下载
                    </a-button>
                </div>
            </div>

            <div>
                <a-table :columns="columns_tc" :data-source="data_tc" size="middle">
                    <template #action>
                        <a @click="delete_tc">删除</a>
                    </template>
                </a-table>
            </div>

            <a-divider />
        </div>
    </div>
</template>

<script>
import Menu from "@/components/menu.vue"
import { defineComponent, ref, watch } from 'vue'
import { PlusOutlined, UploadOutlined, DownloadOutlined } from '@ant-design/icons-vue'
import { EditOutlined, EllipsisOutlined, DeleteOutlined } from '@ant-design/icons-vue'
import { notification } from 'ant-design-vue'
import optAvatar from "@/components/opt-avatar.vue"
import treeTitle from "@/components/tree-title.vue"
export default {
    name: 'example',
    components: {
        Menu, optAvatar, treeTitle,
        
        notification,
        PlusOutlined, UploadOutlined, DownloadOutlined,
        EditOutlined, EllipsisOutlined, DeleteOutlined,
    },
    data() {
        return {
            columns : [
                { title: '选项名称', dataIndex: 'name', key: 'name', width: 100 },
                { title: '选项类型', dataIndex: 'type', key: 'type', width: 100 },
                { title: '选项值域', dataIndex: 'value', key: 'value', width: 200 },
            ],

            data: [
                { key: 0, name: "Par0", type: "Boolean", value: "true, false" },
                { key: 1, name: "Par1", type: "Category", value: "value0, value1, value2" },
                { key: 2, name: "Par2", type: "Integer", value: "[-10, 20]" }
            ],

            columns_tc : [
                { title: '编号', dataIndex: 'index', key: 'index', fixed: 'left', width: 130 },
                { title: 'Par0', dataIndex: 'value1', key: '1', width: 100 },
                { title: 'Par1', dataIndex: 'value2', key: '2', width: 100 },
                { title: 'Par2', dataIndex: 'value3', key: '3', width: 100 },
            ],

            data_tc : [
                { key: 0, index: "Testcase 1", value1: "False", value2: "value1", value3: "17" },
                { key: 1, index: "Testcase 2", value1: "True", value2: "value2", value3: "-1" },
                { key: 2, index: "Testcase 3", value1: "True", value2: "value0", value3: "-2" },
            ],

            all_options: [
                {
                    id: 0,
                    name: "Par0",
                    type: "Boolean",
                    description: "这是一个示例 Parameter 0",
                    possible_org: [ "True", "False" ]
                },

                {
                    id: 1,
                    name: "Par1",
                    type: "Category",
                    description: "这是一个示例 Parameter 1",
                    possible_org: ["value1", "value2", "value3"]
                },

                {
                    id: 2,
                    name: "Par2",
                    type: "Integer",
                    description: "这是一个示例 Parameter 2",
                    min_value: -10,
                    max_value: 20,
                    possible_org: ["-10 ~ 20"]
                },
            ],

            plainOptions: ["Boolean", "Integer", "Category"],
            display_type: ["Boolean", "Integer", "Category"],

            item: {
                id: 0,
                name: "Par0",
                type: "Boolean",
                description: "这是一个示例 Parameter 0",
                possible_org: [ "True", "False" ]
            },

            chosen_id: 0,

            constraints: [
                {
                    expression : "(Par0 = true) OR (Par2 > 10)",
                    description : "这是一个示例 - 约束1",
                    component : [ 
                        { name : "Par0", type : "Boolean" }, 
                        { name : "Par2", type : "Integer"} 
                    ],
                },
                {
                    expression : "(Par1 != value1) OR (Par2 <= 18)",
                    description : "这是一个示例 - 约束2",
                    component : [ 
                        { name : "Par1", type : "Category"},
                        { name : "Par2", type : "Integer"} 
                    ],
                },
            ],
        }
    },

    methods: {
        change_checkbox() {
            this.all_options = []
            if(this.display_type.includes("Boolean"))
                this.all_options.push({
                    id: 0,
                    name: "Par0",
                    type: "Boolean",
                    description: "这是一个示例 Parameter 0",
                    possible_org: [ "True", "False" ]
                })

            if(this.display_type.includes("Category"))
                this.all_options.push({
                    id: 1,
                    name: "Par1",
                    type: "Category",
                    description: "这是一个示例 Parameter 1",
                    possible_org: ["value1", "value2", "value3"]
                })
            
                if(this.display_type.includes("Integer"))
                    this.all_options.push({
                        id: 2,
                        name: "Par2",
                        type: "Integer",
                        description: "这是一个示例 Parameter 2",
                        min_value: -10,
                        max_value: 20,
                        possible_org: ["-10 ~ 20"]
                    })
            
            
            this.set_chosen_id(0)
        },

        set_chosen_id(index) {
            this.chosen_id = index
            if (index >= 0 && index < this.all_options.length)
                this.item = this.all_options[index]
            else
                this.item = undefined
        },

        confirm() {
            notification.open({
                message: '删除选项操作',
                description: '在正式的选项列表中，此操作将删除当前选项。',
            });
        },

        edit_option() {
            notification.open({
                message: '编辑选项操作',
                description: '在正式的选项列表中，此操作将对当前选项进行编辑。',
            });
        },
    },
}
</script>

<style scoped>

.option-down {
    padding: 20px;
    background-color: white;

    display: flex;
    flex-direction: row;
}

.option-form {
    /* background-color:aliceblue; */
    width: 360px;
    padding-right: 30px;
}

.text {
    padding-top: 10px;
    padding-bottom: 20px;
    font-size: 18px;
    font-weight: 300;
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
    align-items: start;
    padding-left: 100px;

    /* background-color: antiquewhite; */
}

.text-4 {
    font-size: 16px;
    font-weight: 200;
    padding: 5px;
}

.format {
    display: flex;
    flex-direction: row;
    justify-items: start;
}

.format-details {
    padding-top: 200px;
    padding-left: 20px;
    display: flex;
    flex-direction: column;
    justify-items: start;
    align-items: flex-start;
    
    color: green;
}

.text-border {
    padding: 20px;
    border: 1px solid #8294C4;
    border-radius: 5px;
    display: flex;
    flex-direction: column;

    align-items: flex-start;

    font-size: 16px;
    font-weight: 200;

    color: gray;
    /* background-color: #ECF2FF; */
    background-color: #f2f6ff;
}

.text-3 {
    padding: 5px;
}

.integer-float-value {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
}

.checkboxs {
    display: flex;
    flex-direction: row;
    justify-content: start;
    padding-bottom: 20px;
}

.list-tutorial {
    display: flex;
    flex-direction: row;
    justify-items: start;
}

.Tag {
    width: 180px;
    display: flex;
    flex-direction: row;
    justify-content: end;
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

.category-avatar {
    background-color: #ACB1D6;
    color: white;
    font-weight: 600;
}

.chosen {
    background-color: rgba(0, 0, 1, 0.05);
}

.details {
    width: 100%;
    padding-top: 20px;
}

</style>
    
