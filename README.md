# Rongjun Geng

**AI/LLM & systems software engineer** — agentic systems, RAG, full-stack. San Francisco Bay Area.

I build LLM-powered products end to end — FastAPI + LangChain backends, React frontends — and
contribute fixes upstream to open-source multi-agent orchestration systems.

#### 🔀 Merged upstream contributions

<!-- AUTO-GENERATED:PR-LIST START — do not hand-edit; scripts/update_readme.py regenerates
     this block on a schedule via .github/workflows/update-pr-list.yml -->
Fixes merged across the [gastownhall](https://github.com/gastownhall) ecosystem — an open-source
multi-agent orchestration platform — each reviewed and approved by independent maintainers.
**18 merged PRs across 2 repos:**

**[gastownhall/gascity](https://github.com/gastownhall/gascity)**
- [#4219](https://github.com/gastownhall/gascity/pull/4219) — fix(runproj): warming snapshot no longer marshals historicalLanes/recentChanges as null
- [#4216](https://github.com/gastownhall/gascity/pull/4216) — fix(cmd/gc): lint no longer flags the documented pool-disable form as a named-session conflict
- [#4213](https://github.com/gastownhall/gascity/pull/4213) — fix(materialize): log a debug line when a shared skill-catalog name is shadowed
- [#4211](https://github.com/gastownhall/gascity/pull/4211) — test(cmd/gc): regression coverage for rig-scoped pool default scale_check + work_query
- [#4186](https://github.com/gastownhall/gascity/pull/4186) — fix(reaper): head+tail window sanitize_output so long-query errors survive
- [#4156](https://github.com/gastownhall/gascity/pull/4156) — fix(materialize): remember gc-written symlink targets so pack-sha bumps self-heal
- [#4129](https://github.com/gastownhall/gascity/pull/4129) — fix(dolt-cleanup): resolve DROP-stage user via GC_DOLT_USER instead of hardcoded root
- [#4019](https://github.com/gastownhall/gascity/pull/4019) — feat(config): gc config explain renders idle/lifecycle-timeout agent keys
- [#3981](https://github.com/gastownhall/gascity/pull/3981) — fix(cmd): imported command groups exit non-zero on unknown subcommands
- [#3979](https://github.com/gastownhall/gascity/pull/3979) — fix(doctor): clarify external Dolt backup message — endpoint may be local
- *…and 7 more — [see all 17](https://github.com/search?q=repo%3Agastownhall%2Fgascity+is%3Apr+is%3Amerged+author%3Arjgeng&type=pullrequests)*

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
