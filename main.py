import Deposito
import Extrato
import Menu
import Saque

saldo = input("Qual seu saldo inicial?\n")
Extrato.extrato = saldo

op = None

while op != 5:
    op = Menu.Menu()
    if op == '2':
        Saque.Saque()
    elif op == '3':
        Deposito.Deposito()
    elif op == '4':
        print('Saldo disponível R$ {} '.format(Extrato.extrato))
    else:
        break
