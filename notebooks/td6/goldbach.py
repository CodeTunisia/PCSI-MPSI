# NOM DU MODULE : goldbach.py
def test_goldbach(n):
    for p in range(2, n-1):
        if test_premier(p) and test_premier(n-p):
            return True
    return False
if __name__ == "__main__":
    # print(list(filter(lambda n : goldbach(n), range(4, 101, 2))))
    for n in range(4, 10001, 2):
        if not goldbach(n):
            print("Conjecture mise en défaut pour {}".format(n))

    if n == 10000:
        print("Conjecture vérifiée")