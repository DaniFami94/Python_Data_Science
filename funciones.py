def printstuff(stuff):
    for index,value in enumerate(stuff):
        print("Album",index,"Rating is ", value)

album_ratings=[10.0,8.5,9.5]

printstuff(album_ratings)
print("***********************")

def f(a, b):
    c = a * b

    return c

print(f(10, 20))

a=4
b=2
print("***********************")

#Complete the function g such that the input c is a list of integers and the output
# is the sum of all the elements in the list.

def sumar_lista(valores):
    lista_total = sum(valores)
    return lista_total

print(sumar_lista([1,2,3,4,5,6,7,8,9,10]))

print("***********************")
# Function example

def type_of_album(artist, album, year_released):
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"

x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)
print("***********************")
#Similarly, The arguments can also be packed into a dictionary as shown:

def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')

print("***********************")

#Come up with a function that divides the first input by the second input:

def dividir_valores(num1,num2):

    resultado = num1 / num2
    return resultado

num1 = int(input("introduce un número: "))
num2 = int(input("introduce otro número: "))

print("El resultado de la división es :" , dividir_valores(num1,num2))

print("***********************")

#Write a function code to find total count of word little in the given string:
# "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.
# Its fleece was white as snow And everywhere that Mary went Mary went,
# Mary went Everywhere that Mary went The lamb was sure to go"**
# Python Program to Count words in a String using Dictionary

def freq(string, passedkey):
    # step1: A list variable is declared and initialized to an empty list.
    words = []

    # step2: Break the string into list of words
    words = string.split()  # or string.lower().split()

    # step3: Declare a dictionary
    Dict = {}

    # step4: Use for loop to iterate words and values to the dictionary
    for key in words:
        if key == passedkey:
            Dict[key] = words.count(key)
            # step5: Print the dictionary
    print("Total Count:", Dict)


# step6: Call function and pass string in it
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go", "little")



