import pygame
import random

pygame.init()

s_width = 500
s_height = 500
clock = pygame.time.Clock()
game_over = False

screen = pygame.display.set_mode((s_width, s_height))

GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (181, 181, 181)

y1 = 0
x1 = 0
x1_change = 0
y1_change = 0
score = 0


class Snake:
    # First three block of snake's body
    snake_body = [[0, 0], [25, 0], [50, 0]]
    default_x = 0
    default_y = 0

    def __init__(self, snake_block, snake_speed):
        self.snake_block = snake_block
        self.snake_speed = snake_speed


class Food:
    foodx = round(random.randrange(0, s_width - 25) / 25.0) * 25.0
    foody = round(random.randrange(0, s_height - 25) / 25.0) * 25.0
    def food_providing(self):
        pygame.draw.rect(screen, RED, [self.foodx, self.foody, 25, 25])


def check_border(x, y):
    if(x >= 0 and y >= 0):
        if(x+25 <= s_width and y+25 <= s_height):
            return False
    return True


count = 0

# Initialize the snake
snake = Snake(snake_block=25, snake_speed=10)
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
        for j in range(0, int(s_width/snake.snake_block), 2):
            pygame.draw.rect(
                screen, GRAY, [j*25, i, snake.snake_block, snake.snake_block])

    for i in range(25, s_width, 50):
        for j in range(1, int(s_width/snake.snake_block), 2):
            pygame.draw.rect(
                screen, GRAY, [j*25, i, snake.snake_block, snake.snake_block])



    pygame.display.update()
    clock.tick(snake.snake_speed)

pygame.quit()
