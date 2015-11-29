from neurone import neurone

# Instancier un neurone
neurone = neurone()

# jeu d'apprentissage
print ("---------APPRENTISSAGE---------")
inputs = [1,0,1,1]
neurone.reasonProcess(inputs, 0)
inputs = [1,1,1,1]
neurone.reasonProcess(inputs, 1)
inputs = [0,1,0,1]
neurone.reasonProcess(inputs, 0)
inputs = [1,1,0,1]
neurone.reasonProcess(inputs, 0)
print ''

# jeu d'essai
print ("---------ESSAIS---------")
inputs = [1,1,1,1]
neurone.reasonProcess(inputs)
inputs = [0,1,1,1]
neurone.reasonProcess(inputs)
inputs = [0,0,1,1]
neurone.reasonProcess(inputs)
inputs = [0,0,0,1]
neurone.reasonProcess(inputs)
inputs = [0,0,0,0]
neurone.reasonProcess(inputs)
print ''