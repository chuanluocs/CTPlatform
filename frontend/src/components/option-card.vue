<template>
    <a-card v-if="item !== undefined" 
        style="width: 300px; background-color: #f2f6ff;">
 
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

    <a-modal v-model:open="visible" title="编辑选项" @ok="handleOk"
    cancelText="取消" okText="确定">
        <!-- <p>Some contents...</p>
        <p>Some contents...</p>
        <p>Some contents...</p> -->
        <a-form style="padding: 30px">
            
            <a-form-item label="名称">
                <a-input v-model:value="formState.name" />
            </a-form-item>

            <a-form-item label="类型">
                <a-select v-model:value="formState.type" placeholder="请选择选项类型">
                    <a-select-option value="Boolean"> Boolean </a-select-option>
                    <a-select-option value="Integer"> Integer </a-select-option>
                    <!-- <a-select-option value="Float"> Float </a-select-option> -->
                    <a-select-option value="Category"> Category </a-select-option>
                </a-select>
            </a-form-item>

            <a-form-item label="描述">
                <a-textarea v-model:value="formState.description"
                    placeholder=""
                    :auto-size="{ minRows: 2, maxRows: 5 }" />
            </a-form-item>
            
            <!-- Category -->
            <a-form-item v-if="formState.type === 'Category'" label="值域">
                <div class="category-add">
                    <a-input v-model:value="new_possible" />
                    <div style="padding-left: 10px;">
                        <a-button @click="add_possible">
                            <PlusOutlined />
                            添加
                        </a-button>
                    </div>
                </div>
            </a-form-item>
            <a-form-item v-if="formState.type === 'Category'">
                <!-- <a-tag v-for="it in formState.possible">
                    {{ it }}
                </a-tag> -->
                <div style="display: flex; flex-wrap: wrap;">
                    <div v-for="it in formState.possible" :key="it">
                        <a-tag closable @close=close_value_Tag(it) >
                            {{ it }}
                        </a-tag>
                    </div>
                </div>
            </a-form-item>

            <!-- Integer -->
            <a-form-item v-if="formState.type === 'Integer'">
                <div class="integer-float-value">
                    <div>最小值: </div>
                    <a-input-number id="inputNumber" v-model:value="formState.min_value" :min="-10000" :max="10000" />
                    <div>最大值: </div>
                    <a-input-number id="inputNumber" v-model:value="formState.max_value" :min="-10000" :max="10000" />
                </div>
            </a-form-item>
        </a-form>
    </a-modal>

</template>

<script>
import { SettingOutlined, EditOutlined, EllipsisOutlined, DeleteOutlined } from '@ant-design/icons-vue';
import { defineComponent } from 'vue';
import { message } from 'ant-design-vue'
export default {
    name: "OptionCard",
    components: {
        defineComponent,
        SettingOutlined,
        EditOutlined,
        EllipsisOutlined,
        DeleteOutlined,

        message,
    },
    data() {
		return {
            item: {
                id: 1,
                name: "Meow",
                type: "Boolean",
                description: "Meow Meow Meow",
                possible: ["True", "False"],
                possible_org: ["True", "False"],
                min_value: -10,
                max_value: 10,
            },

            visible: false,
            visible2: false, 
            formState: {
                id: 0,
                name: '',
                type: undefined,
                description: '',
                possible: [],
                possible_org: [],
                max_value: 0,
                min_value: 0,
            },
            new_possible: ''
        }
    },
    methods: {
        confirm() {
            this.$emit('deleteOpt', this.item)
        },
        executeFunctionInChild2(new_item) {
            console.log(new_item)
            this.item = new_item
            if (new_item !== undefined)
                this.formState.id = this.item.id
        },

        edit_option() {

            this.formState.id = this.item.id
            this.formState.name = this.item.name
            this.formState.type = this.item.type
            this.formState.description = this.item.description

            const tmp = []
            for (let i = 0; i < this.item.possible_org.length; i ++)
                tmp.push(this.item.possible_org[i])

            this.formState.possible = tmp
            this.formState.possible_org = tmp

            this.formState.min_value = this.item.min_value
            this.formState.max_value = this.item.max_value

            this.visible = true
        },

        add_possible() {
            if(this.formState.possible.includes(this.new_possible)) {
                message.error('已添加过同名取值')
            }
            else {
                if(this.new_possible.length > 0) {
                    if(this.new_possible[0] >= '0' && this.new_possible[0] <= '9') {
                        message.error('首字符不能为数字')
                        return
                    }
                    this.formState.possible.push(this.new_possible)
                    this.new_possible = ''
                }
            }
        },

        close_value_Tag(removedTag) {
            // formState.possible
            const tags = this.formState.possible.filter(tag => tag !== removedTag)
            this.formState.possible = tags
            this.formState.possible_org = tags
        },

        handleOk(e) {
            console.log(e)
            const messagef = this.formState

            if(messagef.name === '') {
                message.error('名称不能为空')
                return 
            }
            if(messagef.type === undefined) {
                message.error('请选择类型')
                return
            }
            if(messagef.type === "Category" && messagef.possible.length === 0) {
                message.error('请至少设置一个值域')
                return
            }

            this.visible = false

            if(this.formState.type === "Boolean") {
                this.formState.possible = ["True", "False"]
            }
            else if(this.formState.type === "Integer") {
                if(this.formState.min_value > this.formState.max_value) {
                    message.error('最大最小值设置错误')
                    return
                }
                let str = this.formState.min_value.toString() + " ~ " + this.formState.max_value.toString()
                this.formState.possible = [ str ]
                this.formState.possible_org = [ str ]
            }

            this.$emit('editOpt', [this.item, this.formState] )

            const tmp = []
            for (let i = 0; i < this.formState.possible.length; i ++)
                tmp.push(this.formState.possible[i])

            this.item.name = this.formState.name
            this.item.type = this.formState.type
            this.item.description = this.formState.description
            
            this.item.possible_org = tmp
            this.item.possible = tmp

            this.item.min_value = this.formState.min_value
            this.item.max_value = this.formState.max_value

            this.new_possible = ''
            this.formState = {
                id: this.item.id,
                name: '',
                type: undefined,
                description: '',
                possible: [],
                max_value: 0,
                min_value: 0,
            }
        },
    }
};
</script>

<style>
.category-add {
    display: flex;
    flex-direction: row;
}

.details {
    width: 100%;
    padding-top: 20px;
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

.integer-float-value {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
}

</style>