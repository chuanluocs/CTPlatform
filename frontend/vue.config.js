const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true,
    publicPath: './'
})

// module.exports = {
//     publicPath: '/', // 基本路径，通常设置为 '/'
//     outputDir: 'dist', // 构建输出的目录
//     assetsDir: 'static', // 静态资源目录 (js, css, img, fonts)
//     productionSourceMap: false, // 生产环境不生成 source map
// }

