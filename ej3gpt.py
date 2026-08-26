import pygame

pygame.init()

ancho = 800
alto = 600

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego")

reloj = pygame.time.Clock()

NEGRO = (0, 0, 0)
AZUL = (70, 100, 220)
VERDE = (70, 180, 100)

fondo = pygame.image.load("fondo.jpg")
fondo = pygame.transform.scale(fondo, (ancho, alto))

x = 100
y = 450

personaje = pygame.Rect(
    x,
    y,
    50,
    80
)

velocidad = 5

velocidad_y = 0

gravedad = 1

fuerza_salto = -18

en_suelo = True

suelo = pygame.Rect(
    0,
    530,
    ancho,
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
        personaje.x -= velocidad

    if teclas[pygame.K_d]:
        personaje.x += velocidad

    if teclas[pygame.K_LEFT]:
        personaje.x -= velocidad

    if teclas[pygame.K_RIGHT]:
        personaje.x += velocidad

    velocidad_y += gravedad
    personaje.y += velocidad_y

    if personaje.colliderect(suelo):
        personaje.bottom = suelo.top
        velocidad_y = 0
        en_suelo = True

    if personaje.left < 0:
        personaje.left = 0

    if personaje.right > ancho:
        personaje.right = ancho

    ventana.blit(fondo, (0, 0))

    pygame.draw.rect(
        ventana,
        VERDE,
        suelo
    )

    pygame.draw.rect(
        ventana,
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

    ventana.blit(
        texto,
        (20, 20)
    )

    pygame.display.flip()

    reloj.tick(60)

pygame.quit()
