import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

radius = 10
mode = "draw"
color = (0, 0, 255)

points = []
start_pos = None

# холст (чтобы можно было очищать)
canvas = pygame.Surface((800, 600))
canvas.fill((255, 255, 255))

# палитра
colors = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 165, 0), (255, 255, 255),
    (0, 0, 0)
]

color_rects = []
for i, c in enumerate(colors):
    rect = pygame.Rect(10 + i*50, 10, 40, 40)
    color_rects.append((rect, c))

# кнопка очистки
clear_rect = pygame.Rect(10, 60, 100, 40)
font = pygame.font.Font(None, 30)


def drawLine(surface, points, width, color):
    for i in range(len(points) - 1):
        pygame.draw.line(surface, color, points[i], points[i + 1], width)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_d:
                mode = "draw"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_s:
                mode = "rect"

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # палитра
                for rect, c in color_rects:
                    if rect.collidepoint(event.pos):
                        color = c

                # кнопка очистки
                if clear_rect.collidepoint(event.pos):
                    canvas.fill((255, 255, 255))
                    points = []

                start_pos = event.pos

            if event.button == 3:
                radius = max(1, radius - 2)

        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            if mode == "circle":
                pygame.draw.circle(canvas, color, start_pos, 50)
            elif mode == "rect":
                rect = pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                pygame.draw.rect(canvas, color, rect)

        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                if mode == "draw":
                    points.append(event.pos)
                    points = points[-100:]
                elif mode == "eraser":
                    pygame.draw.circle(canvas, (255, 255, 255), event.pos, radius)

    if mode == "draw":
        drawLine(canvas, points, radius, color)

    # рисуем холст
    screen.blit(canvas, (0, 0))

    # палитра
    for rect, c in color_rects:
        pygame.draw.rect(screen, c, rect)

    # кнопка Clear
    pygame.draw.rect(screen, (200, 200, 200), clear_rect)
    text = font.render("Clear", True, (0, 0, 0))
    screen.blit(text, (clear_rect.x + 15, clear_rect.y + 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()