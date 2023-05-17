numero = input('\nEscriba el número entero de 3 cifras que desea probar: ')
error = 'No ha introducido un número de 3 cifras'
if len(numero) != 3:
    print(f'\n{error}')
    exit()
try:
    int(numero)
    numero_a = int(numero[0])
    numero_b = int(numero[1])
    numero_c = int(numero[2])
    equis = int(f"{numero_a}{numero_b}{numero_c}")
    print(equis)
    aaa = numero_a ** 3
    bbb = numero_b ** 3
    ccc = numero_c ** 3
    equisequis = aaa + bbb + ccc
    print(equisequis)
    if equisequis == equis:
        print(f'{numero} es igual a la suma del cubo de sus tres cifras')
    else:
        print(f'La suma del cubo de las tres cifras de {equis} no es igual a {equis}, sino que es {equisequis}')
except ValueError:
    print(f'{error}')