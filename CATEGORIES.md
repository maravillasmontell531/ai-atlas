# AI Atlas Category Guide

This taxonomy helps keep the directory consistent and searchable. A resource can have one primary category and multiple secondary tags.

## Product and workflow categories

| Category | Includes | Example tags |
|---|---|---|
| Assistants | Chat and general-purpose AI applications | chat, writing, planning, multimodal |
| Search and research | Web search, citations, scientific literature, source synthesis | search, web, papers, citations |
| Coding | Code completion, repository Q&A, refactoring, testing | coding, IDE, debugging, code-review |
| Image and design | Image generation, editing, vector graphics, visual design | image, design, vector, inpainting |
| Video and animation | Video generation, editing, avatars, motion | video, avatar, animation |
| Audio and speech | Speech recognition, synthesis, music, audio understanding | TTS, ASR, voice, music |
| Documents and knowledge | PDF, OCR, extraction, knowledge bases, document Q&A | PDF, OCR, RAG, extraction |
| Agents | Systems that use tools or take multi-step actions | agent, browser, tools, planning |
| Automation | Workflow builders, triggers, integrations, orchestration | workflow, no-code, integration |
| Productivity | Meeting notes, calendars, email, task management | meetings, notes, email |
| Business | Sales, marketing, support, finance, operations | CRM, support, analytics |
| Education | Tutoring, learning support, practice, course tools | tutoring, learning, assessment |
| Data and analytics | Data analysis, SQL, BI, visualization | analytics, SQL, dashboard |
| 3D and spatial | 3D asset generation, reconstruction, spatial workflows | 3D, mesh, reconstruction |
| Robotics and embodied AI | Robotics stacks, simulation, perception, control | robotics, simulation, vision |
| Accessibility | Assistive interfaces and accessibility workflows | captions, speech, assistive |
| Security and governance | Safety evaluation, privacy, policy, monitoring | evaluation, privacy, governance |

## Technical categories

| Category | Includes |
|---|---|
| Models | Named model families and individual releases |
| Model hubs | Search and hosting for models, datasets, and demos |
| APIs and inference | Hosted endpoints, gateways, serving and inference services |
| Local AI | On-device or self-hosted inference tools |
| Training and fine-tuning | Training frameworks, adapters, tuning and optimization |
| Data and datasets | Datasets, synthetic data tools, data preparation |
| Embeddings and retrieval | Embedding models, vector databases, rerankers, retrieval tools |
| Frameworks and SDKs | Libraries for building AI-powered applications |
| Evaluation and benchmarks | Test suites, leaderboards, measurement, red-teaming |
| Infrastructure | Accelerators, deployment, orchestration, observability |
| Research and papers | Papers, labs, research organizations, reproducibility resources |
| Education and documentation | Tutorials, courses, reference docs and learning materials |

## Capability tags

Only add tags backed by reliable sources.

- **Input modalities:** text, image, audio, video, files, structured-data, code, real-time
- **Output modalities:** text, code, image, audio, video, structured-data, actions
- **Tasks:** reasoning, summarization, translation, extraction, classification, generation, transcription, search, retrieval, planning, coding, mathematics
- **Integration:** web-app, desktop, mobile, browser-extension, API, SDK, CLI, IDE, plugin
- **Deployment:** hosted, local, self-hosted, cloud, edge
- **Access model:** free, freemium, subscription, usage-based, open-source, open-weights, proprietary, research-only
- **Audience:** beginner, developer, researcher, creator, business, educator

## Important distinctions

- **Product vs. model:** a product is an interface or service; a model is the underlying system. One product may offer multiple models, and one model may be available through multiple products.
- **Open source vs. open weights:** downloadable weights do not automatically mean that training data, code, and license meet an open-source definition.
- **Free vs. open:** a free web interface may be proprietary; an open model may still involve hosting or hardware costs.
- **Capability vs. guarantee:** a capability describes a supported task, not guaranteed accuracy.
- **Official vs. community resource:** clearly identify third-party wrappers, forks, and unofficial interfaces.

## Suggested detailed-entry schema

~~~yaml
name: Example AI
slug: example-ai
resource_type: product
primary_category: assistants
secondary_categories:
  - search-and-research
official_url: https://example.com/
documentation_url: null
description: A concise, original, plain-language description.
capabilities:
  - text-generation
features: []
modalities:
  input: [text]
  output: [text]
access:
  - web
pricing: unknown
availability: proprietary
limitations: []
last_verified: YYYY-MM-DD
sources:
  - https://example.com/
~~~

This is a template only. Replace placeholders with verified facts before adding a real resource.
