import os
import msvcrt

def imprimir_numero(num):
    os.system('cls' if os.name=='nt' else 'clear')
    print(num)

num = 0
while num <= 50:
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == b'n':
            num += 1
            imprimir_numero(num)
