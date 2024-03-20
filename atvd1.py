nome = input('Digite seu nome: ')
idade = input ("Digite sua idade:")

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome [::-1]}')
if ' ' in nome:
    print('Seu noe contem espaços')
else:
    print("Seu nome não contém espaços")
    
print(f'Seu nome tem {len(nome)} letras')
print(f'A primeira letra do seu é {nome[0]}')
print(f'A ultima letra do seu é {nome[-1]}') 


if nome and idade:

    ...

else:
    print("Desculpe, você deixou campo vazio.")

