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

    def resize(self, img: Image.Image, size: tuple[int, int]) -> Image.Image:
        if ((img.size[0] < size[0]) and (img.size[1] < img.size[1])) or ((size[0] % img.size[0] == 0) and (size[1] % img.size[1] == 0)):
            sampling = Image.Resampling.NEAREST
        else:
            sampling = SAMPLING
        return img.resize(size, sampling)

    def render(self, size: tuple[int, int] = (64, 64)) -> Image.Image:
        badge = Image.new("RGBA", size)
        if self.background:
            with Image.open(f"{IMG_PATH}/{self.background}") as bg:
                bg = self.resize(bg, size).convert("RGBA")
                # bg = bg.filter(ImageFilter.GaussianBlur(0.5))
                if self.foreground:
                    bg = bg.filter(ImageFilter.GaussianBlur(0.5))
                badge.paste(bg)
        if self.foreground:
            with Image.open(f"{IMG_PATH}/{self.foreground}") as fg:
                if self.foreground.startswith("title_"):
                    fg = self.resize(fg.convert("RGBA"), (44,44))
                    pos = (10, 10)
                else:
                    fg = self.resize(fg.convert("RGBA"), size)
                    pos = (0, 0)
                badge.paste(fg, pos, mask=fg)
        if self.border:
            with Image.open(f"{IMG_PATH}/{self.border}") as border:
                border = self.resize(border, size).convert("RGBA")
                badge.paste(border, mask=border)
        if self.icon:
            with Image.open(f"{IMG_PATH}/{self.icon}") as icon:
                margin = 1
                # bottom left
                icon = self.resize(icon.convert("RGBA"), (24, 24))
                pos = (size[0] - icon.size[0] - margin, size[1] - icon.size[1] - margin)
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
