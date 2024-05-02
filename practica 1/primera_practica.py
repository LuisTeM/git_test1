#Importamos los otros ficheros para usar sus funciones
import mensaje  
import operacion
import lista
import ciclo
import ee

#Imprimimos un menu para la seleccion del usuario
opcion = 0  #inicializamos la variable "opcion" para que inicie el bucle while

while(opcion != 6): #Usamos un bucle while con la condicion de repetirse hasta que el usuario ingrese el numero 6
    print("Hola, bienvenido. Por favor elige un programa a ejecutar:")
    print("1.-Mensaje")
    print("2.-operacion")
    print("3.-Lista")
    print("4.-Ciclo")
    print("5.-EE")
    print("6.-Salir")

    opcion = int(input())   #Variable para almacenar la entrada del usuario, le decimos a la maquina que transforme la variable en entero, ya que, por default la convertira en string

    #Empezamos la comparacion de las opciones posibles con la entrada del usuario
    if(opcion == 1):    #primera opcion
        print("Ingrese su nombre: ")
        nombre = input()    #Solicitamos al usuario su nombre y almacenamos en esta variable
        mensaje.mess(nombre)    #Llamamos a la función dentro del fichero llamado "mensaje"
    elif(opcion == 2):  #segunda opcion
        print("vamos a sacar el area de un triangulo")
        print("Ingrese la medida de la base: ")
        b = int(input())    #Ingresamos la variable de la base y la convertimos en entero
        print("Ingrese la altura: ")
        h = int(input())    #Ingresamos la variable de la altura y la convertimos en entero
        resul = operacion.area(b,h) #asignamos el valor que nos devuelve la funcion a una variable para usarla dentro de este fichero
        print(resul)
    elif(opcion == 3):  #tercera opcion
        print("Ingresa 1 elementos para hacer una lista")
        prod = input()  #Ingresamos una variable para agregarla a la lista
        lista1 = lista.list(prod)   #asignamos el valor que nos devuelve la funcion a una variable para usarla dentro de este fichero
        print(lista1)
    elif(opcion == 4):  #cuarta opcion
        print("Ingresa cuantas veces quieres que se repita un mensaje: ")
        rep = int(input())
        ciclo.repeticiones(rep) #Le decimos cuantas repeticiones hara el bucle for
    elif(opcion == 5):
        ee.EE()
    else:   #opcion en caso de ser introducido un valor no valido
        print("woau")