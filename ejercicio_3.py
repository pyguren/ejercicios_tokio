"""Ejercicio de herencia múltiple y polimorfismo:

Crea la clase Vehiculos con un constructor que incluya marca y modelo
Esta clase Vehiculos también tendrá que incluir un método que se llame repostar() el cual imprima por pantalla "Este vehiculo tiene que repostar gasolina"
Crea la clase VElectricos con un constructor que incluya marca, modelo y autonomia
Esta clase VElectricos también tendrá que incluir un método que se llame repostar() el cual imprima por pantalla "Este vehiculo tiene que repostar electricidad"
Crea la clase BicicletaElectrica que herede de Vehiculos y de VElectricos, pero dando prioridad a VElectricos (ya que es un vehículo más electrico que normal)
Crea la clase Quad que herede de Vehiculos y de VElectricos, pero dando prioridad a Vehiculos (ya que sólo usa la electricidad de modo puntual)
Crear un objeto de BicicletaElectrica y otro de Quad
Emplear las técnicas de polimorfismo aprendidas para conseguir que al peguntarle a los objetos que acabamos de crear por su repostaje, ambos nos respondan adecuadamente

"""

class Vehiculos:
    """
    Clase Vehiculos que crea vehiculos a gasolina
    
    Args:
    marca: La marca del vehiculo
    modelo: El modelo del vehiculo
    """
    def __init__(self, marca = None, modelo = None):
        """Constructor de la clase Vehiculos"""
        self.__marca = marca
        self.__modelo = modelo
        print("Se ha creado el vehiculo")
        
    # Getters
    @property
    def marca(self):
        """Método getter del atributo marca"""
        #print("ESTOY EN EL GETTER DE MARCA")
        return self.__marca

     # Setters
    @marca.setter
    def marca(self, nuevaMarca):
        """Método setter del atributo marca"""
        #print("ESTOY EN EL SETTER DE MARCA")
        self.__marca = nuevaMarca
        
    # Getters
    @property
    def modelo(self):
        """Método getter del atributo modelo"""
        #print("ESTOY EN EL GETTER DE MODELO")
        return self.__modelo

     # Setters
    @modelo.setter
    def modelo(self, nuevoModelo):
        """Método setter del atributo modelo"""
        #print("ESTOY EN EL SETTER DE MODELO")
        self.__modelo = nuevoModelo
        
    def repostar(self,vehiculo):
        print("Este vehiculo tiene que repostar gasolina")
        
    # Redefinimos el método string
    def __str__(self):
        """Método str de la clase que retorna un print mostrando la información de la marca y modelo del vehiculo"""
        return "El vehiculo es de marca {} y modelo {}".format(self.marca,self.modelo)

class VElectricos:
    """
    Clase VElectricos que crea vehiculos electricos
    
    Args:
    marca: La marca del vehiculo
    modelo: El modelo del vehiculo
    autonomia: La autonomia del vehiculo
    """
    def __init__(self, marca = None, modelo = None, autonomia = None):
        """Constructor de la clase Vehiculos"""
        self.__marca = marca
        self.__modelo = modelo
        self.__autonomia = autonomia
        print("Se ha creado el vehiculo electrico")
        
    # Getters
    @property
    def marca(self):
        """Método getter del atributo marca"""
        #print("ESTOY EN EL GETTER DE MARCA")
        return self.__marca

     # Setters
    @marca.setter
    def marca(self, nuevaMarca):
        """Método setter del atributo marca"""
        #print("ESTOY EN EL SETTER DE MARCA")
        self.__marca = nuevaMarca
        
    # Getters
    @property
    def modelo(self):
        """Método getter del atributo modelo"""
        #print("ESTOY EN EL GETTER DE MODELO")
        return self.__modelo

     # Setters
    @modelo.setter
    def modelo(self, nuevoModelo):
        """Método setter del atributo modelo"""
        #print("ESTOY EN EL SETTER DE MODELO")
        self.__modelo = nuevoModelo
    
    # Getters
    @property
    def autonomia(self):
        """Método getter del atributo autonomia"""
        #print("ESTOY EN EL GETTER DE AUTONOMIA")
        return self.__autonomia

     # Setters
    @autonomia.setter
    def autonomia(self, nuevaAutonomia):
        """Método setter del atributo autonomia"""
        #print("ESTOY EN EL SETTER DE Autonomia")
        self.__autonomia = nuevaAutonomia
        
    def repostar(self,vehiculo):
        print("Este vehiculo tiene que repostar electricidad")
        
    # Redefinimos el método string
    def __str__(self):
        """Método str de la clase que retorna un print mostrando la información de la marca, modelo y autonomia del vehiculo"""
        return "El vehiculo es de marca {}, modelo {} y tiene una autonomia de {} ".format(self.marca,self.modelo, 
                                                                                           self.autonomia)

class BicicletaElectrica(VElectricos, Vehiculos):
    """
    Clase BicicletaElectrica que crea biciletas electricas. Hereda de VElectricos y de Vehiculos
    
    """
    def __init__(self, marca, modelo, autonomia):
        """Constructor de la clase BiccletaElectrica"""
        VElectricos.__init__(self, marca, modelo, autonomia)
        Vehiculos.__init__(self)
        print("Se ha creado la bicicleta electrica")
        
    # Redefinimos el método string
    def __str__(self):
        return VElectricos.__str__(self)

class Quad(Vehiculos, VElectricos):
    """
    Clase Quad que crea Vehiculos de 4 ruedas. Hereda de Vehiculos y de VElectricos
    
    """
    def __init__(self, marca, modelo):
        """Constructor de la clase Quad"""
        Vehiculos.__init__(self, marca, modelo)
        VElectricos.__init__(self, marca, modelo)
        print("Se ha creado un Quad")
        
    # Redefinimos el método string
    def __str__(self):
        return Vehiculos.__str__(self)    

if __name__ == "__main__":
    
    print("Clase BicicletaElectrica: ")
    v3 = BicicletaElectrica("Shimano", "X25", 110)
    print(v3)
    v3.repostar(v3)
    print("\n***************\n")
    print("Clase Quad: ")
    v4 = Quad("Kawasaki", "Z9")
    print(v4)
    v4.repostar(v4)