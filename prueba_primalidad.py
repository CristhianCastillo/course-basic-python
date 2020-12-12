def es_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    for contador in range(2, numero):
        if numero % contador == 0:
            return False
    return True

def run():
    numero = int(input("Escribe un numero: "))
    if es_primo(numero):
        print("El numero es primo")
    else:
        print("El numero no es primo")


if __name__ == "__main__":
    run()