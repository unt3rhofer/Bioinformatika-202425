# Zadatak 02
Inicijaliziramo score matrix tako da ju popunimo nulama. Matrica je dimenzija _duljina prvog stringa_ x _duljina drugog stringa_
``` python
score_matrix = [[0]*(len(x)+1) for i in range (len(y)+1)]
```
Nulti redak i nulti stupac matrice popunimo negativnim elementima kako je opisano u [`profesorovom primjeru`](https://github.com/unt3rhofer/Bioinformatika-202425/blob/master/Zadaci/Zadatak-02/primjer_koda.py). To radimo jednostavno zato što tako radi algoritam koji koristimo.
```python
for i in range (len(y)+1):
    score_matrix[i][0]=-8*i
for i in range (len(x)+1):
    score_matrix[0][i]=-8*i
```
Također po uzoru na [`profesorov primjer`](https://github.com/unt3rhofer/Bioinformatika-202425/blob/master/Zadaci/Zadatak-02/primjer_koda.py) i Needleman-Wunsch algoritam, kreiramo tri varijable `a`, `b` i `c`. Svaka od tih varijabli predstavlja jednu od tri mogućnosti u posljednjem koraku kreiranja score matrice u NW-algoritmu. Na kraju uzimamo najveću od te tri vrijednosti. Zašto su varijable definirane tako kako jesu će biti jasno kada se pogleda zadnji slide [`prezentacije`](https://github.com/unt3rhofer/Bioinformatika-202425/blob/master/Zadaci/Zadatak-02/NW-algoritam.pdf).
```python
for i in range(1, len(y)+1):
    for j in range(1, len(x)+1):
        a = score_matrix[i][j-1] - 8
        b = score_matrix[i-1][j] - 8
        c = score_matrix[i-1][j-1] + matrica[kiseline.index(y[i-1])][kiseline.index(x[j-1])]
        score_matrix[i][j] = max(a,b,c)
```
