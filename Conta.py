class Conta:
    def __init__(self, titular, numero, saldo):
        self.titular=titular
        self.numero=numero
        self.saldo=0

        @property
        def saldo(self):
            return self._saldo

        @saldo.setter
        def saldo(self, saldo):
            if (saldo < 0):
                print("O saldo não pode ser negativo.")
            else:
                self._saldo = saldo

    def saque(self, valor):
        if (self.saldo>= valor):
            self.saldo-=valor
            print("Saque realizado com sucesso!!")
        else:
            print("Saldo insuficiente!")

    def deposita(self, valor):
        self.saldo+=valor

    def extrato(self):
        print("Cliente: ", self.titular, "Saldo atual: ", self.saldo)
