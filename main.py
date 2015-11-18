from neurone import neurone

# Instancier un neuronne
neuroneCalcul = neurone()

# jeu d'apprentissage
tab = [1,0,1,1]
neuroneCalcul.processusApprend(tab, 0)
tab = [1,1,1,1]
neuroneCalcul.processusApprend(tab, 1)
tab = [0,1,0,1]
neuroneCalcul.processusApprend(tab, 0)
tab = [1,1,0,1]
neuroneCalcul.processusApprend(tab, 0)

# jeu d'essai
tab = [1,1,1,1]
neuroneCalcul.processus(tab)
tab = [0,1,1,1]
neuroneCalcul.processus(tab)
tab = [0,0,1,1]
neuroneCalcul.processus(tab)
tab = [0,0,0,1]
neuroneCalcul.processus(tab)
tab = [0,0,0,0]
neuroneCalcul.processus(tab)