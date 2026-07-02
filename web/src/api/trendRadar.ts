export type SourceSignals = {
  stars?: number | null;
  star_growth?: number | null;
  forks?: number | null;
  language?: string | null;
  owner_repo?: string | null;
  updated_at?: string | null;
};

export type SourceItem = {
  id: string;
  title: string;
  source: string;
  url: string;
  raw_content: string;
  signals: SourceSignals;
  eligibility: {
    can_read: boolean;
    reason: string;
  };
  evidence: unknown[];
};

export type TrendRadarRun = {
  run_id: string;
  collected_at: string;
  enabled_sources: string[];
  items: SourceItem[];
  errors: { source: string; message: string }[];
};

export type TrendRadarResponse = {
  run: TrendRadarRun;
  output_path: string;
};

export async function collectTrendRadar(): Promise<TrendRadarResponse> {
  const response = await fetch("/api/trend-radar/collect", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      query: "AI agent",
      sources: ["github_search", "github_trending"],
      limit: 20,
      output_dir: "data/runs",
    }),
  });

  if (!response.ok) {
    throw new Error(`Collection failed: ${response.status}`);
  }

  return response.json();
}
