my_string="Código facilito"
course="Curso"
result= course +" de "+ my_string
result2="{a} de {b}".format(b=course, a=my_string)
result3=course+" de "+my_string+" otra versión."
result4= result+" versión 2"
print (result)

#<--------------------------Estos son métodos de formato----------------------->

#el método lower sirve para estandarizar todo el string.
#sirve para poner todo el texto en minúsculas.
result2=result2.lower()

print (result2)

#El método upper sirve para estandarizar todo el string.
#Sirve para poner todo el texto en mayúsculas.
result3= result3.upper()

print (result3)

#El método title sirve para estandarizar todo el string.
#Sirve para poner todo el texto como título.

result4=result4.title()

print(result4)

#<--------------------------Estos son métodos de búsqueda--------------------->
# El método de búsqueda find en cuentra la palabra dentro de un string.
# Esta regresa el número de la posición de la primera letra de la palabra
#que estas buscando dentro del string 
#recordando que en python las posiciones se empiezan desde 0.
pos=result.find("facilito")
print(pos)

#El método de búsqueda count cuenta las veces que se repite algo
#este te arroja el número de veces que se repite una palabra o letra dentro del
#string que especifiques
 
count=result.count("c")
print(count)
