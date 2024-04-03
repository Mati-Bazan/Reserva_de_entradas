array_2d = [['L' for _ in range(10)] for _ in range(10)]
bandera = False

def dibujarMapa():
    for row in array_2d:
        print(row)

print('------Bienvenido------')
while not bandera:
    mapa = input('Desea ver los asientos disponibles? S: SI, Cualquier otra tecla: NO ').lower()
    if mapa == 's':
        dibujarMapa()
    
    isOk = False
    while not isOk:
        asiento = int(input("Elija un valor entre 0 y 9 para su ASIENTO: "))
        fila = int(input("Elija un valor entre 0 y 9 para su FILA: "))

        if asiento <= 9 and  asiento >= 0:
            if fila <= 9 and  fila >= 0:
                isOk = True
            else:
                print('El numero de fila no es valido')
        else:
            print('El numero de asiento no es valido')

    if array_2d[fila][asiento] == 'L':
        array_2d[fila][asiento] = 'X'
        print("El asiento fue reservado correctamente")
        bandera = True
    else:
        print("El asiento está ocupado")

    pregunta = input("¿Desea finalizar la reserva? S: si, Cualquier otra tecla NO ").lower()
    if pregunta != 's':
        bandera = False
    else:
        bandera = True