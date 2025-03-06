from maze import Maze
from maze.directions import directions
from maze.tiles import Wall_tile, Room_tile
from ui import graphics
from maze.pathfinder import Pathfinder


class Mouse:
    def __init__(self, x, y, dir = 0):
        self.x, self.y = x, y
        self.size = 1 / 20 # доля тайла, тайлы 1x1
        self.speed = 1 # тайлов в секунду
        self.dir = dir

    def draw(self):
        graphics.draw_circle("yellow", self.x, self.y, self.size)

    def update(self, delta_time):
        # Ничего не умеет вообще
        pass


# немного интеллекта
class Mouse2(Mouse):
    def __init__(self, x, y, dir=0):
        super().__init__(x, y, dir)
        self.x, self.y = x, y
        self.size = 1 / 20  # доля тайла, тайлы 1x1
        self.speed = 1  # тайлов в секунду
        self.dir = dir
        self.maze = Maze.Maze()

    def draw(self):
        graphics.draw_circle("yellow", self.x, self.y, self.size)

    def update(self, delta_time):
        cur_tile = self.maze.get_tile(self.x, self.y)
        dx, dy = directions[self.dir]
        
        # Двигаемся вперед
        self.x += dx * self.speed * delta_time
        self.y += dy * self.speed * delta_time
        
        # Проверка на стену
        next_tile = cur_tile.get_neighb_tile(self.dir)
        if cur_tile.dist_to_border(self.x, self.y, self.dir) < 0.2 and (
                next_tile is None or isinstance(next_tile, Wall_tile)):
            # Поворот по часовой стрелке (уменьшение направления)
            self.dir = (self.dir - 1) % 4  # <-- Изменено с +1 на -1

class SmartMouse(Mouse):
    def __init__(self, x, y, maze):
        super().__init__(x, y)
        self.path = []
        self.current_target = None
        self.search_cooldown = 0
        self.maze = maze
        self.base_speed = 1.0  # Базовая скорость
        self.speed = self.base_speed

    def increase_speed(self, percent=0.1):
        """Увеличить скорость на указанный процент"""
        self.speed = self.base_speed * (1 + percent)
        self.base_speed = self.speed  # Обновляем базовую скорость

    def update(self, delta_time):
        self.search_cooldown -= delta_time
        
        # Обновляем путь каждые 0.5 секунд
        if self.search_cooldown <= 0 and self.maze.cheese:
            start = (int(self.x), int(self.y))
            goal = (int(self.maze.cheese.x), int(self.maze.cheese.y))
            self.path = Pathfinder.find_path(start, goal, self.maze)
            self.search_cooldown = 0.5

        # Движение по пути
        if self.path:
            target_x, target_y = self.path[0]
            target_x += 0.5  # Центр тайла
            target_y += 0.5

            dx = target_x - self.x
            dy = target_y - self.y
            distance = (dx**2 + dy**2)**0.5

            if distance > 0.1:
                speed = self.speed * delta_time
                self.x += dx * speed / distance
                self.y += dy * speed / distance
            else:
                self.path.pop(0)





