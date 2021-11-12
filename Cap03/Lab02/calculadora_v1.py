# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3.
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************\n")

print('Selecione o número da operação desejada:\n')

print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão\n')

opcao = input('Digite a operação desejada (1/2/3/4): ')

x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))

if opcao == '1':
    print(f'{x} + {y} = {x + y}')
elif opcao == '2':
    print(f'{x} - {y} = {x - y}')
elif opcao == '3':
    print(f'{x} * {y} = {x * y}')
elif opcao == '4':
    print(f'{x} / {y} = {x / y}')
else:
    print('Opção inválida')
