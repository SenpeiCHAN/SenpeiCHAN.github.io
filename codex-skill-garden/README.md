# Codex Skill Garden

A portable collection of personal Codex skills, cleaned up to remove duplicate local skills that are already supplied by enabled plugins.

## Package

- `codex-skill-garden-20260609.tar.gz`
- Contains 56 personal Codex skills
- Excludes system skills under `.system`
- Excludes duplicate Figma/plugin compatibility skills

## Install On Another Computer

Download and extract the archive, then copy the folders inside `skills/` into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
tar -xzf codex-skill-garden-20260609.tar.gz
cp -R codex-skills-package-20260609/skills/* ~/.codex/skills/
```

Restart Codex after copying so the skills list refreshes.

## Removed During Cleanup

These local skills were removed before packaging because they duplicate plugin-provided skills or a stronger local skill:

- `figma-code-connect-components`
- `figma-create-new-file`
- `figma-generate-design`
- `figma-generate-library`
- `figma-use`
- `writing-plans`
