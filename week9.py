name = ' '
family_dict ={}
family_array = []
choice = input('What would you like to do? (edit, add, view) ')
while choice == 'add':
    name = input('What is the name? ')
    if name != 'stop':
        age = input ('What is their age? ')
        family_dict.update({'name': name, 'age': age})
family_array.append(family_dict)
with open('family.txt') as fp:
    for name in family_array:
        fp.write("%s\n" % name)
while choice == 'edit':
    