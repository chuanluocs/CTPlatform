<template>
    <div class="main">
        <h1>Meow Meow !</h1>
    </div>
    <div class="content">
        <Menu></Menu>
        <div class="right-content">
            <div class="right">
                <a-steps :current="state - 1">
                    <a-step>
                        <!-- <span slot="title">Finished</span> -->
                        <template #title>Set Options</template>
                        <template #description>
                            <span>This is a description.</span>
                        </template>
                    </a-step>
                    <!-- <a-step title="Set Constraints" sub-title="Left 00:00:08" description="This is a description." /> -->
                    <a-step title="Set Constraints" description="This is a description." />
                    <a-step title="Set Algorithm" description="This is a description." />
                    <a-step title="Result" description="This is a description." />
                </a-steps>

                <div class="bread">
                    <a-breadcrumb>
                        <!-- <a-breadcrumb-item>Step 1</a-breadcrumb-item>
                        <a-breadcrumb-item>Step 2</a-breadcrumb-item>
                        <a-breadcrumb-item>Step 3</a-breadcrumb-item>
                        <a-breadcrumb-item>Step 4</a-breadcrumb-item> -->
                        <a-breadcrumb-item v-for="index in state" @click="setState(index)">
                            {{ "Step " + index }}
                        </a-breadcrumb-item>
                    </a-breadcrumb>
                    
                    <div style="padding-left: 20px;">
                        <a-button type="link" :disabled="state === 1" @click="LastState">
                            <StepBackwardOutlined />
                            Last Step
                        </a-button>
                    </div>

                    <div>
                        <a-button type="link" :disabled="state === 4" @click="NextState">
                            <StepForwardOutlined />
                            Next Step
                        </a-button>
                    </div>

                    
                </div>

                <div v-if="state === 1" class="down-content">
                    <div class="buttons">
                        <a-button @click="clean_opt">
                            <DeleteOutlined />
                            Clean
                        </a-button>
                        <div style="padding-left: 20px;">
                            <a-upload
                            v-model:file="file"
                            name="file"
                            :multiple="false"
                            action="http://124.71.183.200:5000/api/uploader_get_json"
                            :on-success="upload_back"
                            @change="handleChangeFile" >
                                <a-button>
                                    <upload-outlined></upload-outlined>
                                    Click to Upload
                                </a-button>
                            </a-upload>
                        </div>
                        <div style="padding-left: 20px;">
                            <a-button @click="add_option">
                                <PlusOutlined />
                                Add a Option
                            </a-button>
                        </div>
                    </div>
                    
                    <div class="down">
                        <div class="down-left">
                            <OptionList ref="childComponent"
                            @notifyChild2 = "callFunctionInChild2" 
                            @addOption = "addOption">
                            </OptionList>
                        </div>
                        <div class="down-right">
                            <OptionCard ref="child2"
                            @deleteOpt = "delete_option"
                            ></OptionCard>
                        </div>
                    </div>
                    
                </div>

                <div v-if="state === 2" class="down-content">
                    <div class="buttons">
                        <a-button @click="clean_conList">
                            <DeleteOutlined />
                            Clean
                        </a-button>
                        <div style="padding-left: 20px;">
                            <a-button>
                                <upload-outlined></upload-outlined>
                                Click to Upload
                            </a-button>
                        </div>
                        <div style="padding-left: 20px;">
                            <a-button @click="add_constraint">
                                <PlusOutlined />
                                Add a Constraint
                            </a-button>
                        </div>
                    </div>

                    <div class="buttons" style="align-items: center;">
                        <a-checkbox v-model:checked="screen" @change="change_screen">
                            Screen
                        </a-checkbox>
                        
                        <div style="padding-left: 20px;">
                            <a-select
                                show-search
                                v-model:value="screen_new"
                                :options = "select_options"
                                placeholder="Select a Option"
                                style="width: 100px" >
                            </a-select>
                        </div>
                        
                        <div style="padding-left: 20px;">
                            <a-button :disabled = "screen_new === undefined"
                                @click="add_screen">
                                <PlusOutlined />
                                add
                            </a-button>
                        </div>
                    </div>
                    
                    <div class="buttons">
                        <div v-for="(tag, index) in screen_list" :key="tag">
                            <a-tag closable 
                                @close="closeTag(tag)">
                                {{ tag }}
                            </a-tag>
                        </div>
                        
                    </div>

                    <div class="down">
                        <div>
                            <!-- <ConstraintList ref="conList"
                            @notifyConCard="callFunctionInConCard">
                            </ConstraintList> -->

                            <ConstraintList2 ref="conList"
                            @notifyConCard="callFunctionInConCard">
                            </ConstraintList2>
                        </div>

                        <div
                            style="width: 500px; 
                            padding-left: 50px;">

                            <!-- <ConstraintCard ref="conCard"
                            @deleteCon="delete_constraint"></ConstraintCard> -->
                            
                            <ConstraintCard2 ref="conCard"
                            @deleteCon="delete_constraint"></ConstraintCard2>
                        </div>
                        <!-- <div>
                            <tmpCard></tmpCard>
                        </div> -->
                    </div>
                </div>

                <!-- 算法设置 -->
                <div v-if="state === 3" style="padding-top: 100px">
                    <a-button type="primary" size="large" @click="get_testcases">Start</a-button>
                </div>

                <!-- 结果展示 -->
                <div v-if="state === 4" class="down-content">
                    <div class="buttons">
                        <a-button @click="clean_tc">
                            <DeleteOutlined />
                            Clean
                        </a-button>
                        <div style="padding-left: 20px;">
                            <a-button @click="download_tc">
                                <DownloadOutlined />
                                Download
                            </a-button>
                        </div>
                    </div>
                    
                    <div class="down">
                        <div>
                            <TestcaseList ref="tcList"
                            @notifyTcCard="callFunctionInTcCard"></TestcaseList>
                        </div>
                        <div style="width: 500px; padding-left: 50px;">
                            <TestcaseCard ref="tcCard"></TestcaseCard>
                        </div>
                    </div>
                </div>

                <div v-if="state === 0" style="padding-top: 50px">
                    <a-empty />
                </div>
                
            </div>
        </div>
    </div>
    
    <a-modal v-model:open="visible" title="Add a Option" @ok="handleOk">
        <!-- <p>Some contents...</p>
        <p>Some contents...</p>
        <p>Some contents...</p> -->
        <a-form style="padding: 30px">
            
            <a-form-item label="Name">
                <a-input v-model:value="formState.name" />
            </a-form-item>

            <a-form-item label="Type">
                <a-select v-model:value="formState.type" placeholder="please select the type">
                    <a-select-option value="Boolean"> Boolean </a-select-option>
                    <a-select-option value="Integer"> Integer </a-select-option>
                    <a-select-option value="Float"> Float </a-select-option>
                    <a-select-option value="Category"> Category </a-select-option>
                </a-select>
            </a-form-item>

            <a-form-item label="Description">
                <a-textarea v-model:value="formState.description"
                    placeholder="This is a description."
                    :auto-size="{ minRows: 2, maxRows: 5 }" />
            </a-form-item>
            
            <!-- Category -->
            <a-form-item v-if="formState.type === 'Category'" label="Possible Value">
                <div class="category-add">
                    <a-input v-model:value="new_possible" />
                    <div style="padding-left: 10px;">
                        <a-button @click="add_possible">
                            <PlusOutlined />
                            add
                        </a-button>
                    </div>
                </div>
            </a-form-item>
            <a-form-item v-if="formState.type === 'Category'">
                <a-tag v-for="it in formState.possible">
                    {{ it }}
                </a-tag>
            </a-form-item>

            <!-- Integer -->
            <a-form-item v-if="formState.type === 'Integer'">
                <div class="integer-float-value">
                    <div>Minimum Value: </div>
                    <a-input-number id="inputNumber" v-model:value="formState.min_value" :min="-10" :max="10" />
                    <div>Maximum Value: </div>
                    <a-input-number id="inputNumber" v-model:value="formState.max_value" :min="-10" :max="10" />
                </div>
            </a-form-item>

            <!-- Float -->
            <a-form-item v-if="formState.type === 'Float'">
                <div class="integer-float-value">
                    <div>Minimum Value: </div>
                    <a-input-number id="inputNumber" v-model:value="formState.min_value" :min="-10" :max="10" :step="0.01"/>
                    <div>Maximum Value: </div>
                    <a-input-number id="inputNumber" v-model:value="formState.max_value" :min="-10" :max="10" :step="0.01"/>
                </div>
            </a-form-item>
        </a-form>
    </a-modal>

    <a-modal v-model:open="visible_con"
        title="Add a Constraint" @ok="handleOk_con"
        :bodyStyle="'con-bodyStyle'">
        <div style="overflow-y: auto; 
            padding: 0 !important;
            height: 100%;">

            <div class="add-constraint">
                <div class="add-constraint-left">
                    <div>
                        <a-button :disabled="selected.length === 0"
                            @click="cleanSelected">
                            <DeleteOutlined />
                            Clean
                        </a-button>
                    </div>

                    <a-list item-layout="horizontal" :data-source="selected">
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
                                
                                <div v-if="item.possible.length === 1">
                                    <a-tag v-for="it in item.possible">
                                        {{ it }}
                                    </a-tag>
                                </div>
                                <div v-if="item.possible.length > 1">
                                    <a-tag> ... </a-tag>
                                </div>
                                
                            </a-list-item>
                        </template>
                    </a-list>
                </div>

                <div class="add-constraint-right">
                    <a-select
                        show-search
                        v-model:value="select_value"
                        :options = "select_options"
                        placeholder="Select a Option"
                        style="width: 200px" 
                        @change="handleChange" >
                    </a-select>

                    <div v-if="new_con_option != undefined" class="new-con-option">
                        <a-avatar v-if="new_con_option.type === 'Boolean'" class="boolean-avatar">01</a-avatar>
                        <a-avatar v-if="new_con_option.type === 'Integer'" class="integer-avatar">Z</a-avatar>
                        <a-avatar v-if="new_con_option.type === 'Float'" class="float-avatar">R</a-avatar>
                        <a-avatar v-if="new_con_option.type === 'Category'" class="category-avatar">C</a-avatar>
                        
                        <div style="font-size: 16px; font-weight: 500;">
                            {{ new_con_option.name }}
                        </div>

                        <div style="font-size: 14px; font-weight: 300;">
                            {{ new_con_option.type }}
                        </div>
                    </div>

                    <div v-if="new_con_option != undefined"
                        style="padding-left: 20px; padding-top: 10px;">
                        <a-tag v-for="it in new_con_option.possible_org">
                            {{ it }}
                        </a-tag>
                    </div>

                    <div v-if="new_con_option != undefined" class="Set-Values">
                        <div style="padding-bottom: 15px;">
                            Set Values
                        </div>

                        <!-- <a-checkbox
                            v-model:checked="checkAll"
                            :indeterminate="indeterminate"
                            @change="onCheckAllChange"
                            style="font-size: 16px;"> 
                            Check all 
                        </a-checkbox> -->
                        
                        <a-checkbox-group v-if="new_con_option.type === 'Category' || new_con_option.type === 'Boolean'" 
                            v-model:value="con_checkedList" 
                            :options="new_con_option.possible_org" 
                            style="font-size: 16px;" />
                        
                        <div v-if="new_con_option.type === 'Integer'">
                            <div style="padding-bottom: 5px;">Minimum Value: </div>
                            <a-input-number id="inputNumber" v-model:value="new_con_option.min_value" :min="-10" :max="10" />
                            <div style="padding-bottom: 5px; padding-top: 5px;">Maximum Value: </div>
                            <a-input-number id="inputNumber" v-model:value="new_con_option.max_value" :min="-10" :max="10" />
                        </div>

                        <div v-if="new_con_option.type === 'Float'">
                            <div style="padding-bottom: 5px;">Minimum Value: </div>
                            <a-input-number id="inputNumber" v-model:value="new_con_option.min_value" :min="-10" :max="10" :step="0.01" />
                            <div style="padding-bottom: 5px; padding-top: 5px;">Maximum Value: </div>
                            <a-input-number id="inputNumber" v-model:value="new_con_option.max_value" :min="-10" :max="10" :step="0.01" />
                        </div>
                    </div>

                    <div style="padding-top: 30px">
                        <a-button :disabled = "new_con_option === undefined"
                            @click="add_con_opt">
                            <PlusOutlined />
                            add
                        </a-button>
                    </div>
                    
                </div>
            </div>
        </div>
    </a-modal>
