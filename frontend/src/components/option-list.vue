<template>
    <div class="checkboxs">
        <a-checkbox-group 
        v-model:value="display_type" 
        name="checkboxgroup" 
        :options="plainOptions"
        @change="change_checkbox" />
    </div>
    
    
    <a-list item-layout="horizontal" :data-source="data_display">
        <template #renderItem="{ item, index }">

            <a-list-item v-if="index === chosen_id" class="chosen">
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
                    <!-- <a-tag v-for="it in item.possible">
                        {{ it }}
                    </a-tag>
                    <a-tag v-if="item.possible_org.length > 3">
                        ...
                    </a-tag> -->

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

            <a-list-item v-else @click="set_chosen_id(index)">
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
                    <!-- <a-tag v-for="it in item.possible">
                        {{ it }}
                    </a-tag> -->
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
</template>

<script>
import { defineComponent } from 'vue'
import { message } from 'ant-design-vue'
export default {
    name: "OptionList",
    components: { defineComponent, message, },
    data() {
		return {
            chosen_id: 0,
            receivedMessage: {},
            number: 4,
            data: [],
            data_display: [],
            plainOptions: ["Boolean", "Integer", "Category"],
            display_type: ["Boolean", "Integer", "Category"],
        }
    },
    // watch : {
    //     data : function (new_data, old_data) {
    //         sessionStorage.setItem("option_list_data", this.data)
    //     }
    // },
    mounted() {
        if(this.chosen_id >= this.data.length) {
            this.$emit('notifyChild2', undefined)
            return 
        }
        const new_item = this.data[this.chosen_id]
        this.$emit('notifyChild2', new_item)
    },
    created() {
        // 在组件创建时加载数据
        this.loadDataFromSessionStorage()
    },
    methods: {
        loadDataFromSessionStorage() {
            // 在组件创建时尝试从 sessionStorage 中加载数据
            // const jsonObject = JSON.parse(jsonString)
            const storedData = sessionStorage.getItem("option_list_data")
            if (storedData) {
                this.data = JSON.parse(storedData)
                this.number = this.data.length
                this.chosen_id = 0
                this.receivedMessage = {}
                this.number = this.data.length
                // if(this.number === 0)
                //     this.$emit('notifyChild2', undefined)
            }
            
            this.data_display = []
            for (let i = 0; i < this.data.length; i ++)
                this.data_display.push(this.data[i])
            /*
            chosen_id: 0,
            receivedMessage: {},
            number: 4,
            */
        },

        cleanUp() {

            // chosen_id: 0,
            // receivedMessage: {},
            // number: 4,
            // data:

            this.chosen_id = 0
            this.$emit('notifyChild2', undefined)
            this.receivedMessage = {}
            this.number = 0
            this.data = []
            this.data_display = []
            sessionStorage.setItem("option_list_data", JSON.stringify(this.data))
        },

        delete_option(removedItem) {
            const options = this.data.filter(item => item !== removedItem)
            this.data = options

            const options_display = this.data_display.filter(item => item !== removedItem)
            this.data_display = options_display

            sessionStorage.setItem("option_list_data", JSON.stringify(this.data))

            this.number = this.data.length
            if(this.number > 0)
                this.set_chosen_id(0)
            else {
                this.chosen_id = 0
                this.$emit('notifyChild2', undefined)
            }
        },

        edit_option(old_option, new_option) {
        
            let options = []
            for (let i = 0; i < this.data.length; i ++) {
                if(this.data[i] !== old_option)
                    options.push(this.data[i])
                else options.push(new_option)
            }
            this.data = options

            let options_display = []
            for (let i = 0; i < this.data_display.length; i ++) {
                if(this.data_display[i] !== old_option)
                    options_display.push(this.data_display[i])
                else options_display.push(new_option)
            }
            this.data_display = options_display

            sessionStorage.setItem("option_list_data", JSON.stringify(this.data))
        },

        set_chosen_id(index) {
            this.chosen_id = index
            const new_item = this.data_display[this.chosen_id]
            this.$emit('notifyChild2', new_item)
        },

        change_checkbox() {
            
            // console.log(this.display_type)
            this.data_display = []
            for(let i = 0; i < this.data.length; i ++)
                if(this.display_type.includes(this.data[i].type))
                    this.data_display.push(this.data[i])
            this.set_chosen_id(0)
        },

        executeFunctionInChild(Rmessage) {
            this.receivedMessage = Rmessage
            console.log(this.receivedMessage)

            let new_data = {
                id: 1,
                name: Rmessage.name,
                type: Rmessage.type,
                description: Rmessage.description,
                possible: [],
                possible_org: [],
                min_value: 0,
                max_value: 0,
            }

            for (let i = 0; i < this.data.length; i ++)
                if(this.data[i].name === Rmessage.name) {
                    message.error('选项名称重复')
                    return 
                }

            if(Rmessage.type === "Boolean") {
                new_data.possible.push("True")
                new_data.possible.push("False")

                new_data.possible_org.push("True")
                new_data.possible_org.push("False")
            }
            else if(Rmessage.type === "Integer") {
                if(Rmessage.min_value > Rmessage.max_value) {
                    message.error('最小值大于最大值')
                    return 
                }
                let str = Rmessage.min_value.toString() + " ~ " + Rmessage.max_value.toString()
                new_data.possible.push(str)
                new_data.possible_org.push(str)

                new_data.min_value = Rmessage.min_value
                new_data.max_value = Rmessage.max_value
            }
            else if(Rmessage.type === "Float") {
                if(Rmessage.min_value > Rmessage.max_value) {
                    message.error('最小值大于最大值')
                    return 
                }
                let str = "[ " + Rmessage.min_value.toString() + " , " + Rmessage.max_value.toString() + "]"
                new_data.possible.push(str)
                new_data.possible_org.push(str)

                new_data.min_value = Rmessage.min_value
                new_data.max_value = Rmessage.max_value
            }
            else if(Rmessage.type === "Category") {
                if(Rmessage.possible.length < 1) {
                    message.error('值域不能为空')
                    return 
                }
                new_data.possible.push(Rmessage.possible[0])
                if(Rmessage.possible.length >= 2)
                    new_data.possible.push(Rmessage.possible[1])

                if(Rmessage.possible.length == 3)
                    new_data.possible.push(Rmessage.possible[2])
                else if(Rmessage.possible.length > 3)
                    new_data.possible.push("...")
                
                for (let i = 0; i < Rmessage.possible.length; i ++)
                    new_data.possible_org.push(Rmessage.possible[i])
            }
            
            this.number = this.number + 1
            new_data.id = this.number

            this.data.push(new_data)
            // console.log(this.data_display)
            if(this.display_type.includes(new_data.type))
                this.data_display.push(new_data)
            // console.log(this.data_display)

            this.$emit('addOption', new_data)
            // sessionStorage.setItem("option_list_data", this.data)
            sessionStorage.setItem("option_list_data", JSON.stringify(this.data))
        },
    }
};
</script>

<style scoped>

.checkboxs {
    display: flex;
    flex-direction: row;
    justify-content: start;
    padding-bottom: 20px;
}

.add-constraint {
    display: flex;
    flex-direction: row;
    height: 450px;
}
.add-constraint-left {
    width: 600px;
    background-color: black;
}
.add-constraint-right {
    width: 350px;
    display: flex;
    flex-direction: column;
    align-items: center;
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