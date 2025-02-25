import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { Game, GameFilters, PaginationMetadata } from '@/types/game'

function formatQueryParams(params: Record<string, any>): Record<string, string> {
  const result: Record<string, string> = {}
  
  Object.entries(params).forEach(([key, value]) => {
    if (value === null || value === undefined) return
    
    if (Array.isArray(value)) {
      result[key] = value.join(',')
    } else {
      result[key] = String(value)
    }
  })
  
  return result
}

export const useGamesStore = defineStore('games', () => {
  const games = ref<Game[]>([])
  const isLoading = ref(false)
  const error = ref<string | null>(null)
  const metadata = ref<PaginationMetadata>({
    total_items: 0,
    total_pages: 0,
    current_page: 1,
    items_per_page: 20
  })

  async function fetchGames(page: number = 1, filters: Partial<GameFilters> = {}) {
    isLoading.value = true
    error.value = null
    
    try {
      const cleanFilters = Object.fromEntries(
        Object.entries(filters).filter(([_, value]) => value !== null && value !== undefined)
      )
      
      const queryParams = new URLSearchParams(
        formatQueryParams({
          page,
          ...cleanFilters
        })
      )
      
      const response = await fetch(`${process.env.API_URL}/api/v1/games?${queryParams}`)
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      
      const data = await response.json()
      games.value = data.items
      metadata.value = data.metadata
    } catch (e) {
      error.value = 'Failed to load games'
      console.error(e)
    } finally {
      isLoading.value = false
    }
  }

  return {
    games,
    isLoading,
    error,
    metadata,
    fetchGames
  }
})
