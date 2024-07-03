import numpy as np

def isNum():
    while(True):
        try:
            x=input()
            x=int(x)
            break
        except:
            print("Error, se esperaba un número, reintente")
    return(x)

def showMenu():
    print("BIENVENIDO AL REGISTRO CIVIL")
    print("----------------------------------------")
    print("1) Registrar Ciudadano")
    print("2) Buscar Registro de Ciudadano")
    print("3) Obtener Certificado de Nacimiento")
    print("4) Obtener Certificado de Antecente Penales")
    print("5) Salir")

def isRut():
    while(True):
        x=input()
        if x=="":
            print("Error, campo ingresado vacío, reintente")
        else:
            break
    return(x)

def showPersona(i,j):
    if j==0:
        print("Nombre:",pac[i,j])
    elif j==1:
        print("Rut:",pac[i,j])
    elif j==2:
        print("Edad:",pac[i,j])
    elif j==3:
        print("Fecha de Nacimiento: ",pac[i,j])
    elif j==4:
        print("Estado Civil: ",pac[i,j])


pac=np.empty([50,7],dtype="object")
f=0

while(True):
    showMenu()
    opt=isNum()
    if opt==1:
        for i in range(0,7):
            if i==0:
                print("Ingrese el nombre ")
                pac[f,i]=input()
            elif i==1:
                print("Ingrese el rut ")
                pac[f,i]=isRut()
            elif i==2:
                print("Ingrese la edad ")
                pac[f,i]= int(input())
            elif i==3:
                print("Ingrese la fecha de nacimiento ")
                pac[f,i]=input()
            elif i==4:
                print("Ingrese el estado civil ")
                pac[f,i]=input()
        f+=1
        print("Ciudadano ingresado con éxito")

    elif opt==2:
        print("Ingrese el rut del paciente a buscar")
        x=input()
        for i in range(0,50):
            if x==pac[i,1]:
                print("Ciudadano encontrado, sus datos son los siguientes:")
                for j in range(0,6):
                    showPersona(i,j)
                if pac[i,2] >= 18:
                  print("Esta disponible para sacar Licencia de Conducir")
                
                else: 
                  print("No esta disponible para sacar Licencia de Conducir")
                break
            else:
              print("Ciudadano no encontrado")

    elif opt==3:
      x= input("Ingrese rut del ciudadano")
      for i in range(0,50):
        if x==pac[i,1]:
          print("El rut es correcto, estos son los datos del certificado: ")
          print("CERTIFICADO DE NACIMIENTO")
          print(pac[i,1])
          print(pac[i,0])
          print(pac[i,2])
          print(pac[i,4])
        else:
          print("Rut no registrado")
        break 
      
    elif opt==4:
      x= input("Ingrese rut del ciudadano")
      for i in range(0,50):
        if x==pac[i,1]:
          print("El rut es correcto, estos son los datos del certificado: ")
          print("CERTIFICADO DE ANTECEDENTES PENALES")
          print(pac[i,2])
          print(pac[i,0])
          print(pac[i,4])
        
        else:
          print("Rut no registrado") 
        break

    elif opt==5:
        break

    else:
        print("Error, ingrese opción válida")