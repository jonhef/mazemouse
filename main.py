# main.py
import pygame
import settings
from maze.Maze import Maze  # Импорт класса
from ui import events, graphics

def main():
    pygame.init()
    clock = events.Clock()
    FPS = 60
    
    screen = pygame.display.set_mode(settings.window_size)
    pygame.display.set_caption("Maze Mouse")
    clock = pygame.time.Clock()
    
    maze_width = settings.width
    maze_height = settings.height
    maze = Maze(maze_width, maze_height)

    running = True
    while running:
        delta_time = clock.tick(FPS) / 1000.0

        # Обработка событий
        for event in events.get_event_queue():
            if event.type == events.QUIT:
                running = False
            elif event.type == events.MOUSEBUTTONDOWN and event.button == 1:
                screen_x, screen_y = event.pos
                maze_x = (screen_x - settings.view_left_top[0]) / settings.tile_size[0]
                maze_y = (screen_y - settings.view_left_top[1]) / settings.tile_size[1]
                maze.add_mouse(maze_x, maze_y)  # Вызов метода экземпляра
            elif event.type == events.MOUSEBUTTONDOWN:
                if event.button == 3:  # Правая кнопка
                    screen_x, screen_y = event.pos
                    maze_x = (screen_x - settings.view_left_top[0]) / settings.tile_size[0]
                    maze_y = (screen_y - settings.view_left_top[1]) / settings.tile_size[1]
                    maze.add_cheese(maze_x, maze_y)  # Будет только один сыр

        # Обновление и отрисовка
        maze.update(delta_time)
        screen.fill((0, 0, 0))
        maze.draw()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()