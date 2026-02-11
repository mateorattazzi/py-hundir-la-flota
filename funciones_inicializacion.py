from constantes import *
from errores import *
import funciones_mostrar as f_most

def crear_tablero() -> list:
    tablero = []
    for _ in range (TAMANO_TABLERO):
        fila = []
        for __ in range(TAMANO_TABLERO):
            fila.append("··")
        tablero.append(fila)
    return tablero

def pedir_coordenada(tamano_tablero:int) -> tuple:
    texto = input("Coordenada (ej: A3 o A,3): ").strip().upper()
    """
    Permitir A3 o A,3
    """
    if "," in texto:
        partes = texto.split(",")
        if len(partes) == 2:
            letra = partes[0].strip()
            num = partes[1].strip()
        else:
            raise CoordenadaError("Formato inválido. Ejemplos: A3 o A,3")
    else:
        if len(texto) < 2:
            raise CoordenadaError("Formato inválido. Ejemplos: A3 o A,3")
        letra = texto[0]
        num = texto[1:].strip()

    """
    Validar letra
    """
    if letra not in LETRA_NUM_CODIGO or not num.isdecimal():
        raise CoordenadaError("Letra inválida o Número inválido. Usa A, B, C... y 1, 2, 3...")
    col = int(num) - 1   # a índice 0
    fila = LETRA_NUM_CODIGO[letra]
    """
    Validar rango con el tamaño de tablero
    """
    if not (0 <= fila < tamano_tablero and 0 <= col < tamano_tablero):
        raise CoordenadaError("Coordenada fuera del tablero.")
    return (fila, col)


def puede_colocar(tablero:list, inicio:tuple, longitud:int, orientacion:str) -> bool:
    tamano = len(tablero)
    f, c = inicio
    orientacion = orientacion.upper()
    if orientacion not in ("H", "V"):
        raise CoordenadaError("La orientación debe ser Horizonatl (H) o Vertical (V)")
    for _ in range(longitud - 1):
        if tablero[f][c] == "##":
            raise CoordenadaError("El barco se solapa con otro barco.")
        
        else:
            if orientacion == "V":
                f += 1
            else:
                c += 1
            if not (0 <= f < tamano and 0 <= c < tamano):
                raise CoordenadaError("El barco se sale del tablero. Elige una coordenada adecuada.")

        """
        Confirma que ninguna coordenada se salga del tablero o solape con otro barco ya colocado
        """
    return True

def colocar_barco(tablero:list, inicio:tuple, longitud:int, orientacion:str) -> None:
    posiciones = []
    f, c = inicio
    orientacion = orientacion.upper()
    tablero[f][c] = "##"
    posiciones.append((f, c))
    for _ in range(longitud - 1):
        if orientacion == "V":
            f += 1
        else:
            c += 1
        tablero[f][c] = "##"
        posiciones.append((f, c))
    return posiciones  

def colocar_barcos(tablero:list, num_barcos:int, barcos_info:list) -> None:
    longitudes = DIMENSION_BARCOS[:num_barcos]
    num_barco = 0
    while num_barco < num_barcos:
        longitud = longitudes[num_barco]
        try:
            print(f"Colocando barco {num_barco + 1}/{num_barcos} (tamaño {longitud})")
            print("Tablero")
            f_most.mostrar_tablero(tablero)
            inicio = pedir_coordenada(len(tablero))
            orientacion = input("Orientación (H/V): ").strip().upper()
            puede_colocar(tablero, inicio, longitud, orientacion)
            posiciones = colocar_barco(tablero, inicio, longitud, orientacion)
            registrar_barco(barcos_info, posiciones)
            num_barco += 1
        except CoordenadaError as error:
            print(f"Error: {error}")

def registrar_barco(barcos_info:list, posiciones:list) -> None:
    """
    Guarda un barco en la lista barcos_info.
    """
    barco = {"id": len(barcos_info), "posiciones": posiciones, "tocadas": []}
    barcos_info.append(barco)
