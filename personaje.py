import pygame

class Personaje():
    def __init__(self, x, y, image, flip=False, animaciones_x=None, animaciones_y=None):
        if animaciones_x is None and animaciones_y is None:
            animaciones = [image] # Valor por defecto si no se pasan animaciones
            
        self.animaciones_x = animaciones_x
        self.animaciones_y = animaciones_y

        self.frame_index_x = 0
        self.frame_index_y = 0

        self.image = self.animaciones_x[self.frame_index_x]
        
        self.forma = pygame.Rect(0, 0, self.image.get_width(), self.image.get_height())
        self.forma.center = (x, y)
        
        # Se almacena el tiempo en milisegundos desde que se inicializa pygame
        self.update_time = pygame.time.get_ticks()
        if self.animaciones_x:
            self.flip = flip

    
    def update(self, en_movimiento_eje_x, en_movimiento_eje_y):
        cooldown_animacion = 100
        tiempo_actual = pygame.time.get_ticks()

        # Elegir la animación según el eje del movimiento
        if en_movimiento_eje_x:
            animacion_actual = self.animaciones_x
            indice = "x"

        elif en_movimiento_eje_y:
            animacion_actual = self.animaciones_y
            indice = "y"

        else:
            # Si está quieto, mostrar la primera imagen de perfil
            self.image = self.animaciones_x[0]
            return

        # Avanzar la animación cada 100 milisegundos
        if tiempo_actual - self.update_time >= cooldown_animacion:
            if indice == "x":
                self.frame_index_x += 1
                if self.frame_index_x >= len(animacion_actual):
                    self.frame_index_x = 0
            else:
                self.frame_index_y += 1
                if self.frame_index_y >= len(animacion_actual):
                    self.frame_index_y = 0

            self.update_time = tiempo_actual

        # Seleccionar el fotograma correspondiente
        if indice == "x":
            self.image = self.animaciones_x[self.frame_index_x]
        else:
            self.image = self.animaciones_y[self.frame_index_y]


    def dibujar(self, screen):
        image_flip = pygame.transform.flip(self.image, self.flip, False)

        # Mantener el centro del dibujo en la misma coordenada
        image_rect = image_flip.get_rect(center=self.forma.center)

        screen.blit(image_flip, image_rect)
