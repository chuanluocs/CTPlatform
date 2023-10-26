<template>
    <div class="content">
        <Menu></Menu>
        <div class="right-content">
            <h2> Step 1 设置选项 </h2>
            
            <a-divider />
            <h3> 选项类型 </h3>
            
            <div class="text">
                支持三种类型的选项：Boolean、Integer、Category，具体介绍如下：
            </div>
            <a-collapse v-model:activeKey="activeKey"
            style="width: 800px;">
                <a-collapse-panel key="1" header="类型一：Boolean (True / False)">
                    <div class="text-2">
                        {{ "在以下示例中，" + Option[0].name + " 可能的取值为 True 或 False"}}
                    </div>

                    <a-list item-layout="horizontal" :data-source="Option"
                    style="width: 500px;">
                        <template #renderItem="{ item, index }">
                            <a-list-item class="chosen">
                                <a-list-item-meta
                                :description = item.description>
                                <template #title>
                                    {{ item.name + " ( " + item.type + " ) " }}
                                </template>
                                
                                <template #avatar>
                                    <a-avatar class="boolean-avatar">01</a-avatar>
                                </template>
                            </a-list-item-meta>
                            
                            <div class="Tag">
                                <div v-for="(it, index) in item.possible_org">
                                    <a-tag> {{ it }} </a-tag>
                                </div>
                            </div>
                            </a-list-item>
                        </template>
                    </a-list>

                    <a-divider />
                    
                    <div class="option-down">
                        <div class="option-form">
                            <a-form style="padding-right: 30px">
                                <a-form-item label="名称">
                                    <a-input :value="Option[0].name" />
                                </a-form-item>
                                <a-form-item label="类型">
                                    <a-input :value="Option[0].type" />
                                </a-form-item>
                                <a-form-item label="描述">
                                    <a-textarea :value="Option[0].description"
                                        placeholder=""
                                        :auto-size="{ minRows: 2, maxRows: 5 }" />
                                </a-form-item>
                            </a-form>
                        </div>

                        <a-card style="
                        width: 300px; height: 188px; 
                        background-color: #f2f6ff;">
                            <template class="ant-card-actions" #actions>
                                <DeleteOutlined key="delete"/>
                                <edit-outlined key="edit" />
                                <ellipsis-outlined key="ellipsis" />
                            </template>
                    
                            <a-card-meta :title="Option[0].name + ' ( ' + Option[0].type + ' ) '" 
                                :description=Option[0].description>
                                <template #avatar>
                                    <a-avatar class="boolean-avatar">01</a-avatar>
                                </template>
                            </a-card-meta>
                    
                            <div class="details">
                                <a-tag v-for="it in Option[0].possible_org">
                                    {{ it }}
                                </a-tag>
                            </div>
                        </a-card>
                    </div>
                </a-collapse-panel>
                
                <a-collapse-panel key="2" header="类型二：Integer (整数)">
                    <div class="text-2">
                        {{ "在以下示例中，" + Option_int[0].name + " 可能的取值为 " + Option_int[0].possible_org[0] + " 的整数。"}}
                    </div>

                    <a-list item-layout="horizontal" :data-source="Option_int"
                    style="width: 500px;">
                        <template #renderItem="{ item, index }">
                            <a-list-item class="chosen">
                                <a-list-item-meta
                                :description = item.description>
                                <template #title>
                                    {{ item.name + " ( " + item.type + " ) " }}
                                </template>
                                
                                <template #avatar>
                                    <a-avatar class="integer-avatar">Z</a-avatar>
                                </template>
                            </a-list-item-meta>
                            
                            <div class="Tag">
                                <div v-for="(it, index) in item.possible_org">
                                    <a-tag> {{ it }} </a-tag>
                                </div>
                            </div>
                            </a-list-item>
                        </template>
                    </a-list>

                    <a-divider />

                    <div class="option-down">
                        <div class="option-form">
                            <a-form style="padding-right: 30px">
                                <a-form-item label="名称">
                                    <a-input :value="Option_int[0].name" />
                                </a-form-item>
                                <a-form-item label="类型">
                                    <a-input :value="Option_int[0].type" />
                                </a-form-item>
                                <a-form-item label="描述">
                                    <a-textarea :value="Option_int[0].description"
                                        placeholder=""
                                        :auto-size="{ minRows: 2, maxRows: 5 }" />
                                </a-form-item>
                                <a-form-item>
                                    <div class="integer-float-value">
                                        <div>最小值: </div>
                                        <a-input-number disabled v-model:value="Option_int[0].min_value" :min="-10000" :max="10000" />
                                        <div>最大值: </div>
                                        <a-input-number disabled v-model:value="Option_int[0].max_value" :min="-10000" :max="10000" />
                                    </div>
                                </a-form-item>
                            </a-form>
                        </div>

                        <a-card style="
                        width: 300px; height: 188px; 
                        background-color: #f2f6ff;">
                            <template class="ant-card-actions" #actions>
                                <DeleteOutlined key="delete"/>
                                <edit-outlined key="edit" />
                                <ellipsis-outlined key="ellipsis" />
                            </template>
                    
                            <a-card-meta :title="Option_int[0].name + ' ( ' + Option_int[0].type + ' ) '" 
                                :description=Option_int[0].description>
                                <template #avatar>
                                    <a-avatar class="integer-avatar">Z</a-avatar>
                                </template>
                            </a-card-meta>
                    
                            <div class="details">
                                <a-tag v-for="it in Option_int[0].possible_org">
                                    {{ it }}
                                </a-tag>
                            </div>
                        </a-card>
                    </div>
                </a-collapse-panel>

                <a-collapse-panel key="3" header="类型三：Category">
                    <div class="text-2">
                        {{ "在以下示例中，" + Option_cate[0].name + " 可能的取值为 value-1 ~ value-5 这五种。"}}
                    </div>

                    <a-list item-layout="horizontal" :data-source="Option_cate"
                    style="width: 500px;">
                        <template #renderItem="{ item, index }">
                            <a-list-item class="chosen">
                                <a-list-item-meta
                                :description = item.description>
                                <template #title>
                                    {{ item.name + " ( " + item.type + " ) " }}
                                </template>
                                
                                <template #avatar>
                                    <a-avatar class="category-avatar">C</a-avatar>
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

                    <a-divider />
                    
                    <div class="option-down">
                        <div class="option-form">
                            <a-form style="padding-right: 30px">
                                <a-form-item label="名称">
                                    <a-input :value="Option_cate[0].name" />
                                </a-form-item>
                                <a-form-item label="类型">
                                    <a-input :value="Option_cate[0].type" />
                                </a-form-item>
                                <a-form-item label="描述">
                                    <a-textarea :value="Option_cate[0].description"
                                        placeholder="" 
                                        :auto-size="{ minRows: 2, maxRows: 5 }" />
                                </a-form-item>
                                <a-form-item label="值域">
                                    <div class="category-add">
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
                                        <div v-for="it in Option_cate[0].possible_org" :key="it">
                                            <a-tag closable disabled>
                                                {{ it }}
                                            </a-tag>
                                        </div>
                                    </div>
                                </a-form-item>
                            </a-form>
                        </div>
                        <a-card style="
                        width: 300px; height: 188px; 
                        background-color: #f2f6ff;">
                            <template class="ant-card-actions" #actions>
                                <DeleteOutlined key="delete"/>
                                <edit-outlined key="edit" />
                                <ellipsis-outlined key="ellipsis" />
                            </template>
                    
                            <a-card-meta :title="Option_cate[0].name + ' ( ' + Option_int[0].type + ' ) '" 
                                :description=Option_cate[0].description>
                                <template #avatar>
                                    <a-avatar class="integer-avatar">Z</a-avatar>
                                </template>
                            </a-card-meta>
                    
                            <div class="details">
                                <a-tag v-for="it in Option_cate[0].possible_org">
                                    {{ it }}
                                </a-tag>
                            </div>
                        </a-card>
                    </div>
                </a-collapse-panel>
            </a-collapse>
            
            <a-divider />
            <h3> 选项列表 </h3>
            <div class="text">
                在选项列表中可以根据选项的类型对选项进行筛选，可以查看选中的选项的详细信息，并进行编辑或删除。
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
            <h3> 文件格式 </h3>
            <div class="text">
                可以使用上传文件的方式，快速批量地添加选项，具体格式要求如下。
            </div>

            <div class="format">
                <div class="text-border">
                    <code class="text-3"> Model Example </code>
                    <code class="text-3"> Parameters : </code>
                    <code class="text-3"> <span class="name">example-Boolean</span> : <span class="highlight">Boolean</span> </code>
                    <code class="text-3"> <span class="name">example-Integer</span> : <span class="highlight">[ -50 .. 100 ]</span> </code>
                    <code class="text-3"> <span class="name">example-Category</span> : <span class="highlight">{ value-1, value-2, value-3, value-4, value-5 }</span> </code>
                </div>

                <div class="format-details">
                    <code class="text-4"> // 对于 Boolean 类型的选项: "名称 : Boolean" </code>
                    <code class="text-4"> // 对于 Integer 类型的选项: "名称 : [最小值 .. 最大值]" </code>
                    <code class="text-4"> // 对于 Category 类型的选项: "名称 : { 所有可能的取值 }"</code>
                </div>
            </div>
            
            <a-divider />
        </div>
    </div>
