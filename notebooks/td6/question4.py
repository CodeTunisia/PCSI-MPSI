from question1 import estUneMaj
from question2 import chaineListe

def compteMaj(ch):
    "comptage des mots débutant par une majuscule dans la chaîne ch"
    cpt = 0
    lst = chaineListe(ch) # convertir la phrase en une liste de mots
    print(lst)
    for mot in lst:       # analyser chacun des mots de la liste
        for car in mot:
            if estUneMaj(car):
                cpt = cpt +1
    
    return cpt
        
# Test :
if __name__ == '__main__':
    phrase = "Le prix Nobel de Physique 2020 est un prix Nobel en astronomie : il revient à l’astrophysicien Britannique Roger Penrose et l’autre moitié à l’Allemand Reingard Genzel  et à l’Américaine Andrea Ghez."
    print("Phrase à tester : ", phrase)
    print("Cette phrase contient", compteMaj(phrase), "majuscules.")