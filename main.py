from neurone import neurone
from functions import *

# Instancier deux neurones AND
neuroneAND = neurone(1)
neuroneAND2 = neurone(1)
# Instancier un neurone OR (va utiliser les sorties des deux premiers neurones)
neuroneOR = neurone()

# Desactive le mode debug : n'affiche plus la sortie pendant l'apprentissage
neuroneAND.setDebug(1)
neuroneAND2.setDebug(1)
neuroneOR.setDebug(1)

# Nombre d'apprentissage a faire pour chaque neurone
learnNumber = 4
# Nombre d'essais a faire pour chaque neurone
tryNumber = 5
# Definit le nombre d'entres des neurones
inputsNumber = 2

# Permet de stocker les valeurs de sorties des deux premiers neuronnes
outputs1 = []
outputs2 = []

'''---------------------------NEURONE 1-----------------------------'''
# jeu d'apprentissage premiere porte AND
print ("---------APPRENTISSAGE-1-------- PORTE ET")
# On utilise le neurone "neuroneAND" avec "inputsNumber" entrees, on l'utile "learnNumber" fois en mode apprentissage "1"
useAndNeurone(neuroneAND, inputsNumber, learnNumber, 1)
neuroneAND.showWeight()
print ''

# jeu d'essai premiere porte AND
print ("---------ESSAIS-1-------- PORTE ET")
# On utilise le neurone "neuroneAND" avec "inputsNumber" entrees, on l'utile "tryNumber" fois en mode non-apprentissage
useAndNeurone(neuroneAND, inputsNumber, tryNumber)
print ''


'''---------------------------NEURONE 2-----------------------------'''
# jeu d'apprentissage deuxieme porte AND
print ("---------APPRENTISSAGE-2-------- PORTE ET")
# On utilise le neurone "neuroneAND2" avec "inputsNumber" entrees, on l'utile "learnNumber" fois en mode apprentissage "1"
useAndNeurone(neuroneAND2, inputsNumber, learnNumber, 1)
neuroneAND2.showWeight()
print ''

# jeu d'essai deuxieme porte AND
print ("---------ESSAIS-2-------- PORTE ET")
# On utilise le neurone "neuroneAND2" avec "inputsNumber" entrees, on l'utile "tryNumber" fois en mode non-apprentissage
useAndNeurone(neuroneAND2, inputsNumber, tryNumber)
print ''


'''---------------------------NEURONE 3-----------------------------'''
# jeu d'apprentissage porte OR
print ("---------APPRENTISSAGE--------- PORTE OU")
# On utilise le neurone "neuroneOR" avec "2" entrees, on l'utilise "learnNumber" fois en mode apprentissage "1"
useOrNeurone(neuroneOR, 2, learnNumber, 1)
neuroneOR.showWeight()
print ''


# On recupere toutes les sorties des deux neurones precedents
outputs1 = neuroneAND.getAllOutputs()
outputs2 = neuroneAND2.getAllOutputs()

# jeu d'essai porte OR
# L'entree de la porte OR est la sortie des deux portes AND precedentes
print ("---------ESSAIS--------- PORTE OU")
# On rempli le tableau avec les sorties des deux premiers neurones
for i in range(0,tryNumber):
	inputs = [outputs1[i], outputs2[i]]

# On utilise le neurone "neuroneOR" avec "2" entrees, on l'utile "tryNumber" fois en mode non-apprentissage
useOrNeurone(neuroneOR, 2, tryNumber)
print ''


