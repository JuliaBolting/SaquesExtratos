import Extrato


def Deposito():
    dep = input("Quanto quer depositar?\n")
    Extrato.extrato = Extrato.extrato + float(dep)
    print("Depósito efetuado. Saldo disponível {}".format(Extrato.extrato))
