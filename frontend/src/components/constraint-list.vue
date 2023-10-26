<template>
    <!-- <h1>Meow</h1> -->
    <a-list item-layout="horizontal" :data-source="constraints_display"
        style="width: 780px">
        <template #renderItem="{ item, index }">
            <a-list-item v-if="index === chosen_id" class="chosen">
                <div class="list-item">
                    <div v-for="(it, index) in item" class="items">
                        <div v-if="index > 0 && index < 3" class="in_items">
                            <!-- <a-avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" /> -->
                            <a-avatar class="union-avatar">V</a-avatar>
                        </div>
                        <div v-if="index < 3" class="in_items">
                            <!-- <a-avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" /> -->
                            <a-avatar v-if="it.type === 'Boolean'" class="boolean-avatar">01</a-avatar>
                            <a-avatar v-if="it.type === 'Integer'" class="integer-avatar">Z</a-avatar>
                            <a-avatar v-if="it.type === 'Float'" class="float-avatar">R</a-avatar>
                            <a-avatar v-if="it.type === 'Category'" class="category-avatar">C</a-avatar>
                        </div>
                        <div v-if="index < 3" class="in_items" style="padding-left: 10px; font-weight: 500; font-size: 18px;">
                            {{ it.name }}
                        </div>
                        <div v-if="index < 3" class="in_items" style="padding-left: 10px;">
                            <a-tag v-for="tg in it.possible">
                                {{ tg }}
                            </a-tag>
                        </div>
                    </div>

                    <div v-if="item.length > 3" class="items">
                        <div  class="in_items" style="padding-left: 10px; font-weight: 500; font-size: 18px;">
                            ...
                        </div>
                    </div>
                </div>
            </a-list-item>

            <a-list-item v-else @click="set_chosen_id(index)">
                <div class="list-item">
                    <div v-for="(it, index) in item" class="items">
                        <div v-if="index > 0 && index < 3" class="in_items">
                            <!-- <a-avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" /> -->
                            <a-avatar class="union-avatar">V</a-avatar>
                        </div>
                        <div v-if="index < 3" class="in_items">
                            <!-- <a-avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" /> -->
                            <a-avatar v-if="it.type === 'Boolean'" class="boolean-avatar">01</a-avatar>
                            <a-avatar v-if="it.type === 'Integer'" class="integer-avatar">Z</a-avatar>
                            <a-avatar v-if="it.type === 'Float'" class="float-avatar">R</a-avatar>
                            <a-avatar v-if="it.type === 'Category'" class="category-avatar">C</a-avatar>
                        </div>
                        <div  v-if="index < 3" class="in_items" style="padding-left: 10px; font-weight: 500; font-size: 18px;">
                            {{ it.name }}
                        </div>
                        <div  v-if="index < 3" class="in_items" style="padding-left: 10px;">
                            <a-tag v-for="tg in it.possible">
                                {{ tg }}
                            </a-tag>
                        </div>
                    </div>

                    <div v-if="item.length > 3" class="items">
                        <div  class="in_items" style="padding-left: 10px; font-weight: 500; font-size: 18px;">
                            ...
                        </div>
                    </div>
                </div>
            </a-list-item>
        </template>
    </a-list>
</template>

