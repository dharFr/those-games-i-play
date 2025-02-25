<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<template>
  <header class="header">
    <nav>
      <RouterLink to="/">Games</RouterLink>
      <RouterLink to="/recommendations">Recommendations</RouterLink>
    </nav>
    <div class="search">
      <input type="search" placeholder="Search games..." />
    </div>
  </header>
</template>

<style scoped>
.header {
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid var(--color-border);
}

nav a {
  margin-right: 1rem;
}
</style>
