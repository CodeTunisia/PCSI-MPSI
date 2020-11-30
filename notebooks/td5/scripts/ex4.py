def voyelle(car):
    "teste si le caractère <car> est une voyelle"
    if car in "AEIOUYÀÉÈÊËÎÏÔÛÙaeiouyàéèêëîïôûù":
        return True     
    else:
        return False

def compteVoyelles(phrase):
    "compte les voyelles présentes dans la chaîne de caractères"
    n = 0
    for c in phrase:
        if voyelle(c):
            n = n + 1 
    return n

texte ="Maître corbeau sur un arbre perché"

print(compteVoyelles(texte))
