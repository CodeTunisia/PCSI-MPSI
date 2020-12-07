# MODULE : calcul.py
print("exemple  de print à ne pas  faire !")
# l'instruction print sera exécuté avec l'import du module!
# ce qui n'est pas désirable!
# DÉFINITION DES FONCTIONS
def f(x,y):
    """
    Multiplication de deux nombres x et y:
      c'est la fonction à importé!
    """
    return(x*y)
# PARTIE DE TESTS
if  __name__ == '__main__' :
    print(f(3, 4))
    print(f("abc", 2))
    print(f([1,2,3], 3))