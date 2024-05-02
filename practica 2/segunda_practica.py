print("Hola, este es un programa para iniciar una lista")
opcion = "si"   #Inicializamos la variable "opcion" en "si" para iniciar el bucle

while(opcion != "no"):  #Inicia el bucle y continuara hasta que el usuario responda "no"
    print("Creara una nueva lista?")
    print("Si o NO")
    opcion = input().lower()    #Recibimos la respuesta del usuario y la convertimos en minuscula para usarla en la comparación

    if(opcion == "si" or opcion == "no"):   #Es una condicional para saber si la respuesta del usuario es valida, ya que, solo aceptamos "si" o "no"
        if(opcion == "si"):     #condicional para saber si la respuesta del usuario es "si"
            opcion1 = "si"      #Iniciamos otra variable para el siguiente bucle
            lista = []          #iniciamos una variable como una lista vacia
            while(opcion1 != "no"):     #Un Bucle para agregar un nuevo producto
                print("Dime que producto agregaras: ")
                elemento = input()      #Variable para recibir la entrada del usuario
                lista.append(elemento)      #Agregamos el producto que usuario ingreso a la lista
                print("Agregaras otro producto?")       #Preguntamos al usuario si agregara otro producto
                print("Si o No")
                opcion1 = input().lower()      #Recibimos la entrada del usuario y la convertimos en minuscula
            print(lista)        #Mandamos a la pantalla la lista escrita por el usuario
        elif(opcion == "no"):   #Condicional para saber si la respuesta es "no"
            print("Bueno, adios")
    else:       #Respuesta en caso de que la respuesta del usuario no sea la esparada
        print("Lo siento pero no puedo entender tu petición")