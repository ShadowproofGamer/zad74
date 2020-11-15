plik = open('hasla.txt')
dane = plik.read().split()
tabelka = []

def cyfry(tablica):
    liczba = 0
    cyferki = []
    for k in range(0,10):
        cyferki.append(ord(str(k)))
    for i in tablica:
        same_cyfry = True
        for j in i:
            if cyferki.count(ord(j)) == 0:
                same_cyfry = False
        if same_cyfry:
            liczba+=1
    return liczba


tabelka.append("zadanie 1")
print("zadanie 1")
tabelka.append(cyfry(dane))
print(cyfry(dane))

def powtorzenie(tablica):
    powtorzenia = []
    for i in tablica:
        if tablica.count(i) > 1 and powtorzenia.count(i) == 0:
            powtorzenia.append(i)
    powtorzenia.sort()
    return powtorzenia


tabelka.append("\nzadanie 2")
print("\nzadanie 2")
for i in powtorzenie(dane):
    tabelka.append(i)
    print(i)


def asci(tablica):
    slowa = []
    for i in tablica:
        i.lower()
        for j in range(0, len(i)-3, 1):
            temp = [ord(i[j]), ord(i[j+1]), ord(i[j+2]), ord(i[j+3])]
            temp.sort()
            if temp[0] == temp[1] -1 and temp[0] == temp[2] -2 and temp[0] == temp[3] -3:
                slowa.append(i)
                break
    return slowa

tabelka.append("\nzadanie 3")
print("\nzadanie 3")
tabelka.append(len(asci(dane)))
print(len(asci(dane)))


def silne_haslo(tablica):
    liczba = 0
    for i in tablica:
        mala_litera = False
        duza_litera = False
        cyfra = False
        for j in i:
            if ord(j)>=97 and ord(j)<=122:
                mala_litera = True
            elif ord(j)>=65 and ord(j)<=90:
                duza_litera = True
            elif ord(j)>=48 and ord(j)<=57:
                cyfra = True
        if mala_litera and duza_litera and cyfra:
            liczba+=1
    return liczba


tabelka.append("\nzadanie4")
print("\nzadanie4")
tabelka.append(silne_haslo(dane))
print(silne_haslo(dane))

plik2 = open('wyniki_hasla.txt', 'w')
for i in tabelka:
    plik2.writelines(str(i)+ '\n')