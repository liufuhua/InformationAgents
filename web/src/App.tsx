import { useEffect, useMemo, useState } from "react";
import {
  collectTrendRadar,
  loadLatestTrendRadar,
  SourceItem,
  TrendRadarResponse,
} from "./api/trendRadar";
import { DetailDrawer } from "./components/DetailDrawer";
import { ResultTable } from "./components/ResultTable";
import { RunSummary } from "./components/RunSummary";
import { SourceRail } from "./components/SourceRail";

const sources = [
  "GitHub Search",
  "GitHub Trending",
  "Hacker News",
  "arXiv",
  "Hugging Face",
  "V2EX",
];

export default function App() {
  const [activeSource, setActiveSource] = useState<string>("All");
  const [status, setStatus] = useState<"idle" | "collecting" | "complete" | "error">("idle");
  const [response, setResponse] = useState<TrendRadarResponse | null>(null);
  const [selectedItem, setSelectedItem] = useState<SourceItem | null>(null);

  const items = response?.run.items ?? [];
  const filteredItems = useMemo(() => {
    if (activeSource === "All") return items;
    return items.filter((item) => item.source === activeSource);
  }, [activeSource, items]);

  useEffect(() => {
    let isCurrent = true;

    async function loadLatestRun() {
      try {
        const result = await loadLatestTrendRadar();
        if (isCurrent && result) {
          setResponse(result);
          setStatus("complete");
        }
      } catch {
        if (isCurrent) {
          setStatus("error");
        }
      }
    }

    loadLatestRun();

    return () => {
      isCurrent = false;
    };
  }, []);

  async function handleCollect() {
    setStatus("collecting");
    setSelectedItem(null);
    try {
      const result = await collectTrendRadar();
      setResponse(result);
      setStatus("complete");
    } catch {
      setStatus("error");
    }
  }

  return (
    <main className="app-shell">
      <header className="top-bar">
        <div>
          <h1 className="title">AI Trend Radar</h1>
          <p>Run once, inspect source data, then pass structured results downstream.</p>
        </div>
        <button className="collect-button" disabled={status === "collecting"} onClick={handleCollect}>
          {status === "collecting" ? "Collecting" : "Collect"}
        </button>
      </header>

      <section className="workbench">
        <SourceRail
          activeSource={activeSource}
          sources={sources}
          items={items}
          onSelectSource={setActiveSource}
        />
        <section className="panel">
          <RunSummary response={response} status={status} />
          <ResultTable items={filteredItems} onSelectItem={setSelectedItem} />
        </section>
        <DetailDrawer item={selectedItem} />
      </section>
    </main>
  );
}
