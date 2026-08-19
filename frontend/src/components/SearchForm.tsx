import { useState, FormEvent } from "react";

interface SearchFormProps {
  onSubmit: (query: string) => void;
  isLoading: boolean;
}

export default function SearchForm({ onSubmit, isLoading }: SearchFormProps) {
  const [query, setQuery] = useState("");

  function handleSubmit(event: FormEvent) {
    event.preventDefault();
    const trimmed = query.trim();
    if (!trimmed || isLoading) return;
    onSubmit(trimmed);
  }

  return (
    <form className="search-form" onSubmit={handleSubmit}>
      <input
        className="search-form__input"
        type="text"
        value={query}
        onChange={(event) => setQuery(event.target.value)}
        placeholder="Ask about a topic, e.g. transformer attention mechanisms"
        aria-label="Research query"
      />
      <button className="search-form__submit" type="submit" disabled={isLoading}>
        {isLoading ? "Researching…" : "Research"}
      </button>
    </form>
  );
}
