from neurone import neurone

# Instancier un neuronne
# neuroneAnd a un jeu d'apprentissage pour la porte AND
neuroneAnd = neurone()
neuroneOr = neurone()


# jeu d'apprentissage AND
tab = [1,0,1,1]
neuroneAnd.processusApprend(tab, 0)
tab = [1,1,1,1]
neuroneAnd.processusApprend(tab, 1)
tab = [0,1,0,1]
neuroneAnd.processusApprend(tab, 0)
tab = [1,1,0,1]
neuroneAnd.processusApprend(tab, 0)
# jeu d'essai AND
tab = [1,1,1,1]
neuroneAnd.processus(tab)
tab = [0,1,1,1]
neuroneAnd.processus(tab)
tab = [0,0,1,1]
neuroneAnd.processus(tab)
tab = [0,0,0,1]
neuroneAnd.processus(tab)
tab = [0,0,0,0]
neuroneAnd.processus(tab)



# jeu d'apprentissage OR
tab = [1,0,1,1]
neuroneOr.processusApprend(tab, 1)
tab = [1,1,1,1]
neuroneOr.processusApprend(tab, 1)
tab = [0,1,0,1]
neuroneOr.processusApprend(tab, 1)
tab = [0,0,0,0]
neuroneOr.processusApprend(tab, 0)
# jeu d'essai OR
tab = [1,1,1,1]
neuroneOr.processus(tab)
tab = [0,1,1,1]
neuroneOr.processus(tab)
tab = [0,0,1,1]
neuroneOr.processus(tab)
tab = [0,0,0,1]
neuroneOr.processus(tab)
tab = [0,0,0,0]
neuroneOr.processus(tab)