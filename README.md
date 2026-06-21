# SenpeiCHAN.github.io

Personal GitHub Pages repository for Chen Senpei / Pacey Chen.

This repo currently contains:

- A static personal design research site: `index.html`, `about.html`, `404.html`, `public/`.
- Vercel deployment configuration: `package.json`, `vercel.json`.
- A robot product research library: `机器人产品资料库_2026-06-21/`.
- Download and extraction utilities for the robot research library: `scripts/`.

## Local Development

```bash
npm run build
```

The build command copies the static site into `dist/`, which is used as the Vercel output directory.

## Robot Research Library

The robot product research library was generated from:

- `机器人产品调研简报索引表.xlsx`
- `个人PRD_人形机器人产品实习能力建设系统.docx`

The committed library contains downloaded PDFs, saved web pages, source sidecars, metadata manifests, and a project note:

```text
机器人产品资料库_2026-06-21/
├── 01_Excel链接资料/
├── 02_Word补充资料/
├── 03_下载受限网页快照/
├── _metadata/
└── README_项目说明.md
```

The zip archive is intentionally ignored because the expanded library is already tracked.

## Repo Hygiene

Generated build output, local deployment state, caches, debug images, and archive files are ignored through `.gitignore`.
