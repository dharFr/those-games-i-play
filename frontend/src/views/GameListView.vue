<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useGamesStore } from '@/stores/games'
import GameCard from '@/components/GameCard.vue'
import FilterPanel from '@/components/FilterPanel.vue'
import type { GameFilters } from '@/types/game'

const gamesStore = useGamesStore()
const filters = ref<Partial<GameFilters>>({
  sort_by: 'release_date',
  sort_order: 'desc'
})

async function loadGames() {
  await gamesStore.fetchGames(gamesStore.metadata.current_page, filters.value)
}

function handleFiltersChange() {
  gamesStore.metadata.current_page = 1
  loadGames()
}

onMounted(() => {
  loadGames()
})
</script>

<template>
  <div class="game-list">
    <aside class="filters">
      <FilterPanel v-model="filters" @update:modelValue="handleFiltersChange" />
    </aside>
    
    <div class="content">
      <div v-if="gamesStore.isLoading" class="loading">
        Loading...
      </div>
      <div v-else-if="gamesStore.error" class="error">
        {{ gamesStore.error }}
      </div>
      <div v-else class="games-grid">
        <GameCard 
          v-for="game in gamesStore.games" 
          :key="game.steam_id" 
          :game="game" 
        />
      </div>
    </div>
  </div>
</template>

<style scoped>
.game-list {
  display: grid;
  grid-template-columns: 250px 1fr;
  gap: 2rem;
}

.games-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1rem;
}

.loading, .error {
  text-align: center;
  padding: 2rem;
}
</style>
