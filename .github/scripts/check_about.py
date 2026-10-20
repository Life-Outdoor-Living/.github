#!/usr/bin/env python3
"""Controleer dat wat GitHub onder *About* toont, is wat .github/about.yml zegt.

    python3 .github/scripts/check_about.py --offline   # alleen het bestand: GitHub's grenzen
    python3 .github/scripts/check_about.py             # ook de repository zelf, met GH_TOKEN

De controle tegen GitHub draait in .github/workflows/wiki.yml na elke push naar main. Hij faalt
als de beschrijving, de homepage, de topics of de wiki afwijken van het bestand, en zegt wat er
aangeklikt moet worden: dat zetten is werk voor een beheerder van de repository. Overgenomen uit
`.github/scripts/check_about.py` in Life-Outdoor-Living/skills.
"""

import json
import os
import re
import sys
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
REPO = os.environ.get("GITHUB_REPOSITORY", "Life-Outdoor-Living/.github")
TOPIC = re.compile(r"^[a-z0-9][a-z0-9-]{0,49}$")


def main() -> int:
    want = yaml.safe_load((ROOT / ".github" / "about.yml").read_text(encoding="utf-8"))
    description = " ".join(str(want.get("description") or "").split())
    topics = list(want.get("topics") or [])

    problems = []
    if not description or len(description) > 350:
        problems.append(f"de beschrijving is {len(description)} tekens; GitHub wil er 1 tot 350")
    if len(topics) > 20:
        problems.append(f"{len(topics)} topics; GitHub staat er hooguit 20 toe")
    problems += [f"topic `{t}` voldoet niet aan GitHub's vorm (kleine letters, cijfers, koppeltekens, "
                 f"hooguit 50 tekens)" for t in topics if not TOPIC.match(str(t))]
    if len(set(topics)) != len(topics):
        problems.append("een topic staat er twee keer in")

    if "--offline" not in sys.argv and not problems:
        request = urllib.request.Request(
            f"https://api.github.com/repos/{REPO}",
            headers={"Authorization": f"Bearer {os.environ['GH_TOKEN']}",
                     "Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"})
        with urllib.request.urlopen(request, timeout=30) as answer:
            have = json.load(answer)
        if " ".join((have.get("description") or "").split()) != description:
            problems.append(f"GitHub toont als beschrijving {have.get('description')!r}; zet hem op:\n"
                            f"      {description}")
        if (have.get("homepage") or "").rstrip("/") != str(want.get("homepage") or "").rstrip("/"):
            problems.append(f"GitHub toont als homepage {have.get('homepage')!r}; zet hem op:\n"
                            f"      {want.get('homepage') or '(leeg)'}")
        if sorted(have.get("topics") or []) != sorted(topics):
            problems.append(f"GitHub toont de topics {sorted(have.get('topics') or [])}; zet ze op:\n"
                            f"      {' '.join(topics)}")
        if bool(have.get("has_wiki")) != bool(want.get("wiki")):
            problems.append("de wiki staat " + ("uit" if not have.get("has_wiki") else "aan")
                            + f"; about.yml zegt {'aan' if want.get('wiki') else 'uit'}")

    if problems:
        print(f"{REPO} en .github/about.yml lopen uiteen:\n")
        for p in problems:
            print(f"  - {p}")
        print("\nEen beheerder zet de beschrijving en de topics met het tandwiel naast *About* op de "
              "hoofdpagina, en de wiki onder Settings → General → Features → Wikis.")
        return 1
    print("about.yml klopt" + (" met wat GitHub toont" if "--offline" not in sys.argv else
                                " met GitHub's grenzen (offline)"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
