import { useEffect, useRef } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

import { SourceItem } from "../api/trendRadar";

type Props = {
  item: SourceItem | null;
};

export function DetailDrawer({ item }: Props) {
  const detailPanelRef = useRef<HTMLElement | null>(null);

  useEffect(() => {
    detailPanelRef.current?.scrollTo({ top: 0, behavior: "auto" });
  }, [item?.id]);

  if (!item) {
    return (
      <aside className="detail-panel" ref={detailPanelRef}>
        <p>Select an item to inspect evidence.</p>
      </aside>
    );
  }

  return (
    <aside className="detail-panel" ref={detailPanelRef}>
      <h2>{item.title}</h2>
      <section className="markdown-body">
        <ReactMarkdown remarkPlugins={[remarkGfm]}>
          {item.raw_content || "No raw content provided."}
        </ReactMarkdown>
      </section>
      <p>
        <a href={item.url} target="_blank" rel="noreferrer">
          Source URL
        </a>
      </p>
      <p>{item.eligibility.reason}</p>
      <pre className="json-preview">{JSON.stringify(item, null, 2)}</pre>
    </aside>
  );
}
