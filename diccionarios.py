def run():
    mi_diccionario = {
        'llave': 23,
        'llave-uno': True,
        'llave-dos': 'Prueba'
    }

    # print(mi_diccionario["llave"])
    # print(mi_diccionario["llave-uno"])
    # print(mi_diccionario["llave-dos"])

    poblacion_paises = {
        "Colombia": 100_000_000,
        "Inglaterra": 200_000
    }

    # print(poblacion_paises["Colombia"])

    for pais in poblacion_paises.keys():
        print(pais)

    for pais in poblacion_paises.values():
        print(pais)
    
    for pais, poblacion in poblacion_paises.items():
        print("Pais: " + pais + " tiene una poblacion: "+ str(poblacion))

if __name__ == "__main__":
    run()