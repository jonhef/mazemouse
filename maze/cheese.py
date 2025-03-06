from ui import graphics

class Cheese:
    def __init__(self, x, y):
        self.x = x + 0.5  # Центр тайла
        self.y = y + 0.5
        self.image = graphics.load_image("images/cheese.png", size=(0.8, 0.8))

    def draw(self):
        graphics.draw_image(self.image, self.x - 0.4, self.y - 0.4)