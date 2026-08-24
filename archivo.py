import pygame
pygame.init()

ancho = 800
alto = 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Mi juego")

ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    ventana.fill((0, 0, 0))
    pygame.display.flip()

x = 100
y = 100

pygame.draw.rect(ventana, (80, 200,255), (x, y, 50, 50))