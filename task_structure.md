# Task.yaml Structure

This document describes the structure of `task.yaml`.

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `task_type` | String | The category/type of the task (e.g., `Productivity Flow`). |
| `task_description` | Multi-line String (block scalar `\|`) | The full narrative describing the scenario, context, and interlocking asks the assistant must handle. |
| `system_prompt` | String | System-level prompt for the assistant (empty in this file). |
| `platform` | String | The platform the task runs on (e.g., `MacOs`). |
| `required_apis` | List | APIs that must be connected and used for the task. |
| `distractor_apis` | List | APIs present as distractors that should not be used for core tasks. |

## Detailed Structure

### `task_type`
```yaml
task_type: Productivity Flow
```
A single string value identifying the classification of the task.

### `task_description`
```yaml
task_description: |
  <multi-line narrative text>
```
Uses YAML literal block scalar (`|`) to preserve line breaks. Contains the complete story, constraints, and the enumerated (but woven-in) asks.

### `system_prompt`
```yaml
system_prompt: ""
```
A string field for a custom system prompt. Empty in this task.

### `platform`
```yaml
platform: MacOs
```
Specifies the operating system/platform.

### `required_apis`
```yaml
required_apis:
  [gmail, google-calendar, outlook, slack, whatsapp, twilio, quickbooks, xero,
   salesforce, docusign, notion, airtable, openweather, square, plaid, dropbox, intercom]
```
An inline YAML list of API identifiers required to complete the task.

### `distractor_apis`
```yaml
distractor_apis:
  [sendgrid, mailgun, linear, asana, trello, monday, hubspot, stripe, paypal,
   zendesk, mailchimp, klaviyo]
```
An inline YAML list of API identifiers included as distractors.

## Field Order Summary

1. `task_type`
2. `task_description`
3. `system_prompt`
4. `platform`
5. `required_apis`
6. `distractor_apis`
