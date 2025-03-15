#/home/martin/Documents/Faks/Materijali/G2S2/Bioinformatika/Zadaci

# Loading input files
matrica_file = open("blosum50.txt", "r")
kiseline_file = open("acids.txt", "r")

# Interpreting loaded data

matrica = [[0]*20 for i in range (20)]

for i in range (20):
    redak = matrica_file.readline().split()
    for j in range(20):
        matrica[i][j] = int(redak[j])

kiseline = kiseline_file.readline()
# Calculating sum

def score (kod):
    sum = 0
    for i in range(len(poravnanje[0])):
        if (poravnanje[0][i] == '_' or poravnanje[1][i] == '_'):
            sum-=8
        else:
            sum += matrica[kiseline.index(poravnanje[0][i])][kiseline.index(poravnanje[1][i])]
    return sum
# Closing open files
matrica_file.close()
kiseline_file.close()
