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

# Constructing scoring matrix

x = input()
y = input()
m = len(x)
n = len(y)
score_matrix = [[0]*(m+1) for i in range (n+1)]

for i in range (n+1):
    score_matrix[i][0]=-8*i
for i in range (m+1):
    score_matrix[0][i]=-8*i

for i in range(1, n+1):
    for j in range(1, m+1):
        a = score_matrix[i][j-1] - 8
        b = score_matrix[i-1][j] - 8
        c = score_matrix[i-1][j-1] + matrica[kiseline.index(y[i-1])][kiseline.index(x[j-1])]
        score_matrix[i][j] = max(a,b,c)

for redak in score_matrix:
    print(redak)

# Traceback
i = n
j = m
while (i!=0 or j!=0):
        print(i, j)
        current = score_matrix[i][j]
        if i>0:
            up = score_matrix[i-1][j]
        if i>0 and j>0: 
            diagonal = score_matrix[i-1][j-1]
        if j>0:
            left = score_matrix[i][j-1]

        if max(up, diagonal, left) == diagonal:
           i-=1
           j-=1
        elif max(up, diagonal, left) == left:
           y = y[:i]+'_'+y[i:]
           j-=1
        else:
            x = x[:j]+'_'+x[j:]
            i-=1

print(x)
print(y)
