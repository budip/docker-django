<template>
    <div class="edit-blog-container">
        <header class="blog-header">
            <h2 class="blog-title">📝 Blog - Edit</h2>
        </header>        

        <form @submit.prevent="updatePost">
            <div class="form-group">
                <label for="title">Title:</label>
                <input type="text" id="title" v-model="title" required />
            </div>
    
            <div class="form-group">
                <label for="content">Content (Markdown Supported):</label>
                <textarea id="content" v-model="content" required></textarea>
            </div>
    
            <div class="button-container">
                <button type="submit" class="action-btn save-btn">💾 Save Changes</button>
                <button type="button" class="action-btn cancel-btn" @click="cancelEdit">❌ Cancel</button>
            </div>
        </form>
  
        <div v-if="successMessage" class="success-message">
            ✅ Blog post updated! <router-link :to="`/blog/${postId}`">View post</router-link>
        </div>
    </div>
</template>
  
<script setup>
    import { ref, onMounted } from 'vue';
    import { useRoute, useRouter } from 'vue-router';

    const route = useRoute();
    const router = useRouter();
    const postId = route.params.id;

    const title = ref('');
    const content = ref('');
    const successMessage = ref(null);
  
    onMounted(async () => {
        try {
        const response = await fetch(`http://127.0.0.1:8000/blog/posts/${postId}/`);
        if (!response.ok) throw new Error("Post not found");
        const post = await response.json();
        title.value = post.title;
        content.value = post.content;
        } catch (error) {
        console.error("Error fetching blog post:", error);
        }
    });
  
    const updatePost = async () => {
        try {
        const response = await fetch(`http://127.0.0.1:8000/blog/posts/${postId}/`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title: title.value, content: content.value })
        });
    
        if (response.ok) {
            successMessage.value = "Blog post updated!";
            setTimeout(() => router.push(`/blog/${postId}`), 2000);
        } else {
            throw new Error("Failed to update post");
        }
        } catch (error) {
        console.error("Error updating blog post:", error);
        }
    };
  
    const cancelEdit = () => {
        router.push(`/blog/${postId}`);
    };
</script>
  
<style scoped>
    .edit-blog-container {
        max-width: 800px;
        margin: 40px auto;
        padding: 20px;
        background: #ffffff;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }

    .blog-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-top: 20px;
        margin-bottom: 25px;
        padding-bottom: 12px;
        border-bottom: 2px solid #ddd;
    }
  
    .blog-title {
        font-size: 26px;
        font-weight: bold;
        color: #333;
        display: flex;
        align-items: center;
    }

    .blog-header .button-container {
        display: flex;
        gap: 10px;
    }    
  
    h2 {
        font-size: 26px;
        font-weight: bold;
        color: #333;
        text-align: center;
    }
  
    .form-group {
        margin-bottom: 15px;
    }
  
    label {
        font-weight: bold;
    }
    
    input, textarea {
        width: 100%;
        padding: 12px;
        border: 1px solid #ccc;
        border-radius: 5px;
        background: #f7f7f7;
        font-size: 16px;
    }
  
    textarea {
        height: 400px;
    }
    
    .button-container {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-top: 20px;
    }
     
    .success-message {
        margin-top: 15px;
        padding: 10px;
        background: #d4edda;
        color: #155724;
        border-radius: 5px;
        text-align: center;
    }

    .action-btn {
        padding: 10px 15px;
        font-size: 14px;
        font-weight: bold;
        text-decoration: none;
        border-radius: 5px;
        display: inline-block;
        transition: background 0.3s ease-in-out;
    }

    .save-btn {
        background: #ccd9e8;
        color: #4e4d4d;
        padding: 10px 15px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background 0.2s ease-in-out;
    }

    .save-btn:hover {
        background: #5598e0;
    }

    .cancel-btn {
        background: #dad8d8;
        color: #4e4d4d;
        padding: 10px 15px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background 0.2s ease-in-out;
    }

    .cancel-btn:hover {
        background: #ea8591; /* Soft red on hover */
    }
</style>