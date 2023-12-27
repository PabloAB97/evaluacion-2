def main():  # Funcion main donde desplegamos el menú y pedimos que se realice una acción acorde al número elegido.
    lista_gastos = []

    while True:
        print("Menú\n 1. Agregar compra\n 2. Mostrar compras\n 3. Mostrar total gastado\n 4. Salir")
        opt = int(input("Seleccione una opción: "))

        if opt == 1:
            agregarCompra(lista_gastos)
        elif opt == 2:
            mostrarCompras(lista_gastos)
        elif opt == 3:
            mostrarTotal(lista_gastos)
        elif opt == 4:
            print("Nos vemos pronto!")
            exit()
        else:
            print("Opción incorrecta, intente nuevamente.")

def agregarCompra(lista):
    try:
        x = int(input("Ingrese el monto de la compra: "))
        lista.append(x)
        print("Compra agregada con éxito!")
    except ValueError:  # Creamos este excepción para cuando se ingrese un valor no númerico.
        print("Ingrese el precio utilizando números por favor.")


def mostrarCompras(lista):
    for i, compra in enumerate(lista):
        print(f"Compra n°{i+1}: {compra}")

def mostrarTotal(lista):
    gasto = 0
    for compra in lista:
        gasto += compra
    print(f"El total gastado es de: {gasto}")

if __name__ == "__main__":
    main()