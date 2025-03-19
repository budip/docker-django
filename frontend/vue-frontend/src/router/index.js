import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/Home.vue';
import Space from '../components/Space.vue';
import AIChat from '../components/AIChat.vue';
import Blog from '../components/Blog.vue';
import BlogDetail from '../components/BlogDetail.vue';
import CreateBlog from '../components/CreateBlog.vue';
import EditBlog from '../components/EditBlog.vue'; // Import new page

const routes = [
  { path: '/', component: Home },
  { path: '/space', component: Space },
  { path: '/ai-chat', component: AIChat },
  { path: '/blog', component: Blog },
  { path: '/blog/new', component: CreateBlog },
  { path: '/blog/:id', component: BlogDetail },
  { path: '/blog/:id/edit', component: EditBlog }, // Route for editing posts
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;