</template>

<script>
import Menu from "@/components/menu.vue"
import { defineComponent, ref, watch } from 'vue'
import { PlusOutlined, SettingOutlined, EditOutlined, EllipsisOutlined, DeleteOutlined } from '@ant-design/icons-vue'
import { notification } from 'ant-design-vue'
export default {
    name: 'tutorial_1',
    components: {
        Menu,

        notification,
        PlusOutlined, SettingOutlined, EditOutlined, 
        EllipsisOutlined, DeleteOutlined,
    },
    data() {
        return {
            activeKey: ref(["1"]),
            text: "Test Meow",

            Option: [
                {
                    id: 0,
                    name: "example-Boolean",
                    type: "Boolean",
                    description: "这是一个示例",
                    possible_org: [ "True", "False" ]
                }
            ],

            Option_int: [
                {
                    id: 1,
                    name: "example-Integer",
                    type: "Integer",
                    description: "这是一个示例",
                    min_value: -50,
                    max_value: 100,
                    possible_org: ["-50 ~ 100"]
                }
            ],

            Option_cate: [
                {
                    id: 2,
                    name: "example-Category",
                    type: "Category",
                    description: "这是一个示例",
                    possible_org: ["value-1", "value-2", "value-3",
                    "value-4", "value-5"]
                }
            ],

            all_options: [
                {
                    id: 0,
                    name: "example-Boolean",
                    type: "Boolean",
                    description: "这是一个示例",
                    possible_org: [ "True", "False" ]
                },

                {
                    id: 1,
                    name: "example-Integer",
                    type: "Integer",
                    description: "这是一个示例",
                    min_value: -50,
                    max_value: 100,
                    possible_org: ["-50 ~ 100"]
                },

                {
                    id: 2,
                    name: "example-Category",
                    type: "Category",
                    description: "这是一个示例",
                    possible_org: ["value-1", "value-2", "value-3",
                    "value-4", "value-5"]
                }
            ],

            plainOptions: ["Boolean", "Integer", "Category"],
            display_type: ["Boolean", "Integer", "Category"],

            item: {
                id: 0,
                name: "example-Boolean",
                type: "Boolean",
                description: "这是一个示例",
                possible_org: [ "True", "False" ]
            },

            chosen_id: 0,
        }
    },

    methods: {
        change_checkbox() {
            this.all_options = []
            if(this.display_type.includes("Boolean"))
                this.all_options.push(this.Option[0])
            if(this.display_type.includes("Integer"))
                this.all_options.push(this.Option_int[0])
            if(this.display_type.includes("Category"))
                this.all_options.push(this.Option_cate[0])
            
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
    padding-top: 80px;
    padding-left: 20px;
    display: flex;
    flex-direction: column;
    justify-items: start;
    align-items: flex-start;
    
    color: green;
}

.highlight {
    color: red;
}

.name {
    color: #8294C4;
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

.list-tutorial {
    display: flex;
    flex-direction: row;
    justify-items: start;
}

.text {
    padding-top: 10px;
    padding-bottom: 20px;
    font-size: 18px;
    font-weight: 300;
}

.text-2 {
    padding-bottom: 15px;
    font-size: 16px;
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

.Tag {
    width: 180px;
    display: flex;
    flex-direction: row;
    justify-content: end;
}

.chosen {
    background-color: rgba(0, 0, 1, 0.05);
}

.details {
    width: 100%;
    padding-top: 20px;
}

.integer-float-value {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
}

.option-down {
    padding: 20px;
    background-color: white;

    display: flex;
    flex-direction: row;
}

.option-form {
    /* background-color:aliceblue; */
    width: 400px;
    padding-right: 30px;
}

.integer-float-value {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
}

.category-add {
    display: flex;
    flex-direction: row;
}

.checkboxs {
    display: flex;
    flex-direction: row;
    justify-content: start;
    padding-bottom: 20px;
}

</style>