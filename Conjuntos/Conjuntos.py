### Conjutos são estruturas de dados que não possuem elementos repetidos.

numeros = [1, 2, 3, 5, 4, 6, 2, 1, 9, 8, 7, 2, 5, 6, 3, 4]
palavra = ["Paralelepipedo", "triângulo", "circulo", "triângulo" ]

print(set(numeros))
print(set(palavra))
### Transformando listas em conjuntos.

print(set("abacaxi"))
### Transformando o parâmetro em um conjuto.

### Para acessar os valores de um cojuno, é necessário realizar uma conversão para lista.

pares = {0, 2, 4, 6, 8}

pares = list(pares)
### Converssão para lista.

print(pares[0])

pares = set(pares)
numeros = set(numeros)

for numero in numeros:
    print(numero)
### Utilizando laço for para percorrer o conjunto e exibir seus elementos.

for indice, numero in enumerate(numeros):
    print(f"{indice}: {numero}")
### Exibindo índice e valor com a função enumerate.

impares = {1, 3, 5, 7, 9}

print(pares.union(impares))
### Usando o método union para realizar a união dos dois conjuntos, "pares" e "impares".

print(numeros.intersection(pares))
print(numeros.intersection(impares))
### Usando o método intersection para exibir os numeros presentes tanto em "numeros" quanto em "pares" e em "impares".

print(numeros.difference(pares))
print(numeros.difference(impares))
### O método difference vai retornar a diferença entre os conjuntos.(Qual elemento está presente no conjunto "numeros" e não está presente no conjunto "pares" ou "impares").

print(numeros.symmetric_difference(pares))
print(numeros.symmetric_difference(impares))
### O método symmetric_difference retorna todos os valores que não estão na intersecção.

conjunto_1 = {1, 2, 3, 4, 5, 6}
conjunto_2 = {7, 8, 9}
conjunto_3 = {10, 8}

print(conjunto_1.issubset(conjunto_2))
print(conjunto_2.issubset(conjunto_1))
### O método issubset verifica se todos os elementos de um determinado conjunto estão presentes em outro e retorna um valor bool(True ou False).

print(conjunto_1.issuperset(conjunto_2))
print(conjunto_2.issuperset(conjunto_1))
### O método issuperset verifica se o conjunto especificado tem todos os elementos do conjunto passado como parâmetro e retorna um valor bool(True ou False).

print(conjunto_1.isdisjoint(conjunto_2))
print(conjunto_2.isdisjoint(conjunto_3))
### O método isdisjoint verifica se os elementos do conjunto não estão presentes no conjunto passado como parâmetro e retorna um valor bool(True ou False).

sorteio = {5, 37}

print(sorteio)
sorteio.add(52)
print(sorteio)
sorteio.add(5)
print(sorteio)
sorteio.add(20)
print(sorteio)
### O método add adiciona um elemento no conjunto, caso ele não exista no conjunto.

sorteio_anterior = sorteio.copy()
### O método copy cria uma cópia do conjunto.

sorteio.clear()
print(sorteio)
### O método clear limpa o conjunto.

print(sorteio_anterior)
print(sorteio)

sorteio_anterior.discard(5)
sorteio_anterior.discard(60)
print(sorteio_anterior)
### O método discard, descarta um valor do conjunto. Vale lembrar que se o valor passado não exitir no conjunto, não ocorrerá erro.

numeros.pop()
numeros.pop()
print(numeros)
### O método pop, remove o primeiro item da fila.

numeros.remove(9)
print(numeros)
numeros.remove(46)
### O método remove, remove um valor especificado da mesma maneira que o discard, porém, caso o valor especificado não exista ele retornará um erro.

print(len(numeros))
### O método len, retorna o tamanho do conjunto.

print(9 in numeros)
print(46 in numeros)
### O operador in, serva para verificar se um determinado elemn=ento está presente no conjunto.

