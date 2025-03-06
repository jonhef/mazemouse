# maze/Maze.py
import settings
from maze.mice import SmartMouse
from maze.tiles import Room_tile, Wall_tile
from maze.cheese import Cheese
import random

class Maze:
    def __init__(self, width=8, height=6, spawn_cheese = True):
        self.mouse = None
        self.cheese = None
        self.width = width
        self.height = height
        self.generate_new()
        self.draw()
        self.spawn_cheese = spawn_cheese

    def _load_map(self):
        """Загрузка карты из файла."""
        with open(settings.map_file) as f:
            map_txt = f.readlines()
        for row, line in enumerate(map_txt):
            self.maze.append([])
            for column, tile_type in enumerate(line.strip()):
                if tile_type == "0":
                    self.maze[row].append(Room_tile(row, column, self))
                else:
                    self.maze[row].append(Wall_tile(row, column, self))
    
    @property
    def cheese_position(self):
        if self.cheese:
            return (self.cheese.x, self.cheese.y)
        return None
                    
    def check_cheese_collision(self):
        """Проверка столкновения мыши с сыром"""
        if self.cheese and self.mouse:
            distance = ((self.mouse.x - self.cheese.x)**2 + 
                       (self.mouse.y - self.cheese.y)**2)**0.5
            return distance < 0.4  # Радиус взаимодействия
        return False
                    
    def add_cheese(self, x, y):
        tile_x = int(x)
        tile_y = int(y)
        if self.get_tile(tile_x, tile_y).tile_type == "1":
            return
        if not self.cheese:  # Создаем новый сыр только если его нет
            self.cheese = Cheese(tile_x, tile_y)
        else:  # Перемещаем существующий
            self.cheese.x = tile_x + 0.5
            self.cheese.y = tile_y + 0.5

    def draw(self):
        """Отрисовка лабиринта и мыши."""
        for row in self.maze:
            for tile in row:
                tile.draw()
        if self.mouse:
            self.mouse.draw()
        if self.cheese:
            self.cheese.draw()
    
    def get_tile(self, x, y):
        """Получение тайла по координатам."""
        if 0 <= y < len(self.maze) and 0 <= x < len(self.maze[int(y)]):
            return self.maze[int(y)][int(x)]
        return None

    def update(self, delta_time):
        if self.mouse:
            self.mouse.update(delta_time)
            if self.check_cheese_collision():
                self.cheese = None  # Сыр исчезает
        if self.mouse and self.cheese:
            # Проверка столкновения
            distance = ((self.mouse.x - self.cheese.x)**2 +
                       (self.mouse.y - self.cheese.y)**2)**0.5
            if distance < 0.5:
                # Увеличиваем скорость и удаляем сыр
                self.mouse.increase_speed(0.2)  # +10%
                self.cheese = None
        if self.spawn_cheese and not self.cheese:
            self.spawn_random_cheese()

    def add_mouse(self, x, y):
        """Добавление мыши."""
        if self.get_tile(x, y).tile_type == "1":
            return
        self.mouse = SmartMouse(x, y, self)
        
    def generate_new(self):
        """Генерация нового лабиринта"""
        from maze.generator import MazeGenerator
        generated = MazeGenerator.generate(
            self.width, 
            self.height,
            wall_char="1",
            path_char="0"
        )
        self.maze = []
        for row_idx, row in enumerate(generated):
            self.maze.append([])
            for col_idx, cell in enumerate(row):
                if cell == "1":
                    self.maze[row_idx].append(Wall_tile(row_idx, col_idx, self))
                else:
                    self.maze[row_idx].append(Room_tile(row_idx, col_idx, self))
                    
    def get_free_cells(self):
        """Получить список координат свободных клеток (не стены, без сыра)"""
        free_cells = []
        for y in range(len(self.maze)):
            for x in range(len(self.maze[y])):
                if isinstance(self.maze[y][x], Room_tile):
                    # Проверяем, что здесь нет сыра
                    if self.cheese and (x == int(self.cheese.x) and y == int(self.cheese.y)):
                        continue
                    free_cells.append((x, y))
        return free_cells
    
    def spawn_random_cheese(self):
        """Создать сыр в случайной свободной клетке"""
        free_cells = self.get_free_cells()
        if free_cells:
            x, y = random.choice(free_cells)
            self.cheese = Cheese(x, y)
        else:
            self.cheese = None  # Если нет свободных клеток