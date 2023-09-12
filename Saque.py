import Extrato


def Saque():
    saque = input("Quanto gostaria de sacar?\n")
    extrato = Extrato.extrato
    if float(saque) > float(extrato):
        print('Saque indisponível. Valor de saque {} supera valor disponível na conta {}'.format(saque, extrato))
        return False
    else:
        Extrato.extrato = float(extrato) - float(saque)
        print('Saque efetuado. Saldo disponível de R$ {}'.format(Extrato.extrato))
        return True
