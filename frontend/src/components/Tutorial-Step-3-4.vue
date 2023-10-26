<template>
    <div class="content">
        <Menu></Menu>
        <div class="right-content">
            <h2> Step 3 开始生成 </h2>
            <a-divider />
            <!-- <h3> 喵喵 </h3> -->
            <div class="text">
                点击开始按钮，开始生成测试数据，可能需要一定的等待时间。
            </div>
            <a-button type="primary" size="large">Start</a-button>

            <a-divider />
            <h2> Step 4 查看结果 </h2>
            <a-divider />
            <h3> 查看结果 </h3>
            <div class="text">
                生成的测试数据以表格的方式呈现：
            </div>

            <div style="width: 1000px; padding-bottom: 0px;">
                <a-table :columns="columns" :data-source="data" 
                :scroll="{ x: 1500 }" size="middle">
                    <!-- <template #action>
                        <a @click="delete_tc">删除</a>
                    </template> -->
                </a-table>
            </div>

            <a-divider />
            <h3> 下载结果 </h3>
            <div class="text">
                点击下载按钮，可以下载 xls 格式的结果。
            </div>
            <a-button>
                <DownloadOutlined />
                下载
            </a-button>

            <a-divider />
        </div>
    </div>
</template>

<script>
import Menu from "@/components/menu.vue"
import { defineComponent, ref, watch } from 'vue'
import { DownloadOutlined } from '@ant-design/icons-vue'
import { notification } from 'ant-design-vue'
export default {
    name: 'tutorial_3_4',
    components: {
        Menu,
        notification,
        DownloadOutlined,
    },

    data() {
        return {
            data : [],
            columns : [
                {
                    title: '编号',
                    width: 130,
                    dataIndex: 'index',
                    key: 'index',
                    fixed: 'left',
                },

                {
                    title: 'Par0',
                    dataIndex: 'value',
                    key: '1',
                    width: 100,
                },
                {
                    title: 'Par1',
                    dataIndex: 'value',
                    key: '2',
                    width: 100,
                },
                {
                    title: 'Par2',
                    dataIndex: 'value',
                    key: '3',
                    width: 100,
                },
                {
                    title: 'Par3',
                    dataIndex: 'value',
                    key: '4',
                    width: 100,
                },
                {
                    title: 'Par4',
                    dataIndex: 'value',
                    key: '5',
                    width: 100,
                },
                {
                    title: 'Par5',
                    dataIndex: 'value',
                    key: '6',
                    width: 100,
                },
                {
                    title: 'Par6',
                    dataIndex: 'value',
                    key: '7',
                    width: 100,
                },
                {
                    title: 'Par7',
                    dataIndex: 'value',
                    key: '8',
                    width: 100,
                },
                {
                    title: 'Par8',
                    dataIndex: 'value',
                    key: '9',
                    width: 100,
                },
                // {
                //     title: '删除',
                //     key: 'operation',
                //     fixed: 'right',
                //     width: 100,
                //     slots: {
                //         customRender: 'action',
                //     },
                // },
            ]
        }
    },

    created() {
        this.data = []
        for (let i = 0; i < 5; i ++) {
            this.data.push({
                key : i,
                index: "Testcase " + (i + 1).toString(),
                value: "value" + (i + 1).toString()
            })
        }
    },

    methods : {
        delete_tc() {
            notification.open({
                message: '删除测试数据',
                description: '在正式的测试数据列表中，此操作将删除当前的一组数据。',
            });
        },
    }
}
</script>

<style scoped>
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
    align-items: start;
    padding-left: 100px;

    /* background-color: antiquewhite; */
}

.text {
    padding-top: 10px;
    padding-bottom: 20px;
    font-size: 18px;
    font-weight: 300;
}
</style>