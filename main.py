import pygame, sys
from sprites.block import Block

RGB_WHITE = (255,255,255)
RGB_BLACK = (0,0,0)
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
    text_to_show = font.render(text, 0, color)
    screen.blit(text_to_show, pos)

def display_fps():
    write_text(
        font=pygame.font.SysFont("Arial", 16), 
        text="FPS: " + str(int(clock.get_fps())), 
        color=pygame.Color("black"), 
        pos=(10, 0)
    )

def run_game(debug):
    init_screen_and_clock()

    # TODO: move everything to a MVC pattern, this is not scalable lol
    # just proof of concept for basic clicker game, variables to be deleted

    get_money_button = Block(RGB_BLACK, 80, 80)
    get_money_button.rect.x = 300 - 80 / 2
    get_money_button.rect.y = 400 - 80 / 2
    upgrade_button = Block(RGB_BLACK, 80, 40)
    upgrade_button.rect.x = 300 - 80 / 2
    upgrade_button.rect.y = 600 - 40 / 2

    sprite_group = pygame.sprite.RenderPlain(get_money_button, upgrade_button)

    money = 0
    dmoney = 1
    click_upgrade_cost = 10

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                # clicked on button

                # get a list of all sprites that are under the mouse cursor
                clicked_sprites = [s for s in sprite_group if s.rect.collidepoint(pos)]

                if get_money_button in clicked_sprites:
                    money += dmoney
                if upgrade_button in clicked_sprites:
                    if money >= click_upgrade_cost:
                        money -= click_upgrade_cost
                        click_upgrade_cost *= 2
                        dmoney += 1

        screen.fill(RGB_WHITE)
        if debug: display_fps()
        write_text(
            font=pygame.font.SysFont("Arial", 16), 
            text="Money: " + str(money), 
            color=pygame.Color("black"), 
            pos=(get_money_button.rect.x, get_money_button.rect.y - 100)
        )
        write_text(
            font=pygame.font.SysFont("Arial", 16), 
            text="dMoney: " + str(dmoney), 
            color=pygame.Color("black"), 
            pos=(get_money_button.rect.x, get_money_button.rect.y - 50)
        )
        write_text(
            font=pygame.font.SysFont("Arial", 16), 
            text="Upgrade Cost: " + str(click_upgrade_cost), 
            color=pygame.Color("black"), 
            pos=(upgrade_button.rect.x, upgrade_button.rect.y - 50)
        )
        sprite_group.draw(screen)

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
