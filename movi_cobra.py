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
l =pygame.mixer.Sound('mlpit_peach_scream_1.wav')
movimento_bolx = randint(40, 600)
movimento_boly = randint(50, 430)

velocidadee = 10
x_controle = velocidadee
y_controle = 0

morreu = False


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

cobra = []


                            #tipo    tamanho    negrito      italico
texto = pygame.font.SysFont('arial',   40,        False,       False)
                                #eixo X e eixo Y
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('JOGO')

comprimento_inicial= 5
def aumenta_cobra(cobra):
    for xy in cobra:
        pygame.draw.rect(tela, (0,255,0), (xy[0], xy[1], 20, 30))

def reiniciar():
    global pontos, comprimento_inicial, movimento_x, movimento_y, cobra, cabeca, morreu
    pontos = 0
    comprimento_inicial = 5
    movimento_x = largura/2
    movimento_y = altura/2
    cobra = []
    cabeca = []
    morreu = False
   
    
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
        if event.type == KEYDOWN:
                        #representa a tecla A
            if event.key == K_a:
                if x_controle == velocidadee:
                    ...
                else:
                    x_controle = -velocidadee
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidadee:
                    ...
                else:
                    x_controle = velocidadee
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidadee:
                    ...
                else:
                    x_controle = -0
                    y_controle = -velocidadee
            if event.key == K_s:
                if y_controle == -velocidadee:
                    ...
                else:
                    x_controle = 0
                    y_controle = velocidadee
    
    movimento_x += x_controle
    movimento_y += y_controle
        
                          
    ret_vermelho = pygame.draw.rect(tela, (255,0,0),(movimento_x,  movimento_y,    30,     30))
    bol_azul = pygame.draw.circle(tela, (0,0,225), (movimento_bolx, movimento_boly),20)

    if ret_vermelho.colliderect(bol_azul):
        movimento_bolx = randint(40, 600)
        movimento_boly = randint(40, 430)
        pontos += 1
        mensagem = f'Pontos: {texto}'
        som_colisao.play()
        comprimento_inicial +=1
    #comprimento
    cabeca = []
    cabeca.append(movimento_x)
    cabeca.append(movimento_y)
    cobra.append(cabeca)
    fonte2 = pygame.font.SysFont('arial', 20, True, True)
    msg = 'game over preissone R para continuar'
    formatada =fonte2.render(msg, True, (0,0,0))
    rettexot = formatada.get_rect()

    if cobra.count(cabeca) >1:
        morreu = True
        while morreu:
            tela.fill((23,45,240))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()       
                if event.type ==  KEYDOWN:
                    if event.key == K_r:
                        reiniciar()
            rettexot.center = (largura//2, altura//2)
            tela.blit(formatada, rettexot)
            pygame.display.update()
    if movimento_x > largura:
        movimento_x = 0
    if movimento_x < 0:
        movimento_x = largura
    if movimento_y < 0:
        movimento_y = altura
    if movimento_y > altura:
        movimento_y = 0

    if len(cobra) > comprimento_inicial:
        del cobra[0]
    aumenta_cobra(cobra)

    
    if pontos == 10:
        l
        l.play()

    tela.blit(mensagem_formatada, (410, 40))
    
    pygame.display.update()
