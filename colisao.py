import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

altura = 480
largura = 640
#para movimentar 
movimento_x = largura/2
movimento_y = altura/2

movimento_bolx = randint(40, 600)
movimento_boly = randint(50, 430)
#velocidade do obj
velocidade = pygame.time.Clock()
                                #eixo X e eixo Y
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('JOGO')
while True:
    #quanto maior o numero mais rapido fica (entenda como segundos)
    velocidade.tick(50)
    tela.fill((0,200,200))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()           
    if pygame.key.get_pressed()[K_a]:
        movimento_x -= 20
    if pygame.key.get_pressed()[K_d]:
        movimento_x += 20
    if pygame.key.get_pressed()[K_w]:
        movimento_y -= 20
    if pygame.key.get_pressed()[K_s]:
        movimento_y += 20
        
                           #cor RGB     X                 Y         altura  largura
    ret_vermelho = pygame.draw.rect(tela, (255,0,0),(movimento_x,  movimento_y,    40,     50))
    bol_azul = pygame.draw.circle(tela, (0,0,225), (movimento_bolx, movimento_boly),20)

    if ret_vermelho.colliderect(bol_azul):
        movimento_bolx = randint(40, 600)
        movimento_boly = randint(40, 430)
    
    
    pygame.display.update()