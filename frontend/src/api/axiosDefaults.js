import axios from 'axios';
import { ACCESS_TOKEN } from '../constants';

const api = axios.create({
    baseURL:
        process.env.NODE_ENV === "production"
            ? "https://fitness-tracker-pp5-52ea60f889f7.herokuapp.com/"
            : "/api",
});

api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem(ACCESS_TOKEN);
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

export default api;