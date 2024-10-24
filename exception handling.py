import math

from PIL.ImImagePlugin import number

"""a = 1

try:
    b = int(input("Please enter a number to divide a: "))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete") """

#Exercise 1: Handling ZeroDivisionError

def safe_divide(numerator,denominator):
 try:
    result =  numerator / denominator
    return result
 except ZeroDivisionError:
     print("Error: Cannot divide by Zero.")
     return

numerator = int(input("Introduce numerator: "))
denomitador = int(input("Introduce denominator: "))

print("The result is: " , safe_divide(numerator,denomitador))

#Exercise 2: Handling ValueError

def square_root(number1):
 try:
    result = math.sqrt(number1)
    return result
 except ValueError:
     print("'Invalid input! Please enter a positive integer or a float value.")
     number1 = "Error"
     return number1

number1 = float(input("Enter a positive or a float value: "))
print("The square root of ", number1, "is: ", square_root(number1))

def complex_calculation(x):
 try:
     result = x / (x - 5)
     print(f"Result: {result}")
     return  result

 except Exception as e:
     print("An error occurred during calculation.")

 finally:
    print("Calculation Executed")


x = float(input("introduce a number: "))
complex_calculation(x)




