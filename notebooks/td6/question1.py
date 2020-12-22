def estUneMaj(car):
    if car in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return True
    else:
        return False
# Test :
if __name__ == '__main__':
    caracteres ="Hello World!"
    print("Caractères à tester :", caracteres)
    for car in caracteres:
        print(car, estUneMaj(car))