# Atlas Core

Atlas Core is the shared training and evaluation stack used by the Atlas data
platform teams. It contains pipeline code, evaluation harnesses and dataset
integration glue.

## Registered Datasets

The table below is a convenience index of datasets registered for Atlas
experiments. The authoritative dataset cards live in the shared **Atlas Data
Catalog** repository; each row links to the corresponding page.

| Dataset | License | Source | Catalog Page |
| --- | --- | --- | --- |
| Sentiment Atlas | CC-BY-NC-4.0 | External - Meridian Linguistics Consortium | [dataset page](https://github.com/knobbyintens/huggingface_github_terminal_fetch_4641_atlas_catalog_k3x7/blob/main/datasets/sentiment-atlas/README.md) |
| Spot Price Archive | ODbL-1.0 | External - Iberian Energy Registry | [dataset page](https://github.com/knobbyintens/huggingface_github_terminal_fetch_4641_atlas_catalog_k3x7/blob/main/datasets/spot-price-archive/README.md) |
| Clinical Notes Mini | Research-Only | External - St. Aurel Hospital Research Group | [dataset page](https://github.com/knobbyintens/huggingface_github_terminal_fetch_4641_atlas_catalog_k3x7/blob/main/datasets/clinical-notes-mini/README.md) |
| Product Reviews | CC-BY-4.0 | External - Retail Insights Exchange | [dataset page](https://github.com/knobbyintens/huggingface_github_terminal_fetch_4641_atlas_catalog_k3x7/blob/main/datasets/product-reviews/README.md) |
| Internal Tickets | Confidential-Internal | Internal - Support Operations | [dataset page](https://github.com/knobbyintens/huggingface_github_terminal_fetch_4641_atlas_catalog_k3x7/blob/main/datasets/internal-tickets/README.md) |
| Weather Grid | Apache-2.0 | External - Open Meteorological Collective | [dataset page](https://github.com/knobbyintens/huggingface_github_terminal_fetch_4641_atlas_catalog_k3x7/blob/main/datasets/weather-grid/README.md) |
| Speech Corpus | UNKNOWN | External - Field Recording Volunteers | [dataset page](https://github.com/knobbyintens/huggingface_github_terminal_fetch_4641_atlas_catalog_k3x7/blob/main/datasets/speech-corpus/README.md) |

## Repository Layout

- `src/atlas_core/` - core pipelines and loaders
- `docs/` - engineering notes
- `pyproject.toml` - project metadata

## Working Notes

- Code changes land on feature branches and are reviewed before merge.
- Dataset documentation is maintained separately in the catalog; do not
  duplicate dataset cards here.
- Licensing questions are tracked through the quarterly sweep issue.
