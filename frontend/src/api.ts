import type { ResearchResponse, HistoryItem } from "./types";

const API_BASE_URL: string =
  (import.meta.env.VITE_API_BASE_URL as string | undefined) ??
  "http://localhost:8000";

async function handleResponse<T>(response: Response): Promise<T> {
  if (!response.ok) {
    let detail = `Request failed with status ${response.status}`;
    try {
      const body = await response.json();
      if (body?.detail) {
        detail = typeof body.detail === "string" ? body.detail : detail;
      }
    } catch {
      // response had no JSON body; fall back to the generic message
    }
    throw new Error(detail);
  }
  return response.json() as Promise<T>;
}

export async function postResearch(query: string): Promise<ResearchResponse> {
  const response = await fetch(`${API_BASE_URL}/research`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query }),
  });
  return handleResponse<ResearchResponse>(response);
}

export async function getHistory(): Promise<HistoryItem[]> {
  const response = await fetch(`${API_BASE_URL}/history`);
  return handleResponse<HistoryItem[]>(response);
}

export async function deleteHistoryItem(id: number): Promise<void> {
  const response = await fetch(`${API_BASE_URL}/history/${id}`, {
    method: "DELETE",
  });
  await handleResponse<{ message: string }>(response);
}

export async function toggleFavorite(
  id: number
): Promise<{ id: number; favorite: boolean }> {
  const response = await fetch(`${API_BASE_URL}/history/${id}/favorite`, {
    method: "POST",
  });
  return handleResponse<{ id: number; favorite: boolean }>(response);
}
