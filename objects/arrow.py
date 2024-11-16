from PIL import ImageDraw
import math

from .box import Box

class Arrow:
    def __init__(self, start_box: Box, end_box: Box):
        self.start_box = start_box
        self.end_box = end_box
        self.start_x, self.start_y, _, _ = self.start_box.get_coordinates()
        self.end_x, self.end_y, _, _ = self.end_box.get_coordinates()

    def draw(self, draw_obj: ImageDraw.ImageDraw):
        dx = self.end_x - self.start_x
        dy = self.end_y - self.start_y
        length = math.sqrt(dx ** 2 + dy ** 2)
        reduced_length = length * 0.72

        scale = reduced_length / length

        new_end_x = self.start_x + dx * scale
        new_end_y = self.start_y + dy * scale

        new_start_x = self.start_x + dx * (1 - scale)
        new_start_y = self.start_y + dy * (1 - scale)

        draw_obj.line([new_start_x + self.start_box.width / 2, new_start_y + self.start_box.height / 2,
                    new_end_x + self.end_box.width / 2, new_end_y + self.end_box.height / 2], fill="black", width=2)

        angle = math.atan2(new_end_y - new_start_y, new_end_x - new_start_x)
        arrow_length = 10
        arrow_angle = math.pi / 6
        draw_obj.line([new_end_x + self.end_box.width / 2, new_end_y + self.end_box.height / 2,
                    new_end_x + self.end_box.width / 2 - arrow_length * math.cos(angle - arrow_angle),
                    new_end_y + self.end_box.height / 2 - arrow_length * math.sin(angle - arrow_angle)], fill="black", width=2)
        draw_obj.line([new_end_x + self.end_box.width / 2, new_end_y + self.end_box.height / 2,
                    new_end_x + self.end_box.width / 2 - arrow_length * math.cos(angle + arrow_angle),
                    new_end_y + self.end_box.height / 2 - arrow_length * math.sin(angle + arrow_angle)], fill="black", width=2)