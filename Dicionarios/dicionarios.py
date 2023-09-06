### Dicionários são conjuntos não ordenados de pares(chave:valor). 

pessoa = {"nome": "Fellipe", "idade": 25}
### Declarando um dicionario direto na variável.

cidades = dict(pais="Brasil", estado= "Goiás", cidade= "Nerópolis")
### Declarando um dicionário pelo construtor dict.

cidades ["bairro"] = "Centro"
### Adicionando uma nova chave no dicionário

print(cidades)

cidades["cidade"] = "Goiânia"
### Alterando o valor da chave no dicionário.
print(cidades)

print(pessoa["nome"])
### Acessando os valores do dicionario.

dados_aluno = {
    "João" : {"sala" : "4a", "serie": "9º"},
    "Maria" : {"sala" : "5a", "serie": "9º"},
    "Gabriel" : {"sala" : "3a", "serie": "8º"},
    "Mateus" : {"sala" : "3a", "serie": "8º"},

}
print(dados_aluno["Gabriel"]["serie"])
### Acessando os dados do dicionario aninhado.

for chave in dados_aluno:
    print(chave, dados_aluno[chave])
### Iterando o dicionario e exibindo oas valores das chaves.

for chave, valor in dados_aluno.items():
    print(chave, valor)
### Iterando o dicionario com o meétodo items e exibindo oas valores das chaves. Maneira mais recomendada.

copia = dados_aluno.copy()
### O método copy, copia o dicionário, assim como nas outras estruturas de dados.

dados_aluno.clear()
### O método clear limpa o dicionário.

dados_aluno = dict.fromkeys(["nome", "telefone"], "vazio")
### O método fromkeys cria chaves no dicionário, Elas poder ficar vazias ou definir um valor padrão para elas, como no exemplo acima.

print(dados_aluno)
print(dados_aluno.get("chave"))
print(dados_aluno.get("chave", {}))
print(dados_aluno.get("nome", {}))
### O método get é utilizado para "pegar" o valor de uma chave caso ela exista. Caso ele não encontre a chave ele retorna none ou um valor default especificado por você.

print(copia.items())
### O método items, retorna uma lista de tuplas, o que é muito util para iterar em um laço for.

print(copia.keys())
### O metodo keys retorna as chaves do dicionário.

print(copia.pop("Carlos", {}))
### O método pop, remove e retorna a chave que foi especificada, caso essa chave não seja encontrada ele retorna um valor padrão que também é especificado por você.

print(dados_aluno.popitem())
### O método popitem, remove elementos na sequencia e retorna o valor removido, caso o dicionario esteja vazio ele retornará um keyerror

print(pessoa.setdefault("contato", "40028922"))
print(pessoa.setdefault("nome", "André"))
### O método setdefault é utilizado para criar chaves e atribuir valores a essas chaves. Casso a chave especificada ja exista, o método não altera essa chave.

contato = {"josemaria@gmail.com" : {"nome" : "MariaJose", "telefone" : "55554444"}}

print(contato)
contato.update({"josemaria@gmail.com" : {"nome" : "JoseMaria", "celular" : "988887777"}})
print(contato)
### Atualizando as informações para um chave existente com o método update.

contato.update({"jeremiasarruda@gmail.com" : {"nome" : "Jeremias", "celular" : "963524118"}})
print(contato)
### Atualizando o dicionário com uma chave nova, Nesse caso o método upadate vai adicionar essa chave ao dicionario.

print(contato.values())
### O método values, retornará todos os valores atrelados as chaves do dicionário.

resultado = "josemaria@gmail.com" in contato
print(resultado)
resultado = "fellipe@gmail.com" in contato
print(resultado)
### Verificando sé há a chave especificado no dicionário.

resultado = "idade" in contato["jeremiasarruda@gmail.com"]
print(resultado)
resultado = "celular" in contato["jeremiasarruda@gmail.com"]
print(resultado)
### Verificndo se há a chave especificado no dicionário interno.

del contato["jeremiasarruda@gmail.com"]["celular"]
print(contato)
del contato["jeremiasarruda@gmail.com"]
print(contato)
### Deletando uma uma chave no dicionário interno como o método del, depois deletando uma chave do dicionário.
