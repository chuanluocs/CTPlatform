<template>
    <div>
        <a-tree show-line=true show-icon=true 
            :default-expanded-keys="['0-0-0', '0-0-1', '0-0-2']"
            @select="onSelect" >

            <a-tree-node key="0-0">
                <template #title>
                    <treeTitle :msg="item.type" :expression="item.expression"></treeTitle>
                </template>
                
                <a-tree-node v-for="(node, index) in item.children" :key="'0-0-' + index.toString()">
                    <template #title>
                        <treeTitle :msg="node.type" :expression="node.expression"></treeTitle>
                    </template>

                    <a-tree-node v-for="(node1, index1) in node.children" 
                    :key="'0-0-' + index.toString() + '-' + index1.toString()">
                        <template #title>
                            <treeTitle :msg="node1.type" :expression="node1.expression"></treeTitle>
                        </template>

                        <a-tree-node v-for="(node2, index2) in node1.children" 
                        :key="'0-0-' + index.toString() + '-' + index1.toString() + index2.toString()">
                            <template #title>
                                <treeTitle :msg="node2.type" :expression="node2.expression"></treeTitle>
                            </template>

                            <a-tree-node v-for="(node3, index3) in node2.children" 
                            :key="'0-0-' + index.toString() + '-' + index1.toString() + index2.toString() + index3.toString()">
                                <template #title>
                                    <treeTitle :msg="node3.type" :expression="node3.expression"></treeTitle>
                                </template>
                                <a-tree-node v-for="(node4, index4) in node3.children" 
                                :key="'0-0-' + index.toString() + '-' + index1.toString() + index2.toString() + index3.toString() + index4.toString()">
                                    <template #title>
                                        <treeTitle :msg="node4.type" :expression="node4.expression"></treeTitle>
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
import treeTitle from "@/components/tree-title.vue"
export default {
    name: "tmpCard",
    components: {
        treeTitle,
    },
    data() {
        return {
            item: {
                description: "This is a description",
                expression: "((((not (Par7 = true)) OR Par7 = false) AND (Par8 = true OR Par7 = true)) OR (Par2 = true))",
                type: "OR",
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
    }
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