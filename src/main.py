from shutil import SameFileError

from numpy import true_divide

def  menu_principal():
	inicializar_tablero()
	mostrar_tablero()
	mostrar_reglas()
	mostrar_menu()


def comprobar_coordenada():
	print("TODO")

def comprobar_flota_enemiga(coordenada):
	print("TODO")

def generar_coordenada():
	print("TODO")


def mostrar_menu():
	turno_jugador = True
	
	if turno_jugador:
		print("introducir una coordenada(X,Y): ")
		print("recoger input del usuario y guardarlo en coordenada")
		coordenada = (4,9)
		impacto = comprobar_coordenada(coordenada)
		if impacto:
			comprobar_flota_enemiga(turno_jugador)
	else:
		coordenada = generar_coordenada()
		coordenada = (8,2)
		impacto = comprobar_coordenada(coordenada)
		if impacto:
			comprobar_flota_enemiga(turno_jugador)





"""
def acerca_de():
	print("Programado por Laura Ledo y Arturo Campos")


def mostrar_menu ():
	eleccion = ""
	while eleccion != "3":
		menu = """
1. Jugar
2. Acerca de
3. Salir
Elige:"""
		eleccion = input(menu)
		if eleccion == "1":
			jugar()
		elif eleccion == "2":
			acerca_de()
			
def mostrar_menu():
	salir = False
	while True:
		print (f"Turno de {turno_actual}")
		if turno_actual = Jugador1



"""

//Comienza partida
Inicializa tablero
...
Generar barcos jugador1 aleatoriamente
Pintar los barcos con O en tablero del jugador 1
...

i=0
while True

//empieza el while


Si es turno del jugador1:
	Mostramos mensaje --> "Jugador1, por favor introduce una coordenada (X,Y):" 
	prinr(1,2) <-- jugador1  //el jugador 1 introdujo (1,2)
	Comprobamos coordenadas // seguramente será una llamada a uno función de alguna de las clases

	Si hay impacto en algún barco:
		Pintamos X en barco
		Restamos 1 al número total de celdas referentes a barcos
		Si quedan barcos enemigos:
			Fin de la iteración // break
		Si NO quedan barcos enemigos:
			Salir del bucle while // por definir cómo
	Si NO hay impacto en algún barco:
		Pintamos . en agua
		Fin de la iteración
Si NO es turno del jugador1 (es turno de la máquina):
	Generamos coordenadas aleatorias
	Comprobramos coordenadas
	Si hay impacto en algún barco:
		Pintamos X en barco
		Restamos 1 al número total de celdas referentes a barcos
		Si quedan barcos enemigos:
			Fin de la iteración // break
		Si NO quedan barcos enemigos:
			Salir del bucle while // por definir cómo
	Si NO hay impacto en algún barco:
		Pintamos . en agua
		Fin de la iteración


------------------------------------------------------

...
var turno_jugador = true
var condicion_salida = true
while (condicion_salida): 
	if (turno_jugador):
		print("Jugador1, por favor introduce una coordenada (X,Y):")
		(1,2) <-- jugador1  //el jugador 1 introdujo (1,2)
		comprobar_coordenadas(coordenadaX, coordenadaY)
	else:
		tupla_coordenada_aleatoria = generar_coordenadas_aleatorias()
		comprobar_coordenadas(tupla_coordenada_aleatoria[0], tupla_coordenada_aleatoria[1])


comprobar_coordenadas(coordenadaX, coordenadaY):
	if (hay_impacto()):
		tablero_jugador[coordenadaX][coordenadaY] = "X"
		coordenadas_barcos_restantes -= 1
		if (coordenadas_barcos_restantes > 0):
			break
		else:
			condicion_salida = false
	else:
		tablero_jugador[coordenadaX][coordenadaY] = "."

"""