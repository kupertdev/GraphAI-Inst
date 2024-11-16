from typing import List
from PIL import Image, ImageDraw

from .box import Box
from .arrow import Arrow

class Graph:
    def __init__(self):
        self.boxes: List[Box] = []
        self.arrows: List[Arrow] = []
        self.image = None
        self.draw_obj = None

    def add_box(self, obj: str, x: int, y: int, text: str):
        box = Box(obj, x, y, text)
        self.boxes.append(box)

    def add_arrow(self, box1: Box, box2: Box):
        arrow = Arrow(box1, box2)
        self.arrows.append(arrow)

    def create_image(self):
        max_x = max([box.x + box.width for box in self.boxes])
        max_y = max([box.y + box.height for box in self.boxes])
        
        padding_x = 50
        padding_y = 50

        self.image = Image.new("RGB", (int(max_x + padding_x), int(max_y + padding_y)), "white")
        self.draw_obj = ImageDraw.Draw(self.image)

        for box in self.boxes:
            box.draw(self.draw_obj)

        for arrow in self.arrows:
            arrow.draw(self.draw_obj)

    def show_image(self):
        if self.image:
            self.image.show()

    def save_image(self, path: str):
        if self.image:
            self.image.save(path)