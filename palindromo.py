def palindromo(word):
    word = word.replace(' ', '').lower()
    invers_word = word[::-1]
    if word == invers_word:
        return True
    else:
        return False


def run():
    word = input("Ecribe una palabra: ")
    is_palindromo = palindromo(word)
    if is_palindromo == True:
        print("La palabra es palindromo.")
    else:
        print("La palabra no es palindromo.")


# Punto de entrada de la aplicacion
if __name__ == "__main__":
    run()