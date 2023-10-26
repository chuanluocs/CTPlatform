// add username and token into headers
import axios from 'axios'
import store from '@/store'
import qs from 'qs'
import router from '@/router'
const instance=axios.create({
    // baseURL:'http://192.168.117.134:80/',
    baseURL:'http://124.71.183.200:5000/',
    // baseURL:'http://127.0.0.1:5000/',
    timeout: 50000,
    headers: {
        'Content-Type':'application/json;charset=UTF'
    },
})
instance.defaults.withCredentials = false

// instance.interceptors.request.use(
//     (config) => {
//         const username = localStorage.getItem('username');
//         const authorization = localStorage.getItem('token');
//         // 若 localStorage 中含有这两个字段，则添加入请求头
//         //config.data = qs.stringify(config.data)
//         if (username && authorization) {
//             console.log(authorization)
//             config.headers.authorization = authorization;
//             config.headers.username = username;
//         }
//         return config;
//     },
//     (error) => {
//         return Promise.reject(error)
//     }
// )
// instance.interceptors.response.use(
//     response=> {
//         return response
//     },
// )

export default instance


