class Main:
    pass
from Cliente import Cliente
from Conta import Conta

c1= Cliente("João", "11444-2222")
conta=Conta(c1.get_nome(), 1222,0)

conta.deposita(100)
conta.saque(50)
conta.extrato()