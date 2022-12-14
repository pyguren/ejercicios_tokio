num1 = float(input("Dime cuantos numeros quieres ingresar: "))
num2 = []
i = 0

while i < num1:
    numUsuario= float(input("Cual numero quieres ingresar: "))
    num2.append(numUsuario) 
    #print("El numero ingresado es: ", i + 1)
    i += 1
    
# Mostrar los numeros que se ingresaron por pantalla
print("Los numeros que ingresastes son: ", num2)

# Mostrar los mismos numeros ingresados pero ordenados de menor a mayor
num2.sort()
print("Los numeros que ingresastes ordenados de menor a moyor son: ", num2)

#Obtener el promedio de los numeros ingresados

promedio = sum(num2) / num1
print("El promedio de los numeros ingresados es: ", promedio)


# Seleccionar el numero mas grande y mas pequeño de los que se ingresaron por pantalla
# Esta forma es mediante la funcion max y min

print("El numero mayor de la lista es: ", max(num2))
print("El numero mayor de la lista es: ", min(num2))

# Seleccionar el numero mas grande y mas pequeño de los que se ingresaron por pantalla
# Esta forma es mediante ciclo for


numMax = num2[0]
numMin = num2[0]

for n in range (0, len(num2)):
    if num2[n] > n:
        numMax = num2[n]
    if num2[n] < n:
        numMin = num2[n]
        
# Este ciclo for mostrará por pantalla cual es el numero mas grande y mas pequeño de las listas
        
print("El numero mas grande ingresado es: ", numMax)
print("El numero mas pequeño ingresado es: ", numMin)


