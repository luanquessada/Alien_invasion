import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
# Ao pegarmos uma imagem é melhor coloca-la no formato .bmp

def run_game(): #essa é a função principal do jogo
    pygame.init()
    ai_settings = Settings() #Definimos uma instância para Settings
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) #Criação da tela com seu tamanho
    pygame.display.set_caption("Alien Invasion") #Este será o nome da janela
    ship = Ship(ai_settings, screen)
    bullets = Group() #Cria um grupo no qual serão armazenados os projéteis


    while True:

        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)




run_game()


