# La classe neurone permet d'instancier un neurone a nombre d'entrees variables
# definit par la taille du premier tableau d'entrees envoye.
# Elle permet de faire une weightedSum ponderee des entrees donnees avec une fonction threshold
# qui retourne 1 si le resultat de la weightedSum est superieur a 0.
# Ce neurone est capable d'apprendre lorsque la second parametre de la fonction reasonProcess
# est la sortie attendue.
class neurone:

    # Constructeur de la classe
    def __init__(self):
        # nombre d'entrees du neurone
        self.inputLength = 0
        # flag qui permet de savoir si le nombre d'entrees est definit
        self.first = 0
        # Valeur de la sortie du neurone
        self.output = 0
        # Tableau des valeurs des entrees du neurone
        self.inputs = []
        # Tableau des poids qui correspondent aux entrees du neurone
        self.weights = []

    # Ajuste les poids des entrees (uniquement si la sortie est mauvaise)
    # On parcoure nos entrees et pour chaque on verifie si elle correspond a la sortie
    # Si oui, on augmente le poids de cette entree
    # Si non, on diminue le poids de cette entree
    def adjustWeights(self):
        # Si la sortie est correcte, on ne continue pas
        if self.expected != self.output:
            # Pour chaque entree, on verifie si elle correspond a la sortie
            for i in range(0, self.inputLength):
                if self.inputs[i]*self.weights[i] == self.expected:
                    self.weights[i] += 1
                else:
                    self.weights[i] -= 1

    # Sortie du neurone (fonction threshold)
    # Si la somme ponderee est superieure a 0, sortie = 1
    # Sinon, sortie = 0
    def threshold(self, value):
        # Function seuil
        if value > 0:
            self.output = 1
        else :
            self.output = 0
        return self.output
    # Calcul la somme ponderee en fonction des entrees du neurone
    # Pour chaque entree, on multiplie sa valeur par le poids qui lui correspond
    # Et on additionne les resultats
    def weightedSum(self, inputs, weights):
        # Somme ponderee 
        weightedSum = 0
        # pour chaque entree, on la multiplie par le poids qui y correspond
        for i in range(0, self.inputLength):
            weightedSum += inputs[i] * weights[i]
        # on retourne le resultat de la weightedSum ponderee
        return weightedSum

    # Permet de definir le nombre d'entrees du neurone
    # en fonction du premier tableau envoye
    # Ensuite, verifie que le nombre d'entrees du tableau
    # correspond au nombre d'entrees du neurone
    def inputGate(self, inputs):
        # on regarde le nombre d'entrees recues
        length = len(inputs)
        # si c'est le premier appel, on instancie le tableau de poids a 1
        if self.first == 0:
            for i in range(0, length):
                self.weights.append(1)
            self.first = 1
            self.inputLength = length
        
        # Si la length du tableau correspond au nombre d'entrees,
        # on enregistre les valeurs envoyees et on retourne un "ok"(1)
        if length == self.inputLength:
            self.inputs = inputs
            return 1

        return 0

    # Permet de donner un les entrees aux neurones et la sortie attendue
    # Ainsi, le neurone va pouvoir apprendre si la sortie qu'il donne est mauvaise
    def learningProcess(self, inputs, expected):
        # si la verification du nombre d'entrees est ok, on peut continuer
        if self.inputGate(inputs) == 1:
            # on enregistre la valeur de la sortie correcte
            self.expected = expected
            print ''
            print("entrees = %s" %(inputs))
            # on calcule la weightedSum ponderee de nos entrees
            weightedSum = self.weightedSum(self.inputs, self.weights)
            print ("somme ponderee = %s" %(weightedSum))
            print ("sortie = %s" %(self.threshold(weightedSum)))
            # Si on est en phase d'apprentissage, on ajuste les poids de chaque entree
            if expected != -1:
                self.adjustWeights()
                print ("poids = %s" %(self.weights))
            return 1
        else:
            return 0

    # Permet de demander au neurone un resultat en fonction des entrees donnees
    def reasonProcess(self, inputs):
        # On appelle la fonction d'execution en indiquant que l'on est pas en phase d'apprentissage
        return self.learningProcess(inputs, -1)
