a_betus_elem = []

print("Adj meg egy a betűvel kezdődő szót: ")

while True:   
    a_szo = input("A szó: ")
    if a_szo == "":
        break
    if a_szo[0] == "a":
        a_betus_elem.append(a_szo)

print("\nMegadott a betűs szavak:")
for a_szo in a_betus_elem:
    print(a_szo)