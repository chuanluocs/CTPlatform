<template>
    <div class="Card">
        <a-card>
            <div class="card-buttons">
                <a-button type="text" @click="delete_constraint"
                :disabled = "data === undefined">
                    <DeleteOutlined></DeleteOutlined>
                </a-button>
                <a-button type="text" :disabled = "data === undefined">
                    <edit-outlined></edit-outlined>
                </a-button>
                <a-button type="text" :disabled = "data === undefined">
                    <ellipsis-outlined></ellipsis-outlined>
                </a-button>
            </div>
        </a-card>
        
        <a-list v-if="data !== undefined" item-layout="horizontal" :data-source="data"
            style="padding: 0;">
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
                        <a-tag v-for="it in item.possible">
                            {{ it }}
                        </a-tag>
                    </div>
                </a-list-item>
            </template>
        </a-list>

        <div v-else>
            <a-empty></a-empty>
        </div>
    </div>
</template>

<script>
import { defineComponent } from 'vue'
import { message } from 'ant-design-vue'
import { EditOutlined, EllipsisOutlined, DeleteOutlined } from '@ant-design/icons-vue';
export default {
    name: "ConstraintCard",
    components: { 
        defineComponent, message,
        EditOutlined, EllipsisOutlined, DeleteOutlined,
    },
    data() {
        return {
            data: [
                {
                    id: 1,
                    name: "Meow",
                    type: "Boolean",
                    description: "Meow Meow Meow",
                    possible: ["True", "False"],
                    possible_org: ["True", "False"],
                    min_value: 0,
                    max_value: 0,
                },
                {
                    id: 2,
                    name: "QAQ",
                    type: "Integer",
                    description: "This is a description.",
                    possible: ["-5 ~ 10"],
                    possible_org: ["-5 ~ 10"],
                    min_value: 0,
                    max_value: 0,
                },
                {
                    id: 3,
                    name: "QAQ-Meow",
                    type: "Float",
                    description: "This is a description Meow.",
                    possible: ["(1.0, 55.8)"],
                    possible_org: ["(1.0, 55.8)"],
                    min_value: 0,
                    max_value: 0,
                },
                {
                    id: 4,
                    name: "A",
                    type: "Category",
                    description: "This is NekoPara Meow Meow.",
                    possible: ["A-type", "B-type", "..."],
                    possible_org: ["A-type", "B-type", "C-type", "D-type"],
                    min_value: 0,
                    max_value: 0,
                },
            ]
        }
    },

    methods:{
        executeFunctionInConCard(new_item) {
            console.log(new_item)
            this.data = new_item
        },

        delete_constraint() {
            this.$emit('deleteCon', this.data)
        }
    },
};
</script>
    
<style scoped>

.Card {
    display: flex;
    flex-direction: column;
}

.card-buttons {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    padding: 0;
}

.buttons {
    color: rgba(0, 0, 0, 0.88);
    font-size: 14px;
    line-height: 1.5714285714285714;
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