import numpy as np
import random
from constants import *


#VARIABLES METODO CONSTRUCTOR:

#id_jugador 

# 1 - TABLERO INICIAL JUGADOR

tablero_barcos = np.full((dimensiones_tablero), AGUA)    
print("Tablero barcos: \n\n", tablero_barcos)

tablero_disparos = np.full((dimensiones_tablero), AGUA)
print("Tablero disparos: \n\n", tablero_disparos)

# Lista barcos, por eslora:

lista_barcos = [BUQUE[1], SUBMARINO[1], SUBMARINO[1], CRUCERO[1], CRUCERO[1], CRUCERO[1], LANCHA[1], LANCHA[1], LANCHA[1], LANCHA[1]]




def coordenadas_aleatorias():
    
    fila = np.random.randint(10)
    columna = np.random.randint(10)

    return fila, columna

def direccion_aleatoria():

    #Direccion aleatoria (N, S, E, O):
    orientacion = random.choice(['N', 'S', 'E', 'O'])
    return orientacion

#COMPROBAR QUE EL BARCO ENTRA EN EL TABLERO Y LAS POSICIONES SON DE AGUA

def posicion_libre(tablero, fila, columna, orientacion_barco, eslora):
    
    #Coordenadas barco (segun tamaño) en el tablero
    coord_N = tablero[fila:fila - eslora:-1, columna] 
    coord_S = tablero[fila: fila+ eslora, columna]
    coord_E = tablero[fila, columna: columna + eslora]
    coord_O = tablero[fila, columna: columna - eslora:-1]

    if orientacion_barco == "N":

        if 0 <= fila - eslora < 10 and BARCO not in coord_N:
            return True
        else:
            return False

    elif orientacion_barco == "E":

        if 0 <= columna + eslora < 10 and BARCO not in coord_E:
            return True
        else:
            return False

    elif orientacion_barco == "S":

        if 0 <= fila + eslora < 10 and BARCO not in coord_S:
            return True
        else:
            return False

    else: 
        #orientacion_barco == "O":
        if 0 <= columna - eslora < 10 and BARCO not in coord_O:
            return True
        else:
            return False


# POSICIONAR BARCOS ALEATORIAMENTE EN TABLERO

def posicionar_barcos(lista_barcos):
    
    for eslora in lista_barcos:

        n_barcos_tablero = 0

        while n_barcos_tablero != N_BARCOS:
        
            #Coordenadas y direccion Barco
            coordenadas_barco = coordenadas_aleatorias()
            fila_barco = coordenadas_barco[0]
            columna_barco = coordenadas_barco[1]
            orientacion_barco = direccion_aleatoria()

            if posicion_libre(tablero_barcos, fila_barco, columna_barco, orientacion_barco, eslora) == True:

                n_barcos_tablero += 1

                if orientacion_barco == "N":
                    tablero_barcos[fila_barco:fila_barco-eslora:-1, columna_barco] = BARCO
                
                elif orientacion_barco == "S":
                    tablero_barcos[fila_barco:fila_barco + eslora, columna_barco] = BARCO
                
                elif orientacion_barco == "E":
                    tablero_barcos[fila_barco, columna_barco: columna_barco + eslora] = BARCO
                
                else: #orientacion "O"
                    tablero_barcos[fila_barco, columna_barco: columna_barco - eslora:-1] = BARCO
                
                break        

    print(tablero_barcos)