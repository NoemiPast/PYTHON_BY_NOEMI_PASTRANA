#REALIZADO POR K. NOEMI PASTRANA G., ESTUDIANTE DE ING. EN SOFTWARE Y SISTEMAS COMPUTACIONALES
#Correo: lic.noemipastrana@gmail.com

#def es para definir una función, la cual puede ser usada después
def validar_credenciales(usuario, contraseña):
    
    # Verifica que el usuario tenga al menos 5 caracteres
    condicion_usuario = len(usuario) >= 5
    
    # Verifica que la contraseña tenga al menos 8 caracteres y contenga al menos un número
    #"for" e "in" es un bucle que recorre la cadena "contraseña", caracter por caracter
    #"any" es una función que toma un iterable (es lo que está entre paréntesis) y devuelve "true" 
    #si hay al menos un número en la contraseña devuelve "true". Y si no hay ningún número devuelve "false"
    condicion_contraseña = len(contraseña) >= 8 and any(caracter.isdigit() for caracter in contraseña)
    #isdigit es un método incorporado en Python que se usa en cadenas de texto PARA VERIFICAR SI EL 
    #CARACTER QUE SE INVOCA ES UN DÍGITO NUMÉRICO

    # Si ambas condiciones son verdaderas, las credenciales son válidas

    if condicion_usuario and condicion_contraseña:
        return True
    else:
        return False

# Ejemplo de uso
usuario = "usuario123"
contraseña = "clave1234"

print ("Ingrese el usuario")
usuario = (input("usuario:"))

print ("Ingrese su contraseña")
contraseña = (input("contraseña:"))

if validar_credenciales(usuario, contraseña):
    print("Credenciales válidas. Inicio de sesión exitoso.")
else:
    print("Credenciales inválidas. Por favor, verifica tu usuario y contraseña.")

#Mi primer trabajo, gracias a Dios 
