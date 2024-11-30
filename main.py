import pygame
from funciones import jugar

# Función para mostrar el menú
def mostrar_menu():
    print("-" * 13)
    print("TENIS VIRTUAL")
    print("-" * 13)
    print("Menu Principal")
    print("1. Jugar")
    print("2. Instrucciones")
    print("3. Salir")
    print("-" * 30)

# Función para mostrar las instrucciones
def mostrar_instrucciones():
    print("Jugador 1: utiliza las teclas W y S para mover tu paleta")
    print("Jugador 2: utiliza las teclas ARRIBA y ABAJO para mover tu paleta")
    print("Pulsando la tecla R pueden reiniciar el juego")
    print("Para volver al Menu Principal escribe 'v'")
    print("-" * 30)

    while True:
        volver = input("Escribe 'v' para volver al menú principal: ").lower()
        if volver == "v":
            break  #  vuelvo al menú

def main():
    

    while True:
        mostrar_menu()  # Muestro el menú
        try:
            opcion = int(input("Selecciona una opción: "))  # Solicito la opción del usuario
            
            if opcion == 1:
                jugar()  # función para comenzar a jugar
            elif opcion == 2:
                mostrar_instrucciones()  # función para mostrar las instrucciones
            elif opcion == 3:
                print("¡Gracias por jugar! ¡Hasta luego!")  # Mensaje de despedida
                pygame.quit()  # cierro pygame
                exit()  # Sale del programa
            else:
                print("Opción no válida. Por favor, selecciona una opción entre 1 y 3.")
            
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")  # error no numerico


main()  # Llamo a la función principal para ejecutar el menú
