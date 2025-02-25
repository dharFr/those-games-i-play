<script setup lang="ts">
import type { GameFilters } from '@/types/game'
import { ref, watch } from 'vue'

const props = defineProps<{
  modelValue: Partial<GameFilters>
}>()

const emit = defineEmits<{
  (e: 'update:modelValue', value: Partial<GameFilters>): void
}>()

const filters = ref(props.modelValue)

watch(filters, (newFilters) => {
  emit('update:modelValue', newFilters)
}, { deep: true })
</script>

<template>
  <div class="filter-panel">
    <h3>Filters</h3>
    
    <div class="filter-section">
      <label>Price Range</label>
      <div class="price-range">
        <input 
          type="number" 
          v-model="filters.price_min" 
          placeholder="Min"
          min="0"
        >
        <span>-</span>
        <input 
          type="number" 
          v-model="filters.price_max" 
          placeholder="Max"
          min="0"
        >
      </div>
    </div>

    <div class="filter-section">
      <label>Sort by</label>
      <select v-model="filters.sort_by">
        <option value="release_date">Release Date</option>
        <option value="price">Price</option>
        <option value="review_score">Review Score</option>
      </select>
      <select v-model="filters.sort_order">
        <option value="asc">Ascending</option>
        <option value="desc">Descending</option>
      </select>
    </div>
  </div>
</template>

<style scoped>
.filter-panel {
  padding: 1rem;
  background: var(--color-background-soft);
  border-radius: 8px;
}

.filter-section {
  margin: 1rem 0;
}

.price-range {
  display: flex;
  gap: 0.5rem;
  align-items: center;
}

.price-range input {
  width: 80px;
}
</style>
