import matplotlib.pyplot as plt

class Circle(object):

    def __init__(self, radius, color):  # La función __init__ es el constructor
        self.radius = radius
        self.color = color
#podemos crear metodos para interactuar con los valores de los objetos
    def add_radius(self,r):
        self.radius = self.radius + r
        return self.radius

    def change_color(self,new_color):
        self.color = new_color
        return new_color

    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()

    # Creación del objeto RedCircle fuera de la clase
RedCircle = Circle(10, "red")


RedCircle.add_radius(8) # r se transforma en el valor pasado por parámetro
RedCircle.change_color("blue")

# Imprimir los atributos del objeto RedCircle
print("El radio del círculo es:", RedCircle.radius)
print("El color del círculo es:", RedCircle.color)
print(RedCircle.drawCircle()) # dibuja el gráfico
print(dir(RedCircle))

print("********************************************")

class Car(object):
    def __init__(self,make,model,color):
        self.make=make
        self.model=model
        self.color=color
        self.owner_number = 0
    def car_info(self):
        print("make: ",self.make)
        print("model:", self.model)
        print("color:",self.color)
        print("number of owners:",self.owner_number)
    def sell(self):
        self.owner_number=self.owner_number + 1

my_car = Car("BMW","M3","red")
my_car.car_info() #llamamos al metodo car_info

#Call the method  sell()  in the loop, then call the method  car_info() again

for i in range(5):
    my_car.sell()

my_car.car_info()