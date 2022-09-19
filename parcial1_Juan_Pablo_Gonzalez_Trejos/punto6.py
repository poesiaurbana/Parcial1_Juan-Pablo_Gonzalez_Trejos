class Banco:
	"""se crea la clase banco y se asignan unos atributos"""
	def __init__(self):
		self.cliente1=Cliente("Andres")
		self.cliente2=Cliente("Luis")
		self.cliente3=Cliente("Juan")

	def operacion(self):
		"""Este metodo Permite realizar la operacion"""
		self.cliente1.depositar(1000)
		self.cliente2.depositar(300)
		self.cliente3.depositar(43)
		self.cliente1.extraer(400)

	def depositos(self):
		"""Metodo que permite obtener los depositos totales"""
		total=self.cliente1.Mostrar_Total()+self.cliente2.Mostrar_Total()+self.cliente3.Mostrar_Total()
		print("El total de dinero del banco es: ",total)
		self.cliente1.imprimir()
		self.cliente2.imprimir()
		self.cliente3.imprimir()

class Cliente:
	"""Se crea la clase cliente y se inicializa con los atributos nombte y cantidad esta clase recibe 
    	como atributo el nombre de la clase anterior"""
	def __init__(self,nombre):
		self.nombre=nombre
		self.cantidad=0

	def depositar(self,cantidad):
		"""metodo que permite realizar el deposito del dinero"""
		self.cantidad+=cantidad

	def extraer(self,cantidad):
		"""Metodo para extraer el dinero"""
		self.cantidad-=cantidad

	def Mostrar_Total(self):
		"""metodo que permite obtener la cantidad total de dinero"""
		return self.cantidad

	def imprimir(self):
		"""Metodo para imprimir los datos del cliente"""
		print(self.nombre, " tiene depositada una cantidad de ",self.cantidad)

banco1=Banco()
banco1.operacion()
banco1.depositos()