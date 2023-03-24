"""
Ejercicio 1
Creación
Crea una clase llamada Alumno que tenga los atributos nombre y nota
Crea el constructor de la clase. Añadir en el constructor un print para informar de que el alumno se ha creado con éxito
Sobreescribe el método string (__str__), para que al imprimir por pantalla se vea su informacion
Crear un método llamado calificacion que imprima por pantalla si el alumno ha aprobado o suspendido en base a su nota
Experimentación
Crea algunos alumnos
Prueba a mostrar los objetos alumno y el método calificacion
"""

class Alumno:
    """Clase alumno:
    La siguiente clase busca registrar nuevos alumnos mediante el ingreso del nombre y la nota. Luego imprime
    los datos del alumno y si este aprobo o reprobo en base a su nota.
    
    args:
    - nombre: es un string con el nombre de cada alumno
    - nota: es un integer con la nota final de cada alumno
    
    """
    
    def __init__(self, nombre, nota):
        """Constructor de la clase alumno"""
        self.nombre = nombre
        self.nota = nota
        print("El alumno {} ha sido creado" .format(self.nombre))
        
    def calificacion(self, nota):
        """Método que evalua si el alumno aprobó o reprobó en una escala del 1 al 10, donde 5 es la nota mínima para 
        aprobar"""
        if nota < 5:
            print("El alumno {} ha reprobado la materia con una nota de {}" .format(self.nombre, self.nota))
        else:
            print("El alumno {} ha aprobado la materia con una nota de {}" .format(self.nombre, self.nota))
        
        
    # Redefinimos el método string
    def __str__(self):
        """Método str de la clase que retorna un print mostrando la información del nombre y nota del alumno"""
        return "El alumno {} tiene una nota de {}".format(self.nombre,self.nota)
    
a1 = Alumno("Esteban", 8)
a2 = Alumno("José", 9)
a3 = Alumno("Jaime", 3)
a4 = Alumno("Juan", 4.9)
print("El alumno 1 es: {} " .format(a1.nombre))
#print(a1.nota)
print("El alumno 2 es: {} " .format(a2.nombre))
#print(a2.nota)
print("El alumno 3 es: {} " .format(a3.nombre))
#print(a3.nota)
print("El alumno 4 es: {} " .format(a4.nombre))
#print(a4.nota)
a1.calificacion(a1.nota)
a2.calificacion(a2.nota)
a3.calificacion(a3.nota)
a4.calificacion(a4.nota)