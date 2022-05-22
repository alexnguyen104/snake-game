import pygame
import random

pygame.init()

s_width = 500
s_height = 500
clock = pygame.time.Clock()
game_over = False

screen = pygame.display.set_mode((s_width, s_height))

GREEN = (0, 255, 0)
DARK_GREEN = (3, 110, 1)
RED = (255, 0, 0)
GRAY = (181, 181, 181)

y1 = 0
x1 = 0
x1_change = 0
y1_change = 0
score = 0


class Snake:
    # First three block of snake's body
    default_x = 0
    default_y = 0

    def __init__(self, body, block, speed):
        self.body = body
        self.block = block
        self.speed = speed
        self.direction = "left"

    def draw_snake(self):
        # Draw head of the snake
        snake_head = self.body[-1]
        pygame.draw.rect(screen, DARK_GREEN, [snake_head[0], snake_head[1], self.block, self.block])
        # Draw body of the snake
        for i in range(len(self.body) - 1):
            pygame.draw.rect(screen, GREEN, [self.body[i][0], self.body[i][1], self.block, self.block])


class Food:
    foodx = round(random.randrange(0, s_width - 25) / 25.0) * 25.0
    foody = round(random.randrange(0, s_height - 25) / 25.0) * 25.0
    def food_providing(self):
        pygame.draw.rect(screen, RED, [self.foodx, self.foody, 25, 25])


def check_border(x, y, block):
    if(x >= 0 and y >= 0):
        if(x + block <= s_width and y + block <= s_height):
            return False
    return True


count = 0

# Initialize the snake
block_default = 25
snake = Snake(body = [[block_default * 3, s_height / 2], [block_default * 4, s_height / 2], [block_default * 5, s_height / 2]],block = block_default, speed = 10)
# Initialize the food
food = Food()

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            count += 1
            if event.key == pygame.K_LEFT:
                x1_change = -25
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 25
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -25
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 25
                x1_change = 0

    x1 += x1_change
    y1 += y1_change
    screen.fill([255, 255, 255])

    # Draw the map
    for i in range(0, s_width, 50):
        for j in range(0, int(s_width/snake.block), 2):
            pygame.draw.rect(
                screen, GRAY, [j*25, i, snake.block, snake.block])

    for i in range(25, s_width, 50):
        for j in range(1, int(s_width/snake.block), 2):
            pygame.draw.rect(
                screen, GRAY, [j*25, i, snake.block, snake.block])

    # Draw the snake
    snake.draw_snake()

    pygame.display.update()
    clock.tick(snake.speed)

pygame.quit()
