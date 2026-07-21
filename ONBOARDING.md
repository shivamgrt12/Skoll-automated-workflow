# Skoll Automated Workflow — Onboarding

This repo builds a complete Skoll input bundle for a persona with **one command**.
It is an [opencode](https://opencode.ai) skill (`skoll-bundle-builder`) plus the
sample persona inputs and the mock-service registry it needs.

## What's in here

| Path | What it is |
|------|-----------|
| `.opencode/skills/skoll-bundle-builder/` | The skill: pipeline CLI, generator prompts, QC gates, templates |
| `SKOLL_GK/Environment_SN_Harness/` | The 104-service registry (`service.toml` ports) the skill reads |
| `Persona_testing/` | Three sample persona inputs (`crystal-hayes`, `daichi-mosley`, `vivek-thompson`) |
| `Input_bundles_3rd_july/` | An example output destination (starts empty) |

## One-time setup

1. **Install opencode** (v1.15.0 or newer) and authenticate once:
   ```bash
   opencode auth login
   ```
2. **Install the two Python dependencies** (everything else is standard library):
   ```bash
   pip install -r requirements.txt   # pyyaml
   ```
   Python 3.11+ is required.

## How to run it

**Always run from the repo root** (the folder containing `.opencode/`,
`SKOLL_GK/`, and `Persona_testing/`). The skill finds the service registry via
the relative path `SKOLL_GK/Environment_SN_Harness`, so it must be your working
directory.

### The easy way — in opencode chat

Open `opencode` at the repo root and say, for example:

> build a Skoll bundle for crystal-hayes into ./Input_bundles_3rd_july/crystal-hayes_01

The skill will **ask you three design questions in chat** before it runs:

1. **Turn shape** — `single` or `multi`
2. **Domain** — `enterprise`, `personal`, or `professional`
3. **Fixed anchor** — an event/deadline the task hangs on (optional)

Answer them and it takes over: prompt → rubric/tests → truth → assemble → QC.
You choose where the finished bundle goes; there is no hardcoded output folder.

### The direct way — the CLI

```bash
python3 .opencode/skills/skoll-bundle-builder/cli/skoll_bundle.py \
  --input Persona_testing/crystal-hayes \
  --work /tmp/skoll_work \
  --out  ./Input_bundles_3rd_july/crystal-hayes_01 \
  --meta <your-meta.yaml> \
  --turn-shape multi --domain enterprise
```

`--input`, `--work`, `--out`, and `--meta` are required. Passing `--turn-shape`
and `--domain` (and optionally `--anchor`) skips the interactive questions.
Use `--auto` for a fully unattended run (the model infers any unset design
fields). `--harness` defaults to `SKOLL_GK/Environment_SN_Harness`, so you only
need it if you run from somewhere other than the repo root.

## Quality control

QC runs **mid-pipeline** (after each generating stage, with an auto-fix loop)
**and** once more against the fully assembled bundle. Blocking gates stop the run
so nothing broken ships. See the skill's `SKILL.md` for the gate roster and how
to drop in new gates.
