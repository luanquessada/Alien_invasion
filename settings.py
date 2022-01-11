class Settings():
    """Uma classe para armazenar todas as configurações da Invasão
    Alienígena."""
    def __init__(self):
        """Inicializa as configurações do jogo."""

        # Configurações da tela
        self.screen_width = 1000
        self.screen_height = 600 #Criação da tela com seu tamanho
        self.bg_color = (230, 230, 230) #Definimos uma cor RGB para o fundo

        self.ship_speed_factor = 1.5 #Define a velocidade da espaço-nave

        # Configurações dos projéteis
        self.bullet_speed_factor = 1
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = 80, 60, 120
        self.bullets_allowed = 3


