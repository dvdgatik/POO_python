class CasillaDeVotacion:

	def __init__ (self, identificador, pais):
		self._identificador = identificador
		self._pais = pais
		self._region = None

	@property #decoradores #getters
	def region(self):
		return self._region

	@region.setter #setter
	def region(self, region):
		if region in self._pais:
			self._region = region
		else:
			raise ValueError(f'La region {region} no esta en la lista')

casilla = CasillaDeVotacion(123, ['Ciudad de Mexico', 'Morelos'])

print(casilla.region)

casilla.region = 'Morelos'

print(casilla.region)

