class Agenda:
    """Se crea la clase agenda con un diccionario como atributo para almacenar los datos"""

    def __init__(self):
        self.contactos={}

    def menu(self):
        """Se crea el metodo menu que permite visualizar el menu y las condiciones para cada uno de ellos"""
        opcion=0
        while opcion!=5:
            print("1- Añadir Contacto")
            print("2- Lista de Contactos")
            print("3- Buscar Contacto")
            print("4- Editar Contacto")
            print("5- Salir")
            opcion=int(input("Ingrese su opcion:"))
            if opcion==1:
                self.Agregar()
            elif opcion==2:
                self.lista()
            elif opcion==3:
                self.consultar()
            elif opcion==4:
                self.modificar()

    def Agregar(self):
        """metodo que permite agregar los contactos de la agenda"""
        nombre=input("Ingrese el nombre de la persona:")
        telefono=input("Ingrese el numero de telefono:")
        mail=input("Ingrese el correo:")
        self.contactos[nombre]=(telefono,mail)
        print("______________________________________________")
        
    def lista(self):
        """Permite listar los contactos ya añadidos"""
        print("______________________________________________")        
        print("Lista de Contactos")
        for nombre in self.contactos:
            print(nombre, self.contactos[nombre][0],self.contactos[nombre][1])
        print("______________________________________________")

    def consultar(self):
        """Permite consultar algun contacto de los ya ingresados"""
        print("______________________________________________")        
        nombre=input("Ingrese el nombre de la persona :")
        if nombre in self.contactos:
            print(nombre," telefono: ",self.contactos[nombre][0],"Correo: ",self.contactos[nombre][1])
        else:
            print("No existe un contacto con ese nombre")
        print("______________________________________________")            

    def modificar(self):
        """Permite modificar algun contacto"""
        print("______________________________________________")        
        nombre=input("Ingrese el nombre de la persona a modificar:")
        if nombre in self.contactos:
            telefono=input("Ingrese el nuevo telefono:")
            mail=input("Ingrese el nuevo Correo:")
            self.contactos[nombre]=(telefono,mail)
        else:
            print("No existe un contacto con ese nombre")
        print("______________________________________________")         
        
        
agenda=Agenda()
agenda.menu()