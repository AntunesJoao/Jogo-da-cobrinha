import pygame
from pygame.locals import *
from sys import exit


pygame.init()

altura = 480
largura = 640

                                #eixo X e eixo Y
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('JOGO')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit() 
                           #cor RGB    X     Y   altura  largura
    pygame.draw.rect(tela, (255,0,0),(200,  300,   40,     50))
                            #cor RGB     X     Y     reio do circulo
    pygame.draw.circle(tela, (0,0,225), (300, 260),        40)
                                      #pontos pontos x y       grossura da linha
    pygame.draw.line(tela,(255, 255, 0), (390,0), (390,600),           5)
    pygame.display.update()