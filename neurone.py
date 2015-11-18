# La classe neurone permet d'instancier un neuronne a nombre d'entrees variables
# definit par la taille du premier tableau d'entrees envoye.
# Elle permet de faire une somme ponderee des entrees donnees avec une fonction seuil
# qui retourne 1 si le resultat de la somme est superieur a 0.
# Ce neuronne est capable d'apprendre lorsque la second parametre de la fonction processus
# est la sortie attendue.
class neurone:

    # nombre d'entrees du neuronne
    longueur = 0
    # flag qui permet de savoir si le nombre d'entrees est definit
    first = 0
    # Valeur de la sortie du neuronne
    result = 0
    # Tableau des valeurs des entrees du neurone
    entreeTab = []
    # Tableau des poids qui correspondent aux entrees du neurone
    poidsTab = []

    # Constructeur de la classe
    def __init__(self):
        longueur = 0
        first = 0
        result = 0

    # Ajuste les poids des entrees (uniquement si la sortie est mauvaise)
    # On parcoure nos entrees et pour chaque on verifie si elle correspond a la sortie
    # Si oui, on augmente le poids de cette entree
    # Si non, on diminue le poids de cette entree
    def adjustWeight(self):
        # Si la sortie est correcte, on ne continue pas
        if self.sortieAttendue != self.result:
            # Pour chaque entree, on verifie si elle correspond a la sortie
            for i in range(0, self.longueur):
                if self.entreeTab[i]*self.poidsTab[i] == self.sortieAttendue:
                    self.poidsTab[i] += 1
                else:
                    self.poidsTab[i] -= 1

    # Sortie du neuronne (fonction seuil)
    # Si la somme ponderee est superieure a 0, sortie = 1
    # Sinon, sortie = 0
    def seuil(self, somme):
        # Function seuil
        if somme > 0:
            self.result = 1
            return self.result 
        else :
            self.result = 0
            return self.result

    # Calcul la somme ponderee en fonction des entrees du neuronne
    # Pour chaque entree, on multiplie sa valeur par le poids qui lui correspond
    # Et on additionne les resultats
    def sommePondere(self, inputs_list, weight_list):
        # somme ponderee 
        accumulateur = 0
        # pour chaque entree, on la multiplie par le poids qui y correspond
        for i in range(0, self.longueur):
            accumulateur += inputs_list[i] * weight_list[i]
        # on retourne le resultat de la somme ponderee
        return accumulateur

    # Permet de definir le nombre d'entrees du neurone
    # en fonction du premier tableau envoye
    # Ensuite, verifie que le nombre d'entrees du tableau
    # correspond au nombre d'entrees du neurone
    def entreePorte(self, entree):
        # on regarde le nombre d'entrees recues
        longueur = len(entree)
        # si c'est le premier appel, on instancie le tableau de poids a 1
        if self.first == 0:
            for i in range(0, longueur):
                self.poidsTab.append(1)
            self.first = 1
            self.longueur = longueur
        
        # Si la longueur du tableau correspond au nombre d'entrees,
        # on enregistre les valeurs envoyees et on retourne un "ok"(1)
        if longueur == self.longueur:
            self.entreeTab = entree
            return 1

        return 0

    # Permet de donner un les entrees au neuronnes et la sortie attendue
    # Ainsi, le neuronne va pouvoir apprendre si la sortie qu'il donne est mauvaise
    def processusApprend(self, entree, sortieAttendue):
        # si la verification du nombre d'entrees est ok, on peut continuer
        if self.entreePorte(entree) == 1:
            # on enregistre la valeur de la sortie correcte
            self.sortieAttendue = sortieAttendue
            print ''
            print("entree=%s" %(entree))
            # on calcule la somme ponderee de nos entrees
            somme = self.sommePondere(self.entreeTab, self.poidsTab)
            print ("somme=%s" %(somme))
            print ("sortie=%s" %(self.seuil(somme)))
            # Si on est en phase d'apprentissage, on ajuste les poids de chaque entree
            if sortieAttendue != -1:
                self.adjustWeight()
                print ("poids=%s" %(self.poidsTab))
            return 1
        else:
            return 0

    # Permet de demander au neuronne un resultat en fonction des entrees donnees
    def processus(self, entree):
        # On appelle la fonction d'execution en indiquant que l'on est pas en phase d'apprentissage
        return self.processusApprend(entree, -1)
