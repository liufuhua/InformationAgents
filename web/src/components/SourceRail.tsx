import { SourceItem } from "../api/trendRadar";

type Props = {
  activeSource: string;
  sources: string[];
  items: SourceItem[];
  onSelectSource: (source: string) => void;
};

export function SourceRail({ activeSource, sources, items, onSelectSource }: Props) {
  const allSources = ["All", ...sources];

  return (
    <aside className="panel">
      {allSources.map((source) => {
        const count = source === "All" ? items.length : items.filter((item) => item.source === source).length;
        return (
          <button
            className={`source-button ${activeSource === source ? "active" : ""}`}
            key={source}
            onClick={() => onSelectSource(source)}
          >
            {source} · {count}
          </button>
        );
      })}
    </aside>
  );
}
