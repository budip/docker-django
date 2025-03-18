<template>
    <div class="nasa-container">
      <h2 class="title">NASA Astronomy Picture of the Day</h2>
      <div v-if="apod" class="apod-content">
        <h3 class="apod-title">{{ apod.title }}</h3>
        <p class="apod-date">{{ apod.date }}</p>
        <div class="media-container">
          <img v-if="apod.media_type === 'image'" :src="apod.url" :alt="apod.title" class="apod-image"/>
          <iframe v-else :src="apod.url" frameborder="0" class="apod-video"></iframe>
        </div>
        <p class="apod-explanation">{{ apod.explanation }}</p>
      </div>
      <div v-else class="loading">Loading...</div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  
  const apod = ref(null);
  
  onMounted(async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/nasa/apod/'); // Adjust based on your Django backend
      const data = await response.json();
      apod.value = data;
    } catch (error) {
      console.error("Error fetching APOD data:", error);
    }
  });
  </script>
  
  <style scoped>
  .nasa-container {
    max-width: 900px;
    margin: 50px auto;
    padding: 20px;
    background: #f9f9f9;
    border-radius: 10px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    text-align: center;
  }
  
  .title {
    font-size: 26px;
    font-weight: bold;
    color: #333;
    margin-bottom: 20px;
  }
  
  .apod-content {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .apod-title {
    font-size: 22px;
    font-weight: bold;
    color: #222;
    margin-bottom: 5px;
  }
  
  .apod-date {
    font-size: 16px;
    color: #666;
    margin-bottom: 20px;
  }
  
  .media-container {
    width: 100%;
    display: flex;
    justify-content: center;
    margin-bottom: 20px;
  }
  
  .apod-image {
    max-width: 100%;
    height: auto;
    border-radius: 10px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.15);
  }
  
  .apod-video {
    width: 100%;
    max-width: 700px;
    height: 400px;
    border-radius: 10px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.15);
  }
  
  .apod-explanation {
    font-size: 16px;
    color: #444;
    line-height: 1.6;
    text-align: justify;
    padding: 0 20px;
  }
  
  .loading {
    font-size: 18px;
    font-weight: bold;
    color: #555;
  }
  </style>