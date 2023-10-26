<template>
    <div class="content">
        <Menu></Menu>
        <div class="right-content">
            <h2> Step 2 设置约束 </h2>

            <a-divider />
            <h3> 约束类型 </h3>
            <div class="text">
                约束的设置支持以多种类型的运算，具体介绍如下（按运算优先级从低到高顺序）：
            </div>
            <div>
                <a-collapse v-model:activeKey="activeKey" style="width: 900px;">
                    <a-collapse-panel key="1" header="ImpliesExpression（<=> 和 => 运算）">
                        <div class="collapse-panel-detail">
                            <code class="text-code-exp" style="color: green;">
                                // LeftExpression 和 rightExpression 均为布尔表达式
                            </code>
                            <code class="text-code-exp">
                                {{ "(LeftExpression) <=> (rightExpression)" }} 
                                <span style="color: green;">
                                    // LeftExpression 与 rightExpression 等价
                                </span>
                            </code>
                            <code class="text-code-exp">
                                {{ "(LeftExpression) => (rightExpression)" }}
                                <span style="color: green;">
                                    // 若 LeftExpression 为 True 则 rightExpression 为 True
                                </span>
                            </code>
                        </div>
                        
                    </a-collapse-panel>
                    
                    <a-collapse-panel key="2" header="OrExpression（OR 即「或」运算）">
                        <div class="collapse-panel-detail">
                            <code class="text-code-exp" style="color: green;">
                                // Expression<span style="font-size: 4px; color: grey;">1</span>
                                Expression<span style="font-size: 4px; color: grey;">2</span>
                                ... Expression<span style="font-size: 4px; color: grey;">n</span>
                                均为布尔表达式
                            </code>
                            <code class="text-code-exp">
                                (Expression<span style="font-size: 4px; color: grey;">1</span>) 
                                OR (Expression<span style="font-size: 4px; color: grey;">2</span>) 
                                OR ... OR (Expression<span style="font-size: 4px; color: grey;">n</span>)
                            </code>
                            <code class="text-code-exp" style="color: green;">
                                // 该约束要求 
                                Expression<span style="font-size: 4px; color: grey;">1</span>
                                Expression<span style="font-size: 4px; color: grey;">2</span>
                                ... Expression<span style="font-size: 4px; color: grey;">n</span>
                                中至少有一个为 True
                            </code>
                        </div>
                    </a-collapse-panel>

                    <a-collapse-panel key="3" header="AndExpression（AND 即「与」运算）">
                        <div class="collapse-panel-detail">
                            <code class="text-code-exp" style="color: green;">
                                // Expression<span style="font-size: 4px; color: grey;">1</span>
                                Expression<span style="font-size: 4px; color: grey;">2</span>
                                ... Expression<span style="font-size: 4px; color: grey;">n</span>
                                均为布尔表达式
                            </code>
                            <code class="text-code-exp">
                                (Expression<span style="font-size: 4px; color: grey;">1</span>) 
                                AND (Expression<span style="font-size: 4px; color: grey;">2</span>) 
                                AND ... AND (Expression<span style="font-size: 4px; color: grey;">n</span>)
                            </code>
                            <code class="text-code-exp" style="color: green;">
                                // 该约束要求 
                                Expression<span style="font-size: 4px; color: grey;">1</span>
                                Expression<span style="font-size: 4px; color: grey;">2</span>
                                ... Expression<span style="font-size: 4px; color: grey;">n</span>
                                全部为 True
                            </code>
                        </div>
                    </a-collapse-panel>

                    <a-collapse-panel key="4" header="EqualExpression（=、!= 即「等于」或「不等于」运算）">
                        <div class="collapse-panel-detail">
                            <code class="text-code-exp" style="color: green;">
                                // rightExpression 只能为常量
                            </code>
                            <code class="text-code-exp" style="color: green;">
                                // 例如 LeftExpression 的类型为 Boolean 时，rightExpression 为 True 或 False
                            </code>
                            <code class="text-code-exp">
                                (LeftExpression) = (rightExpression)
                                <span style="color: green;"> // 限制 LeftExpression 的值必须为 rightExpression </span>
                            </code>
                            <code class="text-code-exp">
                                (LeftExpression) != (rightExpression)
                                <span style="color: green;"> // 限制 LeftExpression 的值不能为 rightExpression </span>
                            </code>
                        </div>
                    </a-collapse-panel>

                    <a-collapse-panel key="5" header="RelationalExpression（比较运算，包含 >、>=、<、<=）">
                        <div class="collapse-panel-detail">
                            <code class="text-code-exp" style="color: green;">
                                // LeftExpression 为整数型选项，rightExpression 为整数型常量
                            </code>
                            
                            <code class="text-code-exp">
                                (LeftExpression) > (rightExpression)
                                (LeftExpression) >= (rightExpression)
                            </code>

                            <code class="text-code-exp">
                                {{ "(LeftExpression) < (rightExpression)" }}
                                {{ "(LeftExpression) <= (rightExpression)" }}
                            </code>
                        </div>
                    </a-collapse-panel>

                    <a-collapse-panel key="6" header="NotExpression（非运算）">
                        <div class="collapse-panel-detail">
                            <code class="text-code-exp" style="color: green;">
                                // Expression 为布尔表达式
                            </code>
                            <code class="text-code-exp">
                                not (Expression)
                                <span style="color: green;"> 该约束要求 Expression 必须为 False </span>
                            </code>
                        </div>
                    </a-collapse-panel>
                </a-collapse>
            </div>
            <div class="text" style="padding-top: 20px;">
                尽管运算之间存在优先级，在复杂的约束中仍推荐使用
                <span class="highlight">括号</span>
                分隔不同运算。
            </div>

            <a-divider />
            <h3> 约束的添加与编辑 </h3>
            <div class="text">
                可使用多种方式添加与编辑约束信息。网页使用树状图的方式渲染每条约束。
            </div>
            <div style="display: flex; flex-direction: row;">
                <div class="text">
                    直接输入表达式：
                </div>
                <div class="text" style="padding-left: 250px;">
                    使用树状图可视化界面：
                </div>
            </div>

            <div style="display: flex; flex-direction: row;">
                <div style="display: flex; flex-direction: column;">
                    <a-input value="(Par0 = true) OR (Par2 > 10)"
                    style="width: 200px; height: 40px;"></a-input>
                    
                    <div style="display: flex; flex-direction: column;
                    padding-top: 20px; align-items: start;">
                        <code>
                            该约束表示：
                        </code>
                        <code style="padding-top: 10px;">
                            Par0 = true 和 Par2 > 10
                        </code>
                        <code style="padding-top: 10px;">
                            至少有一个成立。
                        </code>

                        <code style="padding-top: 10px; color: green;">
                            {{ "即 Par0 = false 且 Par2 <= 10 的情况非法" }}
                        </code>
                    </div>
                    
                </div>
               

                <div style="padding-left: 50px; height: 220px;">
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
            </div>

            <a-divider />
            <h3> 约束列表 </h3>
            <div class="text">
                在约束列表中可以根据<span style="color: #8294C4;">约束所涉及的选项</span>对约束进行筛选，可以查看选中的约束的详细信息，并进行编辑或删除。
            </div>
            
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

            <div class="text">
                添加了 Par1 作为筛选标签后：
            </div>

            <div style="display: flex; flex-direction: row; 
            justify-items: flex-start; align-items: start; align-content: start;">
                <div>
                    <div style="display: flex; flex-direction: row; align-items: center;">
                        <a-checkbox :checked="true">
                            筛选
                        </a-checkbox>
                        <div style="padding-left: 20px;">
                            <a-select disabled
                                placeholder="选择已有选项"
                                style="width: 150px" >
                            </a-select>
                        </div>

                        <div style="padding-left: 20px;">
                            <a-button disabled>
                                <PlusOutlined />
                                添加
                            </a-button>
                        </div>
                    </div>

                    <div style="padding-top: 15px; display: flex; flex-direction: row;
                    align-items: start; justify-items: start;">
                        <a-tag closable>
                            Par1
                        </a-tag>
                    </div>

                    <div style="width: 600px; padding-top: 15px;">
                        <a-list item-layout="horizontal" :data-source="constraints_2">
                            <template #renderItem="{ item, index }">
                                <a-list-item style="background-color: rgba(0, 0, 1, 0.05);">
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
                </div>
                
                <div style="padding-left: 20px;">
                    <a-card style="width: 300px; background-color: #f2f6ff;">
                        <span style="font-size: 16px; font-weight: 500;">
                            {{ constraints_2[0].description }} 
                        </span>

                        <span style="padding-top: 50px;"></span>
                        
                        <template class="ant-card-actions" #actions>
                            <a-popconfirm
                                title="是否确定删除此约束"
                                ok-text="确定" cancel-text="取消"
                                @confirm="confirm" @cancel="cancel" >
                                <a href="#">
                                    <DeleteOutlined key="delete"/>
                                </a>
                            </a-popconfirm>
                            
                            <edit-outlined key="edit" @click="edit_con" />
                            <ellipsis-outlined key="ellipsis" />
                        </template>

                        <span style="padding-top: 50px;"></span>
                        <div style="background-color: white; height: 50px;">
                            <div style="padding-top: 15px;"></div>
                            被选中的约束的树的视图
                        </div>
                    </a-card>
                </div>
                
            </div>
            
            
            <a-divider />
            <h3> 文件格式 </h3>
            <div class="text">
                可以使用上传文件的方式，快速批量地同时添加选项与约束，具体格式要求如下。
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

                <div class="format-details">
                    <code class="text-4"> // 每条约束占用一行，表达式的首尾用 # 标记 </code>
                    <code class="text-4"> // 推荐使用括号分隔不同的运算符 </code>
                </div>
            </div>

            <a-divider />
            <h3> 模型下载 </h3>
            <div class="text">
                对于手动添加而非上传文件添加的选项与约束，点击下载按钮，可下载包含当前的选项与限制的文件。
            </div>
            <div class="text">
                文件格式见上文格式。
            </div>
            <a-button>
                <DownloadOutlined />
                下载模型
            </a-button>

            <a-divider />
        </div>
    </div>
