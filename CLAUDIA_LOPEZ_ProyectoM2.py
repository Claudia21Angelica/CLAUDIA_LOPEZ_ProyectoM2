#Inicio de la consulta para validacion de una frase acorde al rango de entre 4 y 8 digitos.
print("----------------------------------------------------")
#Cadena de texto para informar sobre la funcion del programa.)
print("Este programa tiene la finalidad de identificar la longitud de una palabra ingresada.")
print("*Favor de responder acorde a lo que se solicita*")
print("----------------------------------------------------")
#Mientras la sentencia sea verdadera se ejecuta el siguiente recuadro de codigo.
while True:
        try:
            personas = int(input( "Cantidad de consultas a realizar: "))
        except ValueError:
            print("Debes escribir un numero")
            continue
        if personas == 0:
            print("Parece ser que no necesitas realizar alguna consulta.")
            break
        if personas < 0:
            print("Las consultas negativas no son posibles")
            continue
        else:
            break
print("----------------------------------------------------") 
#Mientras la variable sea menor o igual a 0 se cierra el programa.
while personas > 0:
        while True:
            try:
                #Se declara la variable palabra para crear la condicional correspondiente.
                palabra = len(input( "Ingrese una palabra de entre cuatro y ocho caracteres: "))
            
            #Si no se ingresa un valor indicado se despliega el siguiente mensaje de error.
            except ValueError:
                palabra("Debes escribir una frase de entre cuatro y ocho caracteres")
                continue
            #Condicionales acorde a la cantidad de caracteres en la frase.
            if palabra > 8:
                print("Debes escribir menos digitos ya que cuenta con",palabra, "caracteres.")
                continue
            if palabra < 4:
                print("Debes escribir más digitos ya que la palabra ingresada solo tiene",palabra,"caracteres.")
                continue
            if palabra == 0:
                print("Favor de escribir alguna frase de entre cuatro y ocho caracteres")
                continue       
            #Si no se establecio alguna condicion anterior la palabra a evaluar si cumple las caracteristicas acordadas.
            else:
                print("----------------------------------------------------")
                print("Es una palabra correcta con", palabra, "caracteres")
                break
        personas = personas - 1
        continue     
#Si se realizan las encuestas solicitadas se realiza una salida del programa.
if personas == 0: 
    #Cadena de texto de salida.
    print("----------------------------------------------------")
    print("----------Fin de la consulta----------")
    input("Presione enter para concluir esta consulta.")

print("----------------------------------------------------")

lista = ["########################################","########## SALTO DE PROGRAMA ###########","########################################"]
for l in lista:
    print (l)

#Inicio de la evaluacion de cuadrantes mediante el ingreso de dos numeros.
print("----------------------------------------------------")
#Cadena de texto para informar sobre la funcion del programa.
print("Este programa tiene la finalidad de evaluar el cuadrante correspondiente ingresando dos números.")
print("*Favor de responder acorde a lo que se solicita*")
print("----------------------------------------------------")
while True:
        try:
            personas = int(input( "Cantidad de consultas a realizar: "))
        except ValueError:
            print("Debes escribir un numero")
            continue
        if personas == 0:
            print("No necesita realizar alguna consulta")
            break
        if personas < 0:
            print("Las consultas negativas no son posibles")
            continue
        else:
            break
#Se declaran las variables x , y para solicitar dos numeros ya sean positivos o negativos.
while personas > 0:
        while True:
            try:
                #Definimos la variable y para solicitar numeros.
                x = float (input ('Ingresa el valor de x: '))
            #En caso de que el usuario ingrese un valor que no corresponda a un número se desplegará el siguiente mensaje.
            except ValueError:
                print("Debes escribir algún número positivo o negativo.")
                continue 
            try:
                #Definimos la variable y para solicitar numeros.
                y = float (input ('Ingresa el valor de y: '))
            #En caso de que el usuario ingrese un valor que no corresponda a un número se desplegará el siguiente mensaje.
            except ValueError:
                print("Debes escribir algún número positivo o negativo.")
                continue
            #Definimos condicion de punto de origen
            if x == 0 and y == 0:
                print ('Punto de origen')
                print("----------------------------------------------------")
            #Eje y
            if x == 0 and y > 0:
                print ("Eje Y:",y)
                print("----------------------------------------------------")
            #Eje x
            if y == 0 and x > 0:
                print ("Eje X:",x)
                print("----------------------------------------------------")
            #Cuadrante positivo, positivo.
            if x > 0 and y > 0:
                print ("Cuadrante I")
                print("----------------------------------------------------")
            
            #Cuadrante negativo, positivo.
            if x < 0 and y > 0:
                print ("Cuadrante II")
                print("----------------------------------------------------")
              
            #Cuadrante negativo, negativo.
            if x < 0 and y < 0:
                print ("Cuadrante III")
                print("----------------------------------------------------")
            #Cuadrante positivo, negativo.
            if x > 0 and y < 0:
                print ("Cuadrante IV") 
                print("----------------------------------------------------")      
            else:
                break   
        personas = personas - 1
        continue      
if personas == 0:
    #Salimos del programa
    print("----------------------------------------------------")
    input("Presione enter para cerrar el programa.")