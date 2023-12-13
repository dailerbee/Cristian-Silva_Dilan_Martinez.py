# Lista de palabras propuestas por el usuario.
Palabras = []
for i in range(5):
    Palabra = input(f"Ingrese la palabra{i+1}:")
    Palabras.append(Palabra)

#Funcion para organizar las palabras. 
def ordenar_por_tamaño(Palabras):
    return sorted(Palabras, key=len, reverse=True)

#Menu de seleccion.
while True: 
    print("\nSeleccione una opcion:")
    print("1. Orden alfabetico")
    print("2. Orden de tamañano, de la mas larga a la mas corta")
    print("3. Orden aleatirio")
    print("4. Orden inverso al ingreso")
    print("5. Orden igual al ingreso")
    print("6. Salir")

    seleccion = input ("Elija una opcion:")

    match seleccion:
        case "1":
            Palabras_Ordenadas = sorted(Palabras)
        case "2":
            Palabras_Ordenadas= ordenar_por_tamaño(Palabras)
        case "3":
            import random
            random.shuffle(Palabras)
            Palabras_Ordenadas=Palabras 
        case "4":
            Palabras_Ordenadas=list(reversed(Palabras))
        case "5":
            Palabras_Ordenadas = Palabras
        case "6":
            break
        case "_":
            print("Opcion no valida. Elija una opcion del 1 a 6.")
            continue
        #Realizar y Escribir un listado en el orden seleccionado en el menu. 
    print("\n palabras ordenadas:")
    for palabras in Palabras_Ordenadas:
         print(palabras)
