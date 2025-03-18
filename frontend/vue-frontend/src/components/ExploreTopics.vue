<template>
    <section class="explore-topics text-center">
      <div class="container">
        <h2>Explore Topics</h2>
        <h6>coming soon...</h6>
        <div class="topics-container">
          <div class="topic">
            <span class="icon">🌍</span>
            <h3>Travel & Adventure</h3>
            <p>Discover breathtaking landscapes, capture the world through my lens, and embrace the thrill of exploration.</p>
          </div>
          <div class="topic">
            <span class="icon">⚙️</span>
            <h3>Engineering & Technology</h3>
            <p>From software engineering to system architecture and tech leadership—building solutions that drive innovation.</p>
          </div>
          <div class="topic">
            <span class="icon">🛰️</span>
            <h3>Science & Innovation</h3>
            <p>Exploring space, AI, cloud computing, and the future of scientific discovery.</p>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <style scoped>
  .explore-topics {
    padding: 50px 0;
    background: #f8f9fa;
  }
  
  /* Ensuring Cards Stay in One Line While Being Responsive */
  .topics-container {
    display: flex;
    justify-content: center;
    gap: 20px; /* Space between cards */
    align-items: stretch;
    max-width: 1100px; /* Prevents cards from being too wide */
    margin: 0 auto; /* Centers the container */
    width: 100%;
  }
  
  /* Individual Card Styling */
  .topic {
    flex: 1; /* Ensures all cards take the same width dynamically */
    max-width: 320px; /* Prevents cards from being too wide */
    min-width: 250px; /* Allows the cards to slim down if needed */
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    padding: 20px;
    border-radius: 10px;
    background: white;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
  }
  
  .topic:hover {
    transform: translateY(-5px);
  }
  
  .icon {
    font-size: 40px;
  }
  
  /* Media Query to Adjust for Narrow Screens */
  @media (max-width: 900px) {
    .topics-container {
      gap: 10px; /* Reduce space between cards */
    }
    .topic {
      max-width: 280px; /* Adjust max width on smaller screens */
      min-width: 220px; /* Make cards slimmer if needed */
    }
  }
  </style>