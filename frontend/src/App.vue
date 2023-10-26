<template>
    <div style="padding-top: 20px;">
        <h1>CTPlatform：面向可配置软件的测试用例集合生成平台</h1>
    </div>
    <nav>
        <router-link to="/">Tutorial</router-link> 
        |
        <router-link to="/main">Main</router-link> 
        <!-- |
        <router-link to="/about">About</router-link> -->
    </nav>
    <router-view />
</template>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
}
nav {
    padding: 30px;
}
nav a {
    font-weight: bold;
    color: #2c3e50;
}
nav a.router-link-exact-active {
    color: #42b983;
}
</style>