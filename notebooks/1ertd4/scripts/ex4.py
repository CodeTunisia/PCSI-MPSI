precipitations = {}
print("Appuyez sur <Entrer> pour terminer la saisie.")
while True:
    nom_ville = input("Saisir le nom de la vile: ")
    if nom_ville:
        nom_ville = nom_ville.title()
        pluie_mm = int(input("Entrer la quantité de pluie en mm : "))
        precipitations[nom_ville] = pluie_mm
    else:
        break

for ville, pluie in precipitations.items():
    print(f"{ville} : {pluie} mm")