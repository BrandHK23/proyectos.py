#Definimos la funcion que contendra las variables
def address(name,bdate,address,metasp):
    print("\n Nombre: ", name, "\n Fecha de nacimiento: ", bdate, "\n Direccion: ", 
    address, "\n Metas personales: ", metasp)

#Utilizamos palabras clave para asignar las variables 
n = input("Ingrese su nombre: ")
bd = input("Ingrese su fecha de nacimento(dd/mm/aa): ")
ad = input("Ingrese su direccion: ")
mp = input("¿Cuales son sus metas personales? ")

#Invocamos la funcion con los parametros    
    #Se ordenan en el orden que son declaradas en la funcion (n = name).
address(n,bd,ad,mp)