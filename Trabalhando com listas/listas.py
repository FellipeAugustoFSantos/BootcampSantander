frutas = ["maça", "laranja", "mamao", "uva", "goiaba"]

###exempro de declaração de lista com colchete 

nomes = []
### Declaração de lista vazia

letras = list("python")
### Declarando lista com o costrutor "list" que vai atribuir cada letra da string como um elememto da lista.

numeros = list(range(100))
### Declarando lista com o construtor e utilizando a função "range" para preencher a lista.

carro = ["Ferrari", "F8", 420000, 2020, 2900, "São Paulo", True]
### Adicionando vários tipos de elementos na lista.

print(frutas[-1])
### Acessando o ultimo elemento da lista usando índice negativo.

matriz = [
    ["a", 1, 2],
    [3, "b", 4],
    [5, 6, "c"]
    ]

print(matriz[0])
### imprimindo uma linha da matriz

print(matriz[0][-1])
print(matriz[0][1])
print(matriz[-1][2])
### Acessando elementos específicos da matriz

### Também é possível urilizar fatiamento em listas.

print(letras[2:])
print(letras[:2])
print(letras[1:3])
print(letras[0:3:2])
print(letras[::])
print(letras[::-1])

### Iterando listas, utilizando o laço "for"

for fruta in frutas:
    print (fruta)

for i, fruta in enumerate(frutas): ### Enumerando o indice e exibindo elemnto desse indice
    print(f"{i}: {fruta}")


pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    print(pares)

### Adicionando os numeros pares na lista pares

impares = [numero for numero in numeros if numero % 2 != 0] ### Usando compreensão de lista para adicionar numeros ímpares na lista.
### O primeiro "numero" é o retorno. o "for" é o laço iteravel. e o "if" é a condiçao para retornar o valor pra lista.

print(impares)
quadrados = []

for numero in numeros:
    quadrados.append(numero ** 2)

### Elevando numeros ao quadrado.
### Exemplo com compreenssão
#quadrados = [numeros ** 2 for numero in numeros]

lista = []
lista.append(10)
lista.append([20, 30, 40, 50])
print(lista)
### o método append adiciona um elemento na lista, pode ser tanto string, float, int, boll ou até mesmo uma outra lista.

lista.clear()
print(lista)
### O método clear limpa a lista.

l2 = lista.copy()
l2.append(5)
print(lista)
print(l2)
### O comando copy duplica uma lista para outra variável/enderesso de memória, tornando possível alterar elementos em uma delas, sem modificar a outra.

lista = [10, 20, 40, 10, 80, 60, 40, 10]
print(lista.count(10))
### O método count é utilizado para contar quantas vezes um elemento aparece na lista.

lista.extend([90, 50, 70, 120, 880])
### O método extend é usado para juntar duas listas, caso haja elementos iguas nas duas listas eles serçao duplicados.

print(lista.index(80))
### O método index exibe em qual index ocorre a primeira ocorrencia do elemento buscado.

lista.pop()
lista.pop(0)
print(lista)
### O método pop remove o ultimo elemento da lista, também aceita o indice como parametro para remoção.

lista.remove(10)
print(lista)
### O método remove deleta um elemento específico na lista que é passado como parametro. Remove apenas uma ocorrência do elementp especificado.

lista.reverse()
print(lista)
### O método reverse faz um espelhamento da lista.

lista.sort()
print(lista)
### O método sort organiza a lista em ordem alfábetica.

lista.sort(reverse=True)
print(lista)
### Ordenando e espelhando a lista.

frutas.sort(key=lambda x: len(x))
print(frutas)
### Organizando a lista pela quantidade de letras da string, em ordem crescente.

frutas.sort(key=lambda x: len(x), reverse=True)
print(frutas)
### Organizando a lista pela quantidade de letras da string, em ordem decrescente.
### També há uma função built in chamada sorted que tem a mesma função q sort.