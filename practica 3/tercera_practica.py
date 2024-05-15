
#Inicializamos las variables a usar
opcion = "si"
lista = []
inicial = "l"
respuesta2 = ""

#Empezamos con el bucle while para ingresar todos los nombres que deseemos
print("**Bienvenido, crearemos una lista con los nombres que usted desee.**")
while(opcion != "no"):  #El bucle terminara hasta que ingresemos la respuesta "no"
    print("Ingrese un nombre: ")
    respuesta = input()     #Lectura de la variable que el usuario ingrese
    lista.append(respuesta)     #Con la funcion append vamos agregando el nombre dentro de la lista, justo al final de cada elemento
    print("Ingresara otro nombre?")     #Preguntamos si ingresara otro nombre a la lista
    opcion = input().lower()

#Empezamos otro bucle while con otra lista de las cosas que puede hacer con los nombres ingresados
while (respuesta2 != 0):        #El bucle terminara hasta que el usuario ingrese la opcion numero 4
    print("**Estas son las opciones que puede hacer dada la lista creada.**")
    print("1.-Filtrar por cantidad de letras en el nombre")
    print("2.-Filtrar por inicial en el nombre")
    print("3.-Convertir la inicial en mayuscula")
    print("4.-Eliminar elementos repetidos")
    print("5.-Agregar otro elemento")
    print("6.-Mostrar lista")
    print("0.-Salir")
    respuesta2 = int(input())

    if (respuesta2 == 1):   #Comenzamos con el despliegue del algoritmo dependiendo de la opcion ingresada
        try:        #Try es un bloque para hacer un codigo en especifico
            filtro1 = list(filter(lambda nombre: len(nombre) >= 5, lista)) #con la funcion "list" convertimos el resultado que arroje la funcion "filter" en una lista
            print(filtro1)                                                 #lambda es una funcion anonima que nos ahorra crear una funcion aparte
        except TypeError:   #En caso de haber un error con Except hara una excepcion evitando asi que el programa se detenga, en su lugar lanzara un mensaje de error y continuara
            print("Error en el fitro 1")

    elif(respuesta2 == 2):
        try:
            print("Ingrese la inicial: ")
            inicial = input()
            filtro2 = list(filter(lambda nombre: nombre[0] == inicial, lista))  #Recuerda que filter necesita una funcion y un iterable. En este caso Lambda es la funcion y la lista es el iterable
            if(filtro2 == []):      #Si el resultado es una lista vacia se compara y lanzara un mensaje distinto
                print("No hay ningun nombre con esa letra")
            print(filtro2)
        except TypeError:
            print("Error en el filtro 2")

    elif(respuesta2 == 3):
        try:
            filtro3 = list(map(lambda nombre : nombre.capitalize() , lista))      #Map es una funcion que necesita una funcion y un iterable
            print(filtro3)                                                        #a diferencia de filter Map agregara una funcion a cada elemento de una lista, ahorrandonos hacer un for
        except TypeError:
            print("Error en el fitrlo 3")
    elif(respuesta2 == 4):
        conjunto = set(lista)   #Convertimos la lista en un conjunto con la funcion "set", provocando que existan elementos unicos
        print(conjunto)

    elif(respuesta2 == 5):
        respuesta3 = ""
        while(respuesta3 != "no"):
            print("Ingrese un nombre: ")
            respuesta = input()
            lista.append(respuesta)
            print("Ingresara otro nombre?")
            respuesta3 = input().lower()

    elif(respuesta2 == 6):
        print(lista)

    elif(respuesta2 == 0):
        print("Adios")
        break       #Si el usuario elige la opcion 4 entonces se detendra con esta linea de codigo
    else:
        print("Ingrese una respuesa valida por favor")