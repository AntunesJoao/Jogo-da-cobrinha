import pygame
from pygame.locals import *
from sys import exit


pygame.init()

altura = 480
largura = 640
#para movimentar 
movimento_x = largura/2
movimento_y = altura/2

#velocidade do obj
velocidade = pygame.time.Clock()
                                #eixo X e eixo Y
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('JOGO')
while True:
    #quanto maior o numero mais rapido fica (entenda como segundos)
    velocidade.tick(50)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()  

            '''
            OBS: NESSA FORMA DE CODIGO NÃO É POSSIVEL SEGURAR PARA CONTINUAR UM MOVIMENTO
                    #representa todo o teclado KEYDOWN
        if event.type == KEYDOWN:
                        #representa a tecla A
            if event.key == K_a:
                movimento_x -= 20
            if event.key == K_d:
                movimento_x += 20
            if event.key == K_w:
                movimento_y -=20
            if event.key == K_s:
                movimento_y +=20
                                '''
            
    if pygame.key.get_pressed()[K_a]:
        movimento_x -= 20
    if pygame.key.get_pressed()[K_d]:
        movimento_x += 20
    if pygame.key.get_pressed()[K_w]:
        movimento_y -= 20
    if pygame.key.get_pressed()[K_s]:
        movimento_y += 20
        
                           #cor RGB     X                 Y         altura  largura
    pygame.draw.rect(tela, (255,0,0),(movimento_x,  movimento_y,    40,     50))
                            #cor RGB     X     Y     reio do circulo
  
    
    
    pygame.display.update()