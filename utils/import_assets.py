import pycheevos.utils.import_set as importer
from jinja2 import Environment, FileSystemLoader, select_autoescape

JINJA_ENV = Environment(
    loader=FileSystemLoader("utils/templates/"),
    autoescape=select_autoescape(),
    lstrip_blocks=True,
    trim_blocks=True
)

def generate_assets(game_id, achievements, leaderboards, source_name):
    with open("assets.py", "w", encoding="utf-8") as file:
        template = JINJA_ENV.get_template("assets.jinja")
        file.write(template.render(achievements=achievements, leaderboards=leaderboards))

importer.generate_script = generate_assets

if __name__=="__main__":
    import sys
    game_id = int(sys.argv[1])
    importer.process_game(game_id)
