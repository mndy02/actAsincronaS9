#Inicio del programa
print("¡BIENVENIDO AL PROGRMA!\n")

#Solicitar los datos al usuario
print("\nINGRESE LOS DATOS QUE SE LE SOLICITAN PARA SABER A QUE ETAPA PERTENECE")
nombre = str(input("\nIngresa tu nombre: "))
apellido = str(input("\nIngresa tu apellido: "))
edad = int(input("\nIngresa tu edad:  "))
sexo = str(input("\nIngresa tu sexo (F/M): ")).upper()

#si el sexo es 'F'
if sexo == "F" or sexo == "Femenino":
    if edad >=0 and edad <= 18:
        print(f"\n{nombre} {apellido}, usted es una niña")
       
    if edad >=0 and edad <=2:
         print("\nPertenece a la etapa de 'Bebé'")
    
    elif edad >=3 and edad <=5:
        print("\nPertenece a la etapa de 'Infancia'")
    
    elif edad >=6 and edad <=11:
        print("\nPertenece a la etapa de 'Niñez'")
        
    elif edad >=12 and edad <=18:
        print("\nPertenece a la etapa de 'Adolescencia'")
    
    elif edad >=19 and edad <=26:
        print(f"\n{nombre} {apellido}, usted es una señorita")
        
        if edad >=19 and edad <=26:
            print("\nPertenece a la etapa de 'Juventud'")
            
    elif edad >=27 and edad <=40:
        print(f"\n{nombre} {apellido}, usted es una señora")
       
        if edad >=27 and edad <=40:
            print("\nPertenece a la etapa de 'Adultez joven'" )
            
        elif edad >=41 and edad <=55:
          print("\nPertenece a la etapa de 'Adultez'")
          
    elif edad >=56 and edad <=65:
        print(f"\n{nombre} {apellido}, usted es una abuela")
        
        if edad >=56 and edad <=65:
            print("\nPertenece a la etapa de 'Persona mayor'")
            
        elif edad >=66 and edad <=100:
            print("\nPertenece a la etapa de 'Tercera edad'")
    else:
        print(f"\n{nombre} {apellido}, la edad que ingresó no existe")
        
#si el sexo es 'M'
elif sexo == "M" or sexo == "Masculino":
    if edad >=0 and edad <=18:
        print(f"\n{nombre} {apellido}, usted es un niño")
        
    if edad >=0 and edad <=2:
        print("\nPertenece a la etapa de 'Bebé'")
        
    elif edad >=3 and edad <=5:
        print("\nPertenece a la etapa de 'Infancia'")
        
    elif edad >=6 and edad <=11:
        print("\nPertenece a la etapa de 'Niñez'")
        
    elif edad >=12 and edad <=18:
        print("\nPertenece a la etapa de 'Adolescencia'")
        
    elif edad >=19 and edad <=26:
        print(f"\n{nombre} {apellido}, usted es un caballero")
        
        if edad >=19 and edad <=26:
            print("\nPertenece a la etapa de 'Juventud'")
            
    elif edad >=27 and edad <=40:
        print(f"\n{nombre} {apellido}, usted es un señor")
        
        if edad >=27 and edad <=40:
            print("\nPertenece a la etapa de 'Adultez joven'")
            
        elif edad >=41 and edad <=55:
            print("\nPertenece a la etapa de 'Adultez'")
            
    elif edad >=56 and edad <=65:
        print(f"\n{nombre} {apellido}, usted es un abuelo")
        
        if edad >=56 and edad <=65:
            print("\nPertenece a la etapa de 'Persona mayor'")
            
        elif edad >=66 and edad <=100:
            print("\nPertenece a la etapa de 'Tercera edad'")
    else:
        print(f"\n{nombre} {apellido}, la edad que ingresó no existe")
        
else:
    print("\nEl género que fue ingresado, no existe")

#Verificar si la edad es par o impar
if edad % 2 == 0:
    print("\nLa edad ingresada es 'par'")
else:
    print("\nLa edad ingresada es 'impar'")

#Indicar el fin del programa 
print("\nFIN DEL PROGRAMA")
