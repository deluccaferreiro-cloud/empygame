import pygame

pygame.init()

ancho = 800
alto = 600

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego")

reloj = pygame.time.Clock()

NEGRO = (0, 0, 0)
AZUL = (70, 100, 220)
ROJO = (220, 60, 60)
VERDE = (70, 180, 100)

fondo = pygame.image.load("fondo.jpg")
fondo = pygame.transform.scale(fondo, (ancho, alto))

x = 100
y = 100

velocidad = 5

personaje = pygame.Rect(
    x,
    y,
    50,
    80
)

obstaculo1 = pygame.Rect(
    250,
    150,
    200,
    50
)

obstaculo2 = pygame.Rect(
    500,
    350,
    50,
    150
)

ejecutando = True

while ejecutando:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            ejecutando = False

    teclas = pygame.key.get_pressed()

    posicion_anterior = personaje.copy()

    if teclas[pygame.K_w]:
        personaje.y -= velocidad

    if teclas[pygame.K_s]:
        personaje.y += velocidad

    if teclas[pygame.K_a]:
        personaje.x -= velocidad

    if teclas[pygame.K_d]:
        personaje.x += velocidad

    if personaje.left < 0:
        personaje.left = 0

    if personaje.right > ancho:
        personaje.right = ancho

    if personaje.top < 0:
        personaje.top = 0

    if personaje.bottom > alto:
        personaje.bottom = alto

    if personaje.colliderect(obstaculo1):
        personaje = posicion_anterior

    if personaje.colliderect(obstaculo2):
        personaje = posicion_anterior

    ventana.blit(fondo, (0, 0))

    pygame.draw.rect(
        ventana,
        ROJO,
        obstaculo1
    )

    pygame.draw.rect(
        ventana,
        ROJO,
        obstaculo2
    )

    pygame.draw.rect(
        ventana,
        AZUL,
        personaje,
        border_radius=8
    )

    pygame.display.flip()

    reloj.tick(60)

pygame.quit()
