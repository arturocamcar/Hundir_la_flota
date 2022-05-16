from shutil import SameFileError
from jugador import * 

from numpy import true_divide

def aplicarTurno(jugador, coordenada, tocado):
    jugador.turnoActual = tocado
    jugador.getTableroBarcos().mostrarTablero()
    jugador.marcarDisparo(coordenada, tocado)
    jugador.getTableroDisparos().mostrarTablero()
    return tocado

def turnoJugador(jugador, contrincante):
    # Jugador persona
    #try:
        if jugador.tipo == TIPOS_JUGADORES[1]:
            coordenadaFija = eval(input("Introducir una coordenada de 0 a 9 para (X,Y): "))
            tocado = contrincante.disparo(coordenadaFija)
            return aplicarTurno(jugador, coordenadaFija, tocado)
        elif jugador.tipo == TIPOS_JUGADORES[0]:
            disparoAleatorio = contrincante.disparoAleatorio()
            return aplicarTurno(jugador, disparoAleatorio[0], disparoAleatorio[1])

    #except ValueError:
       # print("No ha introducido un numero entero. Por favor, vuelva a intentarlo", coordenadaFija)
        

def empezarPartida():
    # Inicializamos jugadores y sus tableros
    jugador1 = Jugador(TIPOS_JUGADORES[1])
    jugador2 = Jugador(TIPOS_JUGADORES[0])

    jugador1.colocarBarcos()
    jugador2.colocarBarcos()
    
    while True:
        mensaje_inicial = """
        ¡Bienvenido a Hundir la Flota!
        Inserta 1 para jugar
        Inserta 2 para ver las instrucciones del juego
        Inserta 3 para salir del juego
        """
        print(mensaje_inicial)
        
        opcion = int(input("Inserta opción: "))
        if opcion == 1:
            if turnoJugador(jugador1, jugador2):
                print("Turno ", jugador1.turnoActual)
            elif turnoJugador(jugador2, jugador1):
                print("Turno ", jugador2.turnoActual)
        elif opcion == 2:
            mostrarReglas()
        else:
            break


def mostrarReglas():
    instrucciones = '''
    
    INSTRUCCIONES HUNDIR LA FLOTA:

    2 jugadores: tú y la máquina.
    El juego consiste en hundir la flota del contrincante, la máquina, en nuestro caso. 
    Para ello, tendrás que adivinar las coordenadas en las que estan posicionados sus barcos.
    Cada jugador tendrá dos tableros de 10x10:

        - Tablero Barcos: tablero con 10 barcos, colocados aleatoriamente. Los barcos se representan en el tablero con una letra "O" mayuscula.
            Cada jugador tiene 10 barcos en su Tablero Barcos:
                1 Buque: barco de eslora 4 
                2 Submarinos: barco de eslora 3
                3 Cruceros: barco de eslora 2
                4 Lanchas: barcos de eslora 1
                *Eslora = número de posiciones que ocupa el barco en el tablero  

        - Tablero Disparos: tablero donde se marcarán los disparos al 'Tablero Barcos' del contrincante. 
    Cada jugador dispone de un turno de disparo que se irá alternando. 
    En su turno de disparo, deberá decir las coordenadas en las que cree que su contrincante ha colocado un barco:
        Coordenadas: (fila, columna)
            El juego le pedirá un número del 0 al 9 para seleccionar una fila, y otro numero del 0 al 9 para seleccionar la columna. 
            Con los números de fila y columna, tenemos la coordenada de disparo.
            Si acierta, marcamos la casilla en el tablero disparos con una letra "X" que representa el barco, o la parte del barco, que estaba en esa casilla.
            Si acierta, puede volver a disparar.
            Si falla, marcamos la casilla en el tablero disparos con una letra "-", que representa el disparo en el agua.
            Si falla, es el turno de disparo de su contrincante.
    Gana el jugador que antes consiga hundir la flota del otro.
    '''
    print(instrucciones)



    #print("Estas son las reglas a mostrar----> TODO")
    
def mostrarMenu():
    mostrarReglas()
    empezarPartida()

if __name__ == "__main__":
    mostrarMenu()