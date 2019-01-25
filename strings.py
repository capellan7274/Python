my_string="Hola Mundo."

#otra forma de colocar saltos de líneas es colocar (\n) dentro del texto.

my_string="""Este es un string que contiene 
saltos de línea, como puedes ver.
adios."""
course="Python 3"
name="capellan"
final_message="Nuevo curso de "+ course +" por " + name
print (final_message)
print (my_string)

#existen diferentes formas de unir strings
#la primera seria aplicando el ejemplo anterior "Nuevo curso de "+ course +" por " + name 
#la segunda forma "Nuevo curso de %s por %s" %(course, name)
#la tercera forma "Nuevo curso de {} por {}".format(course,name )

my_string="Juan Gabriel"
my_string2="Bernardo Mora"
final_message= my_string+ " y "+ my_string2 +" Real Hasta la muerte."
print(final_message)