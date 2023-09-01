nome = "Fellipe Augusto Fernandes Santos"

print(nome[0])
### Acessando o indice 0, a primeira letra da string, passando o parâmetro -1 a posissão da string acessada será a ultima.

print(nome[:7])
### Quando o parâmetro de start está vazio e parametro de fim esta preenchido, sera retornado do indíce 0 até o indíce especificado.

print(nome[8:])
### Quando não temos o parametro de fim, o retorno será do indíce inicial até o fim da string.

print(nome[8:15])
### Acessando a string do indíce inicial especificado até o indíce final especificado.

print(nome[8:15:2])
### Acessando a string do indíce inicial especificado até o indíce final especificado definindo o passo, nocaso 2 indíces.

print(nome[:])
### Indíce inicial e final vazio, retorna uma cópia da string.

print(nome[::-1])
### Definindo o passo negativo é retornado a string espelhada.