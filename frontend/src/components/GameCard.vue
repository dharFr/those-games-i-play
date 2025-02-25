<script setup lang="ts">
import type { Game } from '@/types/game'

defineProps<{
  game: Game
}>()
</script>

<template>
  <div class="game-card">
    <img :src="`https://cdn.akamai.steamstatic.com/steam/apps/${game.steam_id}/header.jpg`" :alt="game.title">
    <div class="game-info">
      <h3>{{ game.title }}</h3>
      <div class="meta">
        <span class="price">${{ game.price.toFixed(2) }}</span>
        <span class="score">{{ game.review_score }}% ({{ game.review_count }})</span>
      </div>
      <div class="tags">
        <span v-for="genre in game.genres.slice(0, 3)" :key="genre" class="tag">
          {{ genre }}
        </span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.game-card {
  border-radius: 8px;
  overflow: hidden;
  background: var(--color-background-soft);
  transition: transform 0.2s;
}

.game-card:hover {
  transform: translateY(-2px);
}

.game-card img {
  width: 100%;
  height: 150px;
  object-fit: cover;
}

.game-info {
  padding: 1rem;
}

.meta {
  display: flex;
  justify-content: space-between;
  margin: 0.5rem 0;
}

.tags {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.tag {
  font-size: 0.8rem;
  padding: 0.2rem 0.5rem;
  background: var(--color-background-mute);
  border-radius: 4px;
}
</style>
