#/home/martin/Documents/Faks/Materijali/G2S2/Bioinformatika/Zadaci/Zadatak-02

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

# Constructing algorirhm

x = input()
y = input()
score_matrix = [[0]*len(x) for i in range (len(y))]

for i in range (1, len(x)):
    score_matrix[0][i]=-8*i
for i in range (1, len(y)):
    score_matrix[i][0]=-8*i

for redak in score_matrix:
    print(redak)
