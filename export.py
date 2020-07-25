import cairosvg
from PIL import Image, ImageDraw
import random


class Export:
    def png(self, tree):
        self.img = Image.new("RGB", (1920, 1080), (255, 255, 255))
        self.draw = ImageDraw.Draw(self.img)
        for i in tree:
            color = "#afafaf" if i.level > i.treeconfig.levels * \
                .75 and i.level != i.treeconfig.levels else "#000000"

            self.draw.line([(int(i.old_x), int(i.old_y)), (int(i.new_x), int(i.new_y))],
                           fill=color, width=int(i.twig_width), joint='curve')
        self.img.save(f'teste_pil_{random.randint(0, 9999)}.png')

    def svg(self, tree):
        file_name = f'./export/teste_pil_{random.randint(0, 9999)}.svg'
        svg = open(file_name, "a")
        svg.write(
            "<svg viewBox='0 0 1920 1080' xmlns='http://www.w3.org/2000/svg'>")
        svg.write(
            f"<polygon points='0,0 1920,0 1920,1080 0,1080' fill='#e8efef' />")
        for i in tree:
            color = "#afafaf" if i.level > i.treeconfig.levels * \
                .75 and i.level != i.treeconfig.levels else "#000000"
            svg.write(
                f"<line x1='{int(i.old_x)}' y1='{int(i.old_y)}' x2='{int(i.new_x)}' y2='{int(i.new_y)}' stroke='{color}' stroke-linecap='round' stroke-width='{int(i.twig_width)}' />")
        svg.write(
            f"<polygon points='0,900 1920,900 1920,1080 0,1080' fill='#000000' />")
        svg.write("</svg>")
        svg.close()
        cairosvg.svg2png(url=file_name, write_to=f"{file_name}.png", scale=2)
