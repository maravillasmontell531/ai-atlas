# Contributing to AI Atlas

Thanks for helping map the AI ecosystem. Useful contributions include new tools, models, APIs, research resources, category improvements, verified capability details, broken-link fixes, and pricing or availability corrections.

## Before submitting

1. Search the repository to avoid duplicates.
2. Prefer official product pages, documentation, model cards, release notes, or repositories.
3. Write descriptions in your own words. Do not copy large sections of marketing or documentation.
4. Be specific about what a resource does and avoid hype.
5. Mark unknown details as unknown rather than guessing.
6. Include the date information was checked when practical.
7. Respect licenses, trademarks, privacy, and third-party terms.

## What makes a useful entry?

A useful listing answers: What is it? Who maintains it? What can it do? Which input and output formats does it support? Is it a product, model, API, library, dataset, or research resource? How is it accessed? Where is the official documentation? What is known about pricing, licensing, and limitations? Which sources support the claims?

Not every field will apply. Accuracy matters more than filling every field.

## Add an entry to CATALOG.md

Use this format:

~~~markdown
| Name | Description | Official link |
|---|---|---|
| Example AI | Original one-sentence description of the resource and its main use cases. | [Website](https://example.com/) |
~~~

Replace the example with a real resource and verified official URL. Put it in the most relevant category, alphabetize entries within a section where practical, and avoid duplicates.

## Detailed entry template

For resources that need extensive details, propose a separate Markdown file under a suitable folder, such as catalog/assistants/example-ai.md.

~~~markdown
# Resource Name

- **Type:** Product / model / API / library / dataset / research
- **Category:** Primary category
- **Official website:** https://example.com/
- **Documentation:** Link or Unknown
- **Last verified:** YYYY-MM-DD

## Overview
An original, concise description.

## Capabilities
- Capability supported by an official source.

## Features
- Verified feature and relevant conditions.

## Access and pricing
- Access method:
- Pricing: Free / Freemium / Subscription / Usage-based / Unknown
- Availability: Open source / Open weights / Proprietary / Unknown

## Limitations
- Known limitations or Unknown.

## Sources
- Official source URL
~~~

Do not claim a model has a feature just because a third-party interface offers it. Distinguish model capabilities from features of the product hosting it.

## Pull request checklist

- [ ] The resource is relevant and not already listed.
- [ ] The official URL works and points to the intended resource.
- [ ] The description is original, clear, and neutral.
- [ ] Claims about capabilities and pricing have sources.
- [ ] Category and tags are appropriate.
- [ ] No API keys, credentials, personal information, or private data are included.
- [ ] Third-party logos, images, and text are used only where permitted.
- [ ] Broken or outdated details are corrected rather than duplicated.

## Quality rules

- **No fabricated entries:** never invent a tool, feature, benchmark, price, or link.
- **No unsupported superlatives:** avoid claims like “best” or “number one” without clear, dated evidence.
- **No spam:** promotional submissions and referral-only listings may be declined.
- **No duplicates:** use one canonical entry and note meaningful versions or variants.
- **No misleading license labels:** free access, open weights, and open-source licensing are different things.
- **No copied descriptions:** summarize in your own words and cite the official source.
- **Keep links useful:** prefer canonical product and documentation links over tracking links.

## Corrections and removals

Open an issue if a product has shut down, changed names, moved, become unavailable, or has misleading information in the catalog. Include the affected entry and a reliable source.

## Scope

AI Atlas is a directory, not a certification or endorsement service. Inclusion does not mean a product is safe, accurate, private, or suitable for every use case.
