# Definicion de funciones
def print_message():
    print('Mensaje de Salida')

def conversation(message):
    print("Hola")
    print("¿Como estas?")
    print(message)
    print("Adios")

def adition(number_one, number_two):
    return number_one + number_two

print(adition(3,2))

option = int(input("Elige una opcion (1, 2, 3): "))
if option == 1:
    conversation("Elegiste la opcion 1")
elif option == 2:
    conversation("Elegiste la opcion 2")
elif option == 3:
    conversation("Elegiste la opcion 3")
else:
    print("Al opcion seleccionada no es valida")


print_message()