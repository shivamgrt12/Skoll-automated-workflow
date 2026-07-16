# data/

This bundle ships no input-modality artifacts (no PDFs, images, spreadsheets, audio, or scans). All load-bearing inputs live under `mock_data/<api>-api/*.json`. This folder is retained empty to match the STRUCTURE.md layout.

Why `data/` is empty (qc_guide A10): no prompt, rubric criterion, or pytest probe in this bundle consumes a `home/` artifact or any staged input file. The persona `home/` tree is intentional noise and is not part of the task bundle. No `~$` temp files or generator-guide READMEs leaked in. The task is read-and-draft over the mock APIs, and the only agent write-back is Notion page-creation under the hub, so there is no input artifact to stage here.
