"""
Ejercicio 2
Creación
Sobre el ejercicio anterior realizar la siguiente modificación.

Si en el ejercicio hacemos un print(alumno1.nota) esto nos devolverá la nota del alumno. Esto puede llegar a ser un problema de seguridad, vamos a encapsular el código para que no podamos acceder directamente a las variables, y el acceso tenga que ser a través de métodos.

Hacer que las variables de la clase sean privadas. Recordatorio: Añadir doble guion delante del nombre de la variable
Crea métodos getter y setter para poder acceder y modificar las variables de la clase
Experimentación
Crea algunos alumnos
Comprueba que solo podamos acceder a las variables de la clase a través de sus métodos get y set
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
        self.__nombre = nombre
        self.__nota = nota
        print("El alumno ha sido creado")
    
    # Getters
    @property
    def nombre(self):
        """Método getter del atributo nombre"""
        #print("ESTOY EN EL GETTER DE NOMBRE")
        return self.__nombre

     # Setters
    @nombre.setter
    def nombre(self, nuevoNombre):
        """Método setter del atributo nombre"""
        #print("ESTOY EN EL SETTER DE NOMBRE")
        self.__nombre = nuevoNombre
        
    # Getters
    @property
    def nota(self):
        """Método getter del atributo nota"""
        #print("ESTOY EN EL GETTER DE NOTA")
        return self.__nota

     # Setters
    @nota.setter
    def nota(self, nuevaNota):
        """Método setter del atributo nota"""
        #print("ESTOY EN EL SETTER DE NOTA")
        self.__nota = nuevaNota
        
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
print("El alumno 1 tiene la nota: {} " .format(a1.nota))
print("El alumno 2 es: {} " .format(a2.nombre))
print("El alumno 2 tiene la nota: {} " .format(a2.nota))
print("El alumno 3 es: {} " .format(a3.nombre))
print("El alumno 3 tiene la nota: {} " .format(a3.nota))
print("El alumno 4 es: {} " .format(a4.nombre))
print("El alumno 4 tiene la nota: {} " .format(a4.nota))
a1.calificacion(a1.nota)
a2.calificacion(a2.nota)
a3.calificacion(a3.nota)
a4.calificacion(a4.nota)