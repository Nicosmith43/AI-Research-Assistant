import type { HistoryItem } from "../types";

interface HistoryListProps {
  items: HistoryItem[];
  onSelect: (item: HistoryItem) => void;
  onToggleFavorite: (id: number) => void;
  onDelete: (id: number) => void;
}

function formatDate(isoString: string): string {
  try {
    return new Date(isoString).toLocaleDateString(undefined, {
      month: "short",
      day: "numeric",
    });
  } catch {
    return "";
  }
}

export default function HistoryList({
  items,
  onSelect,
  onToggleFavorite,
  onDelete,
}: HistoryListProps) {
  if (items.length === 0) {
    return (
      <p className="state-message">
        No research yet. Ask something above to start building your history.
      </p>
    );
  }

  return (
    <div className="history-list">
      {items.map((item) => (
        <div key={item.id} className="history-row" role="listitem">
          <button
            className="history-row__query"
            style={{
              background: "none",
              border: "none",
              padding: 0,
              font: "inherit",
              color: "inherit",
              cursor: "pointer",
              textAlign: "left",
            }}
            onClick={() => onSelect(item)}
            title={item.query}
          >
            {item.query}
          </button>
          <span className="history-row__date">{formatDate(item.created_at)}</span>
          <div className="history-row__actions">
            <button
              className="icon-button icon-button--favorite"
              data-active={item.favorite}
              onClick={() => onToggleFavorite(item.id)}
              aria-label={item.favorite ? "Remove favorite" : "Mark as favorite"}
              aria-pressed={item.favorite}
            >
              {item.favorite ? "★" : "☆"}
            </button>
            <button
              className="icon-button icon-button--delete"
              onClick={() => onDelete(item.id)}
              aria-label="Delete this research entry"
            >
              ✕
            </button>
          </div>
        </div>
      ))}
    </div>
  );
}
