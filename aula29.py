#try/except

numero = input("Digite um numero para a claculadora dobrar:")#str


try:
    print("Str:", numero)
    numero_float = float(numero)
    print(f'O dobro de {numero} é {numero_float * 2:}')

except:
    print("Isso não é um numero")



