def chaineListe(ch):
    "convertit la chaîne ch en une liste de mots"
    return ch.split()
# Tests :
if __name__ == '__main__':
    li = chaineListe("Ce qu’est l’ours en peluche de l’enfant devient le télescope de l’astronome.")
    print(li)