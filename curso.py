var_1 = 6
var_2=  2
total = var_1/var_2

print(type(total))

def f(x):
    y =  x + 2
    return y

print(f(5))


for i in range(1,20):
    if i % 2 == 0:
        print (i)

def multiplicacion(x,y):

    resultado = x * y
    if resultado == 50:
        print("la variable es la adecuada")
    else:
        print("intenta con otro valor")
    return resultado

print(multiplicacion(5,10))


#hacemos stride para saltar los caracteres del string
cadena = "la cadena es la adecuada"
resultado = cadena[::2]
print(resultado) # l aeae aaeud, va de dos en dos

correct_password = "python1234"
password = input("ingrese contraseña: ")

while True:
    if password == correct_password:
        print("contraseña correcta bienvenido")
        break
    else:
        print("intenta de nuevo contraseña incorrecta")
        password = input("ingrese contraseña: ")
    