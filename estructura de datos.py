#Tuples
#Tuples are not mutable
NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))

print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])

#accedemos a los elementos internos de la tupla
print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])


C_tuple=(-5, 1, -3, 2 , -6 , 6 , 7 ,9 ,0)

ordenar = sorted(C_tuple)

print(ordenar)

print("********************************************")

#Lists
#Lists are mutable

# Sample List

L = ["Michael Jackson", 10.1,1982,"MJ",1]
# List slicing
L[3:5]
# Use extend to add elements to list
L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])

# Use append to add elements to list

L = [ "Michael Jackson", 10.2]
L.append(['pop', 10])

# Change the element based on the index

A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

print("*********************************************")
#Sets es como una lista, pero no deja que se repitan los valores

#transformamos de set a list
list = ['A','B','C','A','B','C']
set_list = set(list)
print(set_list)

#agregamos un elemento
S={'A','B','C'}
S.add('D')

print(S)

A = [1, 2, 2, 1]
print("the sum of A is:", sum(A)) #metodo que suma los valores dentro de una lista o un se

album_set1 = set(["Thriller", 'AC/DC',2])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
album_set3 = album_set1.union(album_set2)

print(album_set3)

#Find out if album_set1 is a subset of album_set3:

print(album_set1.issubset(album_set3))
print(album_set1.issuperset(album_set3))

#Dictionaries, los keys normalmente son strings
# Create a sample dictionary

release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}



lista = ["a","b","c"]

lista.append(["e","f","h","q","s"])

print(len(lista))
print(lista)









