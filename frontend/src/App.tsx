import { useEffect, useState, useCallback } from "react";
import SearchForm from "./components/SearchForm";
import AnswerCard from "./components/AnswerCard";
import HistoryList from "./components/HistoryList";
import { postResearch, getHistory, deleteHistoryItem, toggleFavorite } from "./api";
import type { ResearchResponse, HistoryItem } from "./types";

type ActiveAnswer =
  | { kind: "fresh"; data: ResearchResponse }
  | { kind: "history"; data: HistoryItem }
  | null;

export default function App() {
  const [activeAnswer, setActiveAnswer] = useState<ActiveAnswer>(null);
  const [history, setHistory] = useState<HistoryItem[]>([]);
  const [isSearching, setIsSearching] = useState(false);
  const [isHistoryLoading, setIsHistoryLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const loadHistory = useCallback(async () => {
    setIsHistoryLoading(true);
    try {
      const items = await getHistory();
      const sorted = [...items].sort(
        (a, b) => new Date(b.created_at).getTime() - new Date(a.created_at).getTime()
      );
      setHistory(sorted);
    } catch {
      // History failing to load shouldn't block the rest of the app.
    } finally {
      setIsHistoryLoading(false);
    }
  }, []);

  useEffect(() => {
    loadHistory();
  }, [loadHistory]);

  async function handleSearch(query: string) {
    setIsSearching(true);
    setErrorMessage(null);
    try {
      const result = await postResearch(query);
      setActiveAnswer({ kind: "fresh", data: result });
      await loadHistory();
    } catch (error) {
      setErrorMessage(
        error instanceof Error
          ? error.message
          : "Something went wrong reaching the research API."
      );
    } finally {
      setIsSearching(false);
    }
  }

  function handleSelectHistoryItem(item: HistoryItem) {
    setErrorMessage(null);
    setActiveAnswer({ kind: "history", data: item });
  }

  async function handleToggleFavorite(id: number) {
    try {
      await toggleFavorite(id);
      await loadHistory();
    } catch {
      setErrorMessage("Couldn't update favorite status. Try again.");
    }
  }

  async function handleDelete(id: number) {
    try {
      await deleteHistoryItem(id);
      if (activeAnswer?.kind === "history" && activeAnswer.data.id === id) {
        setActiveAnswer(null);
      }
      await loadHistory();
    } catch {
      setErrorMessage("Couldn't delete that entry. Try again.");
    }
  }

  return (
    <div className="page">
      <header className="site-header">
        <h1 className="site-header__title">AI Research Assistant</h1>
        <p className="site-header__tagline">
          Ask a question and get an explanation synthesized from Wikipedia and arXiv.
        </p>
      </header>

      <SearchForm onSubmit={handleSearch} isLoading={isSearching} />

      {errorMessage && <p className="state-message state-message--error">{errorMessage}</p>}

      {isSearching && !activeAnswer && (
        <p className="state-message">Reading Wikipedia and arXiv…</p>
      )}

      {activeAnswer?.kind === "fresh" && (
        <AnswerCard
          query={activeAnswer.data.query}
          answer={activeAnswer.data.answer}
          sources={activeAnswer.data.sources}
        />
      )}

      {activeAnswer?.kind === "history" && (
        <AnswerCard
          query={activeAnswer.data.query}
          answer={activeAnswer.data.answer}
          sourceLabel={activeAnswer.data.source}
        />
      )}

      <section>
        <div className="history-section__header">
          <p className="eyebrow" style={{ margin: 0 }}>
            History
          </p>
        </div>
        {isHistoryLoading ? (
          <p className="state-message">Loading history…</p>
        ) : (
          <HistoryList
            items={history}
            onSelect={handleSelectHistoryItem}
            onToggleFavorite={handleToggleFavorite}
            onDelete={handleDelete}
          />
        )}
      </section>
    </div>
  );
}
