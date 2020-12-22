#NOM DU MODULE : occurrence.py
def occurences(chaine):
    histo = [0] * 26
    chaine = chaine.lower()
    for c in chaine:
        
        index = ord(c)- ord('a')
        try:
            histo[index] = histo[index] + 1
        except IndexError:
            print("Caractère '{}' non valide!".format(c))
    return histo
if __name__ == "__main__":
    print(occurences("Hello"))