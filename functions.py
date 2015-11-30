from random import randint

# Renpli un tableau avec des valeurs random (0 ou 1)
def fillArray(array):
	length = len(array)
	for i in range(0, length):
		array[i] = randint(0,1)

# Retourne la valeur du ET logique des entrees du tableau donne
def andFunction(array):
	length = len(array)
	output = 1
	for i in range(0, length):
		output = array[i] & output
	return output

# Retourne la valeur du OU logique des entrees du tableau donne
def orFunction(array):
	length = len(array)
	output = 0
	for i in range(0, length):		
		output = array[i] | output
	return output

# Utilise le neurone passe en parametre le nombre de fois desire (iteration)
# sur un tableau de taille donne (inputsNumber)
# On peut choisir si le neurone est en mode apprentissage ou pas (learn)
# Le parametre function permet de definir la fonction a utiliser
def useNeurone(neurone, inputsNumber, iteration, function, learn = 0):
	# Initialise le tableau d'entrees
	inputs = []
	for i in range(0, inputsNumber):
		inputs.append(0)
	# effectue le nombre d'iterations desire
	for i in range(0,iteration):
		# on remplit le tableau avec des valeurs random (0 ou 1)
		fillArray(inputs)
		# si le neurone est en mode apprentissage : on lui passe la valeur de sortie voulue
		if learn == 1:
			# Selon la fonction desiree, on appelle la fonction correspondante
			# fonction ET
			if function == 1:
				neurone.reasonProcess(inputs, andFunction(inputs))
			# fonction OU
			elif function == 0:
				neurone.reasonProcess(inputs, orFunction(inputs))
		# sinon on demande au neurone le resultat 
		else:
			neurone.reasonProcess(inputs)

# Permet d'utiliser un neurone qui repond a la porte ET
def useAndNeurone(neurone, inputsNumber, iteration, learn = 0):
	useNeurone(neurone, inputsNumber, iteration, 1, learn)

# Permet d'utiliser un neurone qui repond a la porte OU
def useOrNeurone(neurone, inputsNumber, iteration, learn = 0):
	useNeurone(neurone, inputsNumber, iteration, 0, learn)