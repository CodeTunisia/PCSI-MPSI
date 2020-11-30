def mon_arctan(x, N):
    from math import atan
    somme = 0
    for k in range(0, N+1):
        if k%2 == 0: # si k est pair signe +
            somme += 1/(2*k+1) * (x **(2*k+1))
        else: # si k est impair signe -
            somme -= 1/(2*k+1) * (x **(2*k+1))
    err = abs(atan(x) - somme)
    return somme, err

def dico_arctan(x):
    setN = {10, 100, 1000, 10000}
    dico = {}
    for n in setN:
        dico[n] = mon_arctan(x, n)
    return dico

print([mon_arctan(1/10**i, 10000)[0] for i in range(9)])

