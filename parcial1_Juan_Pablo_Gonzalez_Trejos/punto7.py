class Cuenta:
	"""Se crea la clase cuenta y se inicializan los atributos de la clase"""
	def __init__(self,titular,cantidad):
		self.titular=titular
		self.cantidad=cantidad

	def imprimir(self):
		"""Se imprimen los datos"""
		print("Titular: ",self.titular)
		print("Cantidad: ", self.cantidad)

class CajaAhorro(Cuenta):
	"""se crea la clase cajaAhorro, esta clase hereda atributos de la clase cuenta
    	y se inicializan los atributod de la clase"""

	def __init__(self,titular,cantidad):
		super().__init__(titular,cantidad)

	def imprimir(self):
		"""Este metodo permite imprimir los atributos de caja de ahorro heredados de la clase cuenta """
		print("Cuenta de caja de ahorros")
		super().imprimir()

class PlazoFijo(Cuenta):
	"""Se crea la clase PlazoFijo, esta clase tambien hereda atributos de la clase Cuenta
    	y se inicializan los atributos de la clase"""
	def __init__(self,titular,cantidad,plazo,interes):
		super().__init__(titular,cantidad)
		self.plazo=plazo
		self.interes=interes

	def ganancia(self):
		"""Este metodo permite calcular la ganancia"""
		ganancia=self.cantidad*self.interes/100
		print("El importe de interés es: ",ganancia)

	def imprimir(self):
		"""Este metodo permite imprimir los resultados"""
		print("Cuenta a plazo fijo")
		super().imprimir()
		print("Plazo disponible en días: ",self.plazo)
		print("Interés: ",self.interes)
		self.ganancia()


caja1=CajaAhorro("Manuel",5000)
caja1.imprimir()

plazo1=PlazoFijo("Isabel",8000,365,1.2)
plazo1.imprimir()