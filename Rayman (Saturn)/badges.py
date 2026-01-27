from PIL import Image, ImageFilter
from csv import DictReader

IMG_PATH = "data/img"
OUTPUT_PATH = "output/badges"
SAMPLING = Image.Resampling.LANCZOS

class Badge:
    id: int
    name: str
    background: str
    foreground: str
    border: str
    icon: str

    def __init__(self, row: dict[str, str]):
        self.__dict__ = row

    def render(self, size: tuple[int, int] = (64, 64)) -> Image.Image:
        badge = Image.new("RGBA", size)
        if self.background:
            with Image.open(f"{IMG_PATH}/{self.background}.png") as bg:
                bg = bg.resize(size, SAMPLING)
                badge.paste(bg)
        if self.border:
            with Image.open(f"{IMG_PATH}/{self.border}.png") as border:
                border = border.resize(size, SAMPLING)
                badge.paste(border, mask=border)
        if self.foreground:
            with Image.open(f"{IMG_PATH}/{self.foreground}.png") as fg:
                fg = fg.resize(size, SAMPLING)
                badge.paste(fg, mask=fg)
        if self.icon:
            icon_size = (size[0] // 3, size[1] // 3)
            pos = (size[0] - icon_size[0], size[1] - icon_size[1])
            with Image.open(f"{IMG_PATH}/{self.icon}.png") as icon:
                icon = icon.resize(icon_size, SAMPLING)
                badge.paste(icon, pos, mask=icon)
        return badge


if __name__=="__main__":
    badges: list[Badge] = []

    with open("data/badges.csv", encoding="utf-8") as file:
        for row in DictReader(file):
            badges.append(Badge(row))

    for badge in badges:
        print(badge.id, badge.name)
        img = badge.render()
        img = img.convert("RGB")
        img.save(f"{OUTPUT_PATH}/{badge.id}.png")