</template>

<script>
import Menu from "@/components/menu.vue"
import optAvatar from "@/components/opt-avatar.vue"
import treeTitle from "@/components/tree-title.vue"

import { defineComponent, ref, watch } from 'vue'
import { DownloadOutlined, PlusOutlined } from '@ant-design/icons-vue'
import { EditOutlined, EllipsisOutlined, DeleteOutlined } from '@ant-design/icons-vue'

import { notification } from 'ant-design-vue'
export default {
    name: 'tutorial_2',
    components: {
        Menu, optAvatar, treeTitle,

        notification,

        DownloadOutlined, PlusOutlined,
        EditOutlined, EllipsisOutlined, DeleteOutlined,
    },
    data() {
        return {
            // activeKey: ref(["1", "2", "3", "4", "5", "6"]),
            activeKey: ref([]),

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
                    expression : "(Par0 = false) OR (Par1 != value1) OR (Par2 <= 5)",
                    description : "这是一个示例 - 约束2",
                    component : [ 
                        { name : "Par0", type : "Boolean" },
                        { name : "Par1", type : "Category"},
                        { name : "Par2", type : "Integer"} 
                    ],
                },
            ],
            
            constraints_2 : [
                {
                    expression : "(Par0 = false) OR (Par1 != value1) OR (Par2 <= 5)",
                    description : "这是一个示例 - 约束2",
                    component : [ 
                        { name : "Par0", type : "Boolean" },
                        { name : "Par1", type : "Category"},
                        { name : "Par2", type : "Integer"} 
                    ],
                },
            ]
        }
    },

    methods: {
        confirm() {
            notification.open({
                message: '删除约束操作',
                description: '在正式的约束列表中，此操作将删除当前约束。',
            });
        },

        edit_con() {
            notification.open({
                message: '编辑约束操作',
                description: '在正式的约束列表中，此操作将对当前约束进行编辑。',
            });
        },
    },
}
</script>

<style scoped>

.highlight {
    color: red;
}

.name {
    color: #8294C4;
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

.collapse-panel-detail {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

.text-code-exp {
    color: #8294C4;
    font-size: 16px;
    font-weight: 500;
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

.list-right {
    display: flex;
    flex-direction: column;
}
</style>