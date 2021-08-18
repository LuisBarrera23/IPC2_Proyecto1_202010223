from xml.dom import minidom

def lecturaXml():
    ruta=input("Ingresa la ruta del archivo XML que desea cargar")
    documento=minidom.parse(ruta)
    terrenos=documento.getElementsByTagName("terreno")
    for terreno in terrenos:
        nombre=terreno.getAttribute("nombre")
        posicioninicio=terreno.getElementsByTagName("posicioninicio")[0]
        iniX=posicioninicio.getElementsByTagName("x")[0].firstChild.data
        iniY=posicioninicio.getElementsByTagName("y")[0].firstChild.data

        posicionfinal=terreno.getElementsByTagName("posicionfin")[0]
        finX=posicionfinal.getElementsByTagName("x")[0].firstChild.data
        finY=posicionfinal.getElementsByTagName("y")[0].firstChild.data
        print("posicion inicio para:",nombre, "X=",iniX,"Y=",iniY,", su posicion final es:","X=",finX,"Y=",finY)

        posiciones=terreno.getElementsByTagName("posicion")

        for posicion in posiciones:
            posX=posicion.getAttribute("x")
            posY=posicion.getAttribute("y")
            combustible=posicion.firstChild.data
            print("posicion:","X:",posX,"Y:",posY,"gasta combustible:",combustible)
    


def menu():
    opcion=0
    while True:
        print("----------MENU PRINCIPAL----------")
        print("\t1.Cargar archivo")
        print("\t2.Procesar archivo")
        print("\t3.Escribir archivo salida")
        print("\t4.Mostrar datos del estudiante")
        print("\t5.Generar gráfica")
        print("\t6.Salida")
        print("----------------------------------")
        try:
            opcion=int(input('Ingrese el numero de opción deseada:\n'))
            if opcion==1:
                print('Cargar archivo')
                lecturaXml()
            elif opcion==2:
                print('Procesar archivo')
            elif opcion==3:
                print('Escribir archivo salida')
            elif opcion==4:
                print('Datos del Estudiante:')
                print('> Luis Angel Barrera Velásquez')
                print('> 202010223')
                print('> Introducción a la Programación y Computación 2 sección E')
                print('> Ingenieria en Ciencias y Sistemas')
                print('> 4to Semestre')
            elif opcion==5:
                print('Generar gráfica')
            elif opcion==6:
                print("Saliendo del programa")
                exit(0)
            else:
                print("Opción no valida")

        except:
            if opcion==6:
                exit(0)
            print("Error, vuelva a intentarlo")


if __name__=='__main__':
    menu()