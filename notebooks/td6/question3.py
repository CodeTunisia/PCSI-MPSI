from question1 import estUneMaj
from question2 import chaineListe
txt = "Le prénom de cette Dame est Élise"
print("Phrase à tester :", txt)
lst = chaineListe(txt) # convertir la phrase en une liste de mots
for mot in lst:
    prem = mot[0]  # extraction du premier caractère
    if estUneMaj(prem):  # test de majuscule
        print(mot) # analyser chacun des mots de la liste

# Variante plus compacte, utilisant la composition :
print("Variante :")
for mot in lst:
    if estUneMaj(mot[0]):
        print(mot)