</template>
  
<script>
import Menu from "@/components/menu.vue"

import OptionList from "@/components/option-list.vue"
import OptionCard from "@/components/option-card.vue"

// import ConstraintList from "@/components/constraint-list.vue"
// import ConstraintCard from "@/components/constraint-card.vue"

import ConstraintList2 from "@/components/constraint-list-2.vue"
import ConstraintCard2 from "@/components/constraint-card-2.vue"

import tmpCard from "@/components/tmpCard.vue"

import TestcaseList from "@/components/testcase-list.vue"
import TestcaseCard from "@/components/testcase-card.vue"

import { UploadOutlined, DownloadOutlined } from '@ant-design/icons-vue'
import { PlusOutlined, DeleteOutlined } from '@ant-design/icons-vue'
import { StepForwardOutlined, StepBackwardOutlined } from '@ant-design/icons-vue'
import { defineComponent, ref } from 'vue'
import { message } from 'ant-design-vue'

import Axios from "axios"
import { test_api, get_testcases } from "@/utils/api"

export default {
	name: "main",
	components: { 
        Menu, OptionList, OptionCard,
        // ConstraintList, ConstraintCard,
        ConstraintList2, ConstraintCard2,
        TestcaseList, TestcaseCard,
        UploadOutlined, DownloadOutlined,
        PlusOutlined, DeleteOutlined,
        StepForwardOutlined, StepBackwardOutlined,

        defineComponent, ref,
        message,

        tmpCard,
    },
	data() {
		return {
            file: undefined,

            indeterminate: false,
            con_checkAll: false,
            con_checkedList: [],
            select_value: undefined,
            new_con_option: undefined,
            visible_con: false,
            selected: [
                {
                    id: 1,
                    name: "Meow",
                    type: "Boolean",
                    description: "Meow Meow Meow",
                    possible: ["True"],
                    possible_org: ["True", "False"],
                    min_value: 0,
                    max_value: 0,
                },
                {
                    id: 2,
                    name: "QAQ",
                    type: "Integer",
                    description: "This is a description.",
                    possible: ["-2 ~ 2"],
                    possible_org: ["-5 ~ 10"],
                    min_value: 0,
                    max_value: 0,
                },
            ],
            select_options: [
                // "Meow", "QAQ", "QAQ-Meow", "A"
                { value: "Meow", lable: "Meow" },
                { value: "QAQ", lable: "QAQ" },
                { value: "QAQ-Meow", lable: "QAQ-Meow" },
                { value: "A", lable: "A" },
            ],


            screen: false,
            screen_list: ["Meow", "QAQ"],
            screen_new: undefined,
            
            visible: false,
            state: 1,
            Steps: ["Step 1", "Step 2", "Step 3", "Step 4"],
            formState: {
                name: '',
                type: undefined,
                description: '',
                possible: [],
                max_value: 0,
                min_value: 0,
            },
            new_possible: '',

            options: [
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
            ],
        }
	},
    watch: {
        'formState.type': function (newType, oldType) {
            this.formState.possible = []
            this.formState.max_value = 0
            this.formState.min_value = 0
        },
        state : function (newState, oldState) {
            sessionStorage.setItem("main-state", JSON.stringify(this.state))
        },
    },
    created() {
        // 在组件创建时加载数据
        this.loadDataFromSessionStorage()
    },
    methods: {
        test_api() {
            console.log("test api")
            const now_options = this.options
            const now_constraints = JSON.parse(sessionStorage.getItem("constraint_list_data"))
            test_api({
                test: "Meow",
                options: now_options,
                constraints: now_constraints,
            }).then((response) => {
                let ret = response.data
                console.log(ret)
            }).catch(error => {
                console.error(error);
            });
        },

        get_testcases() {
            const now_options = this.options
            const now_constraints = JSON.parse(sessionStorage.getItem("constraint_list_data"))
            
            let now_constraints_exp = []
            for (let i = 0; i < now_constraints.length; i ++)
                now_constraints_exp.push(now_constraints[i].expression)

            get_testcases({
                options: now_options,
                // constraints: now_constraints_exp
                constraints: now_constraints
            }).then((response) => {
                let ret = response.data
                const testcases = ret
                console.log(testcases)
                sessionStorage.setItem("testcases", JSON.stringify(testcases))
                this.setState(4)
            }).catch(error => {
                console.error(error);
            });
        },

        delete_constraint(removedItem) {
            console.log(removedItem)
            this.$refs.conList.delete_constraint(removedItem)
        },

        download_tc() {
            this.$refs.tcList.download_tc()
        },

        loadDataFromSessionStorage() {
            // 在组件创建时尝试从 sessionStorage 中加载数据
            const storedData_options = sessionStorage.getItem("main-options")
            if (storedData_options)
                this.options = JSON.parse(storedData_options)

            this.select_options = []
            for (let i = 0; i < this.options.length; i ++)
                this.select_options.push({
                    value: this.options[i].name,
                    lable: this.options[i].name
                })

            const stateDate = sessionStorage.getItem("main-state")
            if(stateDate)
                this.state = JSON.parse(stateDate)
        },

        clean_tc() {
            sessionStorage.setItem("testcases", JSON.stringify([]))
            this.setState(3)
        },
        
        handleChangeFile(info) {
            if (info.file.status !== 'uploading')
                console.log(info.file, info.fileList)
            
            if (info.file.status === 'done')
                message.success(`${info.file.name} file uploaded successfully`)
            
            else if (info.file.status === 'error')
                message.error(`${info.file.name} file upload failed.`)
        },

        upload_back(feedback) {
            const options = feedback.options
            const constraints = feedback.constraints

            this.options = options
            sessionStorage.setItem("main-options", JSON.stringify(options))
            sessionStorage.setItem("option_list_data", JSON.stringify(options))
            sessionStorage.setItem("constraint_list_data", JSON.stringify(constraints))

            this.setState(2)
            // console.log(options)
            // console.log(constraints)
            this.file = []
        },

        clean_opt() {
            this.$refs.childComponent.cleanUp()
            sessionStorage.setItem("constraint_list_data", JSON.stringify([]))
            // console.log(this.$refs.conList)
        },

        clean_conList() {
            this.$refs.conList.cleanUp()
        },

        change_screen() {
            if(this.screen)
                this.$refs.conList.set_screen(this.screen_list)
            else
                this.$refs.conList.cancel_screen()
        },
        
        add_screen() {
            if(this.screen_new != undefined) {
                let flag = false
                for(let i = 0; i < this.screen_list.length; i ++)
                    if(this.screen_new === this.screen_list[i]) {
                        flag = true
                        break
                    }
                if(flag)
                    message.error('This is an error message')
                else {
                    this.screen_list.push(this.screen_new)
                    this.screen_new = undefined
                }

                if(this.screen)
                    this.$refs.conList.set_screen(this.screen_list)
            }
        },

        delete_option(removedItem) {
            const options = this.options.filter(item => item !== removedItem)
            this.options = options
            sessionStorage.setItem("main-options", JSON.stringify(this.options))
        
            const select_options = this.select_options.filter(item => item !== removedItem.name)
            this.select_options = select_options

            this.indeterminate = false
            this.con_checkAll = false
            this.con_checkedList = []
            this.select_value = undefined
            this.new_con_option = undefined
            this.cleanSelected()

            this.$refs.childComponent.delete_option(removedItem)

            sessionStorage.setItem("constraint_list_data", JSON.stringify([]))
        },

        closeTag(removedTag) {
            // const tags = state.tags.filter(tag => tag !== removedTag);
            const tags = this.screen_list.filter(tag => tag !== removedTag)
            console.log(tags);
            this.screen_list = tags

            if(this.screen)
                this.$refs.conList.set_screen(this.screen_list)
        },

        cleanSelected() {
            this.selected = []
        },
        add_con_opt() {
            if(this.new_con_option != undefined) {

                for(let i = 0; i < this.selected.length; i ++)
                    if(this.new_con_option.name === this.selected[i].name) {
                        message.error('This is an error message')
                        return
                    }

                let tmp = JSON.parse(JSON.stringify(this.new_con_option))
                tmp.possible = []
                if(this.new_con_option.type === "Category" || this.new_con_option.type === "Boolean") {
                    for(let i = 0; i < this.con_checkedList.length; i ++)
                        tmp.possible.push(this.con_checkedList[i])
                }
                else if(this.new_con_option.type === "Integer") {
                    let str = this.new_con_option.min_value.toString() + " ~ " + this.new_con_option.max_value.toString()
                    tmp.possible.push(str)
                }
                else if(this.new_con_option.type === "Float"){
                    let str = "( " + this.new_con_option.min_value.toString() + " , " + this.new_con_option.max_value.toString() + " )"
                    tmp.possible.push(str)
                }
                this.selected.push(tmp)
            }

            this.indeterminate = false
            this.con_checkAll = false
            this.con_checkedList = []
            this.select_value = undefined
            this.new_con_option = undefined
        },
        onCheckAllChange(checked) {
            if(checked) {
                // "con_checkedList" :options="new_con_option.possible_org"
                this.con_checkedList = this.new_con_option.possible_org
            }
        },
        handleChange(value) {
            console.log(value)
            for(let i = 0; i < this.options.length; i ++)
                if(this.options[i].name === value) {
                    this.new_con_option = this.options[i]
                    break
                }
            console.log(this.new_con_option)
        },

        addOption(new_option) {
            this.options.push(new_option)
            this.select_options.push(
                {value: new_option.name, lable: new_option.name}
            )
            // sessionStorage.setItem("options", this.options)
            sessionStorage.setItem("main-options", JSON.stringify(this.options))
        },

        LastState() {
            if(this.state > 1)
                this.state = this.state - 1
        },
        NextState() {
            if(this.state < 4)
                this.state = this.state + 1
        },
        setState(index) {
            this.state = index
        },

        callFunctionInChild2(new_item) {
            this.$refs.child2.executeFunctionInChild2(new_item)
        },
        callFunctionInConCard(new_item) {
            this.$refs.conCard.executeFunctionInConCard(new_item)
        },
        callFunctionInTcCard(new_item) {
            this.$refs.tcCard.executeFunctionInTcCard(new_item)
        },

        add_constraint() {
            this.visible_con = true
        },
        handleOk_con(e) {

            if(this.selected.length === 0) {
                message.error('This is an error message')
                return
            }

            this.$refs.conList.add_constraint(this.selected)

            this.visible_con = false
            this.new_con_option = undefined
            this.select_value = undefined
            this.con_checkedList = []
            this.con_checkAll = false
            this.indeterminate = false
        },
        add_option() {
            this.visible = true
        },
        handleOk(e) {
            console.log(e)
            this.visible = false
            const message = this.formState
            this.$refs.childComponent.executeFunctionInChild(message)

            this.new_possible = ''
            this.formState = {
                name: '',
                type: undefined,
                description: '',
                possible: [],
                max_value: 0,
                min_value: 0,
            }
        },
        add_possible() {
            if(this.formState.possible.includes(this.new_possible)) {
                message.error('This is an error message')
            }
            else {
                if(this.new_possible.length > 0) {
                    this.formState.possible.push(this.new_possible)
                    this.new_possible = ''
                }
            }
        },
    },
}
</script>

