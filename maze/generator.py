import random
from maze.directions import directions

class MazeGenerator:
    @staticmethod
    def generate(width, height, wall_char="1", path_char="0"):
        """Генерация лабиринта с клетками-стенами"""
        # Инициализация сетки (все клетки - стены)
        maze = [[wall_char for _ in range(width)] for _ in range(height)]
        
        # Начальная точка (чётные координаты)
        start_x = random.randrange(1, width-1, 2)
        start_y = random.randrange(1, height-1, 2)
        maze[start_y][start_x] = path_char
        
        # Список граничных стен
        walls = MazeGenerator._get_neighbor_walls(start_x, start_y, maze)
        
        while walls:
            # Выбираем случайную граничную стену
            wall = random.choice(walls)
            walls.remove(wall)
            wx, wy = wall
            
            # Находим смежные проходы
            paths = MazeGenerator._find_adjacent_paths(wx, wy, maze)
            
            if len(paths) == 1:
                # Превращаем стену в проход
                maze[wy][wx] = path_char
                # Добавляем новые граничные стены
                walls += MazeGenerator._get_neighbor_walls(wx, wy, maze)
        
        # Устанавливаем вход и выход
        # maze[1][0] = path_char
        # maze[height-2][width-1] = path_char
        
        return maze

    @staticmethod
    def _get_neighbor_walls(x, y, maze):
        """Получить соседние стены"""
        neighbors = []
        for dx, dy in directions:
            nx = x + dx*2
            ny = y + dy*2
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze):
                if maze[ny][nx] == "1":
                    neighbors.append((x+dx, y+dy))
        return neighbors

    @staticmethod
    def _find_adjacent_paths(x, y, maze):
        """Найти соседние проходы"""
        paths = []
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze):
                if maze[ny][nx] == "0":
                    paths.append((nx, ny))
        return paths