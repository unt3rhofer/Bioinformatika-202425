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
Također po uzoru na [`profesorov primjer`](https://github.com/unt3rhofer/Bioinformatika-202425/blob/master/Zadaci/Zadatak-02/primjer_koda.py) i Needleman-Wunsch algoritam, kreiramo tri varijable `a`, `b` i `c`. Svaka od tih varijabli predstavlja jednu od tri mogućnosti u posljednjem koraku kreiranja score matrice u NW-algoritmu. Na kraju uzimamo najveću od te tri vrijednosti. Zašto su varijable definirane tako kako jesu će biti jasno kada se pogleda zadnji slide [`prezentacije`](https://github.com/unt3rhofer/Bioinformatika-202425/blob/master/Zadaci/Zadatak-02/NW-algoritam.pdf).
```python
for i in range(1, n+1):
    for j in range(1, m+1):
        a = score_matrix[i][j-1] - 8
        b = score_matrix[i-1][j] - 8
        c = score_matrix[i-1][j-1] + matrica[kiseline.index(y[i-1])][kiseline.index(x[j-1])]
        score_matrix[i][j] = max(a,b,c)
```
Najteži dio zadatka (iako nije ništa komplicirano) je napisati traceback dio NW-algoritma. Traceback koristeći matricu `scoring_matrix` iz prošlog dijela zadatka popunjava stringove tako da nam vrati optimalno poravnanje.

Budući da krećemo iz donjeg desnog kuta matrice, postavimo `i` i `j` na odgovarajuće koordinate.
```python
i = n
j = m
```
Putujemo do gornjeg lijevog kuta matrice pa postavimo potrebne uvjete za prekid while petlje.
```python
while (i!=0 or j!=0):
```
U matrici se želimo kretati *gore*, *lijevo* i *dijagonalno* pa definiramo varijable koje pamte vrijednost iz scoring matrice na potencijalnim idućim koracima.
```python
        if i>0:
            up = score_matrix[i-1][j]
        if i>0 and j>0: 
            diagonal = score_matrix[i-1][j-1]
        if j>0:
            left = score_matrix[i][j-1]
```
Zatim se pomaknemo u smjeru koji odgovara najvećoj vrijednosti od tri moguća u smislu scoring matrice. Ako se ispostavi da je najveća vrijednost u scoring matrici dijagonalno od naše trenutne pozicije znamo da su na promatranom indeksu aminokiseline već optimalno poravnane. Ako se odlučimo pomaknuti lijevo moramo dodati "gap" ('_' po našem dogovoru) u prvi niz aminokiselina, a u slučaju da se pomaknemo gore dodajemo "gap" u drugi niz aminokiselina.

_Nije mi sasvim jasno zašto i kako je to matematički opravdano, ali na internetu sam pronašao neke simulacije algoritma koje se tako ponašaju pa sam ukrao tu logiku._
```python
        if max(up, diagonal, left) == diagonal:
           i-=1
           j-=1
        elif max(up, diagonal, left) == left:
           y = y[:i]+'_'+y[i:]
           j-=1
        else:
            x = x[:j]+'_'+x[j:]
            i-=1
```
"Gap" dodajemo tako da razdvojimo string koji predstavlja niz aminokiselina na `string[:i]` što odgovara podstringu od početka stringa pa sve do indeksa taman prije `i` i `string[i:]` što odgovara podstringu od indeksa `i` sve do kraja stringa. Nakon što string razdvojimo ga spojimo nazad i dodamo znak `'_'` između njih.
```python
string = string[:j]+ '_' + string[j:]
```
