from neurone import neurone

# Instancier deux neurones AND
neuroneAND = neurone()
neuroneAND2 = neurone()
# Instancier un neurone OR
neuroneOR = neurone()

outputs1 = []
outputs2 = []

# jeu d'apprentissage premiere porte AND
print ("---------APPRENTISSAGE-1-------- PORTE ET")
inputs = [1,0,1,1]
neuroneAND.reasonProcess(inputs, 0)
inputs = [1,1,1,1]
neuroneAND.reasonProcess(inputs, 1)
inputs = [0,1,0,1]
neuroneAND.reasonProcess(inputs, 0)
inputs = [1,1,0,1]
neuroneAND.reasonProcess(inputs, 0)
print ''

# jeu d'essai premiere porte AND
print ("---------ESSAIS-1-------- PORTE ET")
inputs = [1,1,1,1]
neuroneAND.reasonProcess(inputs)
outputs1.append(neuroneAND.getLastOutput())
inputs = [0,1,1,1]
neuroneAND.reasonProcess(inputs)
outputs1.append(neuroneAND.getLastOutput())
inputs = [0,0,1,1]
neuroneAND.reasonProcess(inputs)
outputs1.append(neuroneAND.getLastOutput())
inputs = [0,0,0,1]
neuroneAND.reasonProcess(inputs)
outputs1.append(neuroneAND.getLastOutput())
inputs = [0,0,0,0]
neuroneAND.reasonProcess(inputs)
outputs1.append(neuroneAND.getLastOutput())
print ''

# jeu d'apprentissage deuxieme porte AND
print ("---------APPRENTISSAGE-2-------- PORTE ET")
inputs = [1,0,1,1]
neuroneAND2.reasonProcess(inputs, 0)
inputs = [1,1,1,1]
neuroneAND2.reasonProcess(inputs, 1)
inputs = [0,1,0,1]
neuroneAND2.reasonProcess(inputs, 0)
inputs = [1,1,0,1]
neuroneAND2.reasonProcess(inputs, 0)
print ''

# jeu d'essai deuxieme porte AND
print ("---------ESSAIS-2-------- PORTE ET")
inputs = [1,1,1,1]
neuroneAND2.reasonProcess(inputs)
outputs2.append(neuroneAND2.getLastOutput())
inputs = [0,1,1,1]
neuroneAND2.reasonProcess(inputs)
outputs2.append(neuroneAND2.getLastOutput())
inputs = [0,0,1,1]
neuroneAND2.reasonProcess(inputs)
outputs2.append(neuroneAND2.getLastOutput())
inputs = [0,0,0,1]
neuroneAND2.reasonProcess(inputs)
outputs2.append(neuroneAND2.getLastOutput())
inputs = [0,0,0,0]
neuroneAND2.reasonProcess(inputs)
outputs2.append(neuroneAND2.getLastOutput())
print ''


# jeu d'apprentissage porte OR
print ("---------APPRENTISSAGE--------- PORTE OU")
inputs = [1,1]
neuroneOR.reasonProcess(inputs,1)
inputs = [0,0]
neuroneOR.reasonProcess(inputs,0)
print ''

# jeu d'essai porte OR
print ("---------ESSAIS--------- PORTE OU")
inputs = [outputs1[0], outputs2[0]]
neuroneOR.reasonProcess(inputs)
inputs = [outputs1[1], outputs2[1]]
neuroneOR.reasonProcess(inputs)
inputs = [outputs1[2], outputs2[2]]
neuroneOR.reasonProcess(inputs)
inputs = [outputs1[3], outputs2[3]]
neuroneOR.reasonProcess(inputs)
inputs = [outputs1[4], outputs2[4]]
neuroneOR.reasonProcess(inputs)
print ''