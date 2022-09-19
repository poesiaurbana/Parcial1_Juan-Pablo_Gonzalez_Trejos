class Triangulo():
    """Se crea la clase triangulo y se asignan los atributos a dicha clase,osea cada 
        uno de los lados del triangulo"""
    def __init__ (self,lado1,lado2,lado3):
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3
    def imprimir(self):   
        """se crea un metodo para visualizar los atributos de la clase""" 
        print("Lados del Triangulo: ")
        print("lado1: ",self.lado1)
        print("lado2: ",self.lado2)
        print("lado3: ",self.lado3)
        
    def ladomayor(self):
        """este metodo permite saber cual es el lado mayor del triangulo"""
        if self.lado1>self.lado2 and self.lado1>self.lado3:
            print("lado mayor:", self.lado1)
        else: 
            print("lado mayor:", self.lado3)
            
    def equiso (self):
        """Este metodo permite determinar que tipo de triangulo es
            si uno de los lados es cero se imprimira un mensaje"""
        if self.lado1 == 0 or self.lado2 == 0 or self.lado3 == 0:
            print("no pueden haber lados con longitud cero")
        elif self.lado1 == self.lado2 and self.lado1== self.lado3:
            print("El Triangulo es: equilatero")    
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("El Triangulo es: isoceles")  
        else:
            print("El triangulo Ingresado es: escaleno")   
            
Triangulo1 = Triangulo(0,0,0) #se crea una instancia 
Triangulo1.imprimir() #se imprimen los parametros de la instancia
Triangulo1.ladomayor() #se imprime ual es el lado mayor
Triangulo1.equiso() #se imprime que tipo de triangulo es

 
        