# Mock data QC gate: persona alignment, enrichment, and consistency

You are reviewing whether the persona **mock data** is aligned with the prompt and
the persona for one generated Skoll task. The selection gate already checked which
services are in scope. This gate checks that the data those services carry is real,
rich enough for the job, consistent with the persona, and internally coherent. When
it is not, you may fix it in place under strict values-only rules.

## What to read

- `PROMPT.md` and `prompt_design_notes.md` in the work directory for what the task
  actually asks the agent to do and over what population.
- `api_selection.json` in the work directory for the required vs distractor split.
- The seven persona MD files at the input root (USER, IDENTITY, SOUL, MEMORY,
  HEARTBEAT, TOOLS, AGENTS) for who the persona is and the real names, companies,
  and numbers their world contains.
- The `mock_data/<service>-api/` files for every **required** service.

## What counts as a violation

Judge only the **required** services (distractor data is noise and may be sparse).

- A required service the prompt leans on holds placeholder or stub values where the
  persona clearly implies real ones (for example `TBD`, `example@example.com`,
  `Lorem ipsum`, `Test User`, empty strings in load-bearing fields, or obviously
  templated filler).
- The population a workstream runs over is too thin to support the job the prompt
  describes (for example the prompt asks to reconcile a large ledger but the file
  holds a handful of rows). Scale is the main difficulty lever, so a required
  reconciliation that fits in ten records is a violation.
- The data contradicts the persona (wrong principal, wrong company, a currency or
  locale the persona would not use, records for someone who is not this persona).
- Cross-file references do not line up: an id or key used in one required file has
  no matching record in the file it points at (an invoice for a customer id that is
  not in `customers`, a payment against an account that does not exist). This is a
  referential-integrity check on ids and keys only. Two records holding different
  business *values* for the same quantity is not a broken reference and is covered
  by the rule below.
- A load-bearing value contradicts the persona itself (wrong principal, wrong
  company, a currency or locale the persona would not use) or contradicts a concrete
  number, name, or date stated in `PROMPT.md`.

## What is fine (do not flag)

- **Intended cross-source conflicts.** Two independent sources reporting different
  values for the same real-world quantity (a tracker figure that disagrees with an
  analysis output, a stale total beside a fresh recompute) is a designed feature of
  the task, not a defect. Discovering which source wins is the test. Do **not** flag
  a value merely because it differs from another file, and do **not** flag it because
  it differs from the authoritative value recorded in the design notes conflicts
  table (section 5). The design notes record both the winning and the losing value on
  purpose; the losing value is supposed to live in the mock data. Only flag such a
  value if it independently contradicts the persona, contradicts a number stated in
  `PROMPT.md`, or breaks id/key referential integrity. Never "reconcile", collapse,
  or align two differing business values to each other.
- Valid placeholders that are correct on purpose: an aggregate or summary row such
  as `Multiple - See Batch Detail`, a null field a service genuinely leaves blank,
  a totals row. Only flag a blank when the persona makes clear it should be filled.
- Sparse distractor data. Distractors exist to be ignored.
- JSON-only mock data (the harness accepts JSON).

## How to fix (values only)

If you find violations, revise the mock data in place, then re-emit each changed
file wrapped in its markers, named by its path relative to the persona folder, for
example `mock_data/quickbooks-api/customers.json`. Obey every rule below.

- Change **values** and **add records** only. Replace placeholder or contradictory
  values with real persona-consistent ones; append rows to enrich a thin population.
- **Never change the schema.** Do not rename, add, or drop a field, and do not alter
  the container shape (keep any `{"QueryResponse": {"<Entity>": [...]}}` envelope
  exactly). Match the field set of the records already in the file.
- **Never touch a banned service** (`google-drive-api`, `google-contacts-api`,
  `box-api`, `dropbox-api`).
- **Keep everything consistent.** Every id, name, or key you write or add must line
  up across the files that reference it, and must match the numbers, names, and
  dates in `PROMPT.md`.
- **Never collapse an intended conflict.** Do not resolve, align, or reconcile two
  differing business values that represent the same quantity across files. Those
  disagreements are the trap and must survive. You may only fix stubs, thin
  population, values that contradict the persona, values that contradict `PROMPT.md`,
  and broken id/key references.

Do not fabricate data the prompt never touches, and do not enrich distractors.
