class Termek:
    def __init__(self, nev, ar, eladott_mennyiseg, ev):
        self.nev = nev
        self.ar = int(ar)
        self.eladott_mennyiseg = int(eladott_mennyiseg)
        self.ev = int(ev)

    def __str__(self):
        return f"{self.nev}; {self.ar} Ft; {self.eladott_mennyiseg} db; {self.ev}"


with open('termekek.txt', 'r', encoding='utf-8') as file:
    header = file.readline().strip()  
    termekek = []
    for sor in file:
        adatok = sor.strip().split(';')
        termekek.append(Termek(adatok[0], adatok[1], adatok[2], adatok[3]))


print("A fájl tartalma:")
for termek in termekek:
    print(termek)


legdragabb = max(termekek, key=lambda x: x.ar)
print(f"\nA legdrágább termék: {legdragabb.nev}, ára: {legdragabb.ar} Ft")


atlag_eladas = sum(t.eladott_mennyiseg for t in termekek) / len(termekek)
print(f"\nAz eladott termékek darabszámának átlaga: {atlag_eladas:.2f}")


c_betus_termekek = [t for t in termekek if t.nev.startswith('C')]
print(f"\nA 'C'-vel kezdődő termékek száma: {len(c_betus_termekek)}")


with open('C_betus_termekek.txt', 'w', encoding='utf-8') as c_file:
    for termek in c_betus_termekek:
        c_file.write(f"{termek}\n")


print("\n'C'-vel kezdődő termékek:")
for termek in c_betus_termekek:
    print(termek)



