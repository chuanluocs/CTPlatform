<template>
    <div class="constraint-list">
        <a-list item-layout="horizontal" :data-source="constraints_display">
            <template #renderItem="{ item, index }">
                <a-list-item :class="index === chosen_id ? 'chosen' : 'normal'"
                    @click="set_chosen_id(index)">
                    <a-list-item-meta
                    :description = "item.expression">
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
</template>

<script>
import optAvatar from "@/components/opt-avatar.vue"
import { get_constraint_obj, download_model } from "@/utils/api"
import { ref } from 'vue'
import { message } from 'ant-design-vue'
export default {
    name: "ConstraintList2",
    components: {
        optAvatar, message,
    },
    data() {
		return {
            chosen_id: 0,
            screen_list: [],
            isScreened: false,
            constraints_display: ref([]),
            constraints: ref([])
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
        },

        Download_Model() {
            const options = JSON.parse(sessionStorage.getItem("option_list_data"))
            const constraints = this.constraints
            download_model({
                options : options,
                constraints : constraints
            }).then((response) => {
                const blob = new Blob([response.data], { type: "text/plain" })

                // 创建一个下载链接
                const downloadLink = document.createElement('a')
                downloadLink.href = window.URL.createObjectURL(blob)
                downloadLink.download = "model-file.txt" // 使用 .xls 扩展名
                // 模拟用户点击链接以触发下载
                downloadLink.click()

            }).catch(error => {
                // console.error(error);
                message.error("下载失败")
            });
        },

        delete_constraint(removedItem) {
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

        edit_con(old_constraint, new_constraint) {
            const constraints = []
            for(let i = 0; i < this.constraints.length; i ++) {
                if(this.constraints[i].key === old_constraint.key)
                    constraints.push(new_constraint)
                else constraints.push(this.constraints[i])    
            }
            this.constraints = constraints

            // console.log(this.constraints_display[this.chosen_id].expression)
            // console.log(old_constraint.expression)
            // console.log(this.constraints_display[this.chosen_id] === old_constraint)

            const constraints_display = []
            for(let i = 0; i < this.constraints_display.length; i ++) {
                if(this.constraints_display[i].key === old_constraint.key)
                    constraints_display.push(new_constraint)
                else constraints_display.push(this.constraints_display[i])    
            }
            this.constraints_display = constraints_display
            
            // console.log(this.constraints_display[this.chosen_id].expression)
            this.set_chosen_id(this.chosen_id)

            sessionStorage.setItem("constraint_list_data", JSON.stringify(this.constraints))
        },

        cleanUp() {
            this.chosen_id = 0
            this.screen_list = []
            this.constraints_display = []
            this.constraints = []
            this.$emit('notifyConCard', undefined)

            sessionStorage.setItem("constraint_list_data", JSON.stringify(this.constraints))
        },

        add_constraint(new_constraint) {
            console.log(new_constraint)

            this.constraints.push(new_constraint)
            sessionStorage.setItem("constraint_list_data", JSON.stringify(this.constraints))
        
            if(! this.isScreened)
                this.constraints_display.push(new_constraint)
            else {
                let flag = false
                for (let i = 0; i < new_constraint.component.length; i ++)
                    if(screen_list.includes(new_constraint.component[i].name)) {
                        flag = true; 
                        break ;
                    }
                if(flag)
                    this.constraints_display.push(new_constraint)
            }

            if(this.constraints_display.length === 1)
                this.set_chosen_id(0)
        },

        set_screen(screen_list) {
            this.isScreened = true
            this.screen_list = screen_list
            this.constraints_display = []
            for(let i = 0; i < this.constraints.length; i ++) {
                let flag = false
                for(let j = 0; j < this.constraints[i].component.length; j ++) 
                    if(screen_list.includes(this.constraints[i].component[j].name)){
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

        set_chosen_id(index) {
            this.chosen_id = index
            if(this.constraints.length > index) {
                const new_item = this.constraints[this.chosen_id]
                this.$emit('notifyConCard', new_item)
            }
            else
                this.$emit('notifyConCard', undefined)
        },
    },
}
</script>

<style>

.chosen {
    background-color: rgba(0, 0, 1, 0.05);
}

.normal {
    background-color: white;
}

.constraint-list {
    width: 780px;
}

.list-right {
    display: flex;
    flex-direction: column;
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
</style>