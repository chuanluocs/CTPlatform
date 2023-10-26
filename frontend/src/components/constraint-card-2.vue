<template>
    <a-card style="width: 400px; background-color: #f2f6ff;">

        <span v-if="item != undefined" style="font-size: 16px; font-weight: 500;">
            {{ item.description }} 
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
            
            <edit-outlined key="edit" @click="edit_constraint" />
            <ellipsis-outlined key="ellipsis" />
        </template>

        <div v-if="item != undefined">
            <a-tree show-line=true show-icon=true 
            :default-expanded-keys="['0-0-0', '0-0-1', '0-0-2']"
            @select="onSelect">

                <a-tree-node key="0-0">
                    <template #title>
                        <div style="display: flex; flex-direction : row;">
                            <treeTitle :msg="item.type" :expression="item.expression"></treeTitle>
                        </div>
                    </template>
                    
                    <a-tree-node v-for="(node, index) in item.children" 
                    :key="'0-0-' + index.toString()">
                        <template #title>
                            <div style="display: flex; flex-direction : row;">
                                <treeTitle :msg="node.type" :expression="node.expression"></treeTitle>
                            </div>
                        </template>
                        <a-tree-node v-for="(node1, index1) in node.children" 
                        :key="'0-0-' + index.toString() + '-' + index1.toString()">
                            <template #title>
                                <div style="display: flex; flex-direction : row;">
                                    <treeTitle :msg="node1.type" :expression="node1.expression"></treeTitle>
                                </div>
                            </template>
                            <a-tree-node v-for="(node2, index2) in node1.children" 
                            :key="'0-0-' + index.toString() + '-' + index1.toString() + '-' + index2.toString()">
                                <template #title>
                                    <div style="display: flex; flex-direction : row;">
                                        <treeTitle :msg="node2.type" :expression="node2.expression"></treeTitle>
                                    </div>
                                </template>
                                <a-tree-node v-for="(node3, index3) in node2.children" 
                                :key="'0-0-' + index.toString() + '-' + index1.toString() + '-' + index2.toString() + '-' + index3.toString()">
                                    <template #title>
                                        <div style="display: flex; flex-direction : row;">
                                            <treeTitle :msg="node3.type" :expression="node3.expression"></treeTitle>
                                        </div>
                                    </template>
                                    <a-tree-node v-for="(node4, index4) in node3.children" 
                                    :key="'0-0-' + index.toString() + '-' + index1.toString() + '-' + index2.toString() + '-' + index3.toString() + '-' + index4.toString()">
                                        <template #title>
                                            <div style="display: flex; flex-direction : row;">
                                                <treeTitle :msg="node4.type" :expression="node4.expression"></treeTitle>
                                            </div>
                                        </template>
                                    </a-tree-node>
                                </a-tree-node>
                            </a-tree-node>
                        </a-tree-node>
                    </a-tree-node>
                </a-tree-node>
            </a-tree>
        </div>

        <div v-else>
            <a-empty></a-empty>
        </div>
    </a-card>
</template>

<script>
import { defineComponent } from 'vue'
import treeTitle from "@/components/tree-title.vue"
import { SettingOutlined, EditOutlined, EllipsisOutlined, DeleteOutlined } from '@ant-design/icons-vue'
export default {
    name: "ConstraintCard2",
    components: {
        treeTitle,

        SettingOutlined,
        EditOutlined,
        EllipsisOutlined,
        DeleteOutlined,

        defineComponent,
    },
    data() {
        return {
            item: {
                description: "This is a description",
                expression: "((((not (Par7 = true)) OR Par7 = false) AND (Par8 = true OR Par7 = true)) OR (Par2 = true))",
                type: "OR",
                component : [
                    // ['Par2', 'Par7', 'Par8']
                    { name : 'Par2', type : "Boolean" }, 
                    { name : 'Par7', type : "Boolean" }, 
                    { name : 'Par8', type : "Boolean" }
                ],
                children: [
                    {
                        // ((not (Par7 = true)) OR Par7 = false) 
                        // AND 
                        // (Par8 = true OR Par7 = true)
                        expression: "((not (Par7 = true)) OR Par7 = false) AND (Par8 = true OR Par7 = true)",
                        type: "AND",
                        children: [
                            {
                                // (not (Par7 = true)) OR Par7 = false
                                expression: "(not (Par7 = true)) OR Par7 = false",
                                type: "OR",
                                children: [
                                    {
                                        expression: "not (Par7 = true)",
                                        type: "not",
                                        children: [
                                            {
                                                expression: "Par7 = true",
                                                type: "=",
                                                children: [],
                                            }
                                        ],
                                    },
                                    {
                                        expression: "Par7 = false",
                                        type: "=",
                                        children: [],
                                    }
                                ]
                            },
                            {
                                // (Par8 = true OR Par7 = true)
                                expression: "Par8 = true OR Par7 = true",
                                type: "OR",
                                children: [
                                    {
                                        expression: "Par8 = true",
                                        type: "=",
                                        children: [],
                                    },
                                    {
                                        expression: "Par7 = true",
                                        type: "=",
                                        children: [],
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        // Par2 = true
                        expression: "Par2 = true",
                        type: "=",
                        children: []
                    }
                ]
            },
        }
    },
    methods: {
        executeFunctionInConCard(new_item) {
            this.item = new_item
        },
        confirm() {
            this.$emit('deleteCon', this.item)
        },
        edit_constraint() {
            this.$emit('editCon', this.item)
        },
    },
}
</script>

<style scoped>

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

.or-avatar {
    background-color: #BFACE2;
    color: white;
    font-weight: 400;
}

.and-avatar {
    background-color: #BFACE2;
    color: white;
    font-weight: 400;
}

.implies-avatar {
    background-color: #BFACE2;
    color: white;
    font-weight: 400;
}

.same-avatar {
    background-color: #BFACE2;
    color: white;
    font-weight: 400;
}

.not-avatar {
    background-color: #BFACE2;
    color: white;
    font-weight: 400;
}

.title-font {
    padding-left: 10px;
    font-weight: 300;
    font-size: 16px;
    padding-top: 10px;
}

</style>