# Batch Workflow — Running Many Personas at Once

This guide explains how to generate **many Skoll bundles in parallel** (for example
4 personas × 4 tasks = 16 bundles at the same time) on one machine, using
**opencode chat** — one session per job.

Read the **Steps** first — each step is numbered and short. The **Examples** are
further down.

---

## The steps (do these in order)

1. **Prepare the machine** — install opencode, log in, install Python deps.
2. **Put your inputs in place** — the folder structure + one meta file per job.
3. **Follow the naming rule** — every job uses three matching names (meta / work / output).
4. **Run each job** — one opencode chat per job, with the work dir stated explicitly.
5. **Monitor it** — check progress and spot failures.
6. **Recover failures** — re-run only the jobs that failed, using `--resume`.

---

## Step 1 — Prepare the machine

On the machine that will run the batch (e.g. the EC2 box):

- Install **opencode v1.15.0 or newer** and make sure it is on `PATH`
  (check with `which opencode`).
- Run **`opencode auth login`** on this machine.
  Login is **per-machine** — it is not shared from your laptop.
- Place both config files in `~/.config/opencode/`
  (`opencode.json` + `oh-my-openagent.json`), all models pinned to
  `anthropic/claude-opus-4-8`.
- Install the Python dependencies:

  ```bash
  pip install -r requirements.txt      # pyyaml + Pillow
  ```

---

## Step 2 — Put your inputs in place

When you clone the repo, you get **only these** (everything else you add yourself):

```
bundle-generator/                       # the repo root — run every command from here
├── .opencode/                          # the generator itself (the engine — do not touch)
├── SKOLL_GK/Environment_SN_Harness/    # the harness (default location)
├── metas/                              # ships EMPTY — you add one meta file per job
├── ONBOARDING.md
├── USING_THE_GENERATOR.md
└── requirements.txt
```

You add **exactly two things** yourself:

```
bundle-generator/
├── Persona/<persona>/                  # ADD THIS: persona inputs from your team lead
│                                       #   (7 .md files + home/ + task/ + mock_data/)
└── metas/<persona>__task<N>.yaml       # ADD THESE: one meta file per job (you author them)
```

Everything else is **created for you by the generator** — you never make these by hand:

```
bundle-generator/
├── .work/<persona>__task<N>            # created when the job starts (scratch + manifest)
└── Output/<persona>_task<N>            # created when the job reaches the assemble stage
```

> `Output/<persona>_task<N>` only appears once a job runs far enough to assemble the
> bundle. If a job fails in an early stage, you may not see its Output folder yet —
> that is expected; fix the job and re-run with `--resume`.

So after you drop in a persona and author your metas, the working root looks like:

```
bundle-generator/
├── .opencode/                          # shipped in the clone
├── SKOLL_GK/Environment_SN_Harness/    # shipped in the clone
├── Persona/jennifer-tanaka/            # ← you added
├── metas/                              # ← you authored (one file per job)
│   ├── jennifer-tanaka__task1.yaml
│   ├── jennifer-tanaka__task2.yaml
│   ├── jennifer-tanaka__task3.yaml
│   └── jennifer-tanaka__task4.yaml
├── .work/                              # ← appears automatically when jobs run
└── Output/                             # ← fills up automatically as jobs finish
```

- **One meta file per job** at `metas/<persona>__task<N>.yaml`
  (you author these — each meta is the design brief for one task).

---

## Step 3 — Follow the naming rule (the most important step)

Every `(persona, task)` job is defined by **three matching names**. Pick this scheme
and never deviate:

```
metas/<persona>__task<N>.yaml     ←  you author this (the design brief)
.work/<persona>__task<N>          ←  created automatically (scratch + manifest, unique per job)
Output/<persona>_task<N>          ←  created automatically (final bundle, unique per job)
```

