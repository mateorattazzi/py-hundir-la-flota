from constantes import *
import funciones_inicializacion as f_ini
import funciones_mostrar as f_most
from errores import *
import funciones_juego as f_jgo
"""
Test: 1
"""
print(f"""Test de función creación de tableros para observar simetría
      
      """)
tablero_juego_usuario = f_ini.crear_tablero()
f_most.mostrar_tablero(tablero_juego_usuario)


"""
Test: 2
"""

print(f"""
      
Test de función colocación de barcos
      
      """)

coordenadas_test = {(0, 1):"H", (1, 7):"H", (3, 3):"V", (0, 2):"H"}

"""
El primer y tercer barco deberian poder colocarse al no 
solapar entre si pero el cuarto deberia lanzar un error al solaparse
con el primer barco y el segundo al salirse del tablero.
"""

longitud = 5
for coordenada, orientacion in coordenadas_test.items():
    try:
        se_puede_colocar = f_ini.puede_colocar(tablero_juego_usuario, coordenada, longitud, orientacion)
        f_ini.colocar_barco(tablero_juego_usuario, coordenada, longitud, orientacion)
        print(f"Se pudo colocar la coordenada {coordenada} con orientacion {orientacion}.")
    except CoordenadaError as error:
        print(f"Error: No se pudo colocar la coordenada {coordenada} porque {error}")
    longitud -= 1

"""
Test: 3
"""

print(f"""
      
Test de función para comprobar si un barco esta hundido
      
      """)
"""
El input son dos barcos donde al barco 1 no se le han tocado todas sus coordenadas
y el barco 2 deberia estar hundido al tener todas sus posiciones tocadas.
"""
barco_1 = {"id": 0, "posiciones": [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)], "tocadas": [(0, 2), (0, 3), (0, 4), (0, 5)]}
barco_2 = {"id": 1, "posiciones": [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)], "tocadas": [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]}

barco_1_hundido = f_jgo.esta_hundido(barco_1)
barco_2_hundido = f_jgo.esta_hundido(barco_2)
if barco_1_hundido:
    print(f"El barco 1 está hundido.")
else:
    print(f"El barco 1 no esta hundido porque no se han tocado todas sus posiciones.")

if barco_2_hundido:
    print(f"El barco 2 está hundido.")
else:
    print(f"El barco 2 no esta hundido porque no se han tocado todas sus posiciones.")


"""
Test: 4
"""

print(f"""

Test de función comprobar_disparo

Objetivo:
- Probar disparo al agua
- Probar disparo a barco (tocado)
- Probar hundimiento cuando se tocan todas las posiciones
- Probar disparo repetido (debería lanzar error o ser rechazado según tu lógica)

""")

tablero_barcos = f_ini.crear_tablero()
tablero_disparos = f_ini.crear_tablero()

print("Tablero de disparos (inicial):")
f_most.mostrar_tablero(tablero_disparos)


"""
Se colocan 2 barcos para poder dispararles
Barco A: longitud 3 horizontal desde (5, 5) => (5,5)(5,6)(5,7)
Barco B: longitud 2 vertical desde (2, 0) => (2,0)(3,0)
"""

barcos = [
    {"id": 1, "posiciones": [(5, 5), (5, 6), (5, 7)], "tocadas": []},
    {"id": 2, "posiciones": [(2, 0), (3, 0)], "tocadas": []},
]

"""
Colocación de barcos mientras se muestra error si existe un error inesperado
"""
try:
    f_ini.colocar_barco(tablero_barcos, (5, 5), 3, "H")
    f_ini.colocar_barco(tablero_barcos, (2, 0), 2, "V")
except CoordenadaError as error:
    print("Error inesperado colocando barcos de test:", error)

print("Tablero oculto (con barcos colocados para el test):")
f_most.mostrar_tablero(tablero_barcos)


"""3) Disparos de prueba
    - (0,0) => agua
    - (5,5) => tocado (barco id 1)
    - (5,6) => tocado
    - (5,7) => tocado y HUNDIDO (barco id 1 completo)
    - (5,7) => disparo repetido (debería fallar/avisar)"""
disparos_test = [(0, 0), (5, 5), (5, 6), (5, 7), (5, 7)]

for coord in disparos_test:
    print(f"Disparo a {coord}:")

    try:
        
        resultado = f_jgo.comprobar_disparo(coord, tablero_barcos, tablero_disparos, barcos)
        print(resultado)
        if resultado is not None:
            print("Resultado:", resultado)

    except CoordenadaError as error:
        print("Error de coordenada / disparo inválido:", error)

    print("Tablero de disparos (después del disparo):")
    f_most.mostrar_tablero(tablero_disparos)

    print("Estado de barcos (tocadas):")
    for barco in barcos:
        print(f"  Barco {barco['id']} tocadas: {barco['tocadas']}")

print("Comprobación final de hundimiento:")
for barco in barcos:
    hundido = f_jgo.esta_hundido(barco)
    print(f"Barco {barco['id']} hundido?: {hundido}")
