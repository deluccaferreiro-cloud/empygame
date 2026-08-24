import pygame
pygame.init()

ancho = 800
alto = 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego")
ejecutando = True
reloj = pygame.time.Clock()
y = 225
x = 300
velocidad = 5

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False 
    pygame.draw.rect(ventana, (80, 200, 255), (x, y, 200, 50))
    pygame.draw.rect(ventana, (80, 200, 255), (x, 300, 200, 50))
    pygame.draw.rect(ventana, (80, 200, 255), (x, 375, 200, 50))
    pygame.display.flip()
    
pygame.quit()
