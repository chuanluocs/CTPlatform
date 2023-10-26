import request, {post} from '@/utils/http'
import axios from 'axios'

export function test_api(data){
    return request({
        url: 'api/test',
        method: 'post',
        data,
    })
}

export function get_constraint_obj(data) {
    return request({
        url: 'api/get_constraint_obj',
        method: 'post',
        data,
    })
}

export function get_object(data) {
    return request({
        url: 'api/get_object',
        method: 'post',
        data,
    })
}

export function get_testcases(data) {
    return request({
        url: 'api/get_testcases',
        method: 'post',
        data,
    })
}

export function download_testcases(data) {
    return request({
        url: 'api/download_testcases',
        responseType: 'blob',
        method: 'post',
        data,
    })
}

export function download_model(data) {
    return request({
        url: 'api/download_model',
        responseType: 'blob',
        method: 'post',
        data,
    })
}

// export function download_testcases(data) {
//     return axios.get('http://127.0.0.1:5000/api/download_testcases', {
//         responseType: 'blob',
//         params: data, // Use 'params' to pass data as query parameters
//     });
// }