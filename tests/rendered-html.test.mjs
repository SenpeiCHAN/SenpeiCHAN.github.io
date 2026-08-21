import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

async function render(pathname = "/") {
  const workerUrl = new URL("../dist/server/index.js", import.meta.url);
  workerUrl.searchParams.set("test", `${process.pid}-${Date.now()}-${pathname}`);
  const { default: worker } = await import(workerUrl.href);

  return worker.fetch(
    new Request(`http://localhost${pathname}`, {
      headers: { accept: "text/html" },
    }),
    {
      ASSETS: {
        fetch: async () => new Response("Not found", { status: 404 }),
      },
    },
    {
      waitUntil() {},
      passThroughOnException() {},
    },
  );
}

test("renders the Chinese academic portfolio home", async () => {
  const response = await render("/");
  assert.equal(response.status, 200);
  const html = await response.text();
  assert.match(html, /陈森培 Senpei Chen/);
  assert.match(html, /从人出发，研究技术该怎样回应/);
  assert.match(html, /人与智能硬件设备的交互/);
  assert.match(html, /文献与案例/);
  assert.match(html, /测试与反馈/);
  assert.match(html, /优化与结论/);
  assert.match(html, /chensenpei@email\.gzarts\.edu\.cn/);
  assert.match(html, /images\/profile\/senpei-chen\.png/);
  assert.doesNotMatch(html, /codex-preview|react-loading-skeleton/);
});

test("renders the documents interface", async () => {
  const response = await render("/documents");
  assert.equal(response.status, 200);
  const html = await response.text();
  assert.match(html, /简历与完整作品集/);
  assert.match(html, /Senpei-Chen-CV\.docx/);
  assert.match(html, /Senpei-Chen-Portfolio\.pdf/);
});

test("project content remains data-driven and expandable", async () => {
  const content = await readFile(new URL("../content/site.ts", import.meta.url), "utf8");
  assert.match(content, /status: "published"/);
  assert.match(content, /featuredRank/);
  assert.match(content, /sections:/);
  assert.match(content, /gallery:/);
  assert.match(content, /getPublishedProjects/);
  assert.match(content, /getFeaturedProjects/);
});

test("renders detailed bilingual project galleries", async () => {
  const chinese = await render("/work/qingzhu");
  assert.equal(chinese.status, 200);
  const chineseHtml = await chinese.text();
  assert.match(chineseHtml, /现有专注工具大多把操作留在屏幕里/);
  assert.match(chineseHtml, /07 · 优化与结论/);
  assert.match(chineseHtml, /qingzhu-design-goals\.jpg/);
  assert.match(chineseHtml, /qingzhu-design-system\.jpg/);

  const english = await render("/en/work/co-evo");
  assert.equal(english.status, 200);
  const englishHtml = await english.text();
  assert.match(englishHtml, /Embodied interaction treats movement as expression and input/);
  assert.match(englishHtml, /07 · Refinement &amp; conclusion/);
  assert.match(englishHtml, /co-evo-evaluation\.jpg/);
  assert.match(englishHtml, /co-evo-onsite\.jpg/);
});
