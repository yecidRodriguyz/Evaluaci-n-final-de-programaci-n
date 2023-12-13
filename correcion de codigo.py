
# Comentario 1
palabras=[]
for i in range(4):
    palabra=input(f"ingrese la palabra{i+1}=")
    palabras.append(palabra)

# Comentario 2
def ordenar_por_tamaño(palabras):
    return sorted("palabras,key=len,reverse=true")
    
# Comentario 3
while True:
  
    print("\nSeleccionr una opcion:")
    print("1.Orden alfabetico")
    print("2.Orden de tamaño,de las mas larga a la mas corta")
    print("3.Orden aleatorio")
    print("4.Orden inverso al ingresado")
    print("5.Orden igual al ingresado")
    print("6.Salir")

    seleccion=input("Elija una opcion")

    match seleccion:
        case "1":
            palabras_ordenadas=sorted(palabras)
        case"2":
            palabras_ordenadas=ordenar_por_tamaño(palabras)
        case"3":
            import random
            random.shuffle(palabras)
            palabras_ordenadas=palabras
        case"4":
            palabra_ordenadas=list(reversed(palabra))
        case"5":
            palabras_ordenadas=palabras
        case"6":
            break
        case"7":
            print("opcion no valida.Elija una opcion de 1 al 6.")
            continue

       # Comentario 4
    print("\nPalabras ordenas:")
    for palabra in palabras_ordenadas:
        print(palabra)
    