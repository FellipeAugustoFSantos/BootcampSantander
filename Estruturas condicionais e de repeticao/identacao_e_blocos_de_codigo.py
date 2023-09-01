### Em Python a identação, além de manter o código mais legível e manutenível ela também é essencial para delimitar blocos de código.
def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Sacou!")
    else:
        print("Saldo insuficiente!")


sacar(200)
### Funcionando perfeitamente.

def sacar(valor):
saldo = 500

if saldo >= valor:
print("Sacou!")
else:
 print("Saldo insuficiente!")
### Exemplo de erro di identação.