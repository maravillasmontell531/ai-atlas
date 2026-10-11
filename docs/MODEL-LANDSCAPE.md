# Model Landscape: Families, Checkpoints, APIs and Registries

A family name, checkpoint, hosted alias, API provider, benchmark and product UI are different objects. Record the exact object so comparisons remain meaningful.

| Object | Meaning | Record |
|---|---|---|
| Model family | Related releases | official family page, tasks, owner |
| Checkpoint | Exact weights/revision | repository, immutable revision, hashes |
| Fine-tune/adapter | Adaptation of a base | base model, method, license |
| Quantized artifact | Lower precision weights | format, precision, runtime trade-offs |
| Embedding model | Produces vectors | dimensions, language and retrieval tests |
| Reranker | Scores candidate relevance | input limits, latency, evaluation |
| Hosted alias | Provider-managed ID | alias, provider version policy, date |
| Benchmark | Evaluation under protocol | dataset split, metric, prompt, scorer, date |

## Family discovery map

OpenAI GPT/model APIs ([docs](https://platform.openai.com/docs/models)); Anthropic Claude ([docs](https://docs.anthropic.com/en/docs/about-claude/models/overview)); Google Gemini and Gemma ([Gemini API](https://ai.google.dev/gemini-api/docs), [Gemma](https://ai.google.dev/gemma)); Meta Llama ([site](https://www.llama.com/)); Microsoft Phi/Azure ([Foundry](https://ai.azure.com/)); Mistral/Ministral ([models](https://docs.mistral.ai/getting-started/models/)); DeepSeek ([API](https://api-docs.deepseek.com/)); Qwen ([site](https://qwenlm.github.io/)); GLM ([Z.ai](https://z.ai/)); Grok ([xAI docs](https://docs.x.ai/)); Cohere Command/embed/rerank ([models](https://docs.cohere.com/docs/models)); NVIDIA Nemotron/NeMo/NIM ([NIM](https://developer.nvidia.com/nim)); IBM Granite ([site](https://www.ibm.com/granite)); Amazon Nova/Bedrock ([Bedrock](https://aws.amazon.com/bedrock/)); OLMo ([Ai2](https://allenai.org/)); Falcon ([TII](https://www.tii.ae/)); BGE ([hub](https://huggingface.co/BAAI)); Jina ([site](https://jina.ai/)); Nomic ([site](https://www.nomic.ai/)); Stable Diffusion ([Stability](https://stability.ai/)); FLUX ([Black Forest Labs](https://blackforestlabs.ai/)); Runway ([site](https://runwayml.com/)).

## Open-source is not open weights

Open-source software means source code under a license. Open weights means parameters are accessible; training data/code may not be. Open data is a separate category. Public weights may still have restrictions. Local execution does not prove privacy or commercial rights. Inspect exact license and base-model terms.

## Dynamic registries

[Hugging Face Models](https://huggingface.co/models), [Datasets](https://huggingface.co/datasets), [Spaces](https://huggingface.co/spaces), [ModelScope](https://modelscope.cn/), [Kaggle Models](https://www.kaggle.com/models), [NGC](https://catalog.ngc.nvidia.com/), [Ollama Library](https://ollama.com/library), [OpenRouter](https://openrouter.ai/models), [Replicate](https://replicate.com/explore), [Together AI](https://www.together.ai/), [Fireworks](https://fireworks.ai/), [GroqCloud](https://console.groq.com/docs), [arXiv](https://arxiv.org/), [OpenReview](https://openreview.net/), [Papers with Code](https://paperswithcode.com/), [HELM](https://crfm.stanford.edu/helm/).

## Evaluation discipline

Compare representative tasks and failure modes, exact versions, model settings, allowed tools, graders, sample sizes, quality, latency and cost. Before upgrades, record provider/model IDs, revisions, tokenizer, license, quantization, runtime and hardware. Run the same regression suite across versions. Benchmark rankings are not universal measures of usefulness.
