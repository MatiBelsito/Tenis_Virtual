import pygame
import random

pygame.init()


# Ventana principal

# Dimensiones de la ventana
ANCHO = 800
ALTO = 600

pantalla = pygame.display.set_mode((ANCHO,ALTO)) 
titulo = pygame.display.set_caption ( "Tenis Virtual")

# Fuente para puntaje
fuente = pygame.font.SysFont("Arial",30)

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Paletas
paleta_izquierda = pygame.Rect(30, 250, 20, 100) #  (x,y,width,heigth) pos_x, pos_y, ancho, alto
paleta_derecha = pygame.Rect (750, 250, 20, 100)

# Pelota

pelota = pygame.Rect (390, 290, 20, 20) #(x,y,width,heigth)  pos_x, pos_y, ancho, alto
posicion_pelota_x = 5 * random.choice([1, -1]) # 5 (pixeles por fotograma) * dirección aleatoria
posicion_pelota_y = 5 * random.choice([1, -1])
incremento = 0


# Velocidades de las paletas
posicion_paleta_izquierda = 0
posicion_paleta_derecha = 0

# Puntajes
puntos_jugador1 = 0
puntos_jugador2 = 0

# Banderas
jugador1_gana = False
jugador2_gana = False 

# Función para mostrar el puntaje
def mostrar_puntajes():
    texto = fuente.render(f"Jugador 1: {puntos_jugador1}  Jugador 2: {puntos_jugador2}", True, BLANCO)
    pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, 20))

# Función para mostrar el mensaje de victoria
def mostrar_mensaje(mensaje):
    texto = fuente.render(mensaje, True, BLANCO)
    pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2))


################################# Bucle principal ##################################
while True:
    
    pantalla.fill (NEGRO) # fondo negro
    
    # Gestionar Eventos ############################################################
    for evento in pygame.event.get():
        
        if evento.type == pygame.QUIT: # (cerrar ventana)
            pygame.quit()
            quit()
        
        # Control de movimiento de las paletas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w:
                posicion_paleta_izquierda = -5  # Subir
            if evento.key == pygame.K_s:
                posicion_paleta_izquierda = 5   # Bajar
            if evento.key == pygame.K_UP:
                posicion_paleta_derecha = -5  # Subir
            if evento.key == pygame.K_DOWN:
                posicion_paleta_derecha = 5   # Bajar
            
            # Reiniciar el juego si un jugador ha ganado
            if evento.key == pygame.K_r and (jugador1_gana or jugador2_gana):
                puntos_jugador1 = 0
                puntos_jugador2 = 0
                jugador1_gana = False
                jugador2_gana = False
                pelota.x = ANCHO // 2 - pelota.width // 2
                pelota.y = ALTO // 2 - pelota.height // 2
                posicion_pelota_x = 5 * random.choice([1, -1])
                posicion_pelota_y = 5 * random.choice([1, -1])
                incremento = 0

        # Detener el movimiento de las paletas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_w or evento.key == pygame.K_s:
                posicion_paleta_izquierda = 0
            if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                posicion_paleta_derecha = 0
            
            
    # Actualizar el juego ##########################################################
    
    # Actualizar el juego
    if not jugador1_gana and not jugador2_gana:
        # Mover las paletas
        paleta_izquierda.y += posicion_paleta_izquierda
        paleta_derecha.y += posicion_paleta_derecha

        # Evitar que las paletas se salgan de la pantalla
        if paleta_izquierda.top < 0:
            paleta_izquierda.top = 0
        if paleta_izquierda.bottom > ALTO:
            paleta_izquierda.bottom = ALTO
        if paleta_derecha.top < 0:
            paleta_derecha.top = 0
        if paleta_derecha.bottom > ALTO:
            paleta_derecha.bottom = ALTO

        # Mover la pelota
        pelota.x += posicion_pelota_x
        pelota.y += posicion_pelota_y

        # Rebote de la pelota en las paredes superior e inferior
        if pelota.top <= 0 or pelota.bottom >= ALTO:
            posicion_pelota_y = -posicion_pelota_y # cambio de dirección

        # Colisiones con las palas
        if pelota.colliderect(paleta_izquierda) or pelota.colliderect(paleta_derecha):
            posicion_pelota_x = -posicion_pelota_x # cambio de dirección

        # Si la pelota cruza el límite izquierdo o derecho
        if pelota.left <= 0:
            incremento += 0.25
            puntos_jugador2 += 1
            pelota.x = ANCHO // 2 - pelota.width // 2
            pelota.y = ALTO // 2 - pelota.height // 2
            posicion_pelota_x =(incremento + 5)  * random.choice([1, -1]) # Salida aleatoria con incremento de velocidad
            posicion_pelota_y = (incremento + 5) * random.choice([1, -1])
        if pelota.right >= ANCHO:
            incremento += 0.25
            puntos_jugador1 += 1
            pelota.x = ANCHO // 2 - pelota.width // 2
            pelota.y = ALTO // 2 - pelota.height // 2
            posicion_pelota_x = (incremento + 5) * random.choice([1, -1])
            posicion_pelota_y = (incremento + 5) * random.choice([1, -1])

        # Verificar si algún jugador gana
        if puntos_jugador1 == 10:
            jugador1_gana = True
        if puntos_jugador2 == 10:
            jugador2_gana = True

    # Mostrar el puntaje
    mostrar_puntajes()

    # Mostrar el mensaje de victoria
    if jugador1_gana:
        mostrar_mensaje("¡Jugador 1 Gana!")
    elif jugador2_gana:
        mostrar_mensaje("¡Jugador 2 Gana!")
    
    
    
    # Dibujar en pantalla ##########################################################
    
    # pantalla.fill((0,0,0)) # (relleno de pantalla color negro)
    pygame.draw.rect(pantalla, BLANCO, paleta_izquierda)
    pygame.draw.rect(pantalla, BLANCO, paleta_derecha)
    pygame.draw.ellipse(pantalla, BLANCO, pelota)
    
    
    
    # Actualizar la pantalla ######################################################## 
    
    pygame.display.update()
    pygame.time.Clock().tick(60)  # FPS # moderar la cantidad de ciclos por segundo del bucle principal
    
    
            
    
    

