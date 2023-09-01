nome = "Fellipe"
idade = 25
profissao = "Desenvolvedor"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, quero me tornar %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

### Para colocar variáveis em uma string utilizando esse método é inserido na strins o símbolo "%" acompanhado de um caaractere, ao fim da string o parâmetro % é passado.
# "%s" é usado pra ser substituido por uma variável do tipo string, "%d" é usado par variável do tipo inteiro, "%f" para variáveis do tipo ponto flutuante.
### Esse é o metodo mais antigo de se colocar variáveis em uma string, é complexo e atualmente náo é recomendado.

print("Olá, me chamo {}. Eu tenho {} anos de idade, quero me tornar {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, quero me tornar {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, quero me tornar {profissao} e estou matriculado no curso de {linguagem}.".format(nome = nome, idade = idade, profissao = profissao, linguagem = linguagem))
### O método "format" tem duas maneiras de ser utilizado 
# Primeiro: passando como parâmetro as variáveis em ordem.
# Segundo: especificando a posição da variável no argumrnto dentro da chave, vale lembra que  alinguagem Python é baseada em indíce 0.
# Terceiro: nomeando as variáveis de igual o nome dos argumentos dentro das chaves.
### Esse método não é comum e não é o masi recomendado.


print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, quero me tornar {profissao} e estou matriculado no curso de {linguagem}.")
### "fstring" é o método mais novo e mais recomendado para interpolação de variáveis.

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")
### Formatando a variável PI para exibir apenas duas casas decímais.

print(f"Valor de PI: {PI:10.2f}")
### Formatando a variável PI para adicionar 10 espaços em branco a esquerda e exibir apenas duas casas decímais.