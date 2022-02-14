klucz = 3  # --- o tyle znaków przesuwamy alfabet
alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
list = "TAJNAWIADOMOSC"
for l in list:
    # --- znajdujemy indeks litery i przesuwamy
    index = alfabet.find(l) + klucz
    # trzeba zawinąć do długości alfabetu!
    index = index % len(alfabet)
    print(alfabet[index], end="")

#--- inna wersja     
print()
klucz=klucz%len(alfabet)
alfabet2 = alfabet[klucz:] + alfabet[:klucz]
for i in list:
    print(alfabet2[alfabet.find(i)], end="")
