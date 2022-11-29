print("Bienvenido, este programa indica si un número es par o impar");
r = str;
intento = True
while intento == True:
    if r == "n":
        intento == False;
        print("Programa terminado...");
        break
    else:
        var = int(input("Ingrese un numero entre 1 y 1000: "));
        if (var % 2 == 0):
            print("¡Es un número par!\n");
            r = input("Quiere ingresar otro número?(s/n): ");
        else:
            print("¡Es un número impar!\n");
            r = input("Quiere ingresar otro número?(s/n): ");
            

            
