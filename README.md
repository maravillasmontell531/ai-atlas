<!--
AI Atlas — a community-maintained map of the artificial intelligence ecosystem.
Keep this README focused on AI as a field and ecosystem, not only on APIs.
-->

<div align="center">

<img src="assets/ai-atlas-mark.svg" alt="AI Atlas logo" width="112" />

# AI Atlas

### A map of the artificial intelligence ecosystem.

**Understand the field. Discover the tools. Explore the models. Learn how it all fits together.**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub stars](https://img.shields.io/github/stars/msxfury/ai-atlas?style=flat)](https://github.com/msxfury/ai-atlas/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/msxfury/ai-atlas?style=flat)](https://github.com/msxfury/ai-atlas/commits/main)
[![License](https://img.shields.io/github/license/msxfury/ai-atlas?style=flat)](LICENSE)

*A structured, practical guide to AI research, models, products, engineering, learning, evaluation, and responsible use.*

</div>

---

## What is AI Atlas?

AI Atlas is a curated map of the **artificial intelligence ecosystem**: the ideas behind AI, the methods used to build it, the models that power it, the products people use, the infrastructure that runs it, and the communities advancing it.

AI is much bigger than chatbots or API providers. It includes machine learning, language and vision models, image and video generation, speech, robotics, scientific discovery, data engineering, evaluation, security, governance, and much more. AI Atlas brings these connected areas into one navigable starting point.

This repository is intended for learners, developers, researchers, designers, founders, educators, and curious people who want to understand what exists and where to go next.

> **Scope note:** the AI ecosystem changes continuously. This is a curated guide, not a claim to list every model, company, product, paper, or project in existence. Links, capabilities, availability, and licensing can change; verify important details at the original source.

## Start here

| If you want to… | Start with… |
|---|---|
| Understand AI from the ground up | [AI fundamentals](#1-ai-fundamentals) |
| Learn machine learning and deep learning | [Learning roadmap](#14-learning-roadmaps) |
| Compare AI assistants | [General-purpose assistants](#7-general-purpose-ai-assistants) |
| Build with or run models | [Models and model hubs](#6-models-model-hubs-and-local-ai) |
| Create images, audio, or video | [Generative media](#9-generative-media) |
| Build an AI feature or application | [AI engineering](#11-ai-engineering-and-application-patterns) |
| Build coding agents and workflows | [Coding and developer tools](#8-coding-and-developer-tools) |
| Measure quality instead of trusting hype | [Evaluation and benchmarks](#12-evaluation-benchmarks-and-reliability) |
| Explore research and datasets | [Research and data](#10-research-datasets-and-scientific-ai) |
| Learn about risks and responsible deployment | [Safety, security, and governance](#13-safety-security-privacy-and-governance) |
| Contribute a resource | [Contributing](#16-contributing) |

## Contents

- [What is AI Atlas?](#what-is-ai-atlas)
- [AI at a glance](#ai-at-a-glance)
- [1. AI fundamentals](#1-ai-fundamentals)
- [2. Machine learning approaches](#2-machine-learning-approaches)
- [3. Model architectures and families](#3-model-architectures-and-families)
- [4. AI modalities and capabilities](#4-ai-modalities-and-capabilities)
- [5. The AI development lifecycle](#5-the-ai-development-lifecycle)
- [6. Models, model hubs, and local AI](#6-models-model-hubs-and-local-ai)
- [7. General-purpose AI assistants](#7-general-purpose-ai-assistants)
- [8. Coding and developer tools](#8-coding-and-developer-tools)
- [9. Generative media](#9-generative-media)
- [10. Research, datasets, and scientific AI](#10-research-datasets-and-scientific-ai)
- [11. AI engineering and application patterns](#11-ai-engineering-and-application-patterns)
- [12. Evaluation, benchmarks, and reliability](#12-evaluation-benchmarks-and-reliability)
- [13. Safety, security, privacy, and governance](#13-safety-security-privacy-and-governance)
- [14. Learning roadmaps](#14-learning-roadmaps)
- [15. Choosing the right AI approach](#15-choosing-the-right-ai-approach)
- [16. Contributing](#16-contributing)
- [Repository guide](#repository-guide)
- [Principles](#principles)

## AI at a glance

AI is not one technology. It is a collection of fields, techniques, models, tools, and systems that overlap.

```text
ARTIFICIAL INTELLIGENCE
├── Classical AI
│   ├── Search, planning, logic, knowledge representation
│   └── Constraint solving, expert systems, symbolic reasoning
├── Machine Learning
│   ├── Supervised, unsupervised, self-supervised learning
│   ├── Reinforcement learning and online learning
│   └── Deep learning
│       ├── Language and code models
│       ├── Vision and multimodal models
│       ├── Generative models
│       └── Speech, audio, video and 3D models
├── Applied AI
│   ├── Assistants, search, coding and productivity
│   ├── Recommendation, forecasting and decision support
│   ├── Science, healthcare, education and industry
│   └── Robotics, autonomy and embodied systems
└── AI systems engineering
    ├── Data, training, fine-tuning and inference
    ├── Retrieval, tools, agents and orchestration
    ├── Evaluation, monitoring and observability
    └── Safety, security, privacy and governance
```

The branches are not mutually exclusive. A single product may combine a language model, image understanding, retrieval, external tools, conventional software, and a human approval step.

## 1. AI fundamentals

**Artificial intelligence (AI)** is the broad field of building systems that perform tasks associated with capabilities such as perception, language, prediction, planning, learning, and decision-making.

| Term | What it means | Example |
|---|---|---|
| Algorithm | A procedure for solving a problem | Search or sorting |
| Model | A learned or specified system that maps inputs to outputs | A classifier or language model |
| Training | Adjusting model parameters using data or feedback | Learning from examples |
| Inference | Using a trained model to produce an output | Asking a model a question |
| Dataset | A collection of examples used for training, validation, or testing | Labeled images |
| Parameter | A value learned by a model during training | A neural-network weight |
| Token | A unit used by many language models to represent text or other input | A word fragment |
| Context window | The amount of input a model can consider in one request | Conversation and attached text |
| Embedding | A numerical representation intended to capture useful relationships | Vectors for semantic search |
| Fine-tuning | Additional training to adapt a pretrained model | Adapting a model to a task |
| Evaluation | Measuring a system against defined tasks and criteria | Accuracy, latency, or task success |
| Agent | A system that uses a model to choose actions, often with tools and state | A coding agent editing a project |
| Multimodal | Working with more than one input or output modality | Text plus images or audio |
| Open weights | Model parameters made available to download under stated terms | A downloadable model checkpoint |
| Open source | A term with specific licensing and distribution implications; it is not synonymous with open weights | A project with source and qualifying license |

### Important distinctions

- **AI is not synonymous with generative AI.** Classification, ranking, anomaly detection, planning, and forecasting are also AI applications.
- **A model is not a product.** A product can combine one or more models with a user interface, tools, storage, safety systems, and proprietary services.
- **A benchmark score is not universal intelligence.** It measures performance on a particular test under particular conditions.
- **Fluent output is not proof of truth.** Systems can generate incorrect claims, invented citations, or plausible but invalid code.
- **Bigger is not always better.** Cost, latency, privacy, reliability, hardware, and task fit can matter more than model size.
- **An AI agent is not automatically autonomous or reliable.** Its permissions, available tools, memory, feedback loops, and stopping conditions determine what it can actually do.

## 2. Machine learning approaches

| Approach | Core idea | Common uses |
|---|---|---|
| Supervised learning | Learn from examples with target labels | Classification, regression, prediction |
| Unsupervised learning | Find structure without explicit target labels | Clustering, anomaly exploration |
| Self-supervised learning | Create training signals from the data itself | Pretraining language and vision models |
| Semi-supervised learning | Combine labeled and unlabeled examples | Tasks where labels are expensive |
| Reinforcement learning | Learn behavior from rewards or feedback | Control, planning, policy optimization |
| Transfer learning | Reuse knowledge learned on another task or dataset | Adapting pretrained models |
| Fine-tuning | Further train a model for a target behavior or domain | Instruction following, task adaptation |
| Distillation | Train a smaller model to reproduce useful behavior of a larger one | Efficient deployment |
| Federated learning | Train across distributed data while limiting central data collection | Some privacy-sensitive settings |
| Evolutionary / population methods | Search over candidate solutions using selection and variation | Optimization and research |

### Deep learning in brief

Deep learning uses multi-layer neural networks to learn representations from data. It powers many current language, image, audio, video, and multimodal systems. Neural architectures are chosen based on the structure of the problem; they are not interchangeable.

Common concepts include loss functions, gradient descent, backpropagation, regularization, generalization, overfitting, training/validation/test splits, optimization, and compute scaling.

## 3. Model architectures and families

| Family | What it is good at | Key caveats |
|---|---|---|
| Transformers | Sequence modeling, language, code, vision, and multimodal tasks | Compute and context costs; behavior depends on training and design |
| Large language models (LLMs) | Text generation, summarization, question answering, coding, tool selection | May hallucinate; output quality depends on task and context |
| Small language models (SLMs) | Lower-cost, lower-latency, local or specialized workloads | Capability depends on model and task; size alone is not a quality guarantee |
| Vision models | Image classification, detection, segmentation, visual understanding | Domain shift, image quality, and evaluation limitations |
| Vision-language models (VLMs) | Connect image/video inputs with language tasks | May miss small details, spatial relationships, or visual evidence |
| Diffusion models | Generate or transform images, audio, and other media | Prompt adherence, editing consistency, and compute vary |
| GANs | Generate samples through competing generator/discriminator networks | Training stability and mode coverage can be challenging |
| VAEs | Learn compressed probabilistic representations and generate samples | Reconstructions and sample quality depend on design |
| Speech models | Speech recognition, synthesis, translation, and audio understanding | Noise, accents, language coverage, consent, and latency matter |
| Recommendation and ranking models | Order items or predict relevance and preferences | Feedback loops, bias, and objective design matter |
| Graph neural networks | Learn from graph-structured relationships | Graph quality and scaling can be limiting |
| Reinforcement-learning policies | Choose actions based on observations and rewards | Reward misspecification and unsafe exploration are serious risks |
| World models and robotics policies | Model environments or map observations to actions | Real-world robustness and safety require extensive testing |

### Model names, releases, and licenses

A model family may have multiple sizes, checkpoints, quantizations, modalities, and license terms. Always check the **specific release** rather than assuming that all versions share the same capabilities or permissions. A model being downloadable does not automatically mean its training data, source code, or commercial-use rights are unrestricted.

## 4. AI modalities and capabilities

| Area | Typical tasks | What to inspect |
|---|---|---|
| Text and language | Summarization, translation, extraction, question answering | Factuality, language support, context handling |
| Code | Completion, debugging, refactoring, test generation | Correctness, security, repository context |
| Image understanding | Captioning, OCR, visual question answering | Small text, diagrams, spatial reasoning |
| Image generation | Text-to-image, inpainting, style and composition control | Rights, consistency, prompt adherence |
| Audio understanding | Transcription, speaker and sound analysis | Noise robustness, consent, language support |
| Speech generation | Text-to-speech, voice conversion, dubbing | Voice consent, disclosure, identity misuse |
| Music and sound | Music generation, sound effects, audio editing | Licensing, provenance, similarity concerns |
| Video | Generation, summarization, editing, tracking | Temporal consistency, realism, provenance |
| 3D and spatial AI | Asset generation, reconstruction, scene understanding | Geometry, topology, rigging, export quality |
| Retrieval and search | Semantic search, ranking, question answering over sources | Source quality, freshness, attribution |
| Forecasting and decision support | Demand, time series, risk estimation | Calibration, drift, uncertainty |
| Robotics and embodied AI | Perception, navigation, manipulation | Physical safety, environment shift, fail-safes |
| Scientific AI | Molecular modeling, materials, simulation, research support | Experimental validation and domain expertise |

A system can support several modalities, but **multimodal support is not the same as equal capability across all modalities**. Check what inputs and outputs are actually supported by the specific model and product.

## 5. The AI development lifecycle

A reliable AI system is more than a model call. A typical lifecycle looks like this:

1. **Define the task.** Describe the user problem, success criteria, failure costs, and what should happen when the system is uncertain.
2. **Establish a baseline.** Determine whether ordinary software, search, rules, or a smaller model can solve the problem.
3. **Choose or collect data.** Check provenance, quality, representativeness, consent, privacy, and usage rights.
4. **Select an approach.** Decide whether to use a hosted model, open-weight model, fine-tuning, retrieval, conventional ML, or a hybrid.
5. **Build a prototype.** Keep the first system small enough to understand and measure.
6. **Evaluate offline.** Test representative examples, edge cases, adversarial inputs, and failure modes.
7. **Integrate safely.** Limit tool permissions, validate inputs and outputs, protect secrets, and isolate untrusted content.
8. **Run a controlled release.** Use staged rollout, human review where needed, and rollback procedures.
9. **Monitor in production.** Track quality, latency, cost, errors, user feedback, and distribution changes.
10. **Improve deliberately.** Use documented evaluations to guide prompt, retrieval, model, or workflow changes.

### Training and inference are different

- **Pretraining** learns broad patterns from large datasets.
- **Post-training** can improve instruction following, preference alignment, tool use, or task behavior.
- **Fine-tuning** adapts a model using additional examples or objectives.
- **Inference** runs the model to produce an output.
- **Retrieval-augmented generation (RAG)** supplies relevant external information at inference time; it does not automatically update the model's parameters.
- **Evaluation** tests whether the resulting system performs acceptably for its intended use.

## 6. Models, model hubs, and local AI

These resources help people discover, inspect, download, serve, or run models. Review each model card and license before using a checkpoint.

| Resource | What it offers |
|---|---|
| [Hugging Face](https://huggingface.co/) | Model and dataset hub, documentation, demos, and community |
| [Hugging Face Models](https://huggingface.co/models) | Searchable model repository with cards, files, and metadata |
| [Hugging Face Datasets](https://huggingface.co/datasets) | Dataset discovery and dataset documentation |
| [Ollama](https://ollama.com/) | A convenient way to download and run supported models locally |
| [LM Studio](https://lmstudio.ai/) | Desktop workflow for discovering and running local language models |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Efficient local inference across supported hardware |
| [vLLM](https://github.com/vllm-project/vllm) | High-throughput serving for supported language models |
| [ModelScope](https://modelscope.cn/) | Model and dataset ecosystem |
| [Kaggle Models](https://www.kaggle.com/models) | Model discovery and notebook-oriented workflows |
| [ONNX](https://onnx.ai/) | Interoperable representation for supported machine-learning models |
| [PyTorch](https://pytorch.org/) | Framework for building and training machine-learning systems |
| [JAX](https://jax.readthedocs.io/) | Numerical computing and machine-learning research framework |

### Hosted models versus local models

| Consideration | Hosted service | Local / self-hosted |
|---|---|---|
| Setup | Usually quick to start | Hardware and runtime setup may be required |
| Infrastructure | Provider manages much of it | You manage deployment, updates, and reliability |
| Data handling | Depends on provider terms and configuration | Can provide more control, but only if configured correctly |
| Cost | Usage, subscription, or contract based | Hardware, electricity, maintenance, and engineering |
| Performance | Depends on service and network | Depends on hardware, quantization, model, and workload |
| Control | Limited by product and provider | More control over runtime and configuration |
| Best fit | Rapid development and managed scale | Offline use, customization, or specific control needs |

**Local does not automatically mean private or secure.** Logs, extensions, telemetry, network access, and shared devices still matter. Likewise, hosted services differ significantly in retention and training policies.

## 7. General-purpose AI assistants

The following are useful starting points for exploring different assistant experiences. Features, availability, and plan limits change; this is not a ranking.

| Product | Explore |
|---|---|
| ChatGPT | [chatgpt.com](https://chatgpt.com/) |
| Claude | [claude.ai](https://claude.ai/) |
| Google Gemini | [gemini.google.com](https://gemini.google.com/) |
| Microsoft Copilot | [copilot.microsoft.com](https://copilot.microsoft.com/) |
| Meta AI | [meta.ai](https://www.meta.ai/) |
| Perplexity | [perplexity.ai](https://www.perplexity.ai/) |
| Mistral Le Chat | [chat.mistral.ai](https://chat.mistral.ai/) |
| Grok | [grok.com](https://grok.com/) |
| DeepSeek | [chat.deepseek.com](https://chat.deepseek.com/) |
| Qwen Chat | [chat.qwen.ai](https://chat.qwen.ai/) |
| Poe | [poe.com](https://poe.com/) |
| HuggingChat | [huggingface.co/chat](https://huggingface.co/chat/) |

### How to compare assistants fairly

Use the same representative tasks and compare the result, not just the interface. Check source quality for research, correctness for coding, image understanding for visual tasks, context handling for long documents, and privacy terms for sensitive work. Record the product, model/version if exposed, date, prompt, output, and evaluation criteria so the comparison can be repeated.

## 8. Coding and developer tools

AI coding products differ in how much of the development workflow they can access. Some suggest snippets; others can inspect a repository, edit files, run tests, and use tools under configured permissions.

| Tool | Starting point |
|---|---|
| GitHub Copilot | [github.com/features/copilot](https://github.com/features/copilot) |
| Cursor | [cursor.com](https://cursor.com/) |
| Windsurf | [windsurf.com](https://windsurf.com/) |
| Claude Code | [docs.anthropic.com](https://docs.anthropic.com/) |
| Gemini CLI | [github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |
| Aider | [aider.chat](https://aider.chat/) |
| Continue | [continue.dev](https://www.continue.dev/) |
| Zed | [zed.dev](https://zed.dev/) |
| OpenAI Codex | [openai.com/codex](https://openai.com/codex/) |

### A responsible coding-agent workflow

1. Start from a clean branch or checkpoint.
2. State the goal, constraints, relevant files, and acceptance criteria.
3. Give the agent only the access it needs.
4. Ask it to inspect before editing and explain its plan.
5. Review the actual diff, not just the agent's summary.
6. Run tests, linters, type checks, and security checks independently.
7. Inspect dependencies, generated files, secrets, and configuration changes.
8. Verify the final behavior in the real environment.
9. Keep a rollback path and do not merge unreviewed high-impact changes.

Treat repository text, issues, webpages, logs, and generated code as potentially untrusted. Prompt injection can be embedded in content an agent reads. Never expose production credentials merely to make an agent more convenient.

## 9. Generative media

### Images and visual design

| Tool or ecosystem | Starting point |
|---|---|
| OpenAI image generation | [openai.com](https://openai.com/) |
| Adobe Firefly | [firefly.adobe.com](https://firefly.adobe.com/) |
| Midjourney | [midjourney.com](https://www.midjourney.com/) |
| Stability AI | [stability.ai](https://stability.ai/) |
| Black Forest Labs / FLUX | [blackforestlabs.ai](https://blackforestlabs.ai/) |
| Ideogram | [ideogram.ai](https://ideogram.ai/) |
| Leonardo AI | [leonardo.ai](https://leonardo.ai/) |
| ComfyUI | [github.com/comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI) |

### Video generation and editing

| Tool or ecosystem | Starting point |
|---|---|
| OpenAI Sora | [openai.com](https://openai.com/) |
| Runway | [runwayml.com](https://runwayml.com/) |
| Google Veo | [deepmind.google/technologies/veo](https://deepmind.google/technologies/veo/) |
| Kling AI | [klingai.com](https://klingai.com/) |
| Pika | [pika.art](https://pika.art/) |
| Luma AI | [lumalabs.ai](https://lumalabs.ai/) |

### Speech, audio, and music

| Tool or ecosystem | Starting point |
|---|---|
| Whisper speech recognition | [github.com/openai/whisper](https://github.com/openai/whisper) |
| ElevenLabs | [elevenlabs.io](https://elevenlabs.io/) |
| Suno | [suno.com](https://suno.com/) |
| Udio | [udio.com](https://udio.com/) |
| Stable Audio | [stability.ai](https://stability.ai/) |

### 3D and spatial content

| Tool or ecosystem | Starting point |
|---|---|
| Meshy | [meshy.ai](https://www.meshy.ai/) |
| Tripo | [tripo3d.ai](https://www.tripo3d.ai/) |
| Blender | [blender.org](https://www.blender.org/) |

**Before publishing generated media:** check commercial-use terms, source-material rights, voice and likeness consent, platform rules, and disclosure requirements. Generated assets may require manual cleanup and should not be presented as authentic evidence when they are synthetic.

## 10. Research, datasets, and scientific AI

### Papers, literature, and discovery

| Resource | Purpose |
|---|---|
| [arXiv](https://arxiv.org/) | Preprints across AI, computer science, mathematics, and related fields |
| [Semantic Scholar](https://www.semanticscholar.org/) | Scholarly literature discovery |
| [Papers with Code](https://paperswithcode.com/) | Research papers connected to tasks, benchmarks, and implementations |
| [Google Scholar](https://scholar.google.com/) | Scholarly search |
| [OpenReview](https://openreview.net/) | Research review and conference workflows |
| [Elicit](https://elicit.com/) | AI-assisted research and literature workflows |
| [Consensus](https://consensus.app/) | Search across scientific literature |
| [NotebookLM](https://notebooklm.google.com/) | Source-grounded work with supplied material |

A preprint is not necessarily peer-reviewed. For consequential claims, inspect the original paper, methods, limitations, date, and independent replication rather than relying on a summary alone.

### Datasets and data infrastructure

| Resource | Purpose |
|---|---|
| [Hugging Face Datasets](https://huggingface.co/datasets) | Dataset hosting and discovery |
| [Kaggle](https://www.kaggle.com/datasets) | Public datasets, competitions, and notebooks |
| [UCI Machine Learning Repository](https://archive.ics.uci.edu/) | Classic and contemporary ML datasets |
| [Google Dataset Search](https://datasetsearch.research.google.com/) | Dataset discovery across the web |
| [Common Crawl](https://commoncrawl.org/) | Large-scale web crawl data |
| [ImageNet](https://www.image-net.org/) | A major visual recognition research dataset |
| [LAION](https://laion.ai/) | Open research and dataset projects |

Before using a dataset, inspect its source, collection method, license, consent basis, personal information, known skews, documentation, and restrictions. Publicly accessible data is not automatically free of privacy, copyright, or contractual obligations.

### Research organizations and labs

| Organization | Starting point |
|---|---|
| OpenAI | [openai.com/research](https://openai.com/research/) |
| Anthropic | [anthropic.com/research](https://www.anthropic.com/research) |
| Google DeepMind | [deepmind.google](https://deepmind.google/) |
| Google Research | [research.google](https://research.google/) |
| Meta AI | [ai.meta.com](https://ai.meta.com/) |
| Microsoft Research | [microsoft.com/research](https://www.microsoft.com/en-us/research/) |
| NVIDIA Research | [research.nvidia.com](https://research.nvidia.com/) |
| Allen Institute for AI (AI2) | [allenai.org](https://allenai.org/) |
| Mistral AI | [mistral.ai](https://mistral.ai/) |
| Cohere | [cohere.com](https://cohere.com/) |
| DeepSeek | [deepseek.com](https://www.deepseek.com/) |
| Qwen | [qwen.ai](https://qwen.ai/) |
| EleutherAI | [eleuther.ai](https://www.eleuther.ai/) |

This list is illustrative rather than exhaustive. Research agendas, releases, and publication practices vary between organizations.

## 11. AI engineering and application patterns

Production AI usually requires conventional engineering around the model: input validation, retrieval, business logic, authorization, observability, and failure handling.

### Common patterns

| Pattern | How it works | Good fit |
|---|---|---|
| Direct inference | Send an input to a model and use its output | Simple, bounded transformations |
| Structured output | Constrain the response to a schema and validate it | Extraction, classification, data transformation |
| Retrieval-augmented generation (RAG) | Retrieve relevant documents and provide them as context | Private or frequently changing knowledge |
| Tool calling | Let a model request a predefined application function | Controlled access to search, calculations, or business actions |
| Workflow / orchestration | Run defined steps with explicit transitions and checks | Repeatable multi-step processes |
| Agent loop | Let a model choose actions iteratively within limits | Tasks needing flexible tool use and feedback |
| Fine-tuning | Adapt model behavior with additional training | Repeated patterns not adequately handled by prompting alone |
| Hybrid system | Combine rules, search, models, and human decisions | High-reliability or domain-specific tasks |

### RAG, fine-tuning, and prompting are not substitutes

- Use **prompting** to specify the task, constraints, format, and context.
- Use **RAG** when answers need to reference a changing or private knowledge base.
- Use **fine-tuning** when examples show a persistent behavior or format gap and you have suitable data and evaluation.
- Use **tools** when the system needs current information, calculations, or actions outside the model.
- Use **ordinary code and rules** for deterministic operations where they are simpler and more reliable.

These approaches can be combined. RAG does not guarantee correct answers, fine-tuning does not automatically add current knowledge, and a prompt cannot guarantee that a model will obey every instruction.

### Production checklist

- [ ] Define measurable success criteria and unacceptable failures.
- [ ] Validate inputs and outputs against explicit schemas.
- [ ] Treat retrieved content and tool results as untrusted data.
- [ ] Enforce authorization in application code, not only in model instructions.
- [ ] Keep credentials and sensitive configuration out of prompts and logs.
- [ ] Add timeouts, retry limits, rate limits, and cost controls.
- [ ] Handle refusals, malformed output, missing sources, and unavailable models.
- [ ] Log only what is necessary, with a documented retention policy.
- [ ] Evaluate on representative examples before and after changes.
- [ ] Provide human review or escalation for consequential decisions.
- [ ] Monitor latency, failure rate, drift, quality, and user feedback.
- [ ] Document model versions, prompts, data sources, and deployment changes.

## 12. Evaluation, benchmarks, and reliability

A demo shows what can happen. Evaluation estimates how often a system succeeds under defined conditions.

| Resource or benchmark | Focus |
|---|---|
| [Stanford HELM](https://crfm.stanford.edu/helm/) | Holistic language-model evaluation |
| [LMSYS Chatbot Arena](https://lmarena.ai/) | Human preference comparisons for supported model comparisons |
| [OpenCompass](https://opencompass.org.cn/) | Model evaluation framework and benchmarks |
| [SWE-bench](https://www.swebench.com/) | Software engineering tasks based on real GitHub issues |
| [MLCommons / MLPerf](https://mlcommons.org/) | Standardized ML performance benchmarking |
| [Hugging Face Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) | Community evaluation for supported open models |
| [BIG-bench](https://github.com/google/BIG-bench) | Broad language-model task collection |

Benchmarks can become saturated, be contaminated by training data, or fail to represent real usage. Results may differ with prompting, sampling settings, tool access, model version, and scoring method. Use several complementary tests and your own task-specific evaluation.

### A practical evaluation plan

1. Create a representative test set from real requirements, not only easy examples.
2. Include difficult, ambiguous, multilingual, and adversarial cases where relevant.
3. Define expected behavior and scoring before comparing systems.
4. Measure task success, factuality, completeness, latency, cost, and refusal quality.
5. Check sources and citations manually for research tasks.
6. Test security boundaries, prompt injection, and permission enforcement.
7. Compare against a non-AI baseline.
8. Repeat after changing the model, prompt, retrieval index, or tool set.
9. Record the date and exact configuration so results are reproducible.

## 13. Safety, security, privacy, and governance

AI systems can fail through inaccurate outputs, data leakage, bias, overreliance, unsafe actions, or misuse. Risk depends on the application and its context, not merely on the model's label.

### Risk areas to understand

- **Hallucination and factual errors:** outputs can be confident but incorrect.
- **Prompt injection:** malicious instructions can appear in user input or external content.
- **Privacy and data leakage:** sensitive information may be exposed through prompts, logs, retrieval, or integrations.
- **Insecure tool use:** excessive permissions can turn a model error into a real-world action.
- **Bias and uneven performance:** aggregate scores can hide failures for specific groups, dialects, or contexts.
- **Copyright and provenance:** training data and generated outputs can raise legal and attribution questions.
- **Deepfakes and impersonation:** synthetic media can mislead people or misuse someone's identity.
- **Automation bias:** people may trust a fluent system more than the evidence warrants.
- **Model and data drift:** performance may change as inputs, environments, or dependencies change.
- **Supply-chain risk:** untrusted models, packages, datasets, and extensions can introduce vulnerabilities.

### Security practices

- Give agents the least privilege necessary; isolate risky execution environments.
- Keep secrets in a secret manager or protected environment, never in public repositories or prompts.
- Validate and authorize every action server-side.
- Separate trusted instructions from untrusted documents and retrieved content.
- Require confirmation for destructive, external, financial, or irreversible actions.
- Apply ordinary application security practices: authentication, authorization, dependency review, input validation, and audit trails.
- Test prompt injection and data-exfiltration paths as part of system evaluation.
- Establish incident response and rollback procedures before production use.

### Governance and risk frameworks

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST Generative AI Profile](https://www.nist.gov/itl/ai-risk-management-framework)
- [OECD AI Principles](https://oecd.ai/en/ai-principles)
- [UNESCO Recommendation on the Ethics of Artificial Intelligence](https://www.unesco.org/en/artificial-intelligence/recommendation-ethics)
- [EU AI Act information](https://artificial-intelligence-act.europa.eu/)

These resources provide useful starting points, not legal advice. Applicable obligations depend on jurisdiction, sector, intended use, and the system's actual design.

## 14. Learning roadmaps

Choose a path that matches what you want to build. You do not need to master every subfield before starting a useful project.

### Path A — AI user and researcher

1. Learn the difference between a model, product, dataset, and benchmark.
2. Practice asking precise questions and supplying relevant context.
3. Verify factual claims against primary sources.
4. Learn how to compare answers with a consistent test set.
5. Understand privacy, attribution, and limitations before using outputs publicly.

### Path B — AI application developer

1. Learn Python or JavaScript, HTTP, JSON, Git, and basic testing.
2. Build a small application around one well-defined model task.
3. Add structured outputs, input validation, and error handling.
4. Learn embeddings, retrieval, and source-grounded generation.
5. Add tools only with server-side authorization and bounded permissions.
6. Create evaluations for quality, cost, latency, and security.
7. Deploy with monitoring, logging controls, and rollback.

### Path C — Machine-learning engineer

1. Learn Python, NumPy, data handling, probability, statistics, and linear algebra.
2. Study supervised learning, validation, generalization, and metrics.
3. Train baseline models using [scikit-learn](https://scikit-learn.org/).
4. Learn neural networks and a framework such as [PyTorch](https://pytorch.org/).
5. Study optimization, representation learning, transformers, and experiment tracking.
6. Learn deployment, inference optimization, data quality, and monitoring.
7. Reproduce a paper or benchmark and document limitations.

### Path D — AI researcher

1. Build a foundation in mathematics, algorithms, statistics, and experimental design.
2. Read papers with attention to methods, baselines, ablations, and limitations.
3. Reproduce an established result before making a new claim.
4. Learn dataset construction, evaluation design, and statistical uncertainty.
5. Study the relevant specialty deeply rather than chasing every new release.
6. Publish reproducible code, careful documentation, and honest negative results where appropriate.

### Path E — Local and open-weight AI

1. Inspect model cards, supported tasks, hardware requirements, and license terms.
2. Run a small model locally using a supported runtime.
3. Compare quantization, memory use, latency, and output quality.
4. Test with representative prompts and local data.
5. Secure the runtime and verify whether any components transmit data externally.
6. Document the exact model revision and configuration.

### Free and accessible learning resources

| Resource | Best for |
|---|---|
| [Elements of AI](https://www.elementsofai.com/) | Accessible introduction to AI concepts |
| [fast.ai](https://www.fast.ai/) | Practical deep learning |
| [DeepLearning.AI](https://www.deeplearning.ai/) | Structured AI and ML courses |
| [Hugging Face Course](https://huggingface.co/learn) | Transformers, datasets, and model tooling |
| [Stanford CS229](https://cs229.stanford.edu/) | Machine-learning foundations |
| [Stanford CS231n](https://cs231n.stanford.edu/) | Computer vision and deep learning |
| [MIT OpenCourseWare](https://ocw.mit.edu/) | University-level courses across relevant subjects |
| [PyTorch Tutorials](https://pytorch.org/tutorials/) | Hands-on deep-learning workflows |
| [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html) | Classical ML and evaluation |

Course availability and prerequisites may change. Choose one learning resource and build small projects instead of collecting courses without applying what you learn.

## 15. Choosing the right AI approach

Before choosing a model or product, answer these questions:

1. **What is the task?** Describe the input, desired output, and acceptable error rate.
2. **Does it need generative AI?** A rules engine, database query, or conventional model may be simpler.
3. **Does it need current or private knowledge?** Consider retrieval and source citations.
4. **Does it need to take actions?** Prefer narrow tools, explicit permissions, and human confirmation for high-impact actions.
5. **What are the constraints?** Budget, latency, hardware, offline requirements, languages, context size, and accessibility.
6. **What data can be sent?** Check privacy terms and data-handling configuration.
7. **What does the license allow?** Check the exact model, dataset, and dependency terms.
8. **How will success be measured?** Design task-specific evaluations before committing to a system.

### Quick decision guide

| Need | First approach to consider |
|---|---|
| Deterministic calculations or rules | Ordinary code |
| Search over trusted documents | Search or RAG with source display |
| Repeated structured extraction | Schema-constrained model output plus validation |
| Classification with stable labels | Rules or a supervised model baseline |
| Creative drafting and brainstorming | Generative assistant with human review |
| Repository-level code changes | Coding agent in a controlled branch and environment |
| Offline or highly controlled deployment | Evaluate local/open-weight models and their licenses |
| High-stakes decisions | Domain-specific validation, oversight, and appropriate professional processes—not an unreviewed model alone |

## Repository guide

The README is the entry point; the repository's other files provide deeper catalog and reference material.

| Path | What it is for |
|---|---|
| [CATALOG.md](CATALOG.md) | Browse the project's structured catalog |
| [CATEGORIES.md](CATEGORIES.md) | Explore the category map |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Guidelines for proposing changes |
| [SOURCES.md](SOURCES.md) | Sources and reference guidance |
| [docs/AI-ENCYCLOPEDIA.md](docs/AI-ENCYCLOPEDIA.md) | Broader AI concepts and terminology |
| [docs/AI-ENGINEERING-STACK.md](docs/AI-ENGINEERING-STACK.md) | AI engineering and system components |
| [docs/MODEL-LANDSCAPE.md](docs/MODEL-LANDSCAPE.md) | Model landscape reference |
| [docs/GLOSSARY.md](docs/GLOSSARY.md) | Concise glossary |
| [data/ai-tools.csv](data/ai-tools.csv) | Structured resource data, where available |

If a linked path has moved, browse the [repository root](https://github.com/msxfury/ai-atlas) for the current layout.

## 16. Contributing

AI Atlas improves when resources are accurate, clearly described, and useful to someone other than the person who submitted them.

### Good contributions

- Add a relevant model, research paper, dataset, learning resource, tool, or organization.
- Prefer official documentation or a primary source for product and technical claims.
- Describe what a resource does, who it helps, and its important limitations.
- Distinguish research projects, open-weight models, open-source software, hosted products, and commercial services.
- Include license and access information only when it can be verified.
- Use neutral language; avoid unsupported superlatives, promotional copy, and unverified performance claims.
- Check for duplicates and broken links before submitting.
- State when a resource is experimental, archived, or no longer maintained.

### Suggested resource entry

When proposing a resource, provide as many of these fields as are relevant:

- **Name**
- **Official URL**
- **Category**
- **Resource type** — model, product, framework, dataset, paper, course, benchmark, or organization
- **Short description**
- **Access** — hosted, local, research-only, or other
- **License / terms** — link to the exact terms when available
- **Evidence** — official documentation, paper, repository, or model card
- **Last checked** — useful for fast-changing capabilities and availability

Avoid submitting private data, credentials, scraped personal information, or claims that cannot be traced to a credible source. See [CONTRIBUTING.md](CONTRIBUTING.md) for repository-specific instructions.

## Principles

1. **Accuracy over hype.** Explain what a resource does, not what marketing suggests it might do.
2. **Primary sources first.** Link official documentation, papers, model cards, and repositories whenever possible.
3. **Clear categories.** Do not confuse a model with the product built around it.
4. **Useful context.** A link without an explanation is rarely enough.
5. **Responsible use.** Privacy, security, licensing, evaluation, and human oversight are part of engineering—not afterthoughts.
6. **Respect change.** Models and product features evolve; recheck details that affect decisions.
7. **No false completeness.** The goal is a useful map of a large ecosystem, not an impossible claim of listing everything.
8. **Community knowledge.** Welcome corrections, missing perspectives, and well-supported additions.

---

<div align="center">

**Explore widely. Verify carefully. Build responsibly.**

If AI Atlas helps you understand the ecosystem, consider starring the repository and contributing a resource.

[Explore AI Atlas](https://github.com/msxfury/ai-atlas) · [Browse the catalog](CATALOG.md) · [Contribute](CONTRIBUTING.md)

</div>
