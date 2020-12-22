# NOM DU MODULE : parfait.py
def test_parfait(p): 
    s=0
    for k in range(1,p+1):
        if p%k==0 :
            s+=k
    return s==2*p
if __name__ == "__main__":
    print([k for k in range(1,1001) if test_parfait(k)])
    # Nous pouvons également utilisé la fonction filter
    # print(list(filter(lambda p : test_parfait(p), range(1,1001))))