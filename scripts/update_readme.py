#!/usr/bin/env python3
"""Regenerates the merged-contribution block in README.md from live GitHub data.

Reads merged PRs authored by AUTHOR plus explicitly credited contributions
whose PR was opened by a maintainer (read-only — never writes to those repos).
Only the region between the
AUTO-GENERATED:PR-LIST markers in README.md is replaced; everything else
in the file (intro, maintainer quote, stacks, pinned projects) is
hand-authored and left untouched.

Run by .github/workflows/update-pr-list.yml on a schedule.
"""
import json
import re
import subprocess
import sys

REPOS = [
    "gastownhall/gastown",
    "gastownhall/gascity",
    "gastownhall/gascity-packs",
    "gastownhall/beads",
]
AUTHOR = "rjgeng"
CREDITED_PRS_BY_REPO = {
    # PR #6574 was opened by a maintainer, but includes Rongjun's compatibility
    # follow-up with the original commit authorship preserved.
    "gastownhall/beads": {
        6574: "includes Rongjun's preserved authored compatibility fix",
    },
}
FEATURED_PRS_BY_REPO = {
    # Keep the credited maintainer-opened contribution visible; the remainder
    # link surfaces the authored PRs that GitHub's author search can enumerate.
    "gastownhall/beads": [6574],
}
DEFAULT_MAX_SHOWN_PER_REPO = 5
MAX_SHOWN_BY_REPO = {
    "gastownhall/gascity": 2,
    "gastownhall/gascity-packs": 2,
    "gastownhall/beads": 2,
}
README_PATH = "README.md"
START_MARKER = "<!-- AUTO-GENERATED:PR-LIST START — do not hand-edit; scripts/update_readme.py regenerates\n     this block on a schedule via .github/workflows/update-pr-list.yml -->"
END_MARKER = "<!-- AUTO-GENERATED:PR-LIST END -->"


def fetch_merged_prs(repo):
    out = subprocess.run(
        [
            "gh", "pr", "list", "--repo", repo, "--author", AUTHOR,
            "--state", "merged", "--limit", "200",
            "--json", "number,title,url,mergedAt",
        ],
        check=True, capture_output=True, text=True,
    ).stdout
    prs = json.loads(out)
    known_numbers = {pr["number"] for pr in prs}
    for number, credit_note in CREDITED_PRS_BY_REPO.get(repo, {}).items():
        if number in known_numbers:
            continue
        credited_out = subprocess.run(
            [
                "gh", "pr", "view", str(number), "--repo", repo,
                "--json", "number,title,url,mergedAt",
            ],
            check=True, capture_output=True, text=True,
        ).stdout
        credited_pr = json.loads(credited_out)
        if credited_pr["mergedAt"]:
            credited_pr["creditNote"] = credit_note
            prs.append(credited_pr)
    prs.sort(key=lambda p: p["mergedAt"], reverse=True)
    featured = FEATURED_PRS_BY_REPO.get(repo, [])
    if featured:
        rank = {number: index for index, number in enumerate(featured)}
        prs.sort(key=lambda p: rank.get(p["number"], len(featured)))
    return prs


def clean_title(title):
    # Squash-merge titles often carry a trailing "(#NNNN)" or
    # "(#NNNN follow-up)" referencing the *issue*, not the PR itself —
    # strip it, matching the hand-authored entries' existing style.
    return re.sub(r"\s*\(#\d+(?:\s+follow-up)?\)\s*$", "", title)


def format_repo_section(repo, prs):
    total = len(prs)
    max_shown = MAX_SHOWN_BY_REPO.get(repo, DEFAULT_MAX_SHOWN_PER_REPO)
    shown = prs[:max_shown]
    lines = [f"**[{repo}](https://github.com/{repo})**"]
    for pr in shown:
        credit_note = f" — *{pr['creditNote']}*" if pr.get("creditNote") else ""
        lines.append(
            f"- [#{pr['number']}]({pr['url']}) — {clean_title(pr['title'])}{credit_note}"
        )
    if total > max_shown:
        search_url = (
            f"https://github.com/search?q=repo%3A{repo.replace('/', '%2F')}"
            f"+is%3Apr+is%3Amerged+author%3A{AUTHOR}&type=pullrequests"
        )
        remaining = total - max_shown
        lines.append(f"- *…and {remaining} more — [see all {total}]({search_url})*")
    return "\n".join(lines)


def main():
    total_count = 0
    sections = []
    for repo in REPOS:
        prs = fetch_merged_prs(repo)
        total_count += len(prs)
        sections.append(format_repo_section(repo, prs))

    summary_line = (
        "Contributions merged across the [gastownhall](https://github.com/gastownhall) ecosystem — "
        "an open-source\nmulti-agent orchestration platform — each reviewed and approved by "
        f"independent maintainers.\n**{total_count} merged contributions across {len(REPOS)} repos:**"
    )

    body = summary_line + "\n\n" + "\n\n".join(sections)
    new_block = f"{START_MARKER}\n{body}\n{END_MARKER}"

    with open(README_PATH, "r", encoding="utf-8") as f:
        readme = f.read()

    pattern = re.compile(re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER), re.DOTALL)
    if not pattern.search(readme):
        print("AUTO-GENERATED:PR-LIST markers not found in README.md — aborting without changes.", file=sys.stderr)
        sys.exit(1)

    new_readme = pattern.sub(lambda _m: new_block, readme)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_readme)


if __name__ == "__main__":
    main()
