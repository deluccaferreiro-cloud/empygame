import sys
import pygame

# Inicializar Pygame
pygame.init()

# Configurar ventana
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cambiar de pantalla con clic")
reloj = pygame.time.Clock()

# Variables de configuración
x = 300
fuente = pygame.font.Font(None, 32)

# --- 1. CREAR EL RECTÁNGULO COMO UN OBJETO ---
# Usamos tus mismas coordenadas: x=300, y=300, ancho=200, alto=50
mi_cuadro = pygame.Rect(x, 300, 200, 50)

# --- 2. VARIABLE DE ESTADO ---
# Controla en qué "lugar" o pantalla estamos actualmente
pantalla_actual = "inicio"

# Bucle principal
while True:
  # Captura de eventos
  for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    # --- 3. DETECTAR EL CLIC ---
    if evento.type == pygame.MOUSEBUTTONDOWN:
      if evento.button == 1:  # 1 significa clic izquierdo
        # Si estamos en la pantalla de inicio y hacemos clic adentro del cuadro
        if pantalla_actual == "inicio" and mi_cuadro.collidepoint(evento.pos):
          pantalla_actual = "otro_lugar"  # CAMBIAMOS EL ESTADO

  # --- 4. DIBUJAR SEGÚN EL ESTADO ACTUAL ---
  if pantalla_actual == "inicio":
    # --- PANTALLA A (INICIO) ---
    ventana.fill((0, 0, 0))  # Fondo negro

    # Dibujamos tu cuadro usando el objeto mi_cuadro
    pygame.draw.rect(ventana, (80, 200, 255), mi_cuadro)

    # Dibujamos el texto adentro
    texto_inicio = fuente.render("Ir a otro lugar", True, (0, 0, 0))
    ventana.blit(texto_inicio, (mi_cuadro.x + 15, mi_cuadro.y + 13))

  elif pantalla_actual == "otro_lugar":
    # --- PANTALLA B (EL OTRO LUGAR) ---
    ventana.fill((50, 150, 50))  # Fondo verde (indica que cambiamos de lugar)

    # Texto en el nuevo lugar
    texto_nuevo = fuente.render(
        "¡Bienvenido al otro lugar!", True, (255, 255, 255)
    )
    ventana.blit(texto_nuevo, (250, 280))

  pygame.display.flip()
  reloj.tick(60)
