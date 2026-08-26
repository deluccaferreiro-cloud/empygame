import pygame
import sys

pygame.init()
ANCHO = 800
ALTO = 600

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Personaje que salta")

reloj = pygame.time.Clock()

FONDO = (190, 225, 255)
NEGRO = (0, 0, 0)
AZUL = (70, 100, 220)
VERDE = (70, 180, 100)

personaje = pygame.Rect(
    100,
    450,
    50,
    80
)

velocidad_horizontal = 5

velocidad_y = 0

gravedad = 1

fuerza_salto = -18

en_suelo = True

suelo = pygame.Rect(
    0,
    530,
    ANCHO,
    70
)

ejecutando = True

while ejecutando:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            ejecutando = False

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_SPACE and en_suelo:
                velocidad_y = fuerza_salto
                en_suelo = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_a]:
        personaje.x -= velocidad_horizontal

    if teclas[pygame.K_d]:
        personaje.x += velocidad_horizontal

    if teclas[pygame.K_LEFT]:
        personaje.x -= velocidad_horizontal

    if teclas[pygame.K_RIGHT]:
        personaje.x += velocidad_horizontal

    velocidad_y += gravedad
    personaje.y += velocidad_y

    if personaje.colliderect(suelo):
        personaje.bottom = suelo.top
        velocidad_y = 0
        en_suelo = True

    if personaje.left < 0:
        personaje.left = 0

    if personaje.right > ANCHO:
        personaje.right = ANCHO

    pantalla.fill(FONDO)
    pygame.draw.rect(
        pantalla,
        VERDE,
        suelo
    )
    pygame.draw.rect(
        pantalla,
        AZUL,
        personaje,
        border_radius=8
    )

    fuente = pygame.font.Font(None, 35)

    texto = fuente.render(
        "A / D para moverte - ESPACIO para saltar",
        True,
        NEGRO
    )

    pantalla.blit(
        texto,
        (20, 20)
    )
    pygame.display.flip()

    reloj.tick(60)
pygame.quit()
sys.exit()