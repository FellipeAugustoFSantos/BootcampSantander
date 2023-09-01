### Estruturas de reptição são utilizadas para repetir um bloco de codigos um determinado tipo de vezes, que podem ser determinadas previamente ou por uma expressão lógica.

texto = input("Digite uma frase: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
### Exemplo utilizando um iterável

numero = 3
print(numero)
for i in range (11):
    print(numero * i)
else:
    print("Fim")
### Tabuada do número 3 utilizando a função range.
### Estrutura de repetição FOR, usado em uma estrutura iteravel, quando sabemos quantas vezes o código deve ser repetido. O else no fim da estrutura é opcional.
### A função range é usada para incremento de contador e recebe 3 parâmetros: inicio, fim(exclusivo), passo(usado quando necessário).

numero = int(input("Qual o número desejado? "))
vezes = int(input("Quantas vezes deseja multiplicar o número inserido? "))
i = 0
while i < vezes:
    print(numero * (i + 1), end=" ")
    i += 1

### Exemplo de tabuada interativa.
### Estrutura de repetição WHILE é usada quando o bloco de comando precisa ser executado inumeras vezes.
### A parala reservada "break" é usada para interromper um laço, seja ele WHILE ou FOR.
### A palavra reservada "continue" é usada para saltar uma determinada execução.
 
