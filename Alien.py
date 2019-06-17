
import pygame
from pygame.sprite import Group
from Settings import Settings
from Ship import Ship
import game_functions as gf
def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    game_settings.bg_color = (0,2,100)
    ship = Ship(game_settings,screen)
    bullets = Group()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(game_settings,screen,ship,bullets)

run_game()
