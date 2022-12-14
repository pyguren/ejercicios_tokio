menu = """
===============================
MENU COMPRA-VENTA
1. Comprar
2. Vender
3. Alquilar
4. Mostrar listas de datos
5. Salir
===============================
"""
print(menu)
opcion = input("Introduzca que desea hacer(1-4): ")
comprar = []
vender = []
alquilar = []
mostrarLista = []

while opcion != "5":

    if opcion == "1":
        item = input("Que desea comprar? ")
        comprar += [item]
        print(menu)
        opcion = input("Introduzca que desea hacer(1-4): ")
    elif opcion == "2":
        vender += [input("Que desea vender? ")]
        print(menu)
        opcion = input("Introduzca que desea hacer(1-4): ")
    elif opcion == "3":
        alquilar += [input("Que desea alquilar? ")]
        print(menu)
        opcion = input("Introduzca que desea hacer(1-4): ")
    elif opcion == "4":
        print("Lista de Compras:", comprar)
        print("Lista de Ventas:", vender)
        print("Lista de Alquiler:", alquilar)
        opcion = input("Introduzca que desea hacer(1-4): ")
    
        
