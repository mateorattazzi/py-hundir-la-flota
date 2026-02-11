from constantes import *
from errores import *
import funciones_inicializacion as f_ini
import funciones_juego as f_jgo
import funciones_mostrar as most
import estructura_del_juego as estructura

if __name__ == "__main__":
    """
    INICIALIZACION: Creación de tableros y posicion de barcos
    """
    disparos_usuario = []
    disparos_oponente = []
    barcos_usuario = []
    barcos_oponente = []
    tablero_juego_usuario, tablero_juego_oponente, tablero_barcos_usuario, tablero_barcos_oponente = estructura.inicializar_juego(barcos_usuario, barcos_oponente)
    """
    JUEGO
    """
    ganar = False
    while not ganar:
        print()
        print("Turno de usuario:")
        ganar = estructura.ejecutar_turno(tablero_juego_usuario, tablero_barcos_oponente, disparos_usuario, barcos_usuario, barcos_oponente)
        if not ganar:
            print()
            print()
            print("Turno de oponente:")
            ganar = estructura.ejecutar_turno(tablero_juego_oponente, tablero_barcos_usuario, disparos_oponente, barcos_oponente, barcos_usuario)

    """
    FINALIZACION
    """
    most.mostrar_tableros_finales(tablero_juego_usuario, tablero_barcos_usuario, tablero_juego_oponente, tablero_barcos_oponente)  

