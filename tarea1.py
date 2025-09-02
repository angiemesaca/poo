# Angie Mesa

# encontrar los numeros primos entre 0  y 50 

for numero in range (2,51):
    primo = True
    for division in range (2, numero):
        if numero % division == 0 :
            primo = False
            break
    if primo == True:
        print (numero)