import pygame

RGB_WHITE = (255,255,255)
FPS = 60
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

def init_screen_and_clock():
    global screen, display, clock
    pygame.init()
    pygame.display.set_caption('Game')
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    clock = pygame.time.Clock()

def write_text(text, pos, color, font):
    text_to_show = font.render(text, 0, pygame.Color(color))
    screen.blit(text_to_show, pos)

def display_fps():
    write_text(
        font=pygame.font.SysFont("Arial", 16), 
        text="FPS: " + str(int(clock.get_fps())), 
        color="black", 
        pos=(10, 0)
    )

def run_game():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(RGB_WHITE)
        display_fps()

        # update with no arguments updates the entire screen
        pygame.display.update()

        # Set max FPS
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    init_screen_and_clock()

    run_game()