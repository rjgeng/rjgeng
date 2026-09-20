# Rongjun Geng

**AI/LLM & systems software engineer** — agentic systems, RAG, full-stack. San Francisco Bay Area.

I build LLM-powered products end to end — FastAPI + LangChain backends, React frontends — and
contribute fixes upstream to open-source multi-agent orchestration systems.

#### 🔀 Open-source contributions

<!-- AUTO-GENERATED:PR-LIST START — do not hand-edit; scripts/update_readme.py regenerates
     this block on a schedule via .github/workflows/update-pr-list.yml -->
Fixes merged across the [gastownhall](https://github.com/gastownhall) ecosystem — an open-source
multi-agent orchestration platform — each reviewed and approved by independent maintainers.
**93 merged PRs across 3 repos:**

**[gastownhall/gascity](https://github.com/gastownhall/gascity)**
- [#5939](https://github.com/gastownhall/gascity/pull/5939) — fix(nudge): add a drop verb for stale pending nudges instead of requiring manual state.json surgery
- [#5938](https://github.com/gastownhall/gascity/pull/5938) — fix(sessionlog): thread the transcript entry's own timestamp through to Fact.At instead of stamping now
- [#5933](https://github.com/gastownhall/gascity/pull/5933) — fix(mail): respect cfg.Mail.RetentionTTL in the nudge-mail sweep instead of a hardcoded 60m
- [#5913](https://github.com/gastownhall/gascity/pull/5913) — fix(supervisor): guard the supervisor socket path against Unix domain socket length limits
- [#5756](https://github.com/gastownhall/gascity/pull/5756) — fix(events): fail a short single-record write instead of counting it as written
- *…and 82 more — [see all 87](https://github.com/search?q=repo%3Agastownhall%2Fgascity+is%3Apr+is%3Amerged+author%3Arjgeng&type=pullrequests)*

**[gastownhall/gastown](https://github.com/gastownhall/gastown)**
- [#4173](https://github.com/gastownhall/gastown/pull/4173) — fix(memories): tolerate non-string values in bd kv list

**[gastownhall/gascity-packs](https://github.com/gastownhall/gascity-packs)**
- [#320](https://github.com/gastownhall/gascity-packs/pull/320) — fix(gastown/witness): re-verify liveness before delete, content-check merges past rebase/squash
- [#322](https://github.com/gastownhall/gascity-packs/pull/322) — fix(gastown/witness): complete crashed submit-and-exit handoff instead of resetting to pool
- *…and 3 more — [see all 5](https://github.com/search?q=repo%3Agastownhall%2Fgascity-packs+is%3Apr+is%3Amerged+author%3Arjgeng&type=pullrequests)*
<!-- AUTO-GENERATED:PR-LIST END -->

Themes: concurrency races, operational guardrails, and failure-mode UX in long-running agent systems.

> Maintainer on [#3469](https://github.com/gastownhall/gascity/pull/3469): *"a careful, surgical fix — I especially appreciate that you keyed the dedup signature on the set of active conditions."*

I also file actionable bug reports that maintainers act on — e.g.
[#2814](https://github.com/gastownhall/gascity/issues/2814) (bundled Dolt 2.0.8 corruption → version pin)
and [#2846](https://github.com/gastownhall/gascity/issues/2846) (compactor quarantine race starving GC) —
both closed with a by-name thanks from a core committer.

#### 🧰 Technical stack

**Languages**  
Go · Python · C/C++ · Bash · TypeScript / JavaScript

**Agentic AI & orchestration**  
Gas City · Gas Town · multi-agent orchestration · agent lifecycle & reconciliation · tool-calling workflows · human-in-the-loop workflows

**LLM / GenAI**  
RAG · LangChain · Chroma · FAISS · OpenAI · Claude · DeepSeek · Prompt Engineering

**Full Stack & distributed systems**  
React · Next.js · Tailwind CSS · FastAPI · REST · concurrency control · process & subprocess lifecycle · Linux systems programming · failure recovery

**Data & storage**  
Dolt · PostgreSQL · Redis · SQLite · MongoDB · S3 · Supabase

**CI & tooling**  
Git · GitHub · GitHub Actions · GitLab · SVN

**Debugging & reliability**  
concurrency debugging · root-cause analysis · failure-mode analysis · operational guardrails · observability · regression testing

**Networking / embedded / RF**  
TCP/IP · MQTT · GNU Radio · UHD · LabVIEW · KiCad · Altium Designer · Vivado · Verilog / VHDL

#### 📌 Pinned projects

See the repositories below for selected AI, agentic-systems, systems-software, and engineering projects.
