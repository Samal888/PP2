import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()

# машина игрока
player = pygame.Rect(180, 500, 40, 60)

# враг
enemy = pygame.Rect(random.randint(0, 360), 0, 40, 60)
enemy_speed = 5

# монета
coin = pygame.Rect(random.randint(0, 360), -100, 20, 20)
coin_speed = 5
score = 0

font = pygame.font.Font(None, 36)

running = True

while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.x < WIDTH - 40:
        player.x += 5

    # движение врага
    enemy.y += enemy_speed
    if enemy.y > HEIGHT:
        enemy.y = -60
        enemy.x = random.randint(0, 360)

    # движение монеты
    coin.y += coin_speed
    if coin.y > HEIGHT:
        coin.y = -20
        coin.x = random.randint(0, 360)

    # столкновение с врагом
    if player.colliderect(enemy):
        print("GAME OVER")
        running = False

    # сбор монеты
    if player.colliderect(coin):
        score += 1
        coin.y = -20
        coin.x = random.randint(0, 360)

    # рисуем
    pygame.draw.rect(screen, (0, 255, 0), player)   # игрок
    pygame.draw.rect(screen, (255, 0, 0), enemy)    # враг
    pygame.draw.circle(screen, (255, 255, 0), coin.center, 10)  # монета

    # счет
    text = font.render(f"Coins: {score}", True, (255, 255, 255))
    screen.blit(text, (250, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()