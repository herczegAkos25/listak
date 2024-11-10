nevek = []

print("Adj meg keresztneveket! Nyomj ENTER-t, ha befejezted.")

while True:
    nev = input("Keresztnév: ")
    if nev == "":
        break
    nevek.append(nev)

print("\nA megadott nevek:")
for nev in nevek:
    print(nev)