### Operadores lógicos sao usados em conjunto com operadores comparativos, para montarmos uma expressão lógica. O resultado sempre será um valor booleano.
valor = 10
print(valor > 5 and valor < 20)
print(valor > 5 and valor < 8)
### Quando usamos o operador "E" as duas condições tem q ser verdadeiras para que o resultado seja "True".

valor = 50
print(valor > 15 or valor < 20)
print(valor > 100 or valor < 8)
### Quando usamos o operador "OU" apenas uma das condições tem q ser verdadeiras para que o resultado seja "True", caso as duas sejam falsas o resultado a expressão será "False."

print(not(valor > 15 or valor < 20))
### O operador "NÃO" inverte o resultado da expressão lógica.
### O parêntesis também determina a precedencia das operações em expressões lógicas.
