import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

block = 20
snake = [(300, 300)]
dx, dy = 0, 0

def random_food():
    while True:
        x = random.randrange(0, WIDTH, block)
        y = random.randrange(0, HEIGHT, block)
        if (x, y) not in snake:
            return (x, y)

food = random_food()

score = 0
level = 1
speed = 5

font = pygame.font.Font(None, 36)

running = True

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -block
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, block
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -block, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = block, 0

    # движение
    head = (snake[0][0] + dx, snake[0][1] + dy)
    snake.insert(0, head)

    # еда
    if head == food:
        score += 1
        food = random_food()

        # уровень каждые 3 очка
        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    # столкновение со стенами
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        print("GAME OVER")
        running = False

    # столкновение с собой
    if head in snake[1:]:
        print("GAME OVER")
        running = False

    # рисуем змейку
    for s in snake:
        pygame.draw.rect(screen, (0, 255, 0), (s[0], s[1], block, block))

    # еда
    pygame.draw.rect(screen, (255, 0, 0), (food[0], food[1], block, block))

    # текст
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    level_text = font.render(f"Level: {level}", True, (255, 255, 255))

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()