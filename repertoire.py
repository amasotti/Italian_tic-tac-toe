def benvenuto():
	print('''   TTTTTTTTTTTTTTTTTTTTTTTRRRRRRRRRRRRRRRRR   IIIIIIIIII   SSSSSSSSSSSSSSS 
	T:::::::::::::::::::::TR::::::::::::::::R  I::::::::I SS:::::::::::::::S
	T:::::::::::::::::::::TR::::::RRRRRR:::::R I::::::::IS:::::SSSSSS::::::S
	T:::::TT:::::::TT:::::TRR:::::R     R:::::RII::::::IIS:::::S     SSSSSSS
	TTTTTT  T:::::T  TTTTTT  R::::R     R:::::R  I::::I  S:::::S            
	        T:::::T          R::::R     R:::::R  I::::I  S:::::S            
	        T:::::T          R::::RRRRRR:::::R   I::::I   S::::SSSS         
	        T:::::T          R:::::::::::::RR    I::::I    SS::::::SSSSS    
	        T:::::T          R::::RRRRRR:::::R   I::::I      SSS::::::::SS  
	        T:::::T          R::::R     R:::::R  I::::I         SSSSSS::::S 
	        T:::::T          R::::R     R:::::R  I::::I              S:::::S
	        T:::::T          R::::R     R:::::R  I::::I              S:::::S
	      TT:::::::TT      RR:::::R     R:::::RII::::::IISSSSSSS     S:::::S
	      T:::::::::T      R::::::R     R:::::RI::::::::IS::::::SSSSSS:::::S
	      T:::::::::T      R::::::R     R:::::RI::::::::IS:::::::::::::::SS 
	      TTTTTTTTTTT      RRRRRRRR     RRRRRRRIIIIIIIIII SSSSSSSSSSSSSSS 

	                                    ''')
	print("\nBenvenuti ad una nuova partita a Tris")

# definisco lo scheletro della griglia
griglia_vuota = '   |   |   '
linea_griglia = '-----------'
centrante = '   '*10

# step 1

def tastierino(a,b,c):
	print(centrante + ' '+ a + ' | ' + b +' | '+ c +' ')

def mostra_griglia(griglia):
	print('\n'*150)
	print(centrante + griglia_vuota)
	tastierino(griglia[7],griglia[8],griglia[9])
	print(centrante + griglia_vuota)
	print(centrante + linea_griglia)
	print(centrante + griglia_vuota)
	tastierino(griglia[4],griglia[5],griglia[6])
	print(centrante + griglia_vuota)
	print(centrante + linea_griglia)
	print(centrante + griglia_vuota)
	tastierino(griglia[1],griglia[2],griglia[3])
	print(centrante + griglia_vuota)

# Step 2 : Write a function that can take in a player input and assign their marker as 'X' or 'O'.

def player_input():
	marker = ' '
	while not (marker.lower() == 'x' or marker.lower() == 'o'):
		marker = str(input('Vuoi usare la "x" o la "o"? '))
		marker = marker.upper()
	if marker == 'X':
		return ('X','O')
	elif marker == 'O':
		return ('O','X')

# Step3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9)
# # and assigns it to the board.

def posiziona_marker(griglia, marker, posizione):
	griglia[posizione] = marker

# Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.

def controlla_vincitore(griglia, mark):
	return ((griglia[7] ==  griglia[8] ==  griglia[9] == mark) or
    (griglia[4] ==  griglia[5] ==  griglia[6] == mark) or 
    (griglia[1] ==  griglia[2] ==  griglia[3] == mark) or 
    (griglia[7] ==  griglia[4] ==  griglia[1] == mark) or 
    (griglia[8] ==  griglia[5] ==  griglia[2] == mark) or 
    (griglia[9] ==  griglia[6] ==  griglia[3] == mark) or 
    (griglia[7] ==  griglia[5] ==  griglia[3] == mark) or 
    (griglia[9] ==  griglia[5] ==  griglia[1] == mark))

# Step 5: Write a function that uses the random module to randomly decide which player goes first.

import random

def inizia_per_primo():
	numero_a_caso = random.randint(0,1)
	if numero_a_caso == 1:
		return 'Giocatore 1'
	else:
		return 'Giocatore 2'

# Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.

def controlla_disponibilita(griglia,posizione):
	# Opzionale: stampa cosa c'é nella cella selezionata
	#if griglia[posizione] == "X" or griglia[posizione] == "O":
	#	print('Alla posizione ', posizione, "c'è già un ",griglia[posizione])
	#else:
	#	print('La posizione', posizione, ' è vuota al momento')
	return not (griglia[posizione] == "X" or griglia[posizione] == "O")

# Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise

def controllo_saturazione(griglia):
	for i in range(1,10):
		if controlla_disponibilita(griglia,i):
			return False
	return True

# Step 8: Write a function that asks for a player's next position (as a number 1-9) and
# then uses the function from step 6 to check if it's a free position.
# If it is, then return the position for later use.

def scelta(griglia):
	posizione = 0
	while posizione not in [i for i in range(1,10)] or not controlla_disponibilita(griglia,posizione):
		posizione = int(input('Scegli la tua casella (1-9): '))
	return posizione

# Step 8: Write a function that asks the player if they want to play again
# and returns a boolean True if they do want to play again.

def rivincita():
	ancora = 'wrong'
	while not (ancora.lower() == 'y' or ancora.lower() == 'n'):
		ancora = input("Ne facciamo un'altra (y/n)? ")
	if ancora.lower() == 'n':
		return False
	else:
		return True

# Step 10: hard part ---------------------
# Use while loops and the functions you've made to run the game!

# see file gioco.py