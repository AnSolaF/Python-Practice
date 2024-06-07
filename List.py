#LISTAS
#Este nuevo tipo de variable puede contener cualquier 
# valor valido para las mismas: Stings,boolean,floats,int...

my_list = ['Python', 53, False,10,'Hola Mundo']
print(type(my_list))

print(my_list)
# print(my_list[3])

my_list.append('87') #sirve para agregar un objeto a nuestra lista
print(my_list)

my_list.insert(7, 'Andres')
print(my_list)

my_list.remove('Hola mundo')#Remueve lo que le pidamos.
print(my_list)

print(my_list.pop(2))#remueve cosas segun la posicion que indiquemos.
print(my_list)

my_list.reverse()#Pone la lista al reves
print(my_list)

my_list.clear()#borra la lista y la deja vacia.
print(my_list)