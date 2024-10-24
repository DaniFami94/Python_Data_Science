#You are working on a Python program to simulate a car dealership's inventory management system.
# The system aims to model cars and their attributes accurately.
#Task-1. You are tasked with creating a Python program to represent vehicles using a class.
# Each car should have attributes for maximum speed and mileage.
#Task-2. Update the class with the default color for all vehicles,"white"
#Task-3. Additionally, you need to create methods in the Vehicle class to assign seating capacity to a vehicle
#Task-4. Create a method to display all the properties of an object of the class.
#Task-5. Additionally, you need to create two objects of the Vehicle class object that should have a max speed of 200kph
# and mileage of 50000kmpl with five seating capacities,
# and another car object should have a max speed of 180kph and 75000kmpl with four seating capacities.
class Vehicle(object):

    def __init__(self,maximum_speed,mileage,color = "white"):

        self.seating_capacity = None
        self.color = color
        self.maximum_speed = maximum_speed
        self.mileage = mileage

    def assing_seating_capacity(self,seating_capacity):
        self.seating_capacity = seating_capacity

    def display_properties(self):
        print("Properties of the vehicle")
        print ("Maximum speed : ", self.maximum_speed)
        print("Mileage : ", self.mileage)
        print("Color : ", self.color)
        print("Seating capacity : ", self.seating_capacity)

vehicle_1 = Vehicle("200kph","5000kpml")
vehicle_1.assing_seating_capacity(5)
vehicle_1.display_properties()

vehicle_2 = Vehicle("180kph","75000kmpl")
vehicle_2.assing_seating_capacity(4)
vehicle_2.display_properties()
