class Ticket:
    def __init__(self, numero, fila, asiento, fecha_compra, fecha_validez, precio):
        self.numero = numero
        self.fila = fila
        self.asiento = asiento
        self.fecha_compra = fecha_compra
        self.fecha_validez = fecha_validez
        self.precio = precio

listaTickets = []

Ticket1 = Ticket(numero=4, fila=3, asiento=5, fecha_compra="15/21/2023", fecha_validez="15/21/2023", precio=2045)
Ticket2 = Ticket(numero=5, fila=3, asiento=6, fecha_compra="15/21/2023", fecha_validez="15/21/2023", precio=2045)
Ticket3 = Ticket(numero=6, fila=2, asiento=7, fecha_compra="15/21/2023", fecha_validez="15/21/2023", precio=2045)

listaTickets.append(Ticket1)
listaTickets.append(Ticket2)
listaTickets.append(Ticket3)

#Sumar precios
Sumatoria = 0

for ticket in listaTickets:
    Sumatoria = Sumatoria + ticket.precio

print("La sumatoria de todos los precios es de: ", Sumatoria)

#Pedir fila al usurio
bandera= False
fila = int(input('Ingrese un numero de fila: '))

for ticket in listaTickets:
    if ticket.fila == fila:
        print("Número de ticket:", ticket.numero)
        print("Fila:", ticket.fila)
        print("Asiento:", ticket.asiento)
        print("Fecha de compra:", ticket.fecha_compra)
        print("Fecha de validez:", ticket.fecha_validez)
        print("Precio:", ticket.precio)
        print('')
        bandera = True
    
if bandera == False:
    print('La fila que ingresaste no cuenta con datos:')