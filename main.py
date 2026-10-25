
import pygame
from personaje import Personaje

# Inicializar Pygame
pygame.init()

# Crear ventana
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Mi juego")

# Variables del jugador
x = 50
y = 50
vel = 5

# Estados de movimiento
en_movimiento_eje_x = False
en_movimiento_eje_y = False

# --------------------------------
# CARGAR ANIMACIONES
# --------------------------------

animaciones_x = []
animaciones_y = []

# Animación de perfil: izquierda y derecha
for i in range(3):
    img = pygame.image.load(
        f"assets/images/characters/player/perfil{i}.png"
    )
    img = pygame.transform.scale(img, (75, 100))
    animaciones_x.append(img)

# Animación de frente: arriba y abajo
for i in range(2):
    img = pygame.image.load(
        f"assets/images/characters/player/frente{i}.png"
    )
    img = pygame.transform.scale(img, (130, 120))
    animaciones_y.append(img)

# Imagen base
player_image = pygame.image.load(
    "assets/images/characters/player/character.png"
)

ancho_original = player_image.get_width()
alto_original = player_image.get_height()

player_image = pygame.transform.scale(
    player_image,
    (ancho_original * 3, alto_original * 3)
)

# Crear jugador
jugador = Personaje(
    x=x,
    y=y,
    image=player_image,
    flip=False,
    animaciones_x=animaciones_x,
    animaciones_y=animaciones_y
)

# --------------------------------
# BUCLE PRINCIPAL
# --------------------------------

Running = True

while Running:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

    # Reiniciar estados en cada fotograma
    en_movimiento_eje_x = False
    en_movimiento_eje_y = False

    keys = pygame.key.get_pressed()

    # Movimiento horizontal
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= vel
        jugador.flip = False
        en_movimiento_eje_x = True

    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += vel
        jugador.flip = True
        en_movimiento_eje_x = True

    # Movimiento vertical
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= vel
        en_movimiento_eje_y = True

    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += vel
        en_movimiento_eje_y = True

    # Actualizar posición
    jugador.forma.center = (x, y)

    # Actualizar animación
    jugador.update(
        en_movimiento_eje_x,
        en_movimiento_eje_y
    )

    # Dibujar pantalla
    screen.fill((255, 255, 255))
    jugador.dibujar(screen)

    pygame.display.update()

pygame.quit()
