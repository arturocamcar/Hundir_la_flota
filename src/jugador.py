from constants import *
from tablero import * 

class Jugador:
    tipo = TIPOS_JUGADORES[0]
    tableroBarcos = None
    tableroDisparos = None
    contadorBarcosHundidos = 20
    turnoActual = False
    
    def __init__(self, tipoJugador):
        self.tipo = tipoJugador
        self.tableroBarcos = Tablero()
        self.tableroDisparos = Tablero()
        self.tableroBarcos.rellenarTablero(AGUA)
        self.tableroDisparos.rellenarTablero(AGUA)
        self.turnoActual = True
    
    def disparo(self, coordenada):
        return self.marcarBarco(coordenada)
            
    def disparoAleatorio(self):
        coordenadaAleatoria = self.tableroBarcos.generarCoordenadaAleatoria()
        return coordenadaAleatoria, self.marcarBarco(coordenadaAleatoria)

    def marcarDisparo(self, coordenada, tocado):
        if tocado:
            print(self.tipo)
            self.tableroDisparos.pintarCoordenada(coordenada,DISPARO_BARCO)
        else:
            print(self.tipo)
            self.tableroDisparos.pintarCoordenada(coordenada,DISPARO_AGUA)
    
    def marcarBarco(self, coordenada):
        if self.tableroBarcos.comprobarCoordenada(coordenada):
            self.contadorBarcosHundidos -= 1
            print("Quedan solo: ", self.contadorBarcosHundidos)
            return True
        else:
            return False
    
    def colocarBarcos(self):
        """
        # Barco posiciones manuales
        # Lanchas
        self.tableroBarcos.pintarBarco((2,2))
        self.tableroBarcos.pintarBarco((9,2))
        self.tableroBarcos.pintarBarco((9,5))
        self.tableroBarcos.pintarBarco((1,10))
        
        # Cruceros
        self.tableroBarcos.pintarBarco((1,5))
        self.tableroBarcos.pintarBarco((2,5))
        self.tableroBarcos.pintarBarco((7,4))
        self.tableroBarcos.pintarBarco((8,4))
        self.tableroBarcos.pintarBarco((5,9))
        self.tableroBarcos.pintarBarco((5,10))
        
        # Submarinos
        self.tableroBarcos.pintarBarco((3,7))
        self.tableroBarcos.pintarBarco((3,8))
        self.tableroBarcos.pintarBarco((3,9))
        self.tableroBarcos.pintarBarco((8,9))
        self.tableroBarcos.pintarBarco((9,9))
        self.tableroBarcos.pintarBarco((10,9))
        
        # Buque
        self.tableroBarcos.pintarBarco((5,2))
        self.tableroBarcos.pintarBarco((5,3))
        self.tableroBarcos.pintarBarco((5,4))
        self.tableroBarcos.pintarBarco((5,5))
    """


    def getTableroDisparos(self):
        print(self.tipo)
        return self.tableroDisparos

    
    def getTableroBarcos(self):
        print(self.tipo)
        return self.tableroBarcos