class Persona():
    """se crea la clase alumno y se inicializan los atributos de la clase, nombre y edad. """
    def __init__ (self,nombre,edad):
        self.nombre=nombre
        self.edad= edad
        
    def imprimir(self): 
        """se crea un metodo que permite visualizar los atributos de la clase """   
        print("Nombre: ",self.nombre)
        print("edad: ",self.edad)
        
    def validacion(self):
        """se crea un metodo con un condicional que valida si la persona es mayor de edad. """
        if self.edad >= 18:
            print ("Mayor de Edad")
        else:
            print("Es Menor de edad")  
            
Persona1 = Persona("Juan",18)
Persona1.imprimir()
Persona1.validacion()
#Se crea una instancia llamada Persona1 y se le envian unos atributos al constructor 
#se llama al metodo imprimir y que muestrta en pantalla los datos de la instancia
#Se llama al metodo validacion para saber si la instancia cumple con la validacion 