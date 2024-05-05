#creando una lista (se puede modificar)
lista = ["Juan Toro","Shane","true","1.84"]

#creando una dupla (no se puede modificar)
tupla = ("Juan Toro","Shane","true","1.84")

#esto es valido


#esto no es valido
#tupla[3] = "maquinon"




#creando un conjunto (set) (no se accede a elementos por indice,no almacena datos duplicados) 

conjunto = {"Juan Toro","Shane","true","1.80"}
#print(conjunto[3]) -> no puede acceder al elemento


#creando un diccionaario (dict)  (la estructura es key : value y separamos con comas)
diccionario = {
    'nombre': "Juan Toro",
    'canal': "Shane",
    'esta_emocionado': True,
    'altura': "{:.2f}".format(1.80),  # Formateamos la altura con dos decimales
    'dato_duplicado': "Shane"
}
print(diccionario["altura"])


