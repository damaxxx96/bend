import os
from bend import Gitara
from bend import Bubanj
from bend import Bend


gitara_1 = Gitara("Srbija", True)
gitara_2 = Gitara("Nemacka", False)
bubanj = Bubanj()
bend = Bend("Rade roker", gitara_1, gitara_2, bubanj)

print("-------------------------")
print("-------------------------")
print("------MUZICKI BEND-------")
print("-------------------------")
print("-------------------------")
while True:
    print("Izaberite instrument koji svirate")
    print("1.Gitara")
    print("2.Bubanj")
    print("3.Sviranje benda")
    print("4.Prikaz benda")
    unos = input("Unesite broj instrumenta: ")
    os.system("cls")
    if unos == "1":
        unos_instrumenta = input(
            "Unesite da li je zelite Akusticnu ili Elektricnu gitaru: "
        )
        if unos_instrumenta == "elektricna":
            gitara.elektricna = True
            gitara.sviraj(gitara)
        elif unos_instrumenta == "akusticna":
            gitara.elektricna = False
            gitara.sviraj(gitara)
        else:
            print("Ne postoji takva Gitara!!")
    elif unos == "2":
        bubanj.sviraj(bubanj)
    elif unos == "3":
        bend.sviraj()
