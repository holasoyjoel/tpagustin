import os
from queue import Empty
camiones = 0
contsoja = 0
contmaiz = 0
cont_tara_s = 0
cont_tara_m = 0
maximo_s = 0
menor_m = 0
camion_pn = 0
camion_maximo_s = 0
camion_menor_m = 0
pesonetosoja = 0
pesonetomaiz = 0


# os.system("CLS")
def menu_principal():
    while True: 
        print ("-" * 30)
        print ("Menu principal : ")
        print ("-" * 30)
        print("\n")
        print ("1- Administracion")
        print ("2- Entrega de cupos")
        print ("3- Recepcion")
        print ("4- Registrar calidad")
        print ("5- Registrar peso bruto")
        print ("6- Registrar descarga")
        print ("7- Registrar tara")
        print ("8- Reporte")
        print ("0- Fin del programa")
        print ("-" * 30)
        print ("-" * 30)
        
        opcion = int(input("selecciona una opcion del menu : "))
            
        if opcion == 1:
            os.system("CLS")
            print("\n")
            menu_administracion()
            print("\n")

        elif opcion == 3:
            os.system("CLS")
            print("\n")
            menu_recepcion()
            print("\n")

        elif opcion == 8:
            os.system("CLS")
            print ("\n")
            menu_reporte()
            print("\n")

        # elif opcion == "":
        #     os.system("CLS")
        #     print("\n")
        #     print ("ocurrio un error, vueva a ingresar una opcion del menu")
        #     menu_principal()
        #     print("\n")

        elif opcion == 0:
            print("\n")
            print ("Fin del programa")
            print("\n")
            False

        elif (opcion != 1) and (opcion != 3) and (opcion != 8) and (opcion <= 8):
            os.system("CLS")
            print("\n")
            print ("En construccion, por favor elija otra opcion")
            print("\n")

    
        else:
            os.system("CLS")
            print("\n") 
            print ("Opcion no esta dentro del menu, vuelva a ingresar")
            print("\n")


def menu_administracion():
    while True:
        print ("-" * 30)
        print ("Menu Administracion : ")
        print ("-" * 30)
        print("\n")
        print ("A. Titulares")
        print ("B. Productos")
        print ("C. Rubros")
        print ("D. Rubros x producto")
        print ("E. Silos")
        print ("F. Sucursales")
        print ("G. Producto por titular")
        print ("V. Volver al menu principal")


        opcion_administracion = input("Ingrese una opcion del menu : ")
        if opcion_administracion == "a" or opcion_administracion == "A":
            os.system("CLS")
            print("\n")
            menu_titulares()
            print("\n")

        elif opcion_administracion == "B" or opcion_administracion == "b" or opcion_administracion == "C" or opcion_administracion == "c" or opcion_administracion == "D" or opcion_administracion == "d" or opcion_administracion == "E" or opcion_administracion == "e" or opcion_administracion == "F" or opcion_administracion == "f" or opcion_administracion == "G" or opcion_administracion == "g":
            os.system("CLS")
            print("\n")
            print ("En construccion, por favor elija otra opcion")
            print("\n")
            

        elif opcion_administracion == "V" or opcion_administracion == "v":
            print("\n")
            print ("Volver al menu principal")
            print("\n")
            os.system("CLS")
            break
        else:
            os.system("CLS")
            print("\n")
            print ("opcion no valida, por favor elja otra opcion")
            print("\n")

        

def menu_titulares():
     while True:
        print("\n")
        print ("-" * 30)
        print ("Menu Titulares : ")
        print ("-" * 30)
        print("\n")
        print ("A. Alta")
        print ("B. Baja")
        print ("C. Consulta")
        print ("M. Modificacion")
        print ("V. Volver al menu anterior")

        opcion_titulares = input ("ingrese una opcion del menu : ")
        if opcion_titulares == "A" or opcion_titulares == "a":
            os.system("CLS")
            print("\n")
            print ("En construccion, por favor elija otra opcion")
            print("\n")

        elif opcion_titulares == "B" or opcion_titulares == "b" :
            os.system("CLS")
            print("\n")
            print ("En construccion, por favor elija otra opcion")
            print("\n")

        elif opcion_titulares == "C" or opcion_titulares == "c":
            os.system("CLS")
            print("\n")
            print ("En construccion, por favor elija otra opcion")
            print("\n")

        elif opcion_titulares == "M" or opcion_titulares == "m":
            os.system("CLS")
            print("\n")
            print ("En construccion, por favor elija otra opcion")
            print("\n")

        elif opcion_titulares == "V" or opcion_titulares == "v":
            print("\n")
            print ("Volver al menu anterior")
            print("\n")
            os.system("CLS")
            break

        else:
            os.system("CLS")
            print("\n")
            print ("opcion no valida, por favor elija otra opcion")
            print("\n")


