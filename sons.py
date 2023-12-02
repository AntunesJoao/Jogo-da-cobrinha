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

#para escolher a musica
musica_fundo = pygame.mixer.music.load('Tetris.mp3')

#volume do fundo
pygame.mixer.music.set_volume(0.9)

#para tocar a musica. O "-1" é para a musica ficar repetindo
pygame.mixer.music.play(-1)


#som secundario
som_colisao = pygame.mixer.Sound('smw_1-up.wav')
pontos = 0
#volume 
som_colisao.set_volume(0.90)

                            #tipo    tamanho    negrito      italico
texto = pygame.font.SysFont('arial',   40,        False,       False)
                                #eixo X e eixo Y
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('JOGO')
while True:
    #quanto maior o numero mais rapido fica (entenda como segundos)
    velocidade.tick(30)
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
                                      #mensagem   formatado de pixel            cor
    mensagem_formatada = texto.render(mensagem,       False,               (255,255,255))
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
        pontos += 1
        mensagem = f'Pontos: {texto}'
        som_colisao.play()
    
    tela.blit(mensagem_formatada, (410, 40))
    
    pygame.display.update()




#link dos sons nitendo: https://themushroomkingdom.net/wav.shtml