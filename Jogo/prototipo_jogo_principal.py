import pygame
import imagens




vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
roxo = (255,0,255)
ciano = (0,255,255)
cor = (255,255,0)

tela = pygame.display.set_mode([1366,768])
pygame.draw.rect(tela, vermelho, [1000,0, 366,192])
pygame.draw.rect(tela, verde, [1000,192, 366,192])
pygame.draw.rect(tela, azul, [1000,384, 366,192])
pygame.draw.rect(tela, roxo, [1000,575, 366,192])
pygame.draw.rect(tela, ciano, [0,0, 1000,192])
pygame.draw.rect(tela, cor,[0,192,1000,576])
clock = pygame.time.Clock()

rodando = True

while rodando == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    item_1 = pygame.image.load(imagens.LOGO_MENU)
    logo = pygame.transform.scale(logo, (600, 600))

    pygame.display.flip()
    clock.tick(60)


pygame.quit()