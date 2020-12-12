def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


def run():
    # for contador in range(1000):
    #     if(es_par(contador) == False):
    #         continue
    #     print(contador)

    # for i in range(10000):
    #     if(i == 5678):
    #         break
    #     print(i)
    
    texto = input("Escribe un texto: ")
    for caracter in texto:
        if(caracter == 'o'):
            break
        print(caracter) 
        
if __name__ == "__main__":
    run()