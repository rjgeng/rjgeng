# Rongjun Geng

**AI/LLM & systems software engineer** — agentic systems, RAG, full-stack. San Francisco Bay Area.

I build LLM-powered products end to end — FastAPI + LangChain backends, React frontends — and
contribute fixes upstream to open-source multi-agent orchestration systems.

#### 🔀 Merged upstream contributions

Fixes merged across the [gastownhall](https://github.com/gastownhall) ecosystem — an open-source
multi-agent orchestration platform — each reviewed and approved by independent maintainers.
**7 merged PRs across 2 repos:**

**[gastownhall/gascity](https://github.com/gastownhall/gascity)**
- [#3469](https://github.com/gastownhall/gascity/pull/3469) — fix(dolt): dedup mol-dog-doctor advisory storm
- [#2638](https://github.com/gastownhall/gascity/pull/2638) — fix(gc): warn before supervisor recycle during city init
- [#2316](https://github.com/gastownhall/gascity/pull/2316) — fix(dolt): retry preflight when HEAD races on busy DBs
- [#2136](https://github.com/gastownhall/gascity/pull/2136) — fix(maintenance): retry JSONL push on concurrent ref-update race
- [#2088](https://github.com/gastownhall/gascity/pull/2088) — docs(convoy): clarify --help text re: workflows vs convoys
- [#2037](https://github.com/gastownhall/gascity/pull/2037) — fix(packs): fallback to dolt-provider-state.json

**[gastownhall/gastown](https://github.com/gastownhall/gastown)**
- [#4173](https://github.com/gastownhall/gastown/pull/4173) — fix(memories): tolerate non-string values in `bd kv list`

Themes: concurrency races, operational guardrails, and failure-mode UX in long-running agent systems.

> Maintainer on [#3469](https://github.com/gastownhall/gascity/pull/3469): *"a careful, surgical fix — I especially appreciate that you keyed the dedup signature on the set of active conditions."*

I also file actionable bug reports that maintainers act on — e.g.
[#2814](https://github.com/gastownhall/gascity/issues/2814) (bundled Dolt 2.0.8 corruption → version pin)
and [#2846](https://github.com/gastownhall/gascity/issues/2846) (compactor quarantine race starving GC) —
both closed with a by-name thanks from a core committer.

#### Stacks

-  **Languages**: Python, C/C++, Bash, Rust, JavaScript
-  **LLM Tools & Frameworks**: Hugging Face, LangChain, Gradio, FAISS, Chroma, Ollama, OpenAI, Claude, DeepSeek, Gemini
-  **GenAI Techniques**: RAG, QLoRA, Prompt Engineering, Agents, Fine-tuning, Multi-modal Integration
-  **Backend**: FastAPI + LangChain/OpenAI SDK
-  **Backend & System**: Linux (gdb, perf, valgrind), REST/gRPC/GraphQL APIs, multithreading, system calls
-  **Database**: PostgreSQL + Chroma (or MongoDB for quick prototyping), MySQL, Redis, SQLite
-  **Storage**: S3/Supabase for files
-  **Frontend**: React + TailwindCSS
-  **DevOps & Cloud**: Docker, GitHub Actions, Jenkins, AWS (S3, Lambda, EC2), Nginx
-  **Networking & Security**: TCP/IP, WebSockets, MQTT, SELinux, HAProxy
-  **Embedded & EDA**: Altium Designer, Vivado, Verilog/VHDL, GNURadio, UHD, MATLAB
-  **Version Control**: Git, GitHub, GitLab, SVN

#### Pinned projects

See pinned repos below — an AI trading workstation (FinAlly), a private-corpus RAG + web-search
assistant (web_rag_search), GenAI/RAG notebooks (gen_ai), and an API-cost postmortem with guardrails.
I publish the misses, not just the wins.
