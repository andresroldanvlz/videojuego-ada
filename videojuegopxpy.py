def convertir_mapa_a_matriz(laberinto):
    return [list(fila) for fila in laberinto.split("\n")]

def mostrar_mapa(mapa):
    print("\n".join("".join(fila) for fila in mapa))

def main_loop(mapa, inicio, final):
    px, py = inicio
    jugador = input("Ingrese el nombre del jugador: ")
    while (px, py) != final:
        mapa[px][py] = 'P'
        mostrar_mapa(mapa)
        tecla = input("Ingrese la dirección (w/a/s/d) o 'up' para terminar: ")
        if tecla == 'up':
            print(f"El juego ha terminado. Gracias por jugar, {jugador}!")
            break
        dx, dy = 0, 0
        if tecla == 'w':
            dx = -1
        elif tecla == 's':
            dx = 1
        elif tecla == 'a':
            dy = -1
        elif tecla == 'd':
            dy = 1
        if (0 <= px + dx < len(mapa)) and (0 <= py + dy < len(mapa[0])) and mapa[px + dx][py + dy] != '#':
            mapa[px][py] = '.'
            px += dx
            py += dy

laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

mapa = convertir_mapa_a_matriz(laberinto)
inicio = (0, 0)
final = (len(mapa)-1, len(mapa[0])-1)
main_loop(mapa, inicio, final)
