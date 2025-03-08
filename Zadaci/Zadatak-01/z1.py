#/home/martin/Documents/Faks/Materijali/G2S2/Bioinformatika/Zadaci

# Loading input files
poravnanje_file = open("por001.txt", "r")
matrica_file = open("blosum50.txt", "r")
kiseilne_file = open("acids.txt", "r")

# Interpreting loaded data
poravnanje = [poravnanje_file.readline(), poravnanje_file.readline()]

matrica = [[0]*20 for i in range (20)]

for i in range (20):
    redak = matrica_file.readline().split()
    for j in range(20):
        matrica[i][j] = int(redak[j])