**You only author the meta file.** The `.work/` and `Output/` folders are **created
for you automatically** on the first run — you never make them by hand. Your job is
just to **name** a unique `.work/<persona>__task<N>` for each job (in the prompt or the
`--work` flag); the generator then creates that folder itself.

**Why this matters:** the `__task<N>` part in the **work dir** is what guarantees that
16 jobs running at once never share a manifest and never overwrite each other.
**This one rule is what the whole batch rests on.** If two jobs share a work dir,
they corrupt each other.

Rules of thumb:
- Same persona is fine across many jobs (the persona folder is only read, never changed).
- The **work dir must be unique for every single job** — but you only *name* it, the
  generator *creates* it.
- The output dir must be unique too (also created for you).

---

## Step 4 — Run each job (one opencode chat per job)

Open one opencode chat per job and type the prompt below, filling the three paths
from the naming rule. This is safe for parallel runs **only because you state the
work dir explicitly** — the agent no longer picks it, so two jobs can never collide.

```
build perfect skoll bundle for Persona/jennifer-tanaka,
use work dir .work/jennifer-tanaka__task1,
meta metas/jennifer-tanaka__task1.yaml,
and save it in Output/jennifer-tanaka_task1
```

Each job = one opencode session with its own unique work / meta / output.
Same skill, same 6 stages, same Opus 4.8 — identical output every time.

### CRUCIAL: one prompt per chat, NOT all prompts in one chat

To run tasks **in parallel**, give **one prompt to one chat** — and open a
**separate chat (or terminal) for each task**, all started at the same time.

- **Right way — parallel (~2h total):** open 4 separate opencode sessions and give
  each session a single prompt with its own `__task<N>` paths. All 4 run at once.

  | Session | The one prompt it gets |
  |---|---|
  | Terminal 1 | `... .work/jennifer-tanaka__task1 ... Output/jennifer-tanaka_task1` |
  | Terminal 2 | `... .work/jennifer-tanaka__task2 ... Output/jennifer-tanaka_task2` |
  | Terminal 3 | `... .work/jennifer-tanaka__task3 ... Output/jennifer-tanaka_task3` |
  | Terminal 4 | `... .work/jennifer-tanaka__task4 ... Output/jennifer-tanaka_task4` |

- **Wrong way — sequential (~8h total):** pasting all 4 prompts into **one** chat.
  A single chat works through your messages one at a time, so it builds task1, then
  task2, then task3, then task4 — one after another, not in parallel.

To get separate sessions: open several terminals (or several `tmux` windows/panes),
run `opencode` in each, and paste that session's **single** prompt.

**How many at once:** memory is not the limit on a large box. The real cap is the
**Anthropic rate limit** (requests/tokens per minute), which is shared across every
job on **one login**. Start with a few jobs; if you see stalls or `429` errors,
run fewer at a time.

> **Note on subscriptions:** login is **per-machine, one account**. All jobs on one box
> share **one** subscription's rate limit — buying more seats does not automatically
> spread the load. To use more than one subscription, run on more than one machine
> (one login each), or contact whoever set this up to route jobs across logins.

---

## Step 5 — Monitor the batch

```bash
pgrep -fc skoll_bundle.py                      # how many jobs are running right now
```

Each opencode chat shows that job's stages live in its own session, so watch the
chats for progress and for any stage that reports a failure.

---

## Step 6 — Recover failures

Each job keeps its manifest in its own `.work/<persona>__task<N>` folder, so you can
re-run **only** a failed job and it will skip the stages that already finished by
adding `--resume`.

You can re-run a failed job from a fresh opencode chat with the same prompt (it picks
up the existing work dir), or run the CLI directly:

```bash
python3 .opencode/skills/skoll-bundle-builder/cli/skoll_bundle.py \
  --input Persona/mark-coleman \
  --work  .work/mark-coleman__task3 \
  --out   Output/mark-coleman_task3 \
  --meta  metas/mark-coleman__task3.yaml \
  --auto --resume
```

---
---

# Examples

## Example naming — 4 personas × 4 tasks = 16 jobs

