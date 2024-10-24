import numpy as np

a =[[11,12,13],[21,22,23],[31,32,33]]
a=np.array(a)

print(a.ndim)
print(a.shape) #calcula cuantas filas y columnas tiene el array
print(a.size) # multiplica columnas por filas en esta caso 3*3=9
print(a[1][2])
print(a[0][0])
print(a[0,0:3]) #hacemos slicing  resultado [11 12]
print(a[0][0:3]) # lo mismo de arriba con diferente sintax
x1 = np.array ([[0,1,1],
                [1,0,1]])

y1 = np.array([[1,1]
              ,[1,1],
              [-1,1]])
z1 = np.dot(x1,y1)
print(z1)

""" print(0 * 1 + 1 * 1 + 1 * -1)
print (0 * 1 + 1 * 1 + 1 * 1)
print ( 1 * 1 + 0 * 1 + 1 * -1)
print (1 * 1 + 0 * 1 + 1 * 1) """