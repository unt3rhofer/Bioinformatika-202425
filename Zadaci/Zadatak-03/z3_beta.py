from numpy import random
import numpy as np

# Loading input files
matrica_file = open("blosum50.txt", "r")
kiseline_file = open("acids.txt", "r")
poravnanje_file = open("poravnanje.in", "r")
izlaz = open("poravnanja_i_scoreovi.txt", "w")

# Interpreting loaded data
poravnanje = [poravnanje_file.readline().strip('\n').strip('_'), poravnanje_file.readline().strip('\n').strip('_')]

matrica = [[0]*20 for i in range (20)]

for i in range (20):
    redak = matrica_file.readline().split()
    for j in range(20):
        matrica[i][j] = int(redak[j])

kiseline = kiseline_file.readline()
# Funkcija score 
def score (kod):
    sum = 0
    for i in range(len(kod[0])):
        if (kod[0][i] == '_' or kod[1][i] == '_'):
            sum-=8
        else:
            sum += matrica[kiseline.index(kod[0][i])][kiseline.index(kod[1][i])]
    return sum

print("Koristeno poravnanje: ", poravnanje)

# Bazni kod je lista s potrebnim brojem 0 i 1. 0 ima za jedan manje zbog logike koda
bazni_kod = []
for i in range (len(poravnanje[0])-1):
    bazni_kod.append(0)
for i in range (len(poravnanje[1])):
    bazni_kod.append(1)
kod = np.array(bazni_kod)

# Generiranje nasumicnih permutacija 0 i 1 za kodiranje poravnanja
kodovi = []
for i in range (20): # bio bi bolji veci broj, al za svrhu rjesavanja ovog zadatka je ovo okej 
    temp_kod = [0] 
    temp_kod+=random.permutation(kod).tolist()
    kodovi.append(temp_kod)

print("\nNasumicno generirani kodovi: ")
for kod in kodovi:
    print (kod)

for kod in kodovi:
    it = 0
    n = len(kod)
    while it!=n-1:
        if kod[it]==kod[it+1]:
            kod.insert(it+1, -1)
            n+=1
        it+=1
    if kod[n-1]==0:
        kod.append(-1)
# Prilagodba kodova za lakse dekodiranje
print("\nPrilagodeni kodovi: ")
for kod in kodovi:
    print (kod)

poravnanja = []
print("\nDekodirana poravnanja i njihovi scoreovi: ")
for kod in kodovi:
    protein_a = []
    a = 0
    protein_b = []
    b = 0
    for i in range(len(kod)):
        # print ("Na indeksu", i, "sam. Element je: ", kod[i])
        if kod[i] == -1:
            if i%2 == 0 :
                protein_a.append('_')
                # print("u a sam dodao _ i on sad izgleda: ", protein_a)
            else:
                protein_b.append('_')
                # print("u b sam dodao _ i on sad izgleda: ", protein_b)
        elif kod[i] == 0:
            protein_a.append(poravnanje[0][a])
            a+=1
            # print("u a sam dodao ", poravnanje[0][a-1], "i on sad izgleda: ", protein_a, "a = ", a)
        else:
            protein_b.append(poravnanje[1][b])
            b+=1
            # print("u b sam dodao ", poravnanje[1][b-1], "i on sad izgleda: ", protein_b, "b = ", b)

    poravnanja.append([protein_a, protein_b])

avg = 0
br = 0
for poravnanje in poravnanja:
    avg += score(poravnanje)
    br+=1
    izlaz.write(''.join(poravnanje[0]))
    izlaz.write('\n')
    izlaz.write(''.join(poravnanje[1]))
    izlaz.write('\n')
    izlaz.write(str(score(poravnanje)))
    izlaz.write('\n')
print("average score", avg/br)
izlaz.write("Prosjecni score = ")
izlaz.write(str(avg/br))

