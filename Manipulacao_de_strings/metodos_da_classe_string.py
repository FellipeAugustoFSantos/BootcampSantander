nome = "FelLIpE AUgUStO"

print(nome.upper())
### O método "upper" deixa todas as letras da string maiúsculas.

print(nome.lower())
### O método "lower" deixa todas as letras da string minúsculas.

print(nome.title())
### O método "title" deixa a primeir letra de cada palavra da string maiúscula.

texto = "     Olá mundo!   "

print("." + texto + ".")
### Texto normal.

print("." + texto.strip() + ".")
### O método "strip"  remove todos os espaços vazios antes do primeiro caractere e depois do último.

print("." + texto.lstrip() + ".")
### O método "lstrip" remove todos os espaços a esquerda da string.

print("."+ texto.rstrip() + ".")
### O método "lstrip" remove todos os espaços a direita da string.

menu = "Python"

print("####" + menu + "####")
### Centralizando manualmente.

print(menu.center(14))
### Centralizando com o método "center" e definindo a quantidade de caracteres para centralizar a string.

print(menu.center(14, "#"))
### Centralizando com o método "center" e definindo um caractere para substituir os espaços em branco.

print("P-y-t-h-o-n")
### Colocando os traços manualmente entre as letras.

print("-".join(menu))
### Colocando traços automaticamente entre as letras utilizando o método join.
