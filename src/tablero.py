import numpy as np
from constants import *

class Tablero:
    dimensionX = 0
    dimensionY = 0
    posiciones = None
    
    def __init__(self):
        self.dimensionX = N_FILAS
        self.dimensionY = N_COLUMNAS 
        
    def rellenarTablero(self, caracter):
        self.posiciones = np.full((self.dimensionX, self.dimensionY), caracter)
        
    def comprobarCoordenada(self, coordenada):
        if self.posiciones[coordenada[1]-1][coordenada[0]-1] == BARCO:
            print("Hemos dado en barco", coordenada)
            self.pintarCoordenada(coordenada, DISPARO_BARCO)
            return True
        else:
            print("Hemos dado en agua", coordenada)
            self.pintarCoordenada(coordenada, DISPARO_AGUA)
            return False
    
    def pintarCoordenada(self, coordenada, caracter):
        self.posiciones[coordenada[1]-1][coordenada[0]-1] = caracter
    
    def mostrarTablero(self):
        print(self.posiciones)
    
    def generarCoordenadaAleatoria(self):
        return (np.random.randint(1,self.dimensionX), np.random.randint(1,self.dimensionY))
    
    def pintarBarcoAleatorio(self):
        self.pintarCoordenada(self.generarCoordenadaAleatoria(), BARCO)
    
    def pintarBarco(self, coordenada):
        self.pintarCoordenada(coordenada, BARCO)
        