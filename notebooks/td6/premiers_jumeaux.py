# NOM DU MODULE : premiers_jumeaux.py
from premier import test_premier

def liste_couples_premiers_jumeaux() :
    c=0
    p=3
    res=[]
    while c!=100 :
        if test_premier(p) and test_premier(p+2) :
            res.append((p,p+2))
            c+=1
        p+=2
    return res
if __name__ == "__main__":
    print(liste_couples_premiers_jumeaux())