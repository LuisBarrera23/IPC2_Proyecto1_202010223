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

        except:
            print("Error, vuelva a intentarlo")


if __name__=='__main__':
    menu()