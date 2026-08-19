export interface ResearchSource {
  type: string;
  title: string;
  url: string;
}

export interface ResearchResponse {
  id: number;
  query: string;
  answer: string;
  sources: ResearchSource[];
}

export interface HistoryItem {
  id: number;
  query: string;
  answer: string;
  source: string;
  favorite: boolean;
  created_at: string;
}
