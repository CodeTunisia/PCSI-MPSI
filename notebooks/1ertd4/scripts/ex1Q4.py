dict1 = {'Dix': 10, 'Vingt': 20, 'Trente': 30}
dict2 = {'Trente': 30, 'Quarante': 40, 'Cinquante': 50}
dict3 = dict1.copy() # copier dict1 dans dict3
dict3.update(dict2) # Fusionner dict3 et dict2
print(dict3)