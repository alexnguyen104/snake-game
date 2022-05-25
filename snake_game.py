import pygame
import random

pygame.init()

s_width = 500
s_height = 500
clock = pygame.time.Clock()
game_over = False

screen = pygame.display.set_mode((s_width, s_height))

GREEN = (119, 221, 119)
DARK_GREEN = (92, 181, 92)
RED = (255, 0, 0)
GRAY = (181, 181, 181)
LIGHT_RED = (255, 197, 191)
DARK_RED = (255, 174, 165)
ORANGE = (255, 202, 162)
PURPLE = (203, 170, 203)

class Snake:
    def __init__(self, body, block, speed):
        self.body = body
        self.block = block
        self.speed = speed
        self.x = body[-1][0]
        self.y = body[-1][1]
        self.is_stop = True
        self.direction = None
        self.score = 0

    def draw_snake(self, new_x, new_y):
        # Start to move when the keyboard is pressed for the first time
        if(not self.is_stop):
            self.body.append([new_x, new_y])
            del self.body[0]
            
        # Draw head of the snake
        snake_head = self.body[-1]
        pygame.draw.rect(screen, DARK_GREEN, [snake_head[0], snake_head[1], self.block, self.block])

        # Draw body of the snake
        for i in range(len(self.body) - 1):
            pygame.draw.rect(screen, GREEN, [self.body[i][0], self.body[i][1], self.block, self.block])

    def check_border(self):
        if(self.x >= 0 and self.y >= 0):
            if(self.x + self.block <= s_width and self.y + self.block <= s_height):
                return False
        return True

class Food:
    def __init__(self, block):
        self.x = round(random.randrange(0, s_width - block) / block) * block
        self.y = round(random.randrange(0, s_height - block) / block) * block  
        self.block = block

    def providing(self, snake_body, snake_is_stop):
        # Check if food is spawned on snake's default position
        for i in range(len(snake_body)):
            while(snake_is_stop and [self.x, self.y] == snake_body[i]):
                self.x = round(random.randrange(0, s_width - self.block) / self.block) * self.block
                self.y = round(random.randrange(0, s_height - self.block) / self.block) * self.block  
    
        pygame.draw.rect(screen, RED, [self.x, self.y, self.block, self.block])
    
    def is_eaten(self,snake_x, snake_y):
        return [self.x, self.y] == [snake_x, snake_y]
            
def lose_game(score):
    # Let the function know that game_over is a global variable
    global game_over
    print("You are lose!!!")
    print("Your score is: " + str(score))
    game_over = True

# Initialize the snake
block_default = 25
snake = Snake(body = [[block_default * 3, s_height / 2], [block_default * 4, s_height / 2], [block_default * 5, s_height / 2]],block = block_default, speed = 10)
s_x_change = 0
s_y_change = 0

# Initialize the food
food = Food(snake.block)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if(event.key != pygame.K_LEFT):
                snake.is_stop = False
            if(not snake.is_stop):
                if event.key == pygame.K_LEFT and snake.direction != "right" and snake.direction != "left":
                    snake.direction = "left"
                    s_x_change -= snake.block
                    s_y_change = 0
                elif event.key == pygame.K_RIGHT and snake.direction != "left" and snake.direction != "right":
                    snake.direction = "right"
                    s_x_change += snake.block
                    s_y_change  = 0
                elif event.key == pygame.K_UP and snake.direction != "down" and snake.direction != "up":
                    snake.direction = "up"
                    s_y_change -= snake.block
                    s_x_change = 0
                elif event.key == pygame.K_DOWN and snake.direction != "up" and snake.direction != "down":
                    snake.direction = "down"
                    s_y_change += snake.block
                    s_x_change = 0

    snake.x += s_x_change
    snake.y += s_y_change

    # Set color of background
    screen.fill(LIGHT_RED)

    # Draw the map's patterns
    for i in range(0, s_width, 50):
        for j in range(0, int(s_width/snake.block), 2):
            pygame.draw.rect(
                screen, DARK_RED, [j*25, i, snake.block, snake.block])

    for i in range(25, s_width, 50):
        for j in range(1, int(s_width/snake.block), 2):
            pygame.draw.rect(
                screen, DARK_RED, [j*25, i, snake.block, snake.block])

    # Draw the snake
    snake.draw_snake(snake.x, snake.y)

    # Draw the food
    food.providing(snake.body, snake.is_stop)

    # Check if the snake eats food
    if food.is_eaten(snake.x, snake.y):
        snake.score += 1
        # Set x and y of food again to change its position
        food.x = round(random.randrange(0, s_width - snake.block) / snake.block) * snake.block
        food.y = round(random.randrange(0, s_height - snake.block) / snake.block) * snake.block  
    
    # Check if the snake have touched borders
    if snake.check_border():
        lose_game(snake.score)

    # Update changes and set snake's speed
    pygame.display.update()
    clock.tick(snake.speed)

pygame.quit()
