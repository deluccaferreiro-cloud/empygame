import pygame
pygame.init()

ancho = 800
alto = 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Mi juego")

ejecutando = True
x = 100
velocidad = 5
reloj = pygame.time.Clock()

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
    x += velocidad
    ventana.fill((25, 30, 40))
    pygame.draw.rect(ventana, (80, 200,255), (x, 200, 50, 50))
    pygame.display.flip()

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_w]:
        y -= velocidad
    if teclas[pygame.K_s]:
        y += velocidad
    if teclas[pygame.K_a]:
        x -= velocidad
    if teclas[pygame.K_d]:
        x += velocidad
    pygame.display.flip()
    reloj.tick(60)

    ventana.fill((25, 30, 40))
    


