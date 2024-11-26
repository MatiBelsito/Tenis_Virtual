import pygame

pygame.init()


# Ventana principal
pantalla = pygame.display.set_mode((800,600)) 
titulo = pygame.display.set_caption ( "Tenis Virtual")


################################# Bucle principal ##################################
while True:
    
    # Gestionar Eventos ############################################################
    for evento in pygame.event.get():
        
        if evento.type == pygame.QUIT: # (cerrar ventana)
            pygame.quit()
            quit()
            
            
    # Actualizar el juego ##########################################################
    
    
    
    
    
    # Dibujar en pantalla ##########################################################
    
    pantalla.fill((0,0,0)) # (relleno de pantalla color negro)
    
    
    
    
    # Actualizar la pantalla ######################################################## 
    
    pygame.display.update()
    
    
    
            
    
    

