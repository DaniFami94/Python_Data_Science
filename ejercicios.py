users_choice = "yes"  # Inicializamos la variable para entrar en el bucle

while users_choice.lower() == "yes":  # Convertimos a minúsculas para hacer la comparación insensible a mayúsculas
    # 1. Solicitar la entrada del usuario
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    # 2. Imprimir la entrada del usuario
    print("Your name is " + name + " and you are " + age + " years old")
    print("\n")

    # 3. Solicitar si desea continuar, hasta que el usuario introduzca un valor válido
    while True:
        users_choice = input("Do you want to continue? (Yes/No): ").lower()
        if users_choice in ["yes", "no"]:
            break
        else:
            print("Valor incorrecto, por favor introduce 'Yes' o 'No'.")

    # 4. Si el usuario elige "no", salimos del bucle
    if users_choice == "no":
        print("You have chosen to stop. Goodbye!")


