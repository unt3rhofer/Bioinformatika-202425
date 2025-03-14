# Zadatak 02
Inicijaliziramo score matrix tako da ju popunimo nulama. Matrica je dimenzija _duljina prvog stringa_ x _duljina drugog stringa_
``` python
score_matrix = [[0]*(m+1) for i in range (n+1)]
```
Nulti redak i nulti stupac matrice popunimo negativnim elementima kako je opisano u [`profesorovom primjeru`](https://github.com/unt3rhofer/Bioinformatika-202425/blob/master/Zadaci/Zadatak-02/primjer_koda.py). To radimo jednostavno zato što tako radi algoritam koji koristimo.
```python
for i in range (n+1):
    score_matrix[i][0]=-8*i
for i in range (m+1):
    score_matrix[0][i]=-8*i
```
U ovom koraku kao pripremu za traceback stvaramo i `direction_matrix`. Matricu koja ce pamtiti iz kojeg smjera smo došli pri generiranju _scorea_ optimalnog poravnanja. Očito se u rubovima možemo kretati samo gore ili lijevo ovisno u kojem rubu se nađemo. 
```python
direction_matrix = [['nista']*(m+1) for i in range (n+1)]
for i in range (1, n+1):
    direction_matrix[i][0]='Up'
for i in range (1, m+1):
    direction_matrix[0][i]='Left'
```
Također po uzoru na [`profesorov primjer`](https://github.com/unt3rhofer/Bioinformatika-202425/blob/master/Zadaci/Zadatak-02/primjer_koda.py) i Needleman-Wunsch algoritam, kreiramo tri varijable `a`, `b` i `c`. Svaka od tih varijabli predstavlja jednu od tri mogućnosti u posljednjem koraku kreiranja score matrice u NW-algoritmu. Na kraju uzimamo najveću od te tri vrijednosti. Zašto su varijable definirane tako kako jesu će biti jasno kada se pogleda zadnji slide [`prezentacije`](https://github.com/unt3rhofer/Bioinformatika-202425/blob/master/Zadaci/Zadatak-02/NW-algoritam.pdf).
```python
for i in range(1, n+1):
    for j in range(1, m+1):
        a = score_matrix[i][j-1] - 8
        b = score_matrix[i-1][j] - 8
        c = score_matrix[i-1][j-1] + matrica[kiseline.index(y[i-1])][kiseline.index(x[j-1])]
        score_matrix[i][j] = max(a,b,c)
```
Nakon što odredimo koja mogućnost nam daje optimalan _score_ u `direction_matrix` zapišemo smjer iz kojeg smo došli do tog optimalnog _scorea_.
```python
        if max(a,b,c) == a:
            direction_matrix[i][j] = 'Left'
        elif max(a,b,c) == b:
            direction_matrix[i][j] = 'Up'
        else:
            direction_matrix[i][j] = 'Diagonal'
```

Glavni dio zadatka je napisati traceback dio algoritma. Traceback koristeći matricu `direction_matrix` iz prošlog dijela zadatka popunjava stringove tako da nam vrati optimalno poravnanje.

Budući da krećemo iz donjeg desnog kuta matrice, postavimo `i` i `j` na odgovarajuće koordinate.
```python
i = n
j = m
```
Putujemo do gornjeg lijevog kuta matrice pa postavimo potrebne uvjete za prekid while petlje. Iz svakog polja se krećemo u smjeru definiranom u `direction_matrix`.
```python
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
```

"Gap" dodajemo tako da razdvojimo string koji predstavlja niz aminokiselina na `string[:i]` što odgovara podstringu od početka stringa pa sve do indeksa taman prije `i` i `string[i:]` što odgovara podstringu od indeksa `i` sve do kraja stringa. Nakon što string razdvojimo ga spojimo nazad i dodamo znak `'_'` između njih.
```python
string = string[:j]+ '_' + string[j:]
```
