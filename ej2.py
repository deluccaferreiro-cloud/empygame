import sys
import pygame

pygame.init()

ANCHO = 800
ALTO = 600

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Escenario Mágico")

reloj = pygame.time.Clock()

NEGRO = (0, 0, 0)
MARRON = (110, 65, 40)
MARRON_CLARO = (160, 100, 55)
CELESTE = (80, 170, 230)
AZUL = (50, 100, 200)
AMARILLO = (240, 200, 70)
VIOLETA = (150, 80, 220)

fondo = pygame.image.load("tuntuntun.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

fuente = pygame.font.Font(None, 45)
fuente_pequena = pygame.font.Font(None, 28)

personaje = pygame.Rect(
    245,
    410,
    50,
    80
)

velocidad = 5

ejecutando = True

while ejecutando:
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            ejecutando = False
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        personaje.x -= velocidad

    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        personaje.x += velocidad

    if teclas[pygame.K_UP] or teclas[pygame.K_w]:
        personaje.y -= velocidad

    if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
        personaje.y += velocidad

    if personaje.left < 0:
        personaje.left = 0

    if personaje.right > ANCHO:
        personaje.right = ANCHO

    if personaje.top < 0:
        personaje.top = 0

    if personaje.bottom > ALTO:
        personaje.bottom = ALTO

    pantalla.blit(fondo, (0, 0))

    plataforma = pygame.Rect(
        80,
        490,
        640,
        40
    )

    pygame.draw.rect(
        pantalla,
        MARRON,
        plataforma,
        border_radius=10
    )

    pygame.draw.rect(
        pantalla,
        MARRON_CLARO,
        (80, 490, 640, 10),
        border_radius=10
    )


    puerta = pygame.Rect(
        610,
        320,
        90,
        170
    )

    pygame.draw.rect(
        pantalla,
        MARRON,
        puerta,
        border_radius=8
    )

    pygame.draw.rect(
        pantalla,
        VIOLETA,
        (620, 330, 70, 150),
        border_radius=5
    )

    pygame.draw.circle(
        pantalla,
        AMARILLO,
        (675, 405),
        7
    )
    pygame.draw.circle(
        pantalla,
        CELESTE,
        (personaje.centerx, personaje.y + 20),
        25
    )

    pygame.draw.rect(
        pantalla,
        AZUL,
        (
            personaje.x,
            personaje.y + 25,
            50,
            55
        ),
        border_radius=10
    )

    pygame.draw.rect(
        pantalla,
        MARRON,
        (
            personaje.x + 5,
            personaje.y + 75,
            15,
            25
        )
    )
    pygame.draw.rect(
        pantalla,
        MARRON,
        (
            personaje.x + 30,
            personaje.y + 75,
            15,
            25
        )
    )

    texto = fuente.render(
        "ESCENARIO MÁGICO",
        True,
        NEGRO
    )

    pantalla.blit(
        texto,
        (25, 25)
    )

    texto2 = fuente_pequena.render(
        "Movete con las flechas o WASD",
        True,
        NEGRO
    )

    pantalla.blit(
        texto2,
        (30, 70)
    )

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
sys.exit()