import pygame
import random
pygame.init()

# Colours from google
'''black = (0, 0, 0) gray = (127, 127, 127) white = (255, 255, 255)
red = (255, 0, 0) green = (0, 255, 0) blue = (0, 0, 255)
yellow = (255, 255, 0) cyan = (0, 255, 255) magenta = (255, 0, 255)'''

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)
orange = (255, 100, 10)
blue = (0, 0, 255)

# creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# game title
pygame.display.set_caption("Snakes")
pygame.display.update()


clock = pygame.time.Clock()  # create an object to help track time in short FPS mate
font = pygame.font.SysFont(None, 55)


def text_screen(text, colour, x, y):
    screen_text = font.render(text, True, colour)  # no idea
    gameWindow.blit(screen_text, [x, y])  # update the score


def plot_snake(gameWindow, colour, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, black, [x, y, snake_size, snake_size])

# game loop and event handling:


def game_loop():
    # game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0  # initial value apvi padse
    velocity_y = 0
    snk_list = []
    snk_length = 1
    init_valocity = 5
    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20, screen_height/2)
    score = 0
    snake_size = 30
    fps = 60
    while not exit_game:
        if game_over:
            gameWindow.fill(green)
            text_screen("Game Over! Please Enter To Continue",
                        red,100,250)
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    exit_game = True

                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_RETURN:
                        game_loop()



        else:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    exit_game = True

                if events.type == pygame.KEYDOWN:  # if you pressed any key...
                    if events.key == pygame.K_RIGHT:  # if pressed key is right arrow key....
                        velocity_x = init_valocity  # snake will move in x direction with initial velocity
                        velocity_y = 0  # naitar diagonal ma bhagse if you dont write this line!!!!!

                    if events.key == pygame.K_LEFT:
                        velocity_x = -init_valocity
                        velocity_y = 0

                    if events.key == pygame.K_UP:
                        # pygame exception------> up y direction minus dhareli che....
                        velocity_y = -init_valocity
                        velocity_x = 0

                    if events.key == pygame.K_DOWN:
                        velocity_y = init_valocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
                score = score + 1
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                snk_length = snk_length + 5

            gameWindow.fill(green)
            text_screen("score: " + str(score * 10), blue, 5, 5)
            pygame.draw.rect(gameWindow, red, [
                food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:#all element expect last one etle k head vagar na jetla element hase ema adse to game over or wottt!!!
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            plot_snake(gameWindow, black,
                    snk_list, snake_size)  # pygame.draw.shape(semaa karvu che,kayo colour,[direction na variable,shape ni size])

        # if you change anything which was by default before , then you have to code this line
        pygame.display.update()
        # basically use for framerate per second as per written
        clock.tick(fps)

    pygame.quit()
    quit()
game_loop()
