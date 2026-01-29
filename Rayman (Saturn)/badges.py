from PIL import Image, ImageFilter
from csv import DictReader

IMG_PATH = "data/img"
OUTPUT_PATH = "output/badges"
SAMPLING = Image.Resampling.NEAREST

class Badge:
    id: int
    name: str
    background: str
    foreground: str
    border: str
    icon: str

    def __init__(self, row: dict[str, str]):
        self.__dict__ = row

    def resize(self, img: Image.Image, size: tuple[int, int]) -> Image.Image:
        if (img.size[0] < size[0]) and (img.size[1] < img.size[1]):
            sampling = Image.Resampling.NEAREST
        else:
            sampling = Image.Resampling.LANCZOS
        return img.resize(size, sampling)

    def render(self, size: tuple[int, int] = (64, 64)) -> Image.Image:
        badge = Image.new("RGBA", size)
        if self.background:
            with Image.open(f"{IMG_PATH}/{self.background}.png") as bg:
                bg = self.resize(bg, size).convert("RGB")
                if self.foreground:
                    bg = bg.filter(ImageFilter.BoxBlur(1))
                badge.paste(bg)
        if self.foreground:
            with Image.open(f"{IMG_PATH}/{self.foreground}.png") as fg:
                fg = self.resize(fg.convert("RGBA"), size)
                badge.paste(fg, mask=fg)
        if self.border:
            with Image.open(f"{IMG_PATH}/{self.border}.png") as border:
                border = self.resize(border, size)
                badge.paste(border, mask=border)
        if self.icon:
            with Image.open(f"{IMG_PATH}/{self.icon}.png") as icon:
                margin = 0
                # bottom left
                pos = (size[0] - icon.size[0] - margin, size[1] - icon.size[1] - margin)
                icon = icon.convert("RGBA")
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
