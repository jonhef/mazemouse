## mazemouse

### guide
1. install python 3.8.x
2. create virtual environment
```
# MacOS/Linux
python3 -m venv .venv
source .venv/bin/activate
# Windows
python -m venv .venv
.venv\Scripts\activate
```
3. install dependencies
```
# MacOS/Linux
pip3 install -r requirements.txt
# Windows
pip install -r requirements.txt
```
4. run using python
```
# MacOS/Linux
python3 main.py
# Windows 
python main.py
```

#### maze
`maze/cheese.py`
- `class Cheese` – class for cheese(now using as a way to draw with function `draw`)

`maze/directions.py` - returns all possible directions

`maze/generator.py`
- `class MazeGenerator` – the generator of maze using the Prim's algorithm
- `MazeGenerator.generate()` – generates a maze

`maze/Maze.py` – file with the maze class
- `class Maze(width = 8: int, height = 6: int,  spawn_cheese = True: bool)` – class for maze
    - `Maze().draw()` – drawing the maze
    - `Maze().cheese_position` – cheese's position
    - `Maze().check_cheese_collision()` – check for colission mouse and cheese
    - `Maze().add_cheese(x: float, y: float)` – add cheese to maze
    - `Maze().get_tile(x: float, y: float)`– returns tile by coordinates
    - `Maze().update(delta_time: float)` – updating maze(check for collisions and spawn cheese)
    - `Maze().add_mouse(x: float | int, y: float | int)` – add mouse to maze at given coordinates
    - `Maze().generate_new()` – generate new maze with set height and width
    - `Maze().get_free_cells()` – returns list of tiles without walls or cheese
    - `Maze().spawn_random_cheese()` – spawns cheese with random coordinates at free cell

`maze/mice.py` – all classes for mice
- `Mouse(x: float, y: float, dir: int)` – mouse class
    - `Mouse().draw()` – draws mouse
    - `Mouse().update(delta_time: float)` – updates mouse
- `Mouse2(x: float, y: float, dir: int) : Mouse`
    - `Mouse2().maze` – mouse's maze 
- `SmartMouse(x: float, y: float, maze: Maze)` – mouse with intelligence
    - `SmartMouse().increase_speed(percent: float)` – increases mouse's speed

`maze/pathfinder.py`
- `class Pathfinder` – generates methods for searching paths
    - `Pathfinder.find_path(start: tuple, goal: tuple, maze: Maze)` – finds path from start to goal
    - `Pathfinder.heuristic(a: tuple, b: tuple)` – heuristic function
    - `Pathfinder.get_neighbors(pos: tuple, maze: Maze)` – returns list of neighbors
    - `Pathfinder.reconstruct_path(came_from: dict, current: tuple)` – reconstructs path
`maze/tiles.py`
- `class Tile` – base class for tiles
    - `Tile().draw()` – draws tile
    - `Tile().get_neighb_tile(dir_n: int)` – returns tile by direction
    - `Tile().dist_to_border(x: float, y: float, dir_n: int)` – returns distance to border
- `class Wall_tile(Tile) : Tile` – class for wall tiles
- `class Room_tile(Tile) : Tile` – class for room tiles

#### ui
`ui/events.py` - module for some defines
`ui/graphics.py` - module for drawing
- `fill(color: str)` – fills screen with color
- `load_image(path: str, size: tuple = (1, 1))` – loads image from file
- `draw_image(image: pygame.Surface, x: float, y: float)` – draws image
- `draw_circle(color: str, x: float, y: float, r: float)` – draws circle

#### main.py
- `main()` – main function

#### settings.py
- `tile_size: tuple[int, int]` – size of tile in terms of width and height
- `view_left_top: tuple[int, int]` – margin of view(left and top)
- `window_size: tuple[int, int]` – size of window in terms of width and height