from jinja2 import Environment, FileSystemLoader, select_autoescape
from typing import Any
from pycheevos.utils.import_notes import detect_type, sanitize_name
import json
import sys
import re

JINJA_ENV = Environment(
    loader=FileSystemLoader("utils/templates/"),
    autoescape=select_autoescape(),
    lstrip_blocks=True,
    trim_blocks=True
)

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
        "note": note["Note"].replace("\r\n", "\n"),
        "author": note["User"],
    }

with open(sys.argv[1], encoding="utf-8") as file:
    raw_notes = json.load(file)
notes = [
    process_note(note) for note in raw_notes
]

with open("memory.py", "w", encoding="utf-8") as file:
    template = JINJA_ENV.get_template("code_notes.jinja")
    file.write(template.render(notes=notes))
