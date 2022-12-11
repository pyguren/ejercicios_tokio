def lee_numero(num):
    numUsuario = int(input("Introduce un numero:"))
    return numUsuario

    """
    Con esta funcion le pido al usuario que introduzca un numero y luego lo guardo en la variable numUsuario
    """


def mayor(num1, num2, num3):
    if num2 < num1 and num1 > num3:
        numMayor = num1
    elif num1 < num2 and num2 > num3:
        numMayor = num2
    elif num1 < num3 and num3 > num2: 
        numMayor = num3
    return numMayor

    """
        Con esta funcion busco el numero mayor de los 3 ingresados por el usuario utlizando operadores relacionales
    """


if __name__ == "__main__":
    num1 = lee_numero(1)
    num2 = lee_numero(2)
    num3 = lee_numero(3)
 
    """
        En esta seccion invoco 3 veces la funcion lee_numero y guardo cada valor ingresado por el usuario en 3 variables
        distintas para luego ocuparlos en la siguiente funcion
    """
  
    numMayor = mayor(num1, num2, num3)
    print("El numero mayor es: ", numMayor)
   