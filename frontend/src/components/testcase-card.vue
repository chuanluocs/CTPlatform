<template>
    <a-list item-layout="horizontal" :data-source="data"
    style="background-color: #f2f6ff;">
        <template #renderItem="{ item, index }">
            <a-list-item>
                <a-list-item-meta
                    :description = item.description>
                    <template #title>
                        {{ item.name + " ( " + item.type + " ) " }}
                    </template>
                    
                    <template #avatar>
                        <!-- <a-avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" /> -->
                        <a-avatar v-if="item.type === 'Boolean'" class="boolean-avatar">01</a-avatar>
                        <a-avatar v-if="item.type === 'Integer'" class="integer-avatar">Z</a-avatar>
                        <a-avatar v-if="item.type === 'Float'" class="float-avatar">R</a-avatar>
                        <a-avatar v-if="item.type === 'Category'" class="category-avatar">C</a-avatar>
                    </template>
                </a-list-item-meta>
                
                <div class="Tag">
                    <!-- <a-tag color="purple" size="large">
                        {{ item.value }}
                    </a-tag> -->
                    <a-button danger>
                        {{ item.value }}
                    </a-button>
                </div>
            </a-list-item>
        </template>
    </a-list>
</template>

<script>
import { defineComponent } from 'vue'
import { message } from 'ant-design-vue'
export default {
    name: "TestcaseCard",
    components: { defineComponent, message, },
    data() {
        return {
            data: [
                {
                    id: 1,
                    name: "Meow",
                    type: "Boolean",
                    description: "Meow Meow Meow",
                    value: "True",
                },
                {
                    id: 2,
                    name: "QAQ",
                    type: "Integer",
                    description: "This is a description.",
                    value: "-5",
                },
                {
                    id: 3,
                    name: "QAQ-Meow",
                    type: "Float",
                    description: "This is a description Meow.",
                    value: "2.0",
                },
                {
                    id: 4,
                    name: "A",
                    type: "Category",
                    description: "This is NekoPara Meow Meow.",
                    value: "B-type",
                },
            ]
        }
    },

    methods:{
        executeFunctionInTcCard(new_item) {
            console.log(new_item)
            this.data = new_item
        }
    },
};
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

.chosen {
    background-color: rgba(0, 0, 1, 0.05);
}

.Tag {
    width: 180px;
    display: flex;
    flex-direction: row;
    justify-content: end;
}
</style>