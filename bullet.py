import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''Uma classe que administra os projeteis da nave'''

    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height) #Rect da bala
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top #faz com que o projetil saiu do topo da espaçonave
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move o projétil para cima na tela."""
        # Atualiza a posição decimal do projétil
        self.y -= self.speed_factor
        # Atualiza a posição de rect
        self.rect.y = self.y

    def draw_bullet(self):
        """Desenha o projétil na tela."""
        pygame.draw.rect(self.screen, self.color, self.rect)
