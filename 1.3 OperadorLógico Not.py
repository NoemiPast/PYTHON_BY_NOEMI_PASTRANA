"""
REALIZADO POR K. NOEMI PASTRANA G., ESTUDIANTE DE ING. EN SOFTWARE Y SISTEMAS COMPUTACIONALES
Correo: lic.noemipastrana@gmail.com
Realizado el 09 de Marzo del 2025
"""

#OperadorNot


usuarios_permitidos = ["Noemí", "Noé", "Mimí"] #Se usan corchetes, son necesarios para las f-strings

#Usuario nuevo que tenemos que verificar
usuario_nuevo = "Naomi"

#Verificar que no esté en la lista de "usuarios_permitidos"
if usuario_nuevo not in usuarios_permitidos : #not in verifica que el usuario nuevo no esté en la lista
    print (f"El usuario {usuario_nuevo} no está en la lista. Añadiéndolo...")
    usuarios_permitidos.append(usuario_nuevo)
else:
    print(f"El usuario {usuario_nuevo} ya está en la lista") #Se usan llaves {} 

print("Lista actualizada:", usuarios_permitidos)