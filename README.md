# Full-Stack AI Engineer --- 48-Week Roadmap

A practical, project-driven 12-month plan to grow from a software
developer into a **Full-Stack AI Engineer**. The goal is to build,
evaluate, deploy and explain complete AI products---not just call LLM
APIs.

**Start date:** 3 October 2026

## Table of Contents

-   [Roadmap overview](#roadmap-overview)
-   [How to study](#how-to-study)
-   [48-week curriculum](#48-week-curriculum)
-   [Flagship projects](#flagship-projects)
-   [Daily study structure](#daily-study-structure)
-   [Day 1 setup checklist](#day-1-setup-checklist)
-   [48-week progress tracker](#48-week-progress-tracker)
-   [Final portfolio checklist](#final-portfolio-checklist)

## Roadmap overview

  Phase      Weeks Focus
  ------- -------- ----------------------------------------------------
  1           1--4 Python, backend, FastAPI, PostgreSQL
  2           5--8 Linear algebra, calculus, probability, statistics
  3          9--13 Classical machine learning
  4         14--17 Deep learning and PyTorch
  5         18--21 Computer vision
  6         22--24 Virtual Try-On photo MVP
  7         25--28 LLMs, transformers and model APIs
  8         29--32 Embeddings, vector search and RAG
  9         33--35 Tool calling and reliable agents
  10        36--39 AI Website Builder
  11        40--42 Document AI
  12        43--45 Live try-on, 3D vision and multi-angle prototype
  13        46--48 Evaluation, security, deployment and system design

## How to study

1.  Understand the concept before depending on a framework.
2.  Code small examples yourself; do not only watch tutorials.
3.  Build a working artifact every week.
4.  Record experiments, metrics, bugs and decisions.
5.  Do not skip foundations to reach advanced AI topics faster.
6.  Move forward when the week's exit outcome is achieved. The schedule
    is a guide, not a deadline.

## 48-week curriculum

### Phase 1 --- Python and backend foundations

**Week 1 --- Python basics** - Learn: variables, types, strings, lists,
tuples, sets, dictionaries, conditions, loops, functions, scope,
mutability, exceptions and files. - Practice: small daily problems;
rewrite familiar JavaScript utilities in Python. - Build: CLI expense
tracker with add/list/delete/summary. - Exit goal: write a small Python
program independently.

**Week 2 --- Python data handling** - Learn: comprehensions, slicing,
unpacking, `enumerate`, `zip`, sorting, CSV/JSON, modules, packages,
virtual environments, pip and basic tests. - Practice: clean messy JSON
and CSV data. - Build: data-cleaning CLI that creates a clean file and
validation report. - Exit goal: create and run a fresh Python project
with dependencies.

**Week 3 --- Advanced Python** - Learn: classes, composition,
inheritance, dataclasses, properties, iterators, generators, decorators,
context managers, type hints, logging, environment variables, HTTP and
`async/await`. - Practice: implement a generator, decorator, context
manager and async API client. - Build: async API aggregator with failure
handling and timing logs. - Exit goal: explain when to use the major
Python features.

**Week 4 --- FastAPI and PostgreSQL** - Learn: HTTP, REST, status codes,
FastAPI, Pydantic, dependency injection, middleware, CORS, errors,
OpenAPI, JWT basics, SQL, joins and CRUD. - Practice: endpoints,
validation, SQL queries and API tests. - Build: React/Next.js +
FastAPI + PostgreSQL application with login. - Exit goal: build a
backend from an empty folder and connect a frontend.

### Phase 2 --- Mathematics and statistics

**Week 5 --- Vectors, matrices and similarity** - Learn: scalars,
vectors, magnitude, dot product, Euclidean distance, cosine similarity,
matrix shapes, multiplication, transpose and NumPy broadcasting. -
Practice: calculate cosine similarity manually and with NumPy. - Build:
mini similarity-search experiment. - Exit goal: understand vector
dimensions and valid matrix operations.

**Week 6 --- Linear algebra for ML** - Learn: basis, span, independence,
rank, orthogonality, projection, eigenvalues/eigenvectors, PCA and SVD
intuition. - Practice: implement PCA with NumPy before using
scikit-learn. - Build: reduce a high-dimensional dataset to two
dimensions. - Exit goal: explain PCA and principal directions.

**Week 7 --- Calculus and gradient descent** - Learn: derivatives,
partial derivatives, chain rule, gradients, loss, gradient descent,
learning rate and convergence. - Practice: differentiate simple
functions and implement gradient descent in NumPy. - Build: linear
regression from scratch. - Exit goal: explain how gradients update model
parameters.

**Week 8 --- Probability, statistics and metrics** - Learn: mean,
median, variance, standard deviation, probability, conditional
probability, Bayes, distributions, expectation, correlation, covariance,
sampling, confidence intervals, precision, recall, F1, ROC and AUC. -
Practice: calculate confusion-matrix metrics by hand. - Build: notebook
comparing classifiers with multiple metrics. - Exit goal: explain the
precision/recall trade-off and why accuracy can mislead.

### Phase 3 --- Classical machine learning

**Week 9 --- ML fundamentals** - Learn: AI vs ML vs DL,
supervised/unsupervised/RL, features, labels, train/validation/test
splits, cross-validation, baselines, leakage, regression and
classification. - Practice: identify features, targets, splits and
metrics in sample datasets. - Build: baseline linear and logistic
regression. - Exit goal: explain the flow from raw data to evaluated
prediction.

**Week 10 --- ML algorithms** - Learn: decision trees, random forests,
gradient boosting, XGBoost/LightGBM concepts, KNN, SVM, Naive Bayes,
bias/variance and regularization. - Practice: compare at least three
models on one dataset. - Build: model comparison report. - Exit goal:
justify a model choice for a problem.

**Week 11 --- Data preparation** - Learn: missing values, encoding,
scaling, normalization, standardization, feature selection, leakage,
imbalance, class weights, SMOTE concepts and sklearn pipelines. -
Practice: repair a messy dataset without test-data leakage. - Build:
reusable preprocessing and training pipeline. - Exit goal: explain where
transformations are fitted and applied.

**Week 12 --- Unsupervised learning** - Learn: K-Means, choosing K,
hierarchical clustering, DBSCAN, cluster evaluation and PCA
visualization. - Practice: cluster data, inspect outliers and compare
settings. - Build: customer-segmentation dashboard. - Exit goal: judge
clusters using evidence.

**Week 13 --- First complete ML product** - Learn: problem framing, EDA,
feature pipelines, training, evaluation, serialization, FastAPI
inference and logging. - Practice: perform prediction error analysis. -
Build: end-to-end churn-prediction product with API and React
dashboard. - Exit goal: demo the product and explain every layer.

### Phase 4 --- Deep learning and PyTorch

**Week 14 --- Neural networks** - Learn: perceptrons, neurons, weights,
bias, forward pass, activations, loss, backpropagation, chain rule and
gradient descent. - Practice: build a tiny multilayer network with
NumPy. - Build: small classifier with a loss curve. - Exit goal: explain
forward pass, loss, backward pass and parameter update.

**Week 15 --- PyTorch core** - Learn: tensors, devices,
Dataset/DataLoader, `nn.Module`, autograd, optimizers,
training/validation loops, checkpoints and save/load. - Practice:
rebuild the NumPy network in PyTorch. - Build: PyTorch classifier with
FastAPI inference. - Exit goal: write a basic training loop yourself.

**Week 16 --- CNNs and transfer learning** - Learn: channels, kernels,
convolution, stride, padding, pooling, feature maps, augmentation,
pretrained models and fine-tuning. - Practice: visualize feature maps
and augmentations. - Build: clothing-image classifier using a pretrained
backbone. - Exit goal: explain convolution and transfer learning.

**Week 17 --- Training and GPU engineering** - Learn: CUDA basics, batch
size, learning rate, Adam/SGD, schedulers, early stopping, checkpoints,
experiment tracking, GPU memory and training vs inference. - Practice:
change one training variable at a time and record results. - Build:
reproducible experiment log. - Exit goal: diagnose underfitting,
overfitting, unstable training and OOM errors.

### Phase 5 --- Computer vision

**Week 18 --- Image processing** - Learn: OpenCV, PIL,
RGB/HSV/grayscale, resize, crop, rotation, affine/perspective
transforms, blur, edges, thresholding and morphology. - Practice: apply
image transformations manually and with OpenCV. - Build: person/garment
preprocessing utilities. - Exit goal: explain how a raw image becomes
model input.

**Week 19 --- Object detection** - Learn: classification vs detection,
bounding boxes, IoU, NMS, precision, recall, mAP, YOLO concepts and
confidence thresholds. - Practice: visualize detections and tune
thresholds. - Build: people/clothing detection prototype. - Exit goal:
explain overlapping boxes and NMS.

**Week 20 --- Segmentation** - Learn: semantic vs instance segmentation,
pixel/alpha masks, human segmentation, U-Net, Mask R-CNN concepts, mask
cleanup and compositing. - Practice: overlay masks and inspect failure
cases. - Build: person and clothing mask extraction. - Exit goal:
explain detection vs segmentation.

**Week 21 --- Pose and human parsing** - Learn: keypoints, skeletons,
2D/3D pose, confidence, tracking, human parsing, body regions, occlusion
and depth ambiguity. - Practice: webcam pose tracking and normalized
keypoints. - Build: VTON preprocessing bundle with person image, pose
and masks. - Exit goal: explain the inputs required by virtual try-on.

### Phase 6 --- AI Virtual Try-On

**Week 22 --- VTON architecture** - Learn: person/garment inputs, pose
conditioning, masks, alignment, warping, occlusion, deformation and
generative reconstruction. - Practice: affine/perspective garment
warping. - Build: VTON pipeline diagram and alignment experiment. - Exit
goal: explain each stage and its input/output.

**Week 23 --- Diffusion for try-on** - Learn: noise, denoising,
forward/reverse diffusion, latent space, conditioning, inpainting,
U-Net, VAE and cross-attention. - Practice: run a small inpainting
experiment. - Build: generative garment-reconstruction prototype. - Exit
goal: explain how diffusion changes an image while preserving other
regions.

**Week 24 --- Photo VTON MVP** - Learn: inference lifecycle,
preprocessing, validation, result storage, upload UI, before/after,
history and latency. - Practice: test good inputs, poor inputs and
failure cases. - Build: React/Next.js → FastAPI → CV preprocessing →
VTON inference → result UI. - Exit goal: working photo try-on demo with
documented limitations.

### Phase 7 --- LLMs and transformers

**Week 25 --- NLP, tokens and embeddings** - Learn: NLP basics, tokens,
token IDs, vocabulary, embeddings, context windows and semantic
similarity. - Practice: compare tokenization and embedding similarity. -
Build: small semantic-search experiment. - Exit goal: explain how text
becomes numerical representations.

**Week 26 --- Attention and transformers** - Learn: queries, keys,
values, self-attention, multi-head attention, positional information,
encoder/decoder and transformer blocks. - Practice: small attention
calculation or visualization. - Build: miniature attention/transformer
walkthrough. - Exit goal: explain how attention shares contextual
information.

**Week 27 --- LLM APIs and structured output** - Learn: message roles,
temperature, token limits, streaming, JSON Schema, structured output,
tool calling, validation and retries. - Practice: reject and repair
invalid model outputs. - Build: FastAPI AI assistant with streaming and
schema validation. - Exit goal: integrate an LLM reliably rather than
trusting arbitrary output.

**Week 28 --- Prompting and model selection** - Learn: zero/few-shot
prompting, instructions, constraints, prompt versioning, context
management, prompt injection concepts, hosted/local models, Hugging
Face, LoRA/QLoRA and quantization concepts. - Practice: compare
prompt/model variants using a test set. - Build: prompt and model
evaluation harness. - Exit goal: explain why a prompt or model change
helped or hurt.

### Phase 8 --- RAG

**Week 29 --- Embeddings and vector databases** - Learn: dense vectors,
dimensions, cosine similarity, nearest neighbors, indexes, metadata,
filters, Top-K and pgvector. - Practice: store, query and filter
chunks. - Build: PostgreSQL + pgvector search service. - Exit goal:
trace a query to its retrieved chunks.

**Week 30 --- Ingestion and chunking** - Learn: PDF/text ingestion,
cleaning, chunk size/overlap, semantic vs fixed chunking, metadata,
embedding and indexing. - Practice: compare chunking strategies. -
Build: document-ingestion pipeline. - Exit goal: justify chunking
choices using retrieval results.

**Week 31 --- Retrieval and grounded answers** - Learn: query embedding,
Top-K, context assembly, grounded generation, citations, source
metadata, reranking basics and insufficient-evidence handling. -
Practice: test questions whose answers are absent from the documents. -
Build: RAG assistant with citations. - Exit goal: trace generated
answers to evidence.

**Week 32 --- Advanced retrieval and evaluation** - Learn: BM25, hybrid
search, query rewriting, multi-query, reranking, parent-child retrieval,
contextual retrieval, Graph RAG concepts, agentic RAG concepts and
Recall@K. - Practice: benchmark retrieved chunks and generated
answers. - Build: compare vector-only, hybrid and reranked retrieval. -
Exit goal: justify retrieval design with measurements.

### Phase 9 --- AI agents

**Week 33 --- Tool calling** - Learn: tool schemas, execution lifecycle,
search/database/calculator/API tools, validation, permissions and tool
errors. - Practice: deliberately test tool failures. - Build: assistant
with three or four controlled tools. - Exit goal: explain model → tool
call → execution → result.

**Week 34 --- Workflows and state** - Learn: workflow vs agent,
planner/executor, state, memory concepts, sequential/parallel execution,
context management and loops. - Practice: draw a state machine before
coding. - Build: multi-step workflow with explicit state. - Exit goal:
draw workflow states and transitions.

**Week 35 --- Reliable agents** - Learn: state machines, human approval,
guardrails, retries/backoff, timeouts, validation, idempotency,
iteration limits, token/cost budgets and orchestration framework
concepts. - Practice: test tool failures, timeouts, malformed output and
loops. - Build: agent with human approval for risky actions. - Exit
goal: explain safe failure and recovery.

### Phase 10 --- AI Website Builder

**Week 36 --- Page schema first** - Learn: natural language to schema,
JSON Schema, strict validation, schema versioning, component registries,
props/defaults, layout constraints and schema repair. - Practice: test
20 natural-language requests and validate output. - Build: generate a
valid PageBuilder page and render it in the existing builder. - Exit
goal: generate valid, renderable page schema consistently.

**Week 37 --- Component-aware RAG** - Learn: component metadata,
capabilities, props, documentation embeddings, retrieval and nesting
rules. - Practice: test component retrieval on realistic requests. -
Build: natural language → component retrieval → valid page schema. -
Exit goal: demonstrate that retrieval improves component selection and
validity.

**Week 38 --- Agentic editing and debugging** - Learn: planning,
component selection, schema generation, validation/repair,
content/images, preview, iterative edits, debugging, publishing,
versioning and rollback. - Practice: intentionally break layouts and
test repair. - Build: agentic AI Website Builder prototype. - Exit goal:
create → edit → validate → repair → preview → publish.

**Week 39 --- Production architecture** - Learn: service boundaries,
async jobs, streaming, state, permissions, observability, failure
recovery, cost controls and schema versioning. - Practice: document
architecture and synchronous/asynchronous decisions. - Build:
production-quality vertical slice and architecture document. - Exit
goal: defend architecture choices and trade-offs.

### Phase 11 --- Document AI

**Week 40 --- PDF, OCR and layout** - Learn: PDF structure, scanned vs
text PDFs, OCR, reading order, headings, tables, figures, layout-aware
extraction and classification. - Practice: process clean PDFs, scans,
tables and messy layouts. - Build: extraction service preserving
source/page locations. - Exit goal: explain why layout and source
location matter.

**Week 41 --- Structured extraction and document RAG** - Learn: schema
extraction, field validation, confidence, chunking/indexing, Q&A,
citations and page/section references. - Practice: test missing,
ambiguous and incorrect fields. - Build: grounded document analyst for
invoices, contracts or financial documents. - Exit goal: extracted
fields have evidence and uncertainty is visible.

**Week 42 --- Comparison, audit and security** - Learn: document
comparison, clause finding, uncertainty, audit history, permissions,
tenant isolation, sensitive data and evaluation datasets. - Practice:
test unauthorized access and tenant isolation. - Build: secure document
comparison and clause-finding prototype. - Exit goal: explain access
control and audit behavior.

### Phase 12 --- Advanced Virtual Try-On

**Week 43 --- Live camera try-on** - Learn: `getUserMedia`, WebRTC
basics, camera permissions, local pose/segmentation, low-resolution
preview, server-side high-quality inference, streaming, latency and
FPS. - Practice: measure camera, preprocessing, network and inference
latency separately. - Build: V2 camera try-on prototype. - Exit goal:
report latency and identify bottlenecks.

**Week 44 --- 3D vision and body models** - Learn: depth estimation,
depth maps, camera coordinates, 3D reconstruction, point clouds, meshes,
textures/UVs, camera pose and SMPL/SMPL-X concepts. - Practice:
visualize depth and camera coordinates. - Build: basic 3D body/garment
representation. - Exit goal: explain the data needed to represent a body
and garment in 3D.

**Week 45 --- Three.js and multi-angle** - Learn: Three.js scenes,
cameras, meshes, materials, lights, WebGL/WebGPU concepts, cloth
simulation, collision/deformation, garment attachment and multi-view
consistency. - Practice: build a rotatable scene and inspect
front/side/back consistency. - Build: rotatable 3D human + garment
prototype and gap analysis. - Exit goal: separate current prototype
capabilities from true 360° requirements.

> A photo try-on, live camera preview and true 3D/360° try-on are
> different engineering milestones. Do not claim full 360° capability
> unless the system genuinely supports it.

### Phase 13 --- Production AI and interviews

**Week 46 --- Evaluation and security** - Learn: relevance,
faithfulness, groundedness, hallucination tests, retrieval metrics,
agent success/failure, prompt injection, PII, data leakage, auth/authz,
rate limits, tool permissions, RAG poisoning, SQL injection, XSS and
SSRF. - Practice: create adversarial tests and an evaluation dataset. -
Build: AI evaluation/security report or dashboard. - Exit goal:
identify, measure and mitigate important failure modes.

**Week 47 --- Deployment and performance** - Learn: Docker, Compose,
Redis, production PostgreSQL, CI/CD, AWS fundamentals, GPU
inference/model serving, batching, streaming, caching, quantization,
ONNX/TensorRT concepts, logs, metrics and tracing. - Practice:
containerize and load-test a flagship project. - Build: deployed service
with health checks, logs, metrics and latency/cost tracking. - Exit
goal: deploy, observe and troubleshoot the application.

**Week 48 --- System design and interviews** - Learn: requirements,
architecture, data flow, model selection, retrieval/tools, APIs,
storage, scaling, security, observability, cost, failure modes and
trade-offs. - Practice: draw systems without code and explain your
projects aloud. - Build: three system-design documents, two mock
interviews and final portfolio README. - Exit goal: take an unfamiliar
AI product problem from requirements to a defensible production
architecture.

## Flagship projects

### 1. AI Virtual Try-On

**Problem:** Help shoppers preview a garment on a person before
purchasing.

Build in stages: - V1: upload a person photo and garment image; generate
a try-on result. - V2: camera capture/live preview with measured
latency. - V3: explore multi-angle and 3D representations.

Skills: Python, PyTorch, OpenCV, segmentation, pose estimation,
diffusion/VTON inference, FastAPI, React/Next.js and GPU serving.

Portfolio evidence: architecture diagram, working demo, sample
inputs/outputs, evaluation and failure cases, latency measurements,
limitations and next steps.

### 2. AI Website Builder

**Problem:** Convert natural-language requests into editable websites
using a known component system.

Build: - Generate schema conforming to the PageBuilder contract. -
Retrieve suitable components and supported props. - Validate and repair
generated layouts. - Support iterative editing, preview, versioning and
controlled publishing.

Skills: LLM APIs, structured output, JSON Schema, component registries,
RAG, agents, validation, React/Next.js and backend architecture.

Portfolio evidence: component registry, schema docs, prompt-to-page
examples, validation tests, editing demos and architecture/security
decisions.

### 3. Document AI Analyst

**Problem:** Extract, compare and answer questions about business
documents with evidence.

Build: - Parse digital and scanned PDFs. - Extract structured fields
with validation. - Index content for retrieval. - Answer questions with
citations and page references. - Compare documents and maintain audit
history.

Skills: PDF processing, OCR, layout understanding, structured
extraction, embeddings, RAG, evaluation and access control.

Portfolio evidence: sample documents, extraction schemas, field-level
evidence, citation-grounded answers, comparison results and security
report.

## Daily 3-hour study structure

      Time Activity       Focus
  -------- -------------- -------------------------------------------
    45 min Learn          One focused concept from the current week
    60 min Code           Implement examples yourself
    45 min Project        Apply the concept to the weekly build
    30 min DSA/revision   One DSA problem or review and short notes

Weekly rhythm: Days 1--4 learn and implement; Day 5 integrate and test;
Day 6 revise, solve DSA, document and review; Day 7 rest or catch up.


Suggested repository structure:

``` text
full-stack-ai-engineer-roadmap/
├── README.md
├── python/
├── math/
├── machine-learning/
├── deep-learning/
├── computer-vision/
├── llm/
├── rag/
├── agents/
├── projects/
│   ├── virtual-try-on/
│   ├── ai-website-builder/
│   └── document-ai/
├── dsa/




└── notes/
```
