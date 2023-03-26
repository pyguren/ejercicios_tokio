""" Ejercicio de herencia

Crea la superclase Personal_Universitario con un único atributo que sea un diccionario que incluya: "id", "nombre" y "email"
Crear la clases Oficina, Profesor y Alumno. Todas ellas heredaran de Personal_Universitario y heredaran sus datos
En el caso de Oficina, debe añadir a su diccionario de datos el dato "Puesto"
En el caso de Profesor, debe añadir a su diccionario de datos el dato "Especialización"
En el caso de Alumno, debe añadir a su diccionario de datos el dato "CreditosAprobados" (integer)
Crear métodos que sirvan para mostrar la información de cada clase
Crear objetos de todas las clases
Mostrar la información de esos objetos y comprobar que sale lo que tiene que salir

"""

class Personal_Universitario:
    """
    Clase Personal_Universitario que almacena los datos de las personas dentro de la universidad
    
    Args:
    datos: Este argumento guardará un diccionario con un id, nombre y email de la persona
    """
    def __init__(self, datos):
        """Constructor de la clase Personal_Universitario"""
        self.__datos = datos
        print("Se ha creado un registro de persona")

    # Getters
    @property
    def datos(self):
        """Método getter del atributo datos"""
        #print("ESTOY EN EL GETTER DE DATOS")
        return self.__datos

     # Setters
    @datos.setter
    def datos(self, nuevoDato):
        """Método setter del atributo datos"""
        #print("ESTOY EN EL SETTER DE DATOS")
        self.__datos = nuevoDato
        
        
    def mostrar(self):
        print("ID: {}".format(self.datos["id"]))
        print("Nombre: {}".format(self.datos["nombre"]))
        print("Email: {}".format(self.datos["email"]))
        
        
    # Redefinimos el método string
    def __str__(self):
        """Método str de la clase que retorna un print mostrando la información de los empleados, profesores y alumnos"""
        return "La persona registrada es: {}".format(self.datos)
    

class Oficina(Personal_Universitario):
    def __init__(self, datos, puesto):
        super().__init__(datos)
        self.datos['Puesto'] = puesto
        
    def mostrar_informacion(self):
        print(f"ID: {self.datos['id']}")
        print(f"Nombre: {self.datos['nombre']}")
        print(f"Email: {self.datos['email']}")
        print(f"Puesto: {self.datos['Puesto']}")

        
    # Getters
    @property
    def puesto(self):
        """Método getter del atributo puesto"""
        #print("ESTOY EN EL GETTER DE PUESTO")
        return self.__puesto

     # Setters
    @puesto.setter
    def puesto(self, nuevoPuesto):
        """Método setter del atributo puesto"""
        #print("ESTOY EN EL SETTER DE PUESTO")
        self.__puesto = nuevoPuesto
        
        
    # Redefinimos el método string
    def __str__(self):
        return Personal_Universitario.__str__(self)
        
        
class Profesor(Personal_Universitario):
    def __init__(self, datos, especializacion):
        super().__init__(datos)
        self.datos['Especialización'] = especializacion
        
    def mostrar_informacion(self):
        print(f"ID: {self.datos['id']}")
        print(f"Nombre: {self.datos['nombre']}")
        print(f"Email: {self.datos['email']}")
        print(f"Especialización: {self.datos['Especialización']}")

    
    # Getters
    @property
    def especializacion(self):
        """Método getter del atributo especializacion"""
        #print("ESTOY EN EL GETTER DE ESPECIALIZACION")
        return self.__especializacion

     # Setters
    @especializacion.setter
    def especializacion(self, nuevaEspecializacion):
        """Método setter del atributo especializacion"""
        #print("ESTOY EN EL SETTER DE ESPECIALIZACION")
        self.__especializacion = nuevaEspecializacion
        
        
    # Redefinimos el método string
    def __str__(self):
        return Personal_Universitario.__str__(self)
        
        
class Alumno(Personal_Universitario):
    def __init__(self, datos, creditos_aprobados):
        super().__init__(datos)
        self.datos['CreditosAprobados'] = creditos_aprobados
        
    def mostrar_informacion(self):
        print(f"ID: {self.datos['id']}")
        print(f"Nombre: {self.datos['nombre']}")
        print(f"Email: {self.datos['email']}")
        print(f"Créditos aprobados: {self.datos['CreditosAprobados']}")

        
    # Getters
    @property
    def creditos_aprobados(self):
        """Método getter del atributo creditos_aprobados"""
        #print("ESTOY EN EL GETTER DE CREDITOS APROBADOS")
        return self.__creditos_aprobados

     # Setters
    @creditos_aprobados.setter
    def creditos_aprobados(self, nuevosCreditos_aprobados):
        """Método setter del atributo creditos_aprobados"""
        #print("ESTOY EN EL SETTER DE CREDITOS APROBADOS")
        self.__creditos_aprobados = nuevosCreditos_aprobados
        
        
    # Redefinimos el método string
    def __str__(self):
        return Personal_Universitario.__str__(self)
    
# Creación de 1 objeto por cada clase
datos = {
    'id': 1,
    'nombre': 'Juan',
    'email': 'juan@email.com'
}
oficina1 = Oficina(datos, 'Gerente')

datos = {
    'id': 2,
    'nombre': 'Maria',
    'email': 'maria@email.com'
}
profesor1 = Profesor(datos, 'Matemáticas')

datos = {
    'id': 3,
    'nombre': 'Pedro',
    'email': 'pedro@email.com'
}
alumno1 = Alumno(datos, 80)


print("Información de la Oficina:")
oficina1.mostrar_informacion()
print("\nInformación del Profesor:")
profesor1.mostrar_informacion()
print("\nInformación del Alumno:")
alumno1.mostrar_informacion()
