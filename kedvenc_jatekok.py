import random


print("Add meg 4 kedvenc videójátékodat!")


jatekok = []
osszes = 0


while len(set(jatekok)) < 4:
    osszes+= 1
    uj = input(f"{osszes}. játék: ")
    jatekok.append(uj)


kedvencek = list(set(jatekok))


print(f"\nA kedvenc videójátékaid: {', '.join(kedvencek)}")


ev_jateka = random.choice(kedvencek)
print(f"\nA 2025 év játéka: {ev_jateka}")


