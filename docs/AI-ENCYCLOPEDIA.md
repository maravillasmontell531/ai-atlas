# AI Encyclopedia: Foundations to Systems

## 1. AI, machine learning and generative systems

Artificial intelligence is the umbrella field for systems that perform perception, prediction, language, planning, generation or action selection. Machine learning fits patterns or policies from data; deep learning uses multi-layer neural networks; generative AI synthesizes content. They overlap. Rule-based software follows explicit logic; predictive models estimate labels/values; hybrid systems combine models with code, search, databases and human review.

## 2. Task families

| Family | Common tasks | Risk/evaluation focus |
|---|---|---|
| Classification | routing, labels, moderation | imbalance, calibration, false positives |
| Forecasting/regression | numeric estimates, time series | leakage, distribution shift, uncertainty |
| Ranking/recommendation | search, feeds, products | relevance and feedback loops |
| NLP | extraction, translation, summarization | language coverage and privacy |
| Vision | detection, segmentation, OCR | resolution, lighting and domain shift |
| Speech/audio | recognition, synthesis, tagging | noise, accents, consent and diarization |
| Generation | text, code, images, audio, video | hallucinations, control and provenance |
| Reinforcement learning | sequential control | reward hacking and unsafe exploration |
| Graph ML | linked entities | missing or biased relationships |
| Scientific ML | biology, materials and weather | experimental validation |
| Multimodal AI | joint image/text/audio/video tasks | grounding and actual modality support |
| Agentic systems | tools and multi-step tasks | permissions, stop rules and recovery |

## 3. How models learn

A model is a parameterized function. Training adjusts weights against a loss objective using examples; inference runs trained parameters. Generalization describes transfer to unseen examples; overfitting is poor transfer; distribution shift is a mismatch between development and deployment. Calibration compares stated confidence with observed outcomes. Dataset curation, architecture, objectives, optimization and post-training jointly shape behavior. A single leaderboard cannot summarize quality, language support, latency, cost and safety.

## 4. Transformers, tokens, context and embeddings

Transformers use attention and feed-forward layers. A token is a model-specific piece, not necessarily a word; tokenizers differ across models. A context window caps tokenized information in a given invocation but does not guarantee perfect use of all details. Attention computes relationships among representations, not persistent memory or factual verification. Embeddings map inputs to vectors for useful retrieval relationships; similarity is not proof of truth. Changing embedding models usually requires re-indexing and retrieval tests.

## 5. Language and generative models

Many language models learn to predict the next token. Fluent output is not a truth guarantee. A common but non-universal pipeline includes pretraining, supervised fine-tuning, preference optimization, tool/format training, evaluation and deployment optimization. Reasoning labels do not promise correctness. Dense networks commonly activate most parameters; mixture-of-experts networks route input to selected subnetworks, so total and active parameter counts differ. Autoregressive generation produces sequences incrementally; diffusion/flow systems iteratively transform noise or a state; GANs use generator/discriminator objectives; VAEs learn probabilistic latent spaces. Quantization reduces numerical precision; distillation transfers selected behavior. Both involve trade-offs.

## 6. Modalities and system types

AI modalities include text, code, image, audio, speech, video, 3D, spatial, tabular and graph data. Vision-language models combine visual input with language. ASR converts speech to text; TTS generates speech from text. Image editing conditions on source images; video systems generate sequences. A file upload widget does not prove native support for every format. Keep products separate from model families, exact checkpoints, API providers, frameworks, datasets and benchmarks.

## 7. Retrieval-augmented generation

A RAG system ingests permitted sources, parses files, preserves metadata/permissions, chunks content, embeds and indexes, retrieves lexical/dense/hybrid candidates, optionally reranks, assembles context, generates, checks citations and refreshes stale data. Errors can originate in parsing, chunking, stale indexes, retrieval misses, access-control mistakes or unsupported synthesis. RAG supplies evidence; it does not guarantee truth. SQL/deterministic code is often better for exact structured data. Measure retrieval recall separately from answer quality, citations, abstention, permission isolation and latency. Test unanswerable, conflicting, stale and restricted-source cases.

## 8. Tools and agents

A tool call is a structured proposal to run a host-provided function. The application validates arguments, enforces authorization, executes and returns results. Models do not inherently possess web, terminal or account access. Agent loops observe state, choose actions, invoke tools and continue until a stop rule. Use narrow tools, strict schemas, least privilege, external authorization, explicit approval for consequential actions, bounded time/steps/spend, idempotency, tracing, prompt-injection defenses and recovery. More agents add coordination overhead; use them when measured benefit justifies complexity.

## 9. Search, evaluation and deployment

Lexical search is strong for exact terms; dense search handles semantic matches; hybrid combines both. Rerankers cannot recover sources never retrieved. Knowledge graphs represent typed relations; SQL is often better for exact values and aggregates. Evaluate task success, precision/recall, citations, schema validity, agent completion, policy violations, human intervention, latency percentiles and cost per successful task. LLM-as-judge may be biased and should be calibrated against people. Deployment can be hosted, API, dedicated endpoint, self-hosted, local, on-device, edge or hybrid. Batching, caching, KV cache, speculative decoding, quantization and distillation affect cost/latency with trade-offs.

## 10. Security and privacy

Assess data transmission/retention, provider access, prompt injection, cross-tenant retrieval, connector permissions, model supply-chain and generated code. Use data minimization, scoped credentials, secret storage, server-side authorization, strict schemas, ACL-preserving retrieval, redacted logs, deletion policies and human review proportional to consequences. Model instructions are not an access-control boundary.

References: [Hugging Face Models](https://huggingface.co/models), [OpenAI docs](https://platform.openai.com/docs), [Stanford HELM](https://crfm.stanford.edu/helm/), [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework), [OWASP GenAI](https://genai.owasp.org/).
