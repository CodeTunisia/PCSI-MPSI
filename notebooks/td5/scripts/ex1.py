def inverse(dico):
    "Construction d'un nouveau dico, pas à pas"    
    dic_inv ={}
    for cle in dico.keys():
        val = dico[cle]
        dic_inv[val] = cle
    return dic_inv
