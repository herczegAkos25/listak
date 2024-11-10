gyumolcsok = []

while True:
    gyumolcs = input("Adjon meg egy gyümölcs nevet: ")
    if gyumolcs == "vége":
        break
    elif gyumolcsok.count(gyumolcs) < 1:
        gyumolcsok.append(gyumolcs)
    else:
        print("Van már ilyen gyümölcs!")

print("Gyümölcsök: ")
for gyumolcs in reversed(gyumolcsok):
    print(gyumolcs)

