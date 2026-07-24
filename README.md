# Rongjun Geng

**AI/LLM & systems software engineer** — agentic systems, RAG, full-stack. San Francisco Bay Area.

I build LLM-powered products end to end — FastAPI + LangChain backends, React frontends — and
contribute fixes upstream to open-source multi-agent orchestration systems.

#### 🔀 Merged upstream contributions

<!-- AUTO-GENERATED:PR-LIST START — do not hand-edit; scripts/update_readme.py regenerates
     this block on a schedule via .github/workflows/update-pr-list.yml -->
Fixes merged across the [gastownhall](https://github.com/gastownhall) ecosystem — an open-source
multi-agent orchestration platform — each reviewed and approved by independent maintainers.
**32 merged PRs across 2 repos:**

**[gastownhall/gascity](https://github.com/gastownhall/gascity)**
- [#4583](https://github.com/gastownhall/gascity/pull/4583) — fix(cmd/gc): materialize newly-added skills on every applied config reload
- [#4555](https://github.com/gastownhall/gascity/pull/4555) — fix(storehealth): add an absolute-size floor so small cities don't permanently trip maintenance-overdue
- [#4554](https://github.com/gastownhall/gascity/pull/4554) — fix(sling): warn when --on/default-formula attach drops the target bead's description
- [#4552](https://github.com/gastownhall/gascity/pull/4552) — fix(doctor): rig-pack-coverage recognizes same-name local pack replacements
- [#4549](https://github.com/gastownhall/gascity/pull/4549) — fix(orders): give a never-run cron order one bounded catch-up chance
- *…and 26 more — [see all 31](https://github.com/search?q=repo%3Agastownhall%2Fgascity+is%3Apr+is%3Amerged+author%3Arjgeng&type=pullrequests)*

**[gastownhall/gastown](https://github.com/gastownhall/gastown)**
- [#4173](https://github.com/gastownhall/gastown/pull/4173) — fix(memories): tolerate non-string values in bd kv list
<!-- AUTO-GENERATED:PR-LIST END -->

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
