import random

PASSWORD_SIZE = 30

def generate_password(size):
    mayusculas = ("A", "B", "C", "D", "E", "F", "G", "H", "I")
    minusculas = ("a", "b", "c", "d", "e", "f", "g", "h", "i")
    simbolos = ("*", "$", "&", "/", "(", ")", "=", "?", "'", "¿")
    numeros = (1,2,3,4,5,6,7,8,9,0)

    caracteres = mayusculas + minusculas + simbolos + numeros
    new_password = []
    
    for count in range(size):
        new_password.append(str(random.choice(caracteres)))
    return "".join(new_password)


def run():
    password = generate_password(PASSWORD_SIZE)
    print("Tu nueva contraseña es: " + password)


if __name__ == "__main__":
    run()