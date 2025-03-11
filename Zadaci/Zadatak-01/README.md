# Zadatak 01
U ovom dijelu koda učitavamo zadane ulazne datoteke u varijable. Koristimo funkciju open, a argument `r` postiže otvaranje u modu za čitanje podataka.
```python
poravnanje_file = open("por001.txt", "r")
matrica_file = open("blosum50.txt", "r")
kiseline_file = open("acids.txt", "r")
```
Koristeći funkciju `readline()` u polje `poravnanje` spremamo nama zadana poravnanja aminokiselina kao dva stringa. Nulti element polja je gornji red poravnanja, a prvi element odgovara donjem redu poravnanja.

Koristimo funkciju `strip()` s argumentom `'\n'` kako bismo izbrisali specijalni znak za kraj stringa s kraja učitanog stringa. 
```python
poravnanje = [poravnanje_file.readline().strip('\n'), poravnanje_file.readline().strip('\n')]
```
Pomoću dvije for petlje interpretiramo matricu napisanu u `.txt` dokumentu kao matricu u pythonu koju možemo obrađivati. 

Funkcija `split()` pametno razdvaja dani string na bjelinama i vraća niz podstringova kojeg zapisujemo u varijablu `redak`. Budući da želimo računati s elementima matrice ih je potrebno pravilno konvertirati u tip podatka `int`. U pythonu se to jednostavno odradi dodavanjem `int(stvar_koju_konvertiramo)`
```python
for i in range (20):
    redak = matrica_file.readline().split()
    for j in range(20):
        matrica[i][j] = int(redak[j])
```
