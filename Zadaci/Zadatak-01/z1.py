#/home/martin/Documents/Faks/Materijali/G2S2/Bioinformatika/Zadaci

# Loading input files
poravnanje_file = open("por001.txt", "r")
matrica_file = open("blosum50.txt", "r")
kiseline_file = open("acids.txt", "r")

# Interpreting loaded data
poravnanje = [poravnanje_file.readline().strip('\n'), poravnanje_file.readline().strip('\n')]

matrica = [[0]*20 for i in range (20)]

for i in range (20):
    redak = matrica_file.readline().split()
    for j in range(20):
        matrica[i][j] = int(redak[j])

kiseline = kiseline_file.readline()

# Calculating sum
sum = 0
for i in range(len(poravnanje[0])):
    if (poravnanje[0][i] == '_' or poravnanje[1][i] == '_'):
        sum-=8
    else:
        sum += matrica[kiseline.index(poravnanje[0][i])][kiseline.index(poravnanje[1][i])]

print (sum)
