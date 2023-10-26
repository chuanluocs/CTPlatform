<template>
    <div style="width: 1200px; height: 200px;">
        <a-table :columns="columns" :data-source="data" 
        :scroll="{ x: 1500 }" size="middle">
            <template #action>
                <a>删除</a>
            </template>
        </a-table>
    </div>
    
</template>

<script>
import { defineComponent } from 'vue'
import Axios from "axios"
import { download_testcases } from "@/utils/api"
import { message } from 'ant-design-vue'
export default defineComponent({
    components: { 
        message,
    },
    data() {
        return {
            data : [],
            columns : [],
            // columns : [
            //     {
            //         title: '编号',
            //         width: 130,
            //         dataIndex: 'index',
            //         key: 'index',
            //         fixed: 'left',
            //     },

            //     {
            //         title: 'Par0',
            //         dataIndex: 'value',
            //         key: '1',
            //         width: 100,
            //     },
            //     {
            //         title: 'Par1',
            //         dataIndex: 'value',
            //         key: '2',
            //         width: 100,
            //     },
            //     {
            //         title: 'Par2',
            //         dataIndex: 'value',
            //         key: '3',
            //         width: 100,
            //     },
            //     {
            //         title: 'Par3',
            //         dataIndex: 'value',
            //         key: '4',
            //         width: 100,
            //     },
            //     {
            //         title: 'Par4',
            //         dataIndex: 'value',
            //         key: '5',
            //         width: 100,
            //     },
            //     {
            //         title: 'Par5',
            //         dataIndex: 'value',
            //         key: '6',
            //         width: 100,
            //     },
            //     {
            //         title: 'Par6',
            //         dataIndex: 'value',
            //         key: '7',
            //         width: 100,
            //     },
            //     {
            //         title: 'Par7',
            //         dataIndex: 'value',
            //         key: '8',
            //         width: 100,
            //     },
            //     {
            //         title: 'Par8',
            //         dataIndex: 'value',
            //         key: '9',
            //         width: 100,
            //     },
            //     {
            //         title: '删除',
            //         key: 'operation',
            //         fixed: 'right',
            //         width: 100,
            //         slots: {
            //             customRender: 'action',
            //         },
            //     },
            // ]
        }
    },

    created() {
        this.loadDataFromSessionStorage()
    },
    mounted() {
        
    },
    methods: {
        loadDataFromSessionStorage() {
            const storedData_columns = sessionStorage.getItem("testcases_columns")
            if (storedData_columns)
                this.columns = JSON.parse(storedData_columns)
            
            const storedData_data = sessionStorage.getItem("testcases_data")
            if (storedData_data)
                this.data = JSON.parse(storedData_data)
            
            // console.log(this.columns)
            // console.log(this.data)
        },

        download_tc() {
            const columns = this.columns
            const data = this.data
            download_testcases({
                columns : columns,
                data : data
            }).then((response) => {
                const blob = new Blob([response.data], { type: "application/vnd.ms-excel" })

                // 创建一个下载链接
                const downloadLink = document.createElement('a')
                downloadLink.href = window.URL.createObjectURL(blob)
                downloadLink.download = "downloaded-file.xls" // 使用 .xls 扩展名
                // 模拟用户点击链接以触发下载
                downloadLink.click()

            }).catch(error => {
                message.error("下载失败")
            });
        },
    }
});

</script>