from heapq import heappush, heappop
from maze.tiles import Wall_tile, Room_tile

class Pathfinder:
    @staticmethod
    def find_path(start, goal, maze):
        """Поиск пути от start=(x,y) до goal=(x,y) с использованием A*"""
        open_set = []
        heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: Pathfinder.heuristic(start, goal)}

        while open_set:
            current = heappop(open_set)[1]

            if current == goal:
                return Pathfinder.reconstruct_path(came_from, current)

            for neighbor in Pathfinder.get_neighbors(current, maze):
                tentative_g = g_score[current] + 1
                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + Pathfinder.heuristic(neighbor, goal)
                    heappush(open_set, (f, neighbor))
        return []

    @staticmethod
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    @staticmethod
    def get_neighbors(pos, maze):
        x, y = pos
        neighbors = []
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy
            tile = maze.get_tile(nx + 0.5, ny + 0.5)
            if tile and not isinstance(tile, Wall_tile):
                neighbors.append((nx, ny))
        return neighbors

    @staticmethod
    def reconstruct_path(came_from, current):
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        return path[::-1]
    
