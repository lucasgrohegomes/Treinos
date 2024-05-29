with open(r'C:\Users\Lucas\Desktop\arquivo.txt', 'r') as file:
    conteudo = file.read()
    print(conteudo)

with open(r'C:\Users\Lucas\Desktop\arquivo.txt', 'a') as file3:
    file3.write('Buenas Noches Noches.')

numeros = [x for x in range(10)]
print(numeros)