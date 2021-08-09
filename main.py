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