import funciones_inicializacion as f_ini
import funciones_juego as f_jgo
import funciones_mostrar as most

espacio_separador_tableros = (""" 








""")
def inicializar_juego(barcos_usuario:list, barcos_oponente:list):
    numero_barcos = 999
    while numero_barcos not in range(2, 6):
        numero_barcos = input("Con cuantos barcos deseas jugar [2, 5]: ")
        if numero_barcos.isdecimal():
            numero_barcos = int(numero_barcos)
    tablero_juego_usuario = f_ini.crear_tablero()
    tablero_juego_oponente = f_ini.crear_tablero()
    tablero_barcos_usuario = f_ini.crear_tablero()
    tablero_barcos_oponente = f_ini.crear_tablero()
    print(f"Turno de colocar barcos de Usuario")
    f_ini.colocar_barcos(tablero_barcos_usuario, numero_barcos, barcos_usuario)
    print(espacio_separador_tableros)
    print(f"Turno de colocar barcos de Oponente")
    f_ini.colocar_barcos(tablero_barcos_oponente, numero_barcos, barcos_oponente)
    print(espacio_separador_tableros)
    return ((tablero_juego_usuario, tablero_juego_oponente, tablero_barcos_usuario, tablero_barcos_oponente))

def ejecutar_turno(tablero_juego_jugador:list, tablero_barcos_oponente:list, disparos_jugador:list, barcos_jugador:list, barcos_oponente:list):
    ganar = False
    turno = True
    while turno and not ganar:
        most.mostrar_tablero(tablero_juego_jugador)
        coordenada = f_jgo.pedir_disparo(len(tablero_juego_jugador), disparos_jugador)
        resultado = f_jgo.comprobar_disparo(coordenada, tablero_barcos_oponente, tablero_juego_jugador, barcos_oponente)
        print(f"Resultado: {resultado}")
        ganador = f_jgo.hay_ganador(barcos_jugador, barcos_oponente)
        if ganador != "":
            print(f"¡Ganó el {ganador}!")
            ganar = True
        elif resultado == "AGUA":
            turno = False
        else:
            print("Como se ha dado a un barco, puede jugar de nuevo.")
    return ganar