Say you want to build 4 different tasks each for 4 personas. That is **16 separate
jobs**. You author one meta file per job (`metas/`), and every job then gets its own
matching work dir and output folder. The names all share the same `<persona>__task<N>`
stem so nothing collides:

```
metas/jennifer-tanaka__task1.yaml → .work/jennifer-tanaka__task1 → Output/jennifer-tanaka_task1
metas/jennifer-tanaka__task2.yaml → .work/jennifer-tanaka__task2 → Output/jennifer-tanaka_task2
metas/jennifer-tanaka__task3.yaml → .work/jennifer-tanaka__task3 → Output/jennifer-tanaka_task3
metas/jennifer-tanaka__task4.yaml → .work/jennifer-tanaka__task4 → Output/jennifer-tanaka_task4
metas/mark-coleman__task1.yaml    → .work/mark-coleman__task1    → Output/mark-coleman_task1
...
metas/mark-coleman__task4.yaml    → .work/mark-coleman__task4    → Output/mark-coleman_task4
```

**How to read a line:** each row is one job. The left name is the meta file **you write**;
the middle is the scratch/manifest folder the generator **creates as the job runs**; the
right is where the **finished bundle lands**. Read left to right, it is the life of a
single task. Notice the persona (`Persona/jennifer-tanaka`) is shared across `task1–4` —
that is fine, because inputs are read-only; only the `__task<N>` part changes so each
job keeps its own work dir and output.

## Example — the opencode chat prompt (one per job)

This is what you actually type to start **one** job. Open an opencode chat and paste the
prompt below, filling the three paths from the naming rule above. It names the persona to
build for, the unique work dir for this job, the meta that defines this task, and where to
save the finished bundle:

```
build perfect skoll bundle for Persona/jennifer-tanaka,
use work dir .work/jennifer-tanaka__task1,
meta metas/jennifer-tanaka__task1.yaml,
and save it in Output/jennifer-tanaka_task1
```

To start the **next** job in parallel, open a **separate** chat and change only the
`task1` parts to `task2`. Same persona, new task — new work dir, new output:

```
build perfect skoll bundle for Persona/jennifer-tanaka,
use work dir .work/jennifer-tanaka__task2,
meta metas/jennifer-tanaka__task2.yaml,
and save it in Output/jennifer-tanaka_task2
```

Repeat for `task3` and `task4`, each in its own chat, and all four build at the same time.

## Example — re-running one failed job

If a single job fails (say `mark-coleman` task 3), you don't restart the whole batch —
you re-run just that one. Because its progress is saved in its own `.work` folder, adding
`--resume` skips every stage that already finished and continues from where it broke.
This runs that one job directly from the terminal:

```bash
python3 .opencode/skills/skoll-bundle-builder/cli/skoll_bundle.py \
  --input Persona/mark-coleman \
  --work  .work/mark-coleman__task3 \
  --out   Output/mark-coleman_task3 \
  --meta  metas/mark-coleman__task3.yaml \
  --auto --resume
```

Every flag maps to the naming rule: `--input` is the persona, `--work` is that job's
unique scratch folder (where the saved progress lives), `--out` is its bundle, `--meta`
is its task definition. `--auto` runs it unattended; `--resume` is what makes it continue
instead of starting over.

---

## Quick reference

| Item | Value |
|---|---|
| CLI | `.opencode/skills/skoll-bundle-builder/cli/skoll_bundle.py` |
| Persona input | `Persona/<persona>/` (7 md + `home/` + `task/` + `mock_data/`) |
| Meta per job | `metas/<persona>__task<N>.yaml` |
| Work dir per job | `.work/<persona>__task<N>` (must be unique per job) |
| Output per job | `Output/<persona>_task<N>` |
| Harness (default) | `SKOLL_GK/Environment_SN_Harness` |
| Resume a failed job | `--resume` |

**The one rule to never break:** every job gets its **own unique `--work` dir**.
