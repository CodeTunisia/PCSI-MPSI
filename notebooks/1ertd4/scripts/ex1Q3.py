librairie = {"stylo":187, "crayon" : 21, "rapporteur" : 76, "cahier": 302, "gomme":99}
resultat =  {cl:val for (cl, val) in librairie.items() if val <= 100}
print(resultat)