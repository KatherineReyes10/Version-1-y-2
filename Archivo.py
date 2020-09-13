import sys
import csv

def print_menu():
    print ("**********MENU**********\n")  
    print ("************************\n")
    print ("*1.Nuevo    2.Listar   *\n")
    print ("*3.Eliminar 4.Buscar   *\n")
    print ("************************\n")

    Opcion = input("Elige una opcion:\n ")
    return Opcion

Opcion = "1"

while (Opcion != 5):
    Opcion = print_menu()
    if Opcion == "1":
        print ("**Nuevo Registro**\n")

        Datos = open(sys.argv[1],'a')

        Name = input("Nombre: ")
        LastName = input("Apellido: ")
        Age = input("Edad: ")
        ID = input("Cedula: ")
        print ("!Los Datos fueron guardados con exito!\n")
        Opcion1 = input("Desea Continuar? S/N?")
        new_row = f'{Name}|{LastName}|{Age}|{ID}\n'
        Datos.write(new_row)
        if Opcion1  == "S":
            Datos.close()
            continue

        elif Opcion1  == "N":

            sys.exit()
        

        
    elif Opcion == "2":
        print("**Listar Registros**\n")
        Datos = open(sys.argv[1],"r")
        leer = csv.reader(Datos)
        for row in leer:
            print(row)
         
        Opcion1 = input("Desea Continuar? S/N?")
        if Opcion1  == "S":
            Datos.close()
            continue

        elif Opcion1 == "N":

            sys.exit()

    elif  Opcion == "4":
        print("***Buscar Por cedula***")
        Datos = open(sys.argv[1],"r")
        cedula = input("Ingrese la cedula a buscar: ")
        rows = Datos.readlines()
        for row in rows:
            data = row.split('|')
            if data[3].__contains__(cedula):
                print(f'Registro encontrado con exito: {row}\n')

            Opcion1 = input("Desea Continuar? S/N?")
            if Opcion1 == "S":
                Datos.close()
                continue

            elif Opcion1 == "N":
                sys.exit()
            






        





