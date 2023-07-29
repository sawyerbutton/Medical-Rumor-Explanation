# Medical Rumor Detection Pipeline

## Background

1. The analyzed Rumor file contains 125 valuable data entries.
2. Each data entry spans 5 dimensions: Time, Rumor Nature, Rumor Content Tag, Counter-rumor Explanation, Rumor Summary, and Original Rumor Text.
3. The Huatuo model, fine-tuned for this task, is a model adjusted from the LLaMA model enriched with Chinese medical knowledge. This was accomplished by building a Chinese medical command dataset using a medical knowledge graph and the GPT-3.5 API. The LLaMA was then fine-tuned on these commands, enhancing its performance in medical Q&A scenarios.

### Data analysis

1. Rumor Nature and Rumor Content Tag might be largely irrelevant.
2. Time could be used for logical validation.
3. In most cases, the Rumor Summary is a correct abstraction of the Original Rumor Text. To save on tokenization, the Rumor Summary can be used as the context for subsequent fine-tuning steps.

## Purpose

1. The goal is to train a model suitable for analyzing medical rumors. It should not only categorize the rumors but also provide a level of confidence in its judgment (based on a certain threshold).

## Procedure

1. Construct a fine-tuning dataset that meets the requirements of the Huatuo model from the existing data. The current dataset is limited; additional data scraping/creation is required.
2. Fine-tune the Huatuo model using Lora.
3. Validate the capabilities of the fine-tuned Huatuo model (accuracy across two dimensions: Counter-rumor Explanation and Rumor Judgment Confidence).

## Todos

- [ ] Scrape medical rumors.
- [ ] Build a dataset for fine-tuning the Huatuo model.
- [ ] Set up the base Huatuo model.
- [ ] Verify the rumor analysis capabilities and accuracy of the Huatuo model.
- [ ] Fine-tune the Huatuo model using the dataset.
- [ ] Validate the capabilities of the fine-tuned Huatuo model.

