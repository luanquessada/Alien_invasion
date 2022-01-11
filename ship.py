import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        """Inicializa a espaçonave e define sua posição inicial."""
        self.screen = screen
        self.image = pygame.image.load('Images/Ship.bmp') #carrega a imagem
        self.rect = self.image.get_rect() #vamos considerar a espaço-nave um retangulo
        self.screen_rect = screen.get_rect()

        self.ai_settings = ai_settings

        #Inicia cada espaço-nave na parte central
        self.rect.centerx = self.screen_rect.centerx #Significa que o retangulo estará no centro de X
        self.rect.bottom = self.screen_rect.bottom

        # Flag de movimento
        self.moving_right = False
        self.moving_left = False

        self.center = float(self.rect.centerx) #Armazena valor decimal na espaço-nave

    def blitme(self):
        """Desenha a espaçonave em sua posição atual, na posição rect."""

        self.screen.blit(self.image, self.rect)

    def update(self):
        """Atualiza a posição da espaçonave de acordo com a flag de
        movimento."""
        if self.moving_right and self.rect.right < self.screen_rect.right: #Se o rect for maior que o canto direito da
            #tela ele não permite que a imagem vá além, logo também não permite que rect vá além
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        # Atualiza o objeto rect de acordo com self.center
        self.rect.centerx = self.center
