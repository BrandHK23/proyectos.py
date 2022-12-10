#Pregunta al usuario si informacion en una sola ronda de preguntas
#Nombre, Fecha de nacimiento, Direccion, Metas personales
#Revisar la informacion valida
#Imprimir un resumen de la informacion

                                #NOMBRE 
name = ""
name_word = input("Ingrese su nombre completo: ");

for simbol in name_word:
    if simbol == ".":
        print("Entrada incorrecta, intente nuevamente sin simbolos: ");
        name_word=input("Nombre: ")
    elif simbol == ",":
        print("Entrada incorrecta, intente nuevamente sin simbolos: ");
        name_word=input("Nombre: ")
    elif simbol == "*":
        print("Entrada incorrecta, intente nuevamente sin simbolos: ");
        name_word=input("Nombre: ")
    else:
        name += simbol
name_word = name_word.upper()
                                #Fecha de nacimiento
print("Ingrese su fecha de nacimiento.");
dia = int(input("Dia: "));
if dia > 31:
    print("Dato invalido, intente nuevamente.");
    dia = input("Dia: ");
mes = input("Ingrese el mes: ");
año = int(input("Ingrese el año: "));
if año >= 2022:
    print("Dato incorrecto, ingrese un dato correcto: ");
    año = input("Año: ");

                                #Direccion
print("Ingrese su direccion: ");
calle = input("Ingrese la calle: ");
numcalle = int(input("Ingrese el numero: "));
col = input("Ingrese la colonia: ");
cd = input("Ingrese la ciudad: ");
estado = input("Ingrese el estado: ");

                                #Metas personales
metas = input("¿Cuales son tus metas? ");
print("...");
print("...");
print("...");
print("...");
                                #Resumen
print("Nombre: ",name_word);
print("Fecha de nacimiento: ", dia,"de", mes, "del año ", año);
print("Direccion: ", calle," ", numcalle, "," ,col, ",", cd,",",estado);
print("Metas personales: ", metas);




