lazacar = 3000 
pisztrangar = 2500

print("Üdvözöljük a halboltban!")
print("Kétféle hal kapható:")
print("Lazac - 2500 Ft/kg")
print("Pisztráng - 3000 Ft/kg")

halvalaszt = input("Kérem, válassza ki a halat:")
mennyiseg = int(input("Kérem, adja meg, hány kilogrammot szeretne vásárolni:"))

if halvalaszt == "lazac":
    osszeg = mennyiseg * lazacar
elif halvalaszt == "pisztráng":
    osszeg = mennyiseg * pisztrangar
else:
    print("Nem jó halat aftál meg!")

print(f"Mennyiség: {mennyiseg} kg")
print(f"Az összeg: {osszeg} Ft")


