import type { ResearchSource } from "../types";

interface AnswerCardProps {
  query: string;
  answer: string;
  /** Structured citations, available for a freshly generated result. */
  sources?: ResearchSource[];
  /** Plain-text source label, available when viewing a saved history entry. */
  sourceLabel?: string;
}

function sourceTypeLabel(type: string): string {
  if (type === "wikipedia") return "Wikipedia";
  if (type === "arxiv") return "arXiv";
  return type;
}

export default function AnswerCard({
  query,
  answer,
  sources,
  sourceLabel,
}: AnswerCardProps) {
  return (
    <section className="answer-card">
      <p className="eyebrow">Query</p>
      <h2 className="answer-card__query">{query}</h2>
      <p className="answer-card__answer">{answer}</p>

      {sources && sources.length > 0 && (
        <div className="answer-card__sources">
          <p className="eyebrow" style={{ marginBottom: 2 }}>
            Sources
          </p>
          {sources.map((source, index) => (
            <a
              key={`${source.url}-${index}`}
              className="source-chip"
              href={source.url}
              target="_blank"
              rel="noreferrer noopener"
            >
              <span className={`source-chip__type source-chip__type--${source.type}`}>
                {sourceTypeLabel(source.type)}
              </span>
              <span className="source-chip__title">{source.title}</span>
            </a>
          ))}
        </div>
      )}

      {!sources && sourceLabel && (
        <div className="answer-card__sources">
          <p className="eyebrow" style={{ marginBottom: 2 }}>
            Source
          </p>
          <span className="state-message" style={{ padding: 0 }}>
            {sourceLabel}
          </span>
        </div>
      )}
    </section>
  );
}
