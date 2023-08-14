# conta = Conta(133,'pedro',1000.0,2000.0)

class Conta:

    def __init__(self,numero,titular,saldo,limite): 
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def setLimite(self,limite):
        self.__limite=limite

    def getLimite(self):
        return self.__limite

    def extrato(self):
        print("Seu saldo é {}".format(self.__saldo))

    def deposita(self,saldo):
        self.__saldo += saldo

    def saca(self, valor):
        if(valor<=self.__saldo):
            self.__saldo-=valor 
            return True

        else:
            return False
        
    def transfere(self, valor, destino):
        if(self.saca(valor) == True):
            destino.deposita(valor)
            return True
        else:
            return False
        
        