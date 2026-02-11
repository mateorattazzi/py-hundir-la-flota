from constantes import *
import funciones_inicializacion as f_ini

def mostrar_tablero(tablero:list) -> None:
    letras = LETRAS[:len(tablero)]
    tamano = len(tablero)
    print("   ", end="")
    for i in range(1, tamano + 1):
        print(f"{i}    ", end="")
    print()
    for i in range(tamano):
        print(f"{letras[i]}  ", end="")
        for j in range(tamano):
            print(f"{tablero[i][j]}   ", end="")
        print()


def mostrar_tableros_finales(tablero_juego_usuario:list, tablero_barcos_usuario:list, tablero_juego_oponente:list, tablero_barcos_oponente:list) -> None:
    """
    Muestra los cuatro tableros al final de la partida
    para que los jugadores vean el estado completo del juego.
    """
    print(f"\n{'='*50}")
    print("ESTADO FINAL DE LA PARTIDA")
    print("="*50)

    print("\nTABLERO DE JUEGO DEL USUARIO (disparos realizados):")
    mostrar_tablero(tablero_juego_usuario)

    print("\nTABLERO DE BARCOS DEL USUARIO (posición real):")
    mostrar_tablero(tablero_barcos_usuario)

    print("\nTABLERO DE JUEGO DEL OPONENTE (disparos realizados):")
    mostrar_tablero(tablero_juego_oponente)

    print("\nTABLERO DE BARCOS DEL OPONENTE (posición real):")
    mostrar_tablero(tablero_barcos_oponente)

    print(f"\n{'='*50}")
    print("FIN DEL JUEGO")
    print("="*50)
