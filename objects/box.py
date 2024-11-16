from PIL import ImageDraw, ImageFont

class Box:
    def __init__(self, obj: str, x: int, y: int, text: str, width: int = 120, padding: int = 10):
        self.obj = obj
        self.x = x
        self.y = y
        self.text = text
        self.width = width
        self.padding = padding
        self.lines = []
        self.height = 0
        self.font = ImageFont.truetype("arial.ttf", 16)
        self.calculate_box()

    def calculate_box(self):
        max_line_width = self.width - 2 * self.padding
        words = self.text.split(' ')
        current_line = ""
        self.lines = []

        for word in words:
            test_line = f"{current_line} {word}".strip()
            text_width = self.font.getlength(test_line)
            if text_width <= max_line_width:
                current_line = test_line
            else:
                self.lines.append(current_line)
                current_line = word

        if current_line:
            self.lines.append(current_line)

        for line in self.lines:
            line_width = self.font.getlength(line)
            if line_width + 2 * self.padding > self.width:
                self.width = line_width + 2 * self.padding

        line_height = self.font.getbbox("A")[3]
        self.height = len(self.lines) * line_height + 2 * self.padding

        self.x = self.x - (self.width - max_line_width) / 2

    def draw(self, draw_obj: ImageDraw.ImageDraw):
        draw_obj.rectangle([self.x, self.y, self.x + self.width, self.y + self.height], outline="black", width=2)

        current_y = self.y + self.padding
        for line in self.lines:
            text_width = self.font.getlength(line)
            text_x = self.x + (self.width - text_width) / 2
            draw_obj.text((text_x, current_y), line, fill="black", font=self.font)
            current_y += self.font.getbbox(line)[3]

    def get_coordinates(self):
        return self.x, self.y, self.width, self.height