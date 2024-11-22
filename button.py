from PPlay.window import *
from PPlay.gameimage import *
import constants

# Função para criar os botões

def criar_botoes(menu_options):
    y = constants.BUTTON_MARGIN_TOP  # Posição inicial para o primeiro botão
    margin = constants.BUTTON_MARGIN  # Margem entre os botões
    
    botoes = []
    
    # Lista com os nomes dos botões
    nomes_botoes = menu_options
    
    # Criando os objetos GameImage e atribuindo suas posições
    for nome in nomes_botoes:
        botao = GameImage("./assets/button.png")
        botao.x = constants.WINDOW_WIDTH / 2 - constants.BUTTON_WIDTH / 2
        botao.y = y
        botoes.append( botao)
        
        # Atualiza a posição y para o próximo botão, somando a margem
        y += margin
    
    return botoes