<script>
import { PlusOutlined } from '@ant-design/icons-vue'
export default {
    name: "ConstraintList",
    components: { 
        PlusOutlined, 
    },
    data() {
		return {
            chosen_id: 0,
            screen_list: [],
            isScreened: false,
            constraints_display: [],
            constraints: [
                [
                    {
                        id: 1,
                        name: "Meow",
                        type: "Boolean",
                        description: "Meow Meow Meow",
                        possible: ["True"],
                        possible_org: ["True"],
                    },

                    {
                        id: 2,
                        name: "QAQ",
                        type: "Integer",
                        description: "This is a description.",
                        possible: ["-5 ~ 5"],
                        possible_org: ["-5 ~ 5"],
                    },

                    {
                        id: 3,
                        name: "A",
                        type: "Category",
                        description: "This is NekoPara Meow Meow.",
                        possible: ["A-type", "..."],
                        possible_org: ["A-type", "B-type", "C-type"],
                    },
                ],

                [
                    {
                        id: 1,
                        name: "qwq",
                        type: "Boolean",
                        description: "Meow Meow Meow",
                        possible: ["True"],
                    },

                    {
                        id: 2,
                        name: "YUKI",
                        type: "Boolean",
                        description: "Meow Meow Meow",
                        possible: ["True"],
                    },
                    
                ],
            ],
        }
    },

    mounted() {
        if(this.chosen_id >= this.constraints.length) {
            this.$emit('notifyConCard', undefined)
            return 
        }
        const new_item = this.constraints[this.chosen_id]
        this.$emit('notifyConCard', new_item)
    },
    
    created() {
        // 在组件创建时加载数据
        this.loadDataFromSessionStorage()
    },
    methods: {
        loadDataFromSessionStorage() {
            const storedData = sessionStorage.getItem("constraint_list_data")
            if (storedData)
                this.constraints = JSON.parse(storedData)
            
            this.isScreened = false
            this.screen_list = []
            this.constraints_display = []
            for(let i = 0; i < this.constraints.length; i ++)
                this.constraints_display.push(this.constraints[i])
            
            this.chosen_id = 0
            // if(this.constraints_display.length === 0)
            //     this.$emit('notifyConCard', undefined)
        },

        delete_constraint(removedItem) {
            // console.log(removedItem)
            const constraints = this.constraints.filter(item => item !== removedItem)
            this.constraints = constraints
            sessionStorage.setItem("constraint_list_data", JSON.stringify(this.constraints))

            this.set_chosen_id(0)
            this.constraints_display = []
            if(this.isScreened)
                this.set_screen(this.screen_list)
            
            else {
                for(let i = 0; i < this.constraints.length; i ++)
                    this.constraints_display.push(this.constraints[i])
            }
        },

        cleanUp() {
            this.chosen_id = 0
            this.screen_list = []
            this.constraints_display = []
            this.constraints = []
            this.$emit('notifyConCard', undefined)

            sessionStorage.setItem("constraint_list_data", JSON.stringify(this.constraints))
        },

        set_chosen_id(index) {
            this.chosen_id = index
            if(this.constraints.length > index) {
                const new_item = this.constraints[this.chosen_id]
                this.$emit('notifyConCard', new_item)
            }
            else
                this.$emit('notifyConCard', undefined)
        },

        add_constraint(new_constraint) {
            this.constraints.push(new_constraint)
            sessionStorage.setItem("constraint_list_data", JSON.stringify(this.constraints))
            
            if(this.isScreened) {
                console.log(this.screen_list)
                console.log(new_constraint)
                for(let i = 0; i < new_constraint.length; i ++)
                    if(this.screen_list.includes(new_constraint[i].name)) {
                        console.log(new_constraint[i])
                        this.constraints_display.push(new_constraint)
                        break
                    }
            }
            else
                this.constraints_display.push(new_constraint)
            
            if(this.constraints_display.length === 1)
                this.set_chosen_id(0)
        },

        set_screen(screen_list) {
            this.isScreened = true
            this.screen_list = screen_list
            this.constraints_display = []
            for(let i = 0; i < this.constraints.length; i ++) {
                let flag = false
                for(let j = 0; j < this.constraints[i].length; j ++)
                    if(screen_list.includes(this.constraints[i][j].name)) {
                        flag = true
                        break
                    }
                if(flag)
                    this.constraints_display.push(this.constraints[i])
            }
            this.set_chosen_id(0)
        },
        cancel_screen() {
            this.isScreened = false
            this.screen_list = []
            this.constraints_display = []
            for(let i = 0; i < this.constraints.length; i ++)
                this.constraints_display.push(this.constraints[i])
            this.set_chosen_id(0)
        },
    },
}
</script>

<style scoped>

.union-avatar {
    background-color: transparent;
    color: #8294C4;
    font-weight: 350;
    font-size: 25px;
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

.list-item {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
}

.items {
    display: flex;
    flex-direction: row;
    align-items: center;
}

.in_items {
    width: 60px;
    /* background-color: red; */
}

.Tag {
    width: 180px;
    display: flex;
    flex-direction: row;
    justify-content: end;
}

</style>