from random import randint

INIT_NUMBER = 0
LAST_NUMBER = 100


def generate_random_number(init_number, last_number):
    return randint(init_number, last_number)


def run():
    random_number = generate_random_number(INIT_NUMBER, LAST_NUMBER)
    print("Se ha generado un numero aleatorio entre [" + str(INIT_NUMBER) + " y " + str(LAST_NUMBER) + "] ... Adivinalo!!!")
    while True:
        user_number = int(input("Escribe un numero: "))

        if user_number == random_number:
            print("Exactamente!! es " + str(user_number))
            break
        
        if random_number > user_number:
            print("El numero es mayor")

        if random_number < user_number:
            print("El numero es menor")


if __name__ == "__main__":
    run()