<template>
    <a-menu id="dddddd" style="width: 256px" v-model:openKeys="openKeys" 
    v-model:selectedKeys="selectedKeys"
    mode="inline" @click="handleClick">

        <a-sub-menu key="sub1" @titleClick="titleClick">
            <template #icon>
                <BarsOutlined />
            </template>
            <template #title>Step 1 选项设置</template>
            <a-menu-item key="1">选项类型</a-menu-item>
            <a-menu-item key="2">选项列表</a-menu-item>
            <a-menu-item key="3">文件格式</a-menu-item>
        </a-sub-menu>

        <a-sub-menu key="sub2" @titleClick="titleClick">
            <template #icon>
                <BarsOutlined />
            </template>
            <template #title>Step 2 约束设置</template>
            <a-menu-item key="4">约束类型</a-menu-item>
            <a-menu-item key="5">约束的添加与编辑</a-menu-item>
            <a-menu-item key="6">约束列表</a-menu-item>
            <a-menu-item key="7">文件格式</a-menu-item>
            <a-menu-item key="8">模型下载</a-menu-item>
        </a-sub-menu>
        <a-sub-menu key="sub4">
            <template #icon>
                <BarsOutlined />
            </template>
            <template #title>Step 3 开始生成</template>
            <a-menu-item key="9">开始生成</a-menu-item>
        </a-sub-menu>
        <a-sub-menu key="sub5">
            <template #icon>
                <BarsOutlined />
            </template>
            <template #title>Step 4 查看结果</template>
            <a-menu-item key="10">查看结果</a-menu-item>
            <a-menu-item key="11">下载结果</a-menu-item>
        </a-sub-menu>
        <!-- <a-sub-menu key="sub6">
            <template #icon>
                <BarsOutlined />
            </template>
            <template #title>Step 5 快速开始</template>
        </a-sub-menu> -->
        <!-- <a-menu-item key="12">
            Step 5 快速开始
        </a-menu-item> -->
    </a-menu>
</template>
<script>
import { defineComponent, ref, watch } from 'vue';
import { BarsOutlined, MailOutlined, QqOutlined, AppstoreOutlined, SettingOutlined } from '@ant-design/icons-vue';
export default defineComponent({
    name: "Menu",
    setup() {
        const selectedKeys = ref([]);
        const openKeys = ref(['sub1']);
        const handleClick = e => {
            console.log('click', e);
        };
        const titleClick = e => {
            console.log('titleClick', e);
        };
        watch(
            () => openKeys,
            val => {
                console.log('openKeys', val);
            },
        );
        return {
            selectedKeys,
            openKeys,
            handleClick,
            titleClick,
        };
    },
    components: {
        MailOutlined,
        QqOutlined,
        AppstoreOutlined,
        SettingOutlined,
        BarsOutlined,
    },
});
</script>