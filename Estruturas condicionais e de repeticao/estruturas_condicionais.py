### Estruturas condicionais são blocos de código que alteram o flúxo de controle quando a condição esécificada é atendida.
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Saque realizado!")

if saldo < saque:
    print("Saldo insuficiente!")
### Estrutura condicional "SE" verifica se a condição informada é verdadeira, caso seja o bloco de comandos dentro dela é realizado.

saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Saque realizado!")

else:
    print("Saldo insuficiente!")
### Utilizndo o "SE NÃO" o código fica mais simplificado e sempre que a condição do IF não for atendida o bloco de comandos dentro do ELSE será executado. 

saque = float(input("Informe o valor do saque: "))

if saque % 2 != 1 and saque % 2 != 0:
    print("Valor inválido!")

elif saldo >= saque:
    print("Saque realizado!")

else:
    print("Saldo insuficiente!")

### O comando ELIF é utilizado para substituir o segundo IF caso seja nescessário testar outrs condições. Não há limite de utilização para os ELIFs, porém não é uma boa prática ter grandes estruturas condicionais.

tipo_conta = int(input(" Qual o tipo de conta?\nConta corrente: [1]\nConta poupança [2]\n"))

if tipo_conta == 1:
    limite = 1200
    saque = float(input("Informe o valor do saque: "))
    if saque % 2 != 1 and saque % 2 != 0:
        print("Valor inválido!")

    elif saldo >= saque:
        print("Saque realizado!")

    elif saldo < saque and (saldo + limite) >= saque:
        print("Saque realizado utilizando o limite!")

    else:
        print("Saldo insuficiente!")

elif tipo_conta == 2:
    saque = float(input("Informe o valor do saque: "))
    if saque % 2 != 1 and saque % 2 != 0:
        print("Valor inválido!")

    elif saldo >= saque:
        print("Saque realizado!")

    else:
        print("Saldo insuficiente!")
else:
    print("Tipo de conta inválido!")
### Exemplo de estruturas condicionais aninhadas(IF dentro de IF).

saldo = 500
saque = float(input("Informe o valor do saque: "))


status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar os saque!")
### Exemplo de estrutura IF tenário. Esse tipo de expressão pode ser definida em uma unica linha.