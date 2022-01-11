import sys
import pygame
from bullet import Bullet

#Separamos os eventos pressionados dos não pressionados em função para ficar mais facil de vizualizar
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Responde a pressionamentos de tecla."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    """Responde a solturas de tecla."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """Responde a eventos de pressionamento de teclas e de mouse."""
    for event in pygame.event.get():  # Observa elementos de mouse e teclado
        if event.type == pygame.QUIT:
            sys.exit()  # Fecha o jogo caso o usuário clique no X

        elif event.type == pygame.KEYDOWN: #KeyDown = quando a tecla é pressionada
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP: #Keyup = quando a tecla é solta
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """Atualiza as imagens na tela e alterna para a nova tela."""

    screen.fill(ai_settings.bg_color) #Redesenha a tela a cada passagem pelo laço

    # Redesenha todos os projéteis atrás da espaçonave e dos alienígenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    pygame.display.flip() #deixa visivel a janela mais recente


def update_bullets(bullets):
    '''Atualiza os disparos e elimina disparos fora da tela'''

    # Atualiza as posições dos projéteis
    bullets.update()

    # Livra-se dos projéteis que desapareceram
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):

    # Cria um novo projétil e o adiciona ao grupo de projéteis
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
