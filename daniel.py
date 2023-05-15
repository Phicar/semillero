def c6(n):
    n=str(n)
#un numero es divisible por 25 si sus dos ultimos dijitos son 00,50,25,75
#tengo dos variables pivotes, pv0 que me avisa si he encontrado un numero 0
#pv5 que me avia si he encontrado un numero 5
    pv0 = False
    pv5 = False
#busco de derecha a izquierda
    for i in range(len(n)-1,-1,-1):
#si encuentro un 0 y ya habia encontrado un 0 debo eliminar a todos los numeros entre estos 2
#es decir len(n)-(i+1) - 1
        if n[i]=='0' and  pv0:
            return len(n)-(i+1) - 1
#si encuentro un primer 0 lo registro en pv0
        if n[i]=='0':
            pv0= True
#si habia encontrado un 0 y encuentro un 5, tengo un '50' y elimino a todos los que estan entre
#estos dos es decir len(n)-(i+1) - 1
        if n[i]=='5' and pv0:
            return len(n)-(i+1) - 1
#si encuentro un primer 5 lo registro en pv 5
        if n[i]=='5':
            pv5= True
# si encuentro un 2,7 luego de encontrar un 5 tengo un 25 o 75, por lo que eliminio a todos los
#que estan entre estos dos es decir len(n)-(i+1) - 1 
        if (n[i]=='2' or n[i]=='7') and pv5:
            return len(n)-(i+1) - 1 
    return 'sorry' # si no lo encuentro retorno 'sorry
print(c6('1257'))
print(c6('1253601151'))
print(c6('12532601151'))
