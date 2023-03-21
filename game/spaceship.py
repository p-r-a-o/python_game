import pygame
import sys
from random import randint

# 초기 설정
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("간단한 슈팅 게임")
clock = pygame.time.Clock()

# 색상 정의
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 우주선 설정
ship_width, ship_height = 40, 40
ship_x, ship_y = (WIDTH - ship_width) // 2, HEIGHT - ship_height - 10
ship_speed = 5

# 미사일 설정
missile_width, missile_height = 5, 10
missiles = []

# 외계인 설정
alien_width, alien_height = 40, 40
aliens = []
alien_spawn_time = 1000
pygame.time.set_timer(pygame.USEREVENT, alien_spawn_time)

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                missile_x, missile_y = ship_x + ship_width // 2 - missile_width // 2, ship_y
                missiles.append([missile_x, missile_y])
        if event.type == pygame.USEREVENT:
            alien_x, alien_y = randint(0, WIDTH - alien_width), 0
            aliens.append([alien_x, alien_y])

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ship_x > 0:
        ship_x -= ship_speed
    if keys[pygame.K_RIGHT] and ship_x < WIDTH - ship_width:
        ship_x += ship_speed

    # 미사일 이동
    for missile in missiles:
        missile[1] -= 10

    # 외계인 이동
    for alien in aliens:
        alien[1] += 5

    # 충돌 처리
    for alien in aliens:
        if alien[1] + alien_height > HEIGHT:
            aliens.remove(alien)
        for missile in missiles:
            if (alien[0] < missile[0] < alien[0] + alien_width or alien[0] < missile[0] + missile_width < alien[
                0] + alien_width) \
                    and (
                    alien[1] < missile[1] < alien[1] + alien_height or alien[1] < missile[1] + missile_height < alien[
                1] + alien_height):
                aliens.remove(alien)
                missiles.remove(missile)
                break

    # 화면 그리기
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (ship_x, ship_y, ship_width, ship_height))

    for missile in missiles:
        pygame.draw.rect(screen, RED, (missile[0], missile[1], missile_width, missile_height))

    for alien in aliens:
        pygame.draw.rect(screen, RED, (alien[0], alien[1], alien_width, alien_height))

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)
