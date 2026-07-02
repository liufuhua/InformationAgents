import { SourceItem } from "../api/trendRadar";

type Props = {
  items: SourceItem[];
  onSelectItem: (item: SourceItem) => void;
};

export function ResultTable({ items, onSelectItem }: Props) {
  if (items.length === 0) {
    return <p>Click Collect to run one source collection.</p>;
  }

  return (
    <table className="result-table">
      <thead>
        <tr>
          <th>Title</th>
          <th>Source</th>
          <th>Stars</th>
          <th>Today</th>
          <th>Language</th>
          <th>Readable</th>
        </tr>
      </thead>
      <tbody>
        {items.map((item) => (
          <tr className="result-row" key={item.id} onClick={() => onSelectItem(item)}>
            <td>{item.title}</td>
            <td><span className="badge">{item.source}</span></td>
            <td>{item.signals.stars ?? "-"}</td>
            <td>{item.signals.star_growth ?? "-"}</td>
            <td>{item.signals.language ?? "-"}</td>
            <td>{item.eligibility.can_read ? "Readable" : "Not readable"}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
