import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/Home.vue';
import Space from '../components/Space.vue';
import AIChat from '../components/AIChat.vue';

const routes = [
  { path: '/', component: Home },
  { path: '/space', component: Space },
  { path: '/ai-chat', component: AIChat },
];

const router = createRouter({
  history: createWebHistory(), // Enables clean URLs (no hash `#`)
  routes,
});

export default router;