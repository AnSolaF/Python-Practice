# SETS

my_set = {'Andres', 'Solano', 'Fernandez'}
print(type(my_set))

my_set.add('Ansola')
print(my_set)

#Indica la diferencia que contienen los sets y la agrega a la que no lo tiene 
my_set_0 = {'Andres', 'Solano', 'Fernandez'}
my_set.difference_update(my_set_0)
print(my_set)
