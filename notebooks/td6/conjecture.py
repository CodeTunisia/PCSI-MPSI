# NOM DU MODULE : conjecture.py
def test_conjecture(n):
    k = 1
    while k < n:
        if test_premier(n-k):
            return True
        k *= 2
    return False
if __name__ == "__main__":
    #print(list(filter(lambda n : test_conjecture(n), range(3, 1001, 2))))
    for n in range(3, 10001, 2):
        if not conjecture(n):
            print("Conjecture mise en défaut pour {}".format(n))
            break
        if n == 10000:
            print("Conjecture vérifiée")