import pygame
from pygame.locals import *
from sys import exit


pygame.init()

altura = 480
largura = 640
#para movimentar 
movimento_x = largura/2
movimento_y = 0

#velocidade do obj
velocidade = pygame.time.Clock()
                                #eixo X e eixo Y
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('JOGO')
while True:
    #quanto maior o numero mais rapido fica (entenda como segundos)
    velocidade.tick(300)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit() 
                           #cor RGB     X                 Y         altura  largura
    pygame.draw.rect(tela, (255,0,0),(movimento_x,  movimento_y,    40,     50))
                          
   
    movimento_y +=1
    if movimento_y >= altura:
        movimento_y = 0
    
    pygame.display.update()