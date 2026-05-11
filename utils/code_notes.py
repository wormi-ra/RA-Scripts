from jinja2 import Environment, FileSystemLoader, select_autoescape
from typing import Any
from pycheevos.utils.import_notes import prefix_region, detect_type, sanitize_name
import json
import sys
import re

JINJA_ENV = Environment(
    loader=FileSystemLoader("utils/templates/"),
    autoescape=select_autoescape(),
    lstrip_blocks=True,
    trim_blocks=True
)

def get_region(note_text):
    # List of known regions (case-insensitive)
    regions = ["us", "eu", "jp", "pal", "ntsc"]
    match = re.search(r'^.*[\[\(]([a-zA-Z]+)[\]\)]', note_text)
    if match:
        region = match.group(1).lower() 
        if region in regions:
            return region
    return None

def slugify(text: str) -> str:
    return re.sub(r'[\W_]+', '_', text.upper())

def get_title(note: str) -> str:
    return sanitize_name(note)

def get_type(note: dict[str, str]) -> str:
    return detect_type(note["Note"].splitlines()[0], "")

def process_note(note: dict[str, str]) -> dict[str, Any]:
    return {
        "address": note["Address"],
        "type": get_type(note),
        "slug": slugify(get_title(note["Note"])),
        "note": note["Note"].replace("\r\n", "\n").replace("\\", "\\\\"),
        "author": note["User"],
        "region": get_region(note["Note"]),
    }

with open(sys.argv[1], encoding="utf-8") as file:
    raw_notes = json.load(file)
notes = [
    process_note(note) for note in raw_notes
]
uniques = {}
for note in notes:
    slug = f"{note['region']}_{note['slug']}"
    if slug in uniques:
        uniques[slug] += 1
        note["slug"] = f"{note['slug']}_{uniques[slug]}"
    else:
        uniques[slug] = 0

with open("memory.py", "w", encoding="utf-8") as file:
    template = JINJA_ENV.get_template("code_notes.jinja")
    file.write(template.render(notes=notes))
