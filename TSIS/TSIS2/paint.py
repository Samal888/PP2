import pygame
import sys
from tools import *

pygame.init()

# размеры окна
WIDTH, HEIGHT = 900, 600
TOOLBAR_WIDTH = 150

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# отдельная поверхность для рисования
canvas = pygame.Surface((WIDTH - TOOLBAR_WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

clock = pygame.time.Clock()

# шрифты
font = pygame.font.Font(None, 20)
font_big = pygame.font.Font(None, 30)

# базовые цвета
GRAY = (180, 180, 180)
DARK = (100, 100, 100)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# палитра цветов
COLORS = [BLACK, (255,0,0), (0,255,0), (0,0,255)]

# текущие настройки
current_tool = PENCIL
current_color = BLACK
brush_size_key = 1

drawing = False
start_pos = None
prev_pos = None

# для текста
text_mode = False
text_buffer = ""
text_pos = None

# список кнопок
tools_list = [
    (PENCIL, "Pencil"),
    (LINE, "Line"),
    (RECTANGLE, "Rect"),
    (CIRCLE, "Circle"),
    (SQUARE, "Square"),
    (RIGHT_TRIANGLE, "Tri"),
    (RHOMBUS, "Rhombus"),
    (FILL, "Fill"),
    (TEXT, "Text"),
    (ERASER, "Eraser"),
    (CLEAR, "Clear")
]


# рисуем панель инструментов слева
def draw_toolbar():
    pygame.draw.rect(screen, GRAY, (0,0,TOOLBAR_WIDTH, HEIGHT))

    y = 10
    for tool_id, name in tools_list:
        rect = pygame.Rect(10, y, 130, 30)
        color = BLUE if tool_id == current_tool else DARK
        pygame.draw.rect(screen, color, rect)

        text = font.render(name, True, WHITE)
        screen.blit(text, (rect.x+5, rect.y+5))
        y += 35

    # кнопки размера кисти
    y += 10
    for key in [1,2,3]:
        rect = pygame.Rect(10 + (key-1)*45, y, 40, 25)
        color = BLUE if key == brush_size_key else DARK
        pygame.draw.rect(screen, color, rect)
        t = font.render(str(key), True, WHITE)
        screen.blit(t, (rect.x+10, rect.y+5))

    # палитра цветов
    y += 40
    for i, c in enumerate(COLORS):
        rect = pygame.Rect(10 + i*30, y, 25, 25)
        pygame.draw.rect(screen, c, rect)


# перевод координат мыши в координаты canvas
def canvas_pos(pos):
    return (pos[0] - TOOLBAR_WIDTH, pos[1])


running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # обработка клавиатуры
        elif event.type == pygame.KEYDOWN:

            # смена размера кисти
            if event.key == pygame.K_1:
                brush_size_key = 1
            if event.key == pygame.K_2:
                brush_size_key = 2
            if event.key == pygame.K_3:
                brush_size_key = 3

            # сохранение Ctrl+S
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                save_canvas(canvas)

            # ввод текста
            if text_mode:
                if event.key == pygame.K_RETURN:
                    # подтверждение текста
                    text_surface = font_big.render(text_buffer, True, current_color)
                    canvas.blit(text_surface, text_pos)
                    text_mode = False
                    text_buffer = ""

                elif event.key == pygame.K_ESCAPE:
                    # отмена
                    text_mode = False
                    text_buffer = ""

                elif event.key == pygame.K_BACKSPACE:
                    text_buffer = text_buffer[:-1]

                else:
                    text_buffer += event.unicode

        # нажатие мыши
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos

            # если нажали на панель
            if x < TOOLBAR_WIDTH:
                ty = 10

                # выбор инструмента
                for tool_id, name in tools_list:
                    rect = pygame.Rect(10, ty, 130, 30)
                    if rect.collidepoint(event.pos):
                        if tool_id == CLEAR:
                            canvas.fill(WHITE)  # очистка экрана
                        else:
                            current_tool = tool_id
                        break
                    ty += 35

                # выбор размера кисти
                ty += 10
                for key in [1,2,3]:
                    rect = pygame.Rect(10 + (key-1)*45, ty, 40, 25)
                    if rect.collidepoint(event.pos):
                        brush_size_key = key

                # выбор цвета
                ty += 40
                for i,c in enumerate(COLORS):
                    rect = pygame.Rect(10 + i*30, ty, 25, 25)
                    if rect.collidepoint(event.pos):
                        current_color = c

            else:
                cp = canvas_pos(event.pos)

                if current_tool == FILL:
                    flood_fill(canvas, cp[0], cp[1], current_color)

                elif current_tool == TEXT:
                    text_mode = True
                    text_pos = cp
                    text_buffer = ""

                else:
                    drawing = True
                    start_pos = cp
                    prev_pos = cp

        # отпускание мыши
        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                cp = canvas_pos(event.pos)
                size = BRUSH_SIZES[brush_size_key]

                # рисуем фигуры
                if current_tool == LINE:
                    pygame.draw.line(canvas, current_color, start_pos, cp, size)
                elif current_tool == RECTANGLE:
                    draw_rectangle(canvas, start_pos, cp, current_color, size)
                elif current_tool == CIRCLE:
                    draw_circle(canvas, start_pos, cp, current_color, size)
                elif current_tool == SQUARE:
                    draw_square(canvas, start_pos, cp, current_color, size)
                elif current_tool == RIGHT_TRIANGLE:
                    draw_right_triangle(canvas, start_pos, cp, current_color, size)
                elif current_tool == RHOMBUS:
                    draw_rhombus(canvas, start_pos, cp, current_color, size)

            drawing = False

        # движение мыши
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                cp = canvas_pos(event.pos)
                size = BRUSH_SIZES[brush_size_key]

                if current_tool == PENCIL:
                    draw_pencil(canvas, prev_pos, cp, current_color, size)
                    prev_pos = cp

                elif current_tool == ERASER:
                    pygame.draw.circle(canvas, WHITE, cp, size*2)

    # отрисовка
    screen.fill(WHITE)
    screen.blit(canvas, (TOOLBAR_WIDTH, 0))
    draw_toolbar()

    # отображение текста во время ввода
    if text_mode and text_pos:
        preview = font_big.render(text_buffer + "|", True, current_color)
        screen.blit(preview, (text_pos[0]+TOOLBAR_WIDTH, text_pos[1]))

    pygame.display.flip()

pygame.quit()
sys.exit()