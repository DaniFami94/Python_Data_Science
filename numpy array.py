from stringprep import b1_set
import numpy as np
import time
import sys
import matplotlib.pyplot as plt
#NumPy stands for Numerical Python and it is an open source project

a=np.array([1,2,3,4,5])

print(type(a)) # para saber si es numpy array
print(a.shape) # el valor bidimensional del array
print(a.dtype) # para saber que tipo de dato es
print(a.mean()) # se utiliza para calcular el promedio de los valores del numpy array

x1 = 1
x2 = -1
print(x1 * x2)
#Print the even elements in the given array.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr[1:8:2])
#Esta parte accede a una subsección del array original utilizando slicing, con la notación [start:stop:step].

#Find the sum of maximum and minimum value in the given numpy array
c = np.array([-10, 201, 43, 94, 502])

max_c = c.max()
min_c = c.min()

print("El resultado de" ,max_c, "y", min_c, "es: " , max_c + min_c)

# Definimos los vectores u, v y z
u = np.array([1, 0])  # Vector u
v = np.array([0, 1])  # Vector v
z = np.array([1, 1])  # Vector z

# La función Plotvec1 como ya la tienes
def Plotvec1(u, z, v):
    ax = plt.axes()  # to generate the full window axes
    ax.arrow(0, 0, *u, head_width=0.05, color='r',
             head_length=0.1)  # Add an arrow to the U Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(u + 0.1), 'u')  # Adds the text u to the Axes

    ax.arrow(0, 0, *v, head_width=0.05, color='b',
             head_length=0.1)  # Add an arrow to the V Axes with arrow head width 0.05, color blue and arrow head length 0.1
    plt.text(*(v + 0.1), 'v')  # Adds the text v to the Axes

    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')  # Adds the text z to the Axes
    plt.ylim(-2, 2)  # set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)  # set the xlim to left(-2), right(2)

# Llamada a la función para graficar
Plotvec1(u, z, v)
#plt.show()

print(np.linspace(5, 4, num=6))

#Quiz on 1D Numpy Array

#Implement the following vector subtraction in numpy: u-v

a1 = np.array([1, 0])
a2= np.array([0, 1])

a3= np.subtract(a1,a2)
print(a3)

z = np.array([2, 4])
print(-2 * z)

#Consider the list [1, 2, 3, 4, 5] and [1, 0, 1, 0, 1]. Cast both lists to a numpy array then multiply them together:

b1 = np.array([1, 2, 3, 4, 5])
b2 =  np.array([1, 0, 1, 0, 1])
b3 = np.multiply(b1,b2)
print(b3)

#Convert the list [1, 2, 3, 4, 5] and [6, 7, 8, 9, 10] to numpy arrays arr1 and arr2.
# Then find the even and odd numbers from arr1 and arr2.

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

# Starting index in slice is 1 as first even element(2) in array1 is at index 1
even_arr1 = arr1[1:5:2]
print("even for array1", even_arr1)

# Starting index in slice is 0 as first odd element(1) in array1 is at index 0
odd_arr1 = arr1[0:5:2]
print("odd for array1", odd_arr1)

# Starting index in slice is 0 as first even element(6) in array2 is at index 0
even_arr2 = arr2[0:5:2]
print("even for array2", even_arr2)

# Starting index in slice is 1 as first odd element(7) in array2 is at index 1
odd_arr2 = arr2[1:5:2]
print("odd for array2", odd_arr2)