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
direction_matrix = [['nista']*(m+1) for i in range (n+1)]

for i in range (n+1):
    score_matrix[i][0]=-8*i
for i in range (m+1):
    score_matrix[0][i]=-8*i

for i in range (1, n+1):
    direction_matrix[i][0]='Up'
for i in range (1, m+1):
    direction_matrix[0][i]='Left'

for i in range(1, n+1):
    for j in range(1, m+1):
        a = score_matrix[i][j-1] - 8
        b = score_matrix[i-1][j] - 8
        c = score_matrix[i-1][j-1] + matrica[kiseline.index(y[i-1])][kiseline.index(x[j-1])]
        score_matrix[i][j] = max(a,b,c)
        if max(a,b,c) == a:
            direction_matrix[i][j] = 'Left'
        elif max(a,b,c) == b:
            direction_matrix[i][j] = 'Up'
        else:
            direction_matrix[i][j] = 'Diagonal'

for redak in score_matrix:
    print(redak)
for redak in direction_matrix:
    print(redak)

# Traceback
i = n
j = m
while (i!=0 or j!=0):
    if direction_matrix[i][j] == 'Diagonal':
        i-=1
        j-=1
    elif direction_matrix[i][j] == 'Left':
        y = y[:i]+'_'+y[i:]
        j-=1
    elif direction_matrix[i][j] == 'Up':
         x = x[:j]+'_'+x[j:]
         i-=1
    else:
        print("Zeznuo si nekaj")
        break

print(x)
print(y)
