# AI Engineering Stack: From Idea to Production

## 1. Define the task

Specify the user, workflow, inputs, output contract, success criteria, error tolerance, latency target, total cost budget, data boundary, authorization and representative test set. Consider SQL, ordinary code, rules or search before adding an AI model.

## 2. Choose a pattern

| Pattern | Fit | Trade-off |
|---|---|---|
| Direct model call | Self-contained transformation | Simple, but output can be wrong or variable |
| Structured output | Extraction to typed records | Format can be constrained; meaning must be checked |
| RAG | Changing/private knowledge | Retrieval/freshness/permissions are dependencies |
| Tool calling | Model chooses external operation | Server validates and authorizes every action |
| Deterministic workflow | Known process with selected AI steps | Auditable but state transitions must be explicit |
| Agent loop | Actions branch on new observations | Flexible but harder to bound/recover |
| Fine-tuning | Stable repeated behavior | Data/training/regression burden |
| Local model | Offline or control needs | Hardware and serving burden |

## 3. Model and context decisions

Evaluate representative-task quality, modalities, language, context limits, schema compliance, refusals, latency distribution, rate limits, total cost, deployment, license, retention and region. Record model ID/revision, provider, prompt, settings and date. Context includes instructions, history, memory, retrieved sources, tool schemas and output constraints. Keep it relevant, preserve permissions and provenance, label external content untrusted, avoid secrets, reserve output budget and avoid contradictory stale information.

## 4. RAG engineering

Ingest permitted data; parse format-aware; preserve source IDs, revisions, timestamps and access-control lists; chunk semantically; embed where useful; index lexical/dense/hybrid data; filter permissions; rerank if measured gain justifies latency; assemble cited context; generate; verify evidence; refresh and propagate deletion. Test parsing and retrieval independently. Measure recall and relevance separately from answer quality, citations, abstention, access isolation and latency. Include unanswerable, stale, conflicting and revoked-source tests.

## 5. Tool safety and agents

Tool calls are proposals, not permissions. Define narrow schemas; validate server-side; enforce identity and authorization outside the model; separate reads/writes; require approval for consequential changes; use idempotency; set timeouts and spend/step limits; trace actions; redact outputs; and treat webpages/documents as untrusted. Agents need stop conditions, cancellation, repeated-action detection, partial-state recovery and escalation. Prefer deterministic workflows if the path is known.

## 6. Data, evals and operations

Check data rights, provenance, sensitive fields, deduplication, label quality and train/test leakage. Fine-tune only when measured value justifies ongoing maintenance. Maintain a clean holdout set. Freeze representative tests before changes; record inputs, rubrics, model/version, prompts, tools, outputs, graders, timestamps, latency and cost. Monitor task completion, retrieval recall, groundedness, schema validity, invalid actions, policy violations, human escalation and per-success cost. Automated judges require calibration against human evaluation.

Use bounded retries, timeouts, rate-limit handling, circuit breakers, compatible fallbacks, queues and graceful degradation. Logs can contain sensitive data and require redaction/retention control. Costs include tokens, media, embeddings, reranking, tools, browsers, storage, retries and human review. Test model routing, concise context, caching and batching against quality. Quantization reduces precision; distillation transfers behavior; throughput differs from latency.

## Production checklist

- [ ] Acceptance criteria and baseline defined.
- [ ] Regression dataset exists.
- [ ] Model/configuration versions recorded.
- [ ] Authorization enforced outside model.
- [ ] Prompt injection and untrusted content tested.
- [ ] Privacy, retention, license and region reviewed.
- [ ] Retries, timeouts and budgets bounded.
- [ ] Recovery, fallback, monitoring and rollback tested.
- [ ] Users understand limitations and review paths.

References: [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework), [OWASP GenAI](https://genai.owasp.org/), [OpenTelemetry](https://opentelemetry.io/docs/), [MLflow](https://mlflow.org/docs/latest/).
