import pygame, sys

RGB_WHITE = (255,255,255)
FPS = 60
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

def init_screen_and_clock() -> None:
    global screen, display, clock
    pygame.init()
    pygame.display.set_caption('Game')
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    clock = pygame.time.Clock()

def write_text(text: str, pos: tuple[int, int], color: str, font: pygame.font.Font) -> None:
    text_to_show = font.render(text, 0, pygame.Color(color))
    screen.blit(text_to_show, pos)

def display_fps() -> None:
    write_text(
        font=pygame.font.SysFont("Arial", 16), 
        text="FPS: " + str(int(clock.get_fps())), 
        color="black", 
        pos=(10, 0)
    )

def run_game(debug: bool) -> None:
    init_screen_and_clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(RGB_WHITE)
        if debug: display_fps()

        # update with no arguments updates the entire screen
        pygame.display.update()

        # Set max FPS
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":

    args = sys.argv[1:]
    debug = False

    if len(args) == 2 and args[0] == '-mode':
        mode = args[1]
        if mode == "debug":
            debug = True

    print("running game in debug mode:", debug)
    run_game(debug)