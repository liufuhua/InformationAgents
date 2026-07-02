import { TrendRadarResponse } from "../api/trendRadar";

type Props = {
  response: TrendRadarResponse | null;
  status: "idle" | "collecting" | "complete" | "error";
};

export function RunSummary({ response, status }: Props) {
  return (
    <div className="summary-row">
      <div className="metric">
        <span className="metric-label">Status</span>
        <span className="metric-value">{status}</span>
      </div>
      <div className="metric">
        <span className="metric-label">Items</span>
        <span className="metric-value">{response?.run.items.length ?? 0}</span>
      </div>
      <div className="metric">
        <span className="metric-label">Errors</span>
        <span className="metric-value">{response?.run.errors.length ?? 0}</span>
      </div>
    </div>
  );
}
