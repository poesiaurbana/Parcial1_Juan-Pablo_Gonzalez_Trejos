class Alumno():
    """Se crea la clase Alumno"""
    def __init__ (self,nombre,nota):
        '''se inicializan los atributos de la clase nombre y nota.'''
        self.nombre=nombre
        self.nota= nota
         
    def imprimir(self):    
        """se crea un metodo que permite visualizar los atributos de la clase"""
        print("Nombre: ",self.nombre)
        print("Nota: ",self.nota)
           
    def aprobo(self):
        """se crea un metodo con un condicional que valida si el estudiante aprobo si su nota es es mayor que 3"""
        if self.nota >= 3:
            print ("Aprobo")
        else:
            print("No aprobo")
         
Alumno1 = Alumno("Juan",5)
Alumno1.imprimir()
Alumno1.aprobo()
#Se crea una instancia llamada alumno1 y se le envian unos atributos al constructor 
#se llama al metodo imprimir y que nos envia los datos de la instancia
#Se llama al metodo aprobo para saber si la instancia cumple con la validacion       
    