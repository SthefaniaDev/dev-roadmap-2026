class ContaBancaria:
    def __init__(self, titular, saldo, chavepix):
        self.titular = titular
        self.saldo = saldo
        self.chavePix = chavepix
        self.historico_transacoes = []

    def deposito(self, value):
        if value <= 0:
            print("Operação inválida! Digite um valor válido")
        else:
            self.saldo += value
            self.historico_transacoes.append(f'DEPÓSITO | +{value}')

    
    def sacar(self, value):
        if value <= 0 or value > self.saldo:
            print("Operação inválida! Digite um valor válido")
        else:
            self.saldo -= value
            self.historico_transacoes.append(f'SAQUE | -{value}')

    def mostrar_historico(self):
        for action in self.historico_transacoes:
            print(action)   
        
    