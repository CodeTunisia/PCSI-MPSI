# NOM DU MODULE : premier.py
def test_premier(p):
    if p < 2:
        return False
    k = 2
    while k * k <= p:
        if p % k == 0:
            return False
        k += 1
    return True
if __name__ == "__main__":
    print([k for k in range(2,100) if test_premier(k)])
    # Nous pouvons également utilisé la fonction filter
    # print(list(filter(lambda p : test_premier(p), range(2,100))))
