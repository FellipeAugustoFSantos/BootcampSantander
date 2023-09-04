frutas = ("laranja", "pera", "uva",)
### Tuplas são estrutura de dados imutáveis do início até o fim da execução os valores armazenados nela não podem ser alterados.
# É uma boa prática colocar virgula no fim dos elementos da tupla, para que o interpretador do python não confunda ela com precedência de operações(Comum em casos de tuplas com um único elemento).
 
letras = tuple("python")
### Declarando uma tupla com o construtor "tuple".

numeros = ([1, 2, 3, 4])
### Declarando uma tupla com uma lista no indíce 0. Os valores armazenados na lista também não podem ser alterados

pais = ("Brasil",)

### Para acessar os valores da tupla é utilizado os mesmos métodos que nas listas.

matriz = (
    ("a", 1, 2),
    (3, "b", 4),
    (5, 6, "c")
)
### Tuplas aninhadas.
# Os conceitos e metodos usados para  fatiamento são os mesmos das listas.

print(letras[2:])
print(letras[:2])
print(letras[1:3])
print(letras[0:3:2])
print(letras[::])
print(letras[::-1])

### Os métodos count, index e len são os únicos que existem nas tuplas já que elas são imutáveis.