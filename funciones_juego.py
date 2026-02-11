from constantes import *
from errores import *
import funciones_inicializacion as f_ini
import funciones_mostrar as most

def pedir_disparo(tamano_tablero:int, disparos:list) -> tuple:
    """
    Pide una coordenada de disparo válida:
    - Dentro del tablero
    - No repetida

    Devuelve (fila, col).
    """
    repeticion = True
    while repeticion:
        try:
            fila, col = f_ini.pedir_coordenada(tamano_tablero)  # usa pedir_coordenada (A3 / A,3 / 3A)
            if (fila, col) in disparos:
                print("Ya disparaste ahí. Elige otra coordenada.")
            else:
                disparos.append((fila, col))
                repeticion = False
                return (fila, col)
        except CoordenadaError as error:
            print(error)

def es_barco(coordenada:tuple, tablero_barcos:list) -> bool:
    fila = coordenada[0]
    columna = coordenada[1]
    if tablero_barcos[fila][columna] == "##":
        return True
    else:
        return False
    
def comprobar_disparo(coordenada:tuple, tablero_barcos_objetivo:list, tablero_juego_tirador:list, barcos_objetivo:list) -> str:
    """
    Aplica un disparo en coordenada y actualiza los tableros.

    Devuelve:
    - "AGUA"
    - "TOCADO"
    - "HUNDIDO"
    """
    f, c = coordenada
    celda = tablero_barcos_objetivo[f][c]

    # --- AGUA ---
    if celda == AGUA:
        tablero_barcos_objetivo[f][c] = AGUA_DISPARO
        tablero_juego_tirador[f][c] = AGUA_DISPARO
        return "AGUA"

    # --- BARCO ---
    elif celda == "##":
        barco = buscar_barco_por_coord(barcos_objetivo, coordenada)

        # marcar tocado en ambos tableros
        tablero_barcos_objetivo[f][c] = TOCADO
        tablero_juego_tirador[f][c] = TOCADO

        # registrar tocado en el barco
        if barco is not None:
            agregar_tocado(barco, coordenada)

            # ¿hundido?
            if esta_hundido(barco):
                for (x, y) in barco["posiciones"]:
                    tablero_barcos_objetivo[x][y] = HUNDIDO
                    tablero_juego_tirador[x][y] = HUNDIDO
                return "HUNDIDO"

        return "TOCADO"

    # --- POR SEGURIDAD ---
    return "ERROR"


def buscar_barco_por_coord(barcos_info:list, coord:tuple):
    """
    Devuelve el diccionario del barco que ocupa coord,
    o None si no hay barco en esa coordenada.
    """
    for barco in barcos_info:
        if coord in barco["posiciones"]:
            return barco
    return None

def agregar_tocado(barco:dict, coord:tuple) -> None:
    """
    Añade la coordenada a la lista de tocadas del barco si no estaba.
    """
    if coord not in barco["tocadas"]:
        barco["tocadas"].append(coord)

def esta_hundido(barco:dict) -> bool:
    for pos in barco["posiciones"]:
        if pos not in barco["tocadas"]:
            return False
    return True


def todos_hundidos(barcos_info:list) -> bool:
    """
    Devuelve True si todos los barcos de barcos_info están hundidos.
    """
    for barco in barcos_info:
        if len(barco["tocadas"]) != len(barco["posiciones"]):
            return False
    return True

def hay_ganador(barcos_usuario:list, barcos_oponente:list) -> str:
    """
    Devuelve:
    - "USUARIO" si el usuario hundió todos los barcos del oponente
    - "OPONENTE" si el oponente hundió todos los barcos del usuario
    - "" si no hay ganador todavía
    """
    if todos_hundidos(barcos_oponente):
        return "USUARIO"
    if todos_hundidos(barcos_usuario):
        return "OPONENTE"
    return ""


