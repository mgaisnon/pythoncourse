
table= int(input('Veuillez entrer la table à afficher : '))
list_values = []
for i in range(1, 11):
    if(i* table % 3 == 0):
        list_values.append(f'{i* table}*')
    else:
        list_values.append(i*table)


print(list_values)