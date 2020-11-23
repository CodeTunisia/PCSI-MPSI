list_dict = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"},
          {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Liste originale : ", list_dict)
u_value = set( val for dic in list_dict for val in dic.values())
print("Valeurs uniques : ",u_value)