import json
import re
from pathlib import Path
import pyperclip

def make_toc(filename):

    def _slugify(title: str) -> str:
        title = re.sub(r"\$.*?\$", "", title)
        title = title.lower().strip()
        title = re.sub(r"[^\w\s-]", "", title)
        title = re.sub(r"\s+", "-", title)
        return title

    nb_path = Path(filename).resolve()

    with open(nb_path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    toc_lines = []

    for cell in nb["cells"]:
        if cell["cell_type"] == "markdown":
            for line in cell["source"]:
                stripped = line.lstrip()
                if stripped.startswith("#"):
                    level = len(stripped) - len(stripped.lstrip("#"))
                    title = stripped.strip("#").strip()
                    anchor = _slugify(title)
                    indent = "  " * (level - 1)
                    toc_lines.append(f"{indent}- [{title}](#{anchor})")

    toc = "## Table of Contents\n\n" + "\n".join(toc_lines)

    pyperclip.copy(toc)
    print("TOC copied to clipboard:\n")
    print(toc)
