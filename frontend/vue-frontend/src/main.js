import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // Import Vue Router
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap';

const app = createApp(App);
app.use(router); // Enable Vue Router
app.mount('#app');