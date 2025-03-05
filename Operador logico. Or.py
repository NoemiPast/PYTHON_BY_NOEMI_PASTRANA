#Operador logico Or
#ENTREVISTA DE TRABAJO

#Preguntar su nombre
print("Buenos dias Ing. ¿Cual es su nombre?")
nombre = input () #Asignar una variable a su nombre, para poder usar despues
print("Mucho gusto", nombre)

print("Para el puesto al que quiere ascender le vamos a realizar algunas preguntas")
ok = input()

#Preguntar su edad
print("¿Que edad tiene?")
edad = int(input()) #Se convierte a entero para poder comparar

print("Cuantos años lleva laborando con nosotros (reponda con un numero)")
años_trabajando = int(input())

print("Cual es su nivel de ingles? (responda con A1, A2, B1, B2, C1, C2)")
ingles = input().upper() #Se convierte a mayusculas para poder comparar

#Aplicar los operadores logicos or & and para ver cuantas condiciones se cumplen y ver si 
#es candidato al puesto de trabajo
if (edad >= 18 or edad < 40) and (años_trabajando >= 7) and (ingles == "B1" or ingles == "B2" or ingles == "C1" or ingles == "C2"):
    print("Ing.", nombre, "es candidato al puesto de trabajo")
else:
    print ("Le vamos a mandar un correo con la respuesta a su solicitud, Ing. ", nombre, "muchas gracias")