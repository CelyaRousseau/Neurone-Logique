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
        # flag qui permet de savoir si le neurone est deja initialise ou bien si l'on vient de le creer (#recursivite)
        self.first = 1
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

    # Determine la sortie du neurone (fonction seuil)
    # Si la somme ponderee est superieure a 0, sortie = 1
    # Sinon, sortie = 0
    def threshold(self, value):
        # Function seuil
        if value > 0:
            return 1
        else :
            return 0

    # Calcul la somme ponderee en fonction des entrees du neurone
    # Pour chaque entree, on multiplie sa valeur par le poids qui lui correspond
    # Et on additionne les resultats
    def weightedSum(self, inputs, weights):
        # Somme ponderee 
        weightedSum = 0
        # pour chaque entree, on la multiplie par le poids qui y correspond
        for i in range(0, self.inputLength):
            weightedSum += inputs[i] * weights[i]
        # on retourne le resultat de la somme ponderee
        return weightedSum

    # Permet de verifier le tableau d'entrees que l'on passe au neurone
    # est bien egal au nombre d'entrees du neurone
    def checkInputs(self, inputs):
        # si c'est le premier appel, on initialise les entrees du neurone aisi que ses poids
        if self.isFirstCall():
            self.initializeNeurone(inputs)
            return 1
        # Sinon si la longueur du tableau correspond bien au nombre d'entrees,
        # on enregistre les valeurs envoyees et on retourne un "ok" (1)
        elif len(inputs) == self.inputLength:
            self.inputs = inputs
            return 1
        # Sinon on indique a l'utilisateur qu'un probleme est survenu
        else:
            print "you have a problem with your inputs : check the length please"
            return 0

    # Permet de verifier si c'est la premiere fois que l'on lance notre neurone
    def isFirstCall(self):
        return self.first

    # Permet d'initialiser le neurone avec nos premieres entrees
    def initializeNeurone(self, inputs) :
        self.first = 0
        self.inputs = inputs
        self.inputLength = len(inputs)
        for i in range(0, self.inputLength):
            self.weights.append(1)

    # Lance le processus de raisonnement du neurone
    # Permet de donner les entrees au neurone et la sortie attendue si on l'a
    def reasonProcess(self, inputs, expected = -1):
        # si la verification du nombre d'entrees est ok, on peut continuer
        if self.checkInputs(inputs):
            # on enregistre la valeur de la sortie correcte
            self.expected = expected
      
            # on calcule la somme ponderee de nos entrees
            weightedSum = self.weightedSum(self.inputs, self.weights)
            # on calcul la sortie de notre porte via la fonction seuil
            self.output = self.threshold(weightedSum)

            # Si on est en phase d'apprentissage, on ajuste les poids de chaque entree
            # Ainsi, le neurone va pouvoir apprendre si la sortie qu'il donne est mauvaise
            if self.expected != -1:
                self.adjustWeights()
            
            self.display(weightedSum)        

     # Fonction utilitaire qui permet d'afficher des informations a chaque fois que l'on lance notre neurone
    def display(self, weightedSum) :
        print ''
        print "entrees = %s" %(self.inputs)
        print "poids = %s" %(self.weights)
        print "somme ponderee = %s" %(weightedSum)
        print "sortie = %s" %(self.output)

