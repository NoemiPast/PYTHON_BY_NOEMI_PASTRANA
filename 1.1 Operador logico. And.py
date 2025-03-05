#REALIZADO POR K. NOEMI PASTRANA G., ESTUDIANTE DE ING. EN SOFTWARE Y SISTEMAS COMPUTACIONALES
#Correo: lic.noemipastrana@gmail.com
#Realizado el 05 de Marzo del 2025

#OperadorAnd
#PLANCITO DEL DIA

#Preguntar si esta nublado o soleado
print("¿Esta nublado o soleado? (responde soleado o nublado)")
#Hacer una variable para su respuesta
#.Lower sirve para que no haya diferencia entre mayusculas y minusculas
sol = input().lower() == "soleado"
#Preguntar si es fin de semana
print("¿Es fin de semana? (responde si o no)")
fin_de_semana = input (). lower () #.lower sirve para convertir la respuesta a minuscula

#Aplicamos el operador logico and, ya que se deben cumplir dos condiciones
if sol and fin_de_semana:
    print("Dia de playita")
else:
    print("Dia de trabajo")
