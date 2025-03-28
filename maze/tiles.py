import maze.Maze
from maze import Maze
from maze.directions import directions
from ui import graphics


class Tile:
    def __init__(self, tile_type, row, column, maze):
        self.tile_type = tile_type
        self.row = row
        self.column = column
        self.maze = maze

    def draw(self):
       pass

    def get_neighb_tile(self, dir_n):
        dx, dy = directions[dir_n]
        return self.maze.get_tile(self.column + 0.5 + dx, self.row + 0.5 + dy)

    def dist_to_border(self, x, y, dir_n):
        x -= int(x)
        y -= int(y)
        if dir_n == 0:
            return 1 - x
        elif dir_n == 1:
            return y
        elif dir_n == 2:
            return x
        return 1 - y


class Wall_tile(Tile):
    def __init__(self, row, column, maze):
        super().__init__("1", row, column, maze)
        self.image = graphics.load_image("images/wall.png", size=(1, 1))  # Указан размер

    def draw(self):
        graphics.draw_image(self.image, self.column, self.row)  # x=column, y=row


class Room_tile(Tile):
    def __init__(self, row, column, maze):
        super().__init__("0", row, column, maze)

# пустая комната не нуждается в рисовании
