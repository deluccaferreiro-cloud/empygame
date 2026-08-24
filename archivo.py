import pygame
pygame.init()

ancho = 800
alto = 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego")
ejecutando = True
reloj = pygame.time.Clock()
y = 225
x = 375
velocidad = 5
tamaño = 50

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False 
    teclas = pygame.key.get_pressed()
    
    if teclas[pygame.K_w]:
        y -= velocidad

    if teclas[pygame.K_s]:
        y += velocidad
    
    if teclas[pygame.K_a]:
        x -= velocidad
    
    if teclas[pygame.K_d]:
        x += velocidad
    
    ventana.fill((25, 30, 40))
    pygame.draw.rect(ventana, (80, 200,255), (x, y, tamaño, tamaño))
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
