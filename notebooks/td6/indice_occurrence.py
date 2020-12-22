#NOM DU MODULE : indice_occurrence.py
def indice_occurrence(chaine, occ):
    # obtenir la longueur de l'occurrence occ et la longueur de chaine
    m = len(occ)
    n = len(chaine)
    # partie à compléter
    # initialisation de la liste d'index
    listIndice = []
    # la recherche de tous les index d'occurrence se produit dans la chaîne
    for i in range(0 , n-m):
        if chaine[i : m + i] == occ:
            listIndice.append(i)
    return listIndice
if __name__ == "__main__":
    chaine = "un ver vert va vers un verre vert."
    occ = "ver"
    print(indice_occurrence(chaine, occ))