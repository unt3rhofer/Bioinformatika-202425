import itertools

# Loading input file
poravnanje_file = open("poravnanje.in", "r")

# Loading output file
out = open("kodovi.out", "w")

# Interpreting loaded files
poravnanje = [poravnanje_file.readline().strip('\n'), poravnanje_file.readline().strip('\n')]

# Generating basic code
for i in range (len(poravnanje[0])):
                out.write('1')
for i in range (len(poravnanje[1])):
                out.write('0')

# Ovo prije je zapravo bespotrebno, samo sam isprobavao kako se takve stvari rade u pythonu
kodovi_file = open("kodovi.out", "r")
kodovi = kodovi_file.readline()


