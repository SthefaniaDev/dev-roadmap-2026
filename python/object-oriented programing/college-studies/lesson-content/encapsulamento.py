class contaBancaria:
    def __init__(self, numero, titular, saldo):

        # atributos privados
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo

    # GETTERS
    def get_numero(self):
        return self.__numero
    
    def get_titular(self):
        return self.__titular
    
    def get_saldo(self):
        return self.__saldo

    # SETTERS
    def set_numero(self, numero):
        self.__numero = numero
    
    def set_titular(self, titular):
        self.__titular = titular
    
    def set_saldo(self, saldo):
        self.__saldo = saldo


conta = contaBancaria('1', 'kaio', 10000)

conta.set_numero('2')

print(conta.get_numero())