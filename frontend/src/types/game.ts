export interface Game {
  steam_id: number
  title: string
  genres: string[]
  tags: string[]
  price: number
  release_date: string
  review_score: number
  review_count: number
}

export interface GameFilters {
  genres: string[]
  tags: string[]
  price_min?: number
  price_max?: number
  released_after?: string
  released_before?: string
  sort_by?: string
  sort_order?: 'asc' | 'desc'
}

export interface PaginationMetadata {
  total_items: number
  total_pages: number
  current_page: number
  items_per_page: number
}
