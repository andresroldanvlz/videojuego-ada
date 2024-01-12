import readchar

print("Presiona cualquier tecla, para salir presiona la tecla ↑")

while True:
    key = readchar.readkey()
    print(f"Presionaste la tecla {key}")

    if key == "\x1b[A":  # Representación de la tecla ↑
        print("Has presionado la tecla ↑, saliendo del programa.")
        break
