<template>
    <div>
        <a-tree show-line=true show-icon=true 
            :default-expanded-keys="['0-0-0', '0-0-1', '0-0-2']"
            @select="onSelect">

            <a-tree-node key="0-0">
                <template #title>
                    <div style="display: flex; flex-direction : row;">
                        <treeTitle :msg="item_.type" :expression="item_.expression"></treeTitle>
                        <div v-if="display_button">
                            <span @click="edit0" style="padding-left: 30px; color: grey;">
                                <a href="#">
                                    <EditOutlined />
                                </a>
                            </span>
                            <span @click="add_son0" style="padding-left: 10px; color: grey;">
                                <a href="#">
                                    <PlusOutlined />
                                </a>
                            </span>
                            <span style="padding-left: 10px; color: grey;">
                                <!-- <DeleteOutlined /> -->
                                <a-popconfirm
                                title="是否确认删除"
                                ok-text="确认" cancel-text="取消"
                                @confirm="confirm0">
                                    <a href="#">
                                        <DeleteOutlined key="delete"/>
                                    </a>
                                </a-popconfirm>
                            </span>
                        </div>
                        
                    </div>
                    
                </template>
                
                <a-tree-node v-for="(node, index) in item_.children" 
                :key="'0-0-' + index.toString()">
                    <template #title>
                        <div style="display: flex; flex-direction : row;">
                            <treeTitle :msg="node.type" :expression="node.expression"></treeTitle>
                            <div v-if="display_button">
                                <span @click="edit1(index)" style="padding-left: 30px; color: grey;">
                                    <a href="#"><EditOutlined /></a>
                                </span>
                                <span @click="add_son1(index)" style="padding-left: 10px; color: grey;">
                                    <a href="#"><PlusOutlined /></a>
                                </span>
                                <span style="padding-left: 10px; color: grey;">
                                    <a-popconfirm
                                    title="是否确认删除"
                                    ok-text="确认" cancel-text="取消"
                                    @confirm="confirm1(index)">
                                        <a href="#">
                                            <DeleteOutlined key="delete"/>
                                        </a>
                                    </a-popconfirm>
                                </span>
                            </div>
                        </div>
                    </template>
                    <a-tree-node v-for="(node1, index1) in node.children" 
                    :key="'0-0-' + index.toString() + '-' + index1.toString()">
                        <template #title>
                            <div style="display: flex; flex-direction : row;">
                                <treeTitle :msg="node1.type" :expression="node1.expression"></treeTitle>
                                <div v-if="display_button">
                                    <span @click="edit2(index, index1)" style="padding-left: 30px; color: grey;">
                                        <a href="#"><EditOutlined /></a>
                                    </span>
                                    <span @click="add_son2(index, index1)" style="padding-left: 10px; color: grey;">
                                        <a href="#"><PlusOutlined /></a>
                                    </span>
                                    <span @click="set_selected" style="padding-left: 10px; color: grey;">
                                        <a-popconfirm
                                        title="是否确认删除"
                                        ok-text="确认" cancel-text="取消"
                                        @confirm="confirm2(index, index1)">
                                            <a href="#">
                                                <DeleteOutlined key="delete"/>
                                            </a>
                                        </a-popconfirm>
                                    </span>
                                </div>
                            </div>
                        </template>
                        <a-tree-node v-for="(node2, index2) in node1.children" 
                        :key="'0-0-' + index.toString() + '-' + index1.toString() + '-' + index2.toString()">
                            <template #title>
                                <div style="display: flex; flex-direction : row;">
                                    <treeTitle :msg="node2.type" :expression="node2.expression"></treeTitle>
                                    <div v-if="display_button">
                                        <span @click="edit3(index, index1, index2)" style="padding-left: 30px; color: grey;">
                                            <a href="#"><EditOutlined /></a>
                                        </span>
                                        <span @click="add_son3(index, index1, index2)" style="padding-left: 10px; color: grey;">
                                            <a href="#"><PlusOutlined /></a>
                                        </span>
                                        <span style="padding-left: 10px; color: grey;">
                                            <a-popconfirm
                                            title="是否确认删除"
                                            ok-text="确认" cancel-text="取消"
                                            @confirm="confirm3(index, index1, index2)">
                                                <a href="#">
                                                    <DeleteOutlined key="delete"/>
                                                </a>
                                            </a-popconfirm>
                                        </span>
                                    </div>
                                </div>
                            </template>
                            <a-tree-node v-for="(node3, index3) in node2.children" 
                            :key="'0-0-' + index.toString() + '-' + index1.toString() + '-' + index2.toString() + '-' + index3.toString()">
                                <template #title>
                                    <div style="display: flex; flex-direction : row;">
                                        <treeTitle :msg="node3.type" :expression="node3.expression"></treeTitle>
                                        <div v-if="display_button">
                                            <span @click="edit4(index, index1, index2, index3)" style="padding-left: 30px; color: grey;">
                                                <a href="#"><EditOutlined /></a>
                                            </span>
                                            <span @click="add_son4(index, index1, index2, index3)" style="padding-left: 10px; color: grey;">
                                                <a href="#"><PlusOutlined /></a>
                                            </span>
                                            <span style="padding-left: 10px; color: grey;">
                                                <a-popconfirm
                                                title="是否确认删除"
                                                ok-text="确认" cancel-text="取消"
                                                @confirm="confirm4(index, index1, index2, index3)">
                                                    <a href="#">
                                                        <DeleteOutlined key="delete"/>
                                                    </a>
                                                </a-popconfirm>
                                            </span>
                                        </div>
                                    </div>
                                </template>
                                <a-tree-node v-for="(node4, index4) in node3.children" 
                                :key="'0-0-' + index.toString() + '-' + index1.toString() + '-' + index2.toString() + '-' + index3.toString() + '-' + index4.toString()">
                                    <template #title>
                                        <div style="display: flex; flex-direction : row;">
                                            <treeTitle :msg="node4.type" :expression="node4.expression"></treeTitle>
                                            <div v-if="display_button">
                                                <span @click="edit5(index, index1, index2, index3, index4)" style="padding-left: 30px; color: grey;">
                                                    <a href="#"><EditOutlined /></a>
                                                </span>
                                                <span @click="add_son5(index, index1, index2, index3, index4)" style="padding-left: 10px; color: grey;">
                                                    <a href="#"><PlusOutlined /></a>
                                                </span>
                                                <span style="padding-left: 10px; color: grey;">
                                                    <a-popconfirm
                                                    title="是否确认删除"
                                                    ok-text="确认" cancel-text="取消"
                                                    @confirm="confirm5(index, index1, index2, index3, index4)">
                                                        <a href="#">
                                                            <DeleteOutlined key="delete"/>
                                                        </a>
                                                    </a-popconfirm>
                                                </span>
                                            </div>
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
</template>

