### Operadores de identidade são utilizados para comparar se os objetos testados se encontram na mesma posilçao na memória.
valor = 10
valor_2 = valor
nome, nome_2 = "Python", "Python"

print(valor is valor_2)
### Testando se as duas variáveis estão ocupando a mesma região de memória. Como A variável valor_2 recebeu a volor, o resultado será "True"

print(valor is not valor_2)
### Testando se as duas variáveis não estão ocupando a mesma região de memória.

print(nome is nome_2)
### Como a string armazenada nas variáveis é igual, o resultado também será "True".