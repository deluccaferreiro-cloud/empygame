import pygame
import random

pygame.init()

ancho = 800
alto = 600

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego")

reloj = pygame.time.Clock()

NEGRO = (0, 0, 0)
ROJO = (220, 50, 50)
BLANCO = (255, 255, 255)

fondo = pygame.image.load("fondo.jpg")
fondo = pygame.transform.scale(fondo, (ancho, alto))

puntaje = 0

x = random.randint(50, 700)
y = random.randint(100, 500)

objetivo = pygame.Rect(
    x,
    y,
    80,
    50
)

fuente = pygame.font.Font(None, 40)

ejecutando = True

while ejecutando:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            ejecutando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:

            if evento.button == 1:

                posicion_mouse = pygame.mouse.get_pos()

                if objetivo.collidepoint(posicion_mouse):

                    puntaje += 1

                    x = random.randint(50, 700)
                    y = random.randint(100, 500)

                    objetivo = pygame.Rect(
                        x,
                        y,
                        80,
                        50
                    )

    ventana.blit(fondo, (0, 0))

    pygame.draw.rect(
        ventana,
        ROJO,
        objetivo,
        border_radius=10
    )

    texto = fuente.render(
        "Puntaje: " + str(puntaje),
        True,
        NEGRO
    )

    ventana.blit(
        texto,
        (20, 20)
    )

    pygame.display.flip()

    reloj.tick(60)

pygame.quit()
