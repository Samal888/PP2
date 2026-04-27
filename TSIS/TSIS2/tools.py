import pygame
import collections
from datetime import datetime

# список инструментов (используются в основном файле)
PENCIL = "pencil"
LINE = "line"
RECTANGLE = "rectangle"
CIRCLE = "circle"
SQUARE = "square"
RIGHT_TRIANGLE = "right_triangle"
EQUILATERAL_TRIANGLE = "equilateral_triangle"
RHOMBUS = "rhombus"
ERASER = "eraser"
FILL = "fill"
TEXT = "text"
CLEAR = "clear"

# размеры кисти (толщина линий)
BRUSH_SIZES = {1: 2, 2: 5, 3: 10}


# рисование карандашом (соединяем предыдущую и текущую точки)
def draw_pencil(surface, prev_pos, curr_pos, color, size):
    if prev_pos:
        pygame.draw.line(surface, color, prev_pos, curr_pos, size)


# рисование прямоугольника
def draw_rectangle(surface, start, end, color, size):
    x = min(start[0], end[0])
    y = min(start[1], end[1])
    w = abs(end[0] - start[0])
    h = abs(end[1] - start[1])
    pygame.draw.rect(surface, color, (x, y, w, h), size)


# рисование круга
def draw_circle(surface, start, end, color, size):
    cx, cy = start
    # радиус = расстояние между начальной и конечной точкой
    radius = int(((end[0] - start[0])**2 + (end[1] - start[1])**2) ** 0.5)
    if radius > 0:
        pygame.draw.circle(surface, color, (cx, cy), radius, size)


# рисование квадрата
def draw_square(surface, start, end, color, size):
    side = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
    x = start[0] if end[0] >= start[0] else start[0] - side
    y = start[1] if end[1] >= start[1] else start[1] - side
    pygame.draw.rect(surface, color, (x, y, side, side), size)


# прямоугольный треугольник
def draw_right_triangle(surface, start, end, color, size):
    p1 = start
    p2 = (start[0], end[1])
    p3 = end
    pygame.draw.polygon(surface, color, [p1, p2, p3], size)


# равносторонний треугольник
def draw_equilateral_triangle(surface, start, end, color, size):
    x1, y1 = start
    x2, y2 = end
    mx = (x1 + x2) / 2
    height = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5 * (3**0.5) / 2
    p3 = (int(mx), int(min(y1, y2) - height))
    pygame.draw.polygon(surface, color, [start, end, p3], size)


# ромб по диагоналям
def draw_rhombus(surface, start, end, color, size):
    cx = (start[0] + end[0]) // 2
    cy = (start[1] + end[1]) // 2
    top = (cx, start[1])
    bottom = (cx, end[1])
    left = (start[0], cy)
    right = (end[0], cy)
    pygame.draw.polygon(surface, color, [top, right, bottom, left], size)


# заливка области (Flood Fill)
def flood_fill(surface, x, y, fill_color):
    # цвет пикселя, на который кликнули
    target_color = surface.get_at((x, y))[:3]

    # если уже тот же цвет — ничего не делаем
    if target_color == fill_color[:3]:
        return

    width, height = surface.get_size()

    # очередь для обхода (BFS)
    queue = collections.deque([(x, y)])
    visited = set([(x, y)])

    while queue:
        cx, cy = queue.popleft()

        # если цвет отличается — пропускаем
        if surface.get_at((cx, cy))[:3] != target_color:
            continue

        # закрашиваем пиксель
        surface.set_at((cx, cy), fill_color)

        # проверяем соседей (вверх, вниз, влево, вправо)
        for nx, ny in [(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)]:
            if 0 <= nx < width and 0 <= ny < height and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))


# сохранение canvas в файл
def save_canvas(surface):
    # создаём имя с текущим временем (чтобы не перезаписывать)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"canvas_{timestamp}.png"

    pygame.image.save(surface, filename)
    return filename