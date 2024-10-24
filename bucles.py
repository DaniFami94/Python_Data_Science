#Use loops to print out the elements in the list A:
A=[3,4,5]

for numbers in A:
    print(numbers)

#Find the value of  x  that will print out the sequence  1,2,..,10 :

print("******************************")

x = 11
y = 1
while(y != x):
    print(y)
    y=y+1

print("******************************")
# For loop example

dates = [1982, 1980, 1973]
N = len(dates)

for i in range(N):
 print(dates[i])

 print("******************************")
 #Use for loop to change the elements in list

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])


print("******************************")

# Loop through the list and iterate on both index and element value

squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)


print("******************************")

# While Loop Example

dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while (year != 1973):
    print(year)
    i = i + 1
    year = dates[i]

print("It took ", i, "repetitions to get out of loop.")

print("******************************")

# Print the elements of the following list:
Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']

for i in range(0,6):
    print(Genres[i])
#can be done also:
""" Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print(Genre) """

print("******************************")

"""PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
score = 0
while score < 6:
    print(PlayListRatings[score])
    score = score + 1"""

#Write a while loop to display the values of the Rating of an album playlist stored in the list PlayListRatings.
# If the score is less than 6, exit the loop.
# The list PlayListRatings is given by: PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
rating = PlayListRatings[0]

while i < len(PlayListRatings) and rating >= 6:
    print(rating)
    i = i + 1
    rating = PlayListRatings[i]

#Write a while loop to copy the strings 'orange' of the list squares to the list new_squares.
# Stop and exit the loop if the value on the list is not 'orange':

colors = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_colors = []
j = 0
while j < len(colors) and colors[j] == 'orange':
    new_colors.append(colors[j])  # Añadimos el valor 'orange' a new_colors, usamos append para meter los valores de una lista en otra mientras se recorre el bucle
    print(new_colors[j])
    j = j + 1

#Your little brother has just learned multiplication tables in school.
# Today he has learned tables of 6 and 7.
# Help him memorise both the tables by printing them using for loop.

for i in range (1,10):
    i = i * 6
    print(i)
print("******************************")
for i in range (1,10):
    i = i * 7
    print(i)

#Your brother needs to write an essay on the animals whose names are made of 7 letters.
# Help him find those animals through a while loop and create a separate list of such animals.
#The following is a list of animals in a National Zoo.
Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
new_animals = []
k = 0

# Buscamos animales con nombres de 7 letras

while k < len(Animals):
    if len(Animals[k]) == 7:
        new_animals.append(Animals[k]) # Añadimos a la nueva lista
    k = k + 1

# Imprimimos la lista de animales con 7 letras
print(new_animals)