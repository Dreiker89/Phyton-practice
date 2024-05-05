cadena1 = "hola,soy,el,goleador"

cadena2 = "Bienvenido Maquinon"

#(Upper) convierte a mayuscula 
mayus = cadena1.upper()

#(lower) convierte a minuscula
minusc = cadena1.lower()

#(Cspitalize) primera letra en mayuscula 
primer_letra_mayusc = cadena1.capitalize()

#(find) busca una cadena en otra cadena, sino hay coincidencia devuelve -1
busquedad_find = cadena1.find("a")

#(inndex) busca una cadena en otra cadena, sino hay una coincidencia tira una excepcion
busquedad_index = cadena1.index("a")

#(isnumeric) si es numerico devuelve true, sino devuelve false
es_numerico = cadena1.isnumeric()

#(isalpha) es alfanumerico devolvemos true, sino devolvemos false 
es_alfa_numerico = cadena1.isalpha()

#(count) contamos las coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias 
contar_coincidencias = cadena1.count("a")

#(len) contamos cuantos caracteres tiene una cadena 
contar_caracteres = len(cadena1)

#vericamos si una cadena termina con una cadena dada, si es asi devuelve tue
empieza_con = cadena1.startswith("H")

termina_con = cadena1.endswith("r")

#si el valor 1, se encuentra en la cadena original, reeplaza el valor 1 de la misma, por el valor 2  
cadena_nueva = cadena1.replace(","," ")

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")

print(cadena_separada[3])