<style scoped>

.bodyStyle {
    width: 1000px !important;
    background-color: black !important;
}

::-webkit-scrollbar {
  width: 5px; /* 设置滚动条宽度 */
}

.Set-Values {
    display: flex;
    flex-direction: column;
    padding-top: 10px;
    align-items: start;
    width: 80%;

    font-size: 16px;
    font-weight: 350;
}

.new-con-option {
    padding-top: 30px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    padding-top: 20px;
    width: 80%;
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

.add-constraint {
    display: flex;
    flex-direction: row;
    height: 450px;
}
.add-constraint-left {
    width: 600px;
    /* background-color: black; */
}
.add-constraint-right {
    width: 350px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.category-add {
    display: flex;
    flex-direction: row;
}

.integer-float-value {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
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
    align-items: center;
}

.right {
    width: 95%;
    display: flex;
    justify-content: center;
    padding-top: 10px;
    flex-direction: column;
    /* padding: 20px; */
}

.bread {
    display: flex;
    flex-direction: row;
    justify-content: start;
    align-items: center;
    padding-top: 30px;
}

.down-content {
    display: flex;
    flex-direction: column;
}

.buttons {
    display: flex;
    flex-direction: row;
    justify-content: start;
    padding-top: 20px;
}

.down {
    padding-top: 30px;
    width: 100%;
    display: flex;
    flex-direction: row;
}

.down-left {
    width: 60%;
}

.down-right {
    right: 160px;
    position: fixed;
    /* background-color: black; */
}

.down-right-2 {
    right: 50px;
    position: fixed;
    /* background-color: black; */
}
</style>