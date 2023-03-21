import pygame
import sys

# 초기 설정
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("벽돌깨기 게임")
clock = pygame.time.Clock()

# 색상 정의
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# 패들 설정
paddle_width, paddle_height = 100, 10
paddle_x, paddle_y = (WIDTH - paddle_width) // 2, HEIGHT - paddle_height - 10
paddle_speed = 10

# 공 설정
ball_radius = 10
ball_speed_x, ball_speed_y = 10, -10
ball_x, ball_y = WIDTH // 2, HEIGHT // 2

# 벽돌 설정
brick_rows, brick_cols = 5, 10
brick_width, brick_height = 75, 20
brick_margin = 2
brick_top = 50
bricks = []

for i in range(brick_rows):
    for j in range(brick_cols):
        brick = pygame.Rect(j * (brick_width + brick_margin), brick_top + i * (brick_height + brick_margin), brick_width, brick_height)
        bricks.append(brick)

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed

    # 공 이동
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 공의 벽 충돌 처리
    if ball_x < 0 or ball_x > WIDTH - ball_radius:
        ball_speed_x = -ball_speed_x
    if ball_y < 0:
        ball_speed_y = -ball_speed_y
    if ball_y > HEIGHT - ball_radius:
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2

    # 패들과 공 충돌 처리
    paddle = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    if paddle.colliderect(ball_x, ball_y, ball_radius, ball_radius):
        ball_speed_y = -ball_speed_y

    # 벽돌과 공 충돌 처리
    for brick in bricks:
        if brick.colliderect(ball_x, ball_y, ball_radius, ball_radius):
            ball_speed_y = -ball_speed_y
            bricks.remove(brick)
            break

    # 화면 그리기
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    for brick in bricks:
        pygame.draw.rect(screen, BLUE, brick)

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)