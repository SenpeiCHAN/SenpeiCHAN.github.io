import { cp, mkdir, readFile, rm, writeFile } from "node:fs/promises";
import { dirname, join, resolve } from "node:path";

const root = resolve(process.cwd());
const output = join(root, "docs");
const build = join(root, "dist");
const routes = [
  "/",
  "/work",
  "/work/qingzhu",
  "/work/co-evo",
  "/work/bingbing",
  "/work/hive-wings",
  "/about",
  "/documents",
  "/en",
  "/en/work",
  "/en/work/qingzhu",
  "/en/work/co-evo",
  "/en/work/bingbing",
  "/en/work/hive-wings",
  "/en/about",
  "/en/documents",
];

await rm(output, { recursive: true, force: true });
await mkdir(output, { recursive: true });
await cp(join(build, "client"), output, { recursive: true });
await writeFile(join(output, ".nojekyll"), "\n");

const { default: worker } = await import(`${join(build, "server/index.js")}?static=${Date.now()}`);

for (const route of routes) {
  const response = await worker.fetch(
    new Request(`https://senpeichan.github.io${route}`, {
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

  if (!response.ok) {
    throw new Error(`Could not render ${route}: ${response.status}`);
  }

  const target = route === "/"
    ? join(output, "index.html")
    : join(output, route.replace(/^\//, ""), "index.html");
  await mkdir(dirname(target), { recursive: true });
  await writeFile(target, await response.text());
}

await writeFile(join(output, "404.html"), await readFile(join(output, "index.html")));
console.log(`Exported ${routes.length} routes to ${output}`);
