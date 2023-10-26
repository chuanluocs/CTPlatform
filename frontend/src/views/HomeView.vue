<template>
    <div class="home">
        <div class="home-menu">
            <a-menu v-model:selectedKeys="current" mode="horizontal">
                <a-menu-item key="step1" @click="set_current(1)">
                    Stpe 1 设置选项
                </a-menu-item>
                <a-menu-item key="step2" @click="set_current(2)">
                    Step 2 设置约束
                </a-menu-item>
                <a-menu-item key="step34" @click="set_current(3)">
                    Step 3 & Step 4 获取结果 
                </a-menu-item>
                <a-menu-item key="example" @click="set_current(4)">
                    快速开始（示例）
                </a-menu-item>
            </a-menu>
        </div>
        
        <tutorial_1 v-if="step === 1"></tutorial_1>
        <tutorial_2 v-else-if="step === 2"></tutorial_2>
        <tutorial_3_4 v-else-if="step === 3"></tutorial_3_4>
        <example v-else></example>
    </div>
</template>

<script>
import { defineComponent, ref, watch } from 'vue'
import tutorial_1 from '@/components/Tutorial-Step-1.vue'
import tutorial_2 from '@/components/Tutorial-Step-2.vue'
import tutorial_3_4 from '@/components/Tutorial-Step-3-4.vue'
import example from "@/components/Example.vue"
export default {
    name: 'HomeView',
    components: {
        tutorial_1, tutorial_2, tutorial_3_4, example
    },
    data() {
        return {
            step: 1,
            current: ref(["step1"])
        }
    },
    methods: {
        loadDataFromSessionStorage() {
            const storedData = sessionStorage.getItem("tutorial-step")
            if (storedData) {
                // console.log(storedData)
                this.step = JSON.parse(storedData)
                if (this.step === 1)
                    this.current = ["step1"]
                else if(this.step === 2)
                    this.current = ["step2"]
                else if(this.step === 3)
                    this.current = ["step34"]
                else if(this.step === 4)
                    this.current = ["example"]
            }
        },
        set_current(value) {
            this.step = value
            sessionStorage.setItem("tutorial-step", this.step)
        },
    },
    created() {
        // 在组件创建时加载数据
        this.loadDataFromSessionStorage()
    },
}
</script>

<style scoped>
/* .home {
    display: flex;
    flex-direction: column;
} */

.home-menu {
    padding-left: 300px;
    padding-bottom: 30px;
}
</style>