def menu_recepcion():
    global contsoja
    global contmaiz
    global cont_tara_s
    global cont_tara_m 
    global maximo_s 
    global menor_m
    global camion_pn
    global camion_maximo_s
    global camion_menor_m
    global pesonetosoja
    global pesonetomaiz
    global camiones

    print(maximo_s)

    camiones = int(input("ingrese cuantos camiones arribaran : "))

    for i in range (1,camiones + 1):

        producto = input("ingrese que transporta su camion :")



        if producto == "soja":

            contsoja = contsoja + 1

            tara = int(input("ingrese su tara : "))

            cont_tara_s= cont_tara_s + tara

            if tara>maximo_s:
                print("tara mayor a maximo_s")
                maximo_s=tara
                patente = input("ingrese su patente : ")
                camion_maximo_s= patente
                peso_bruto = int(input("ingrese su peso bruto : "))
                peso_neto = peso_bruto - tara
                pesonetosoja = pesonetosoja + peso_neto
                if peso_neto>0:
                    print("para el camion numero ",i," con patente ",patente," su peso neto es de ",peso_neto)
                else: 
                    print("el peso bruto debe ser mayor que la tara")
                

            else:
                print("tara menor a maximo_s")
                patente = input("ingrese su patente : ")
                camion_maximo_s = patente
                peso_bruto = int(input("ingrese su peso bruto : "))
                peso_neto = peso_bruto - tara
                pesonetosoja = pesonetosoja + peso_neto
                print("para el camion numero ",i," con patente ",patente," su peso neto es de ",peso_neto)

        
        else:
            if producto == "maiz":
                contmaiz = contmaiz + 1
                tara = int(input("ingrese su tara : "))
                cont_tara_m= cont_tara_m + tara
                if menor_m == 0:
                    menor_m = tara
                else:

                    if tara<menor_m:
                            menor_m=tara
                            patente = input("ingrese su patente : ")
                            camion_menor_m = patente
                            peso_bruto = int(input("ingrese su peso bruto : "))
                            peso_neto= peso_bruto - tara
                            pesonetomaiz = pesonetomaiz + peso_neto
                            if peso_neto>0: 
                                print("para el camion numero ",i," con patente ",patente," su peso neto es de ",peso_neto)
                            else: 
                                print("el peso bruto debe ser mayor que la tara")   
                    else: 
                        patente = input("ingrese su patente : ")
                        camion_menor_m = patente
                        peso_bruto = int(input("ingrese su peso bruto : "))
                        peso_neto = peso_bruto - tara
                        pesonetomaiz = pesonetomaiz + peso_neto
                        print("para el camion numero ",i," con patente ",patente," su peso neto es de ",peso_neto)
    
        
            





def menu_reporte():
    while True:
        print("\n")
        print ("Reportes")
        print("\n")
        print (f"- Cantidad total de camiones que llegaron: {camiones} ")
        print (f"- Cantidad total de caminoes de soja: {contsoja} ")
        print (f"- Cantidad total de camiones de maiz {contmaiz}")
        print (f"- Peso neto total de soja: {pesonetosoja} ")
        print (f"- Peso neto total de maiz: {pesonetomaiz} ")
        print ("- Promedio del peso neto de soja por camion:  ")
        print ("- Promedio del peso neto de maiz por camion:  ")
        print (f"- Patente del camion de soja que mayor cantidad de soja descargo: {camion_maximo_s}  ")
        print (f"- Patente del camion de maiz que menor cantidad de maiz descargo: {camion_menor_m} ")
        print("\n")

        input("Presione Enter para volver al menu anterior : ")
        os.system("CLS")
        menu_principal()
    

menu_principal()
