#Q1. 
animaux = ['chien', 'chat', 'perroquet', 'lapin']
maj_animaux = list(map(lambda el: el.upper(), animaux))
print(maj_animaux)
#Q2. 

#Q3. 
ages = [13, 90, 17, 59, 21, 60, 5, 10, 18, 60, 33]
adultes = list(filter(lambda age: age>18, ages))
print(adultes)
#Q4.
original_dict = {'a' : (6, 3), 'b' : (4, 8), 'c' : (8, 4)}
# Filtrer le dictionnaire de tuples par condition
# en utilisant lambda + filtre ()
new_dict = dict(filter(lambda x:  x[1][0] >= 6 and x[1][1] <= 4, original_dict.items()))
print(new_dict)