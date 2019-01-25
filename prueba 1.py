pregunta=input("trabajas desde casa")

if pregunta=="si":
    print "Eres afortunado"
if pregunta=="no":
    print"Trabajas fuera de casa"
tiempo=input("Cuantos minutos haces al trabajo")
if tiempo==0:
    print"trabajas desde casa"
elif tiempo<=20:
    print"Es poco tiempo"
elif tiempo>=21 and tiempo<=45:
        print "Es un tiempo razonable"
else:
            print "busca otras rutas "
            