<script>
import { defineComponent } from 'vue'
import treeTitle from "@/components/tree-title.vue"
import { SettingOutlined, EditOutlined, EllipsisOutlined, DeleteOutlined, PlusOutlined } from '@ant-design/icons-vue'
export default {
    name: "Tree2",
    components: {
        treeTitle,

        SettingOutlined,
        EditOutlined,
        EllipsisOutlined,
        DeleteOutlined,
        PlusOutlined,

        defineComponent,
    },

    data() {
        return {
            item_: {
                description: "This is a description",
                expression: "(((not((Par16!=true)))=>(Par4=false))OR((Par9!=false)=>(not((Par12!=false)))))=>(((not((Par16!=false)))=>(Par16!=false))<=>((not((Par4=true)))AND(not((Par0!=true)))))", 
                type: "=>", 
                component: [
                    { name : 'Par0', type : "Boolean" }, 
                    { name : 'Par4', type : "Boolean" }, 
                    { name : 'Par9', type : "Boolean" },
                    { name : 'Par12', type : "Boolean" },
                    { name : 'Par16', type : "Boolean" },
                ],
                children: [
                    {"expression": "((not((Par16!=true)))=>(Par4=false))OR((Par9!=false)=>(not((Par12!=false))))", "type": "OR", "children": [{"expression": "(not((Par16!=true)))=>(Par4=false)", "type": "=>", "children": [{"expression": "not((Par16!=true))", "type": "not", "children": [{"expression": "Par16!=true", "type": "!=", "children": []}]}, {"expression": "Par4=false", "type": "=", "children": []}]}, {"expression": "(Par9!=false)=>(not((Par12!=false)))", "type": "=>", "children": [{"expression": "Par9!=false", "type": "!=", "children": []}, {"expression": "not((Par12!=false))", "type": "not", "children": [{"expression": "Par12!=false", "type": "!=", "children": []}]}]}]}, {"expression": "((not((Par16!=false)))=>(Par16!=false))<=>((not((Par4=true)))AND(not((Par0!=true))))", "type": "<=>", "children": [{"expression": "(not((Par16!=false)))=>(Par16!=false)", "type": "=>", "children": [{"expression": "not((Par16!=false))", "type": "not", "children": [{"expression": "Par16!=false", "type": "!=", "children": []}]}, {"expression": "Par16!=false", "type": "!=", "children": []}]}, {"expression": "(not((Par4=true)))AND(not((Par0!=true)))", "type": "AND", "children": [{"expression": "not((Par4=true))", "type": "not", "children": [{"expression": "Par4=true", "type": "=", "children": []}]}, {"expression": "not((Par0!=true))", "type": "not", "children": [{"expression": "Par0!=true", "type": "!=", "children": []}]}]}]}
                ],
            },
            selectedKeys : "0-0-0",
            display_button : true,
        }
    },

    methods: {

        test() {
            console.log('test')
        },
        
        get_item(new_item) {
            this.item_ = new_item
            console.log('get_item', this.item_)
        },

        set_selected() {
            console.log("click")
        },
        add_son0() {
            console.log("root")
            this.$emit('add_con_node', undefined)
        },
        add_son1(index) {
            // console.log(index)
            const array = [index]
            this.$emit('add_con_node', array)
        },
        add_son2(index, index1) {
            // console.log(index, index1)
            let array = [index, index1]
            this.$emit('add_con_node', array)
        },
        add_son3(index, index1, index2) {
            // console.log(index, index1, index2)
            let array = [index, index1, index2]
            this.$emit('add_con_node', array)
        },
        add_son4(index, index1, index2, index3) {
            // console.log(index, index1, index2, index3)
            let array = [index, index1, index2, index3]
            this.$emit('add_con_node', array)
        },
        add_son5(index, index1, index2, index3, index4) {
            // console.log(index, index1, index2, index3, index4)
            let array = [index, index1, index2, index3, index4]
            this.$emit('add_con_node', array)
        },

        confirm0() {
            console.log("root")
            this.$emit('delete_con_node', undefined)
            this.item_ = undefined
        },
        confirm1(index) {
            // console.log(index)
            const array = [index]
            this.$emit('delete_con_node', array)
            this.item_.children.splice(index, 1)
        },
        confirm2(index, index1) {
            // console.log(index, index1)
            let array = [index, index1]
            this.$emit('delete_con_node', array)
        },
        confirm3(index, index1, index2) {
            // console.log(index, index1, index2)
            let array = [index, index1, index2]
            this.$emit('delete_con_node', array)
        },
        confirm4(index, index1, index2, index3) {
            // console.log(index, index1, index2, index3)
            let array = [index, index1, index2, index3]
            this.$emit('delete_con_node', array)
        },
        confirm5(index, index1, index2, index3, index4) {
            // console.log(index, index1, index2, index3, index4)
            let array = [index, index1, index2, index3, index4]
            this.$emit('delete_con_node', array)
        },

        edit0() {
            console.log("root")
            this.$emit('edit_con_node', [])
        },
        edit1(index) {
            // console.log(index)
            const array = [index]
            this.$emit('edit_con_node', array)
        },
        edit2(index, index1) {
            // console.log(index, index1)
            let array = [index, index1]
            this.$emit('edit_con_node', array)
        },
        edit3(index, index1, index2) {
            // console.log(index, index1, index2)
            let array = [index, index1, index2]
            this.$emit('edit_con_node', array)
        },
        edit4(index, index1, index2, index3) {
            // console.log(index, index1, index2, index3)
            let array = [index, index1, index2, index3]
            this.$emit('edit_con_node', array)
        },
        edit5(index, index1, index2, index3, index4) {
            // console.log(index, index1, index2, index3, index4)
            let array = [index, index1, index2, index3, index4]
            this.$emit('edit_con_node', array)
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