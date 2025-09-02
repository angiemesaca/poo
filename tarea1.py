# Angie Mesa

# encontrar los numeros primos entre 0  y 50 

for numero in range (2,51):
    primo = true
    for division in range (2, numero):
        if numero % division == 0 :
            primo = false