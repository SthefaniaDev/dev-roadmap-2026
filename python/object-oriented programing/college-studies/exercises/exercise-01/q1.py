class ContaBancaria:
    def __init__(self, titular, numeroconta, saldo, chavepix):
        self.titular = titular
        self.numeroconta = numeroconta
        self.saldo = saldo
        self.chavepix = chavepix
        self.historico_transacoes = []
        
    def depositar(self, valor):
        if valor <= 0:
            print('Operação inválida!')
        else:
            self.saldo += valor
            print(f'Depósito realizado no valor de {valor} na conta de {self.titular}')
            self.historico_transacoes.append(f'DEPOSITO ------------ + {valor}')

    def sacar(self, valor):
        if valor <= 0 or valor > self.saldo:
            print('Operação inválida!')

        else:
            self.saldo -= valor
            print(f'Saque realizado no valor de {valor} por {self.titular}')
            self.historico_transacoes.append(f'SAQUE ------------ - {valor}')
       


    def pix(self, valor, conta_destinatario):
        if valor <= 0 or valor > self.saldo:
            print(f'Valor insuficiente! \n Saldo disponível: R${self.saldo}')
        
        else:
            self.saldo -= valor
            conta_destinatario.saldo += valor
            print(f'PIX realizado com sucesso!\n Pix realizado no valor de {valor} para {conta_destinatario.titular}')
            self.historico_transacoes.append(f'PIX ENVIADO -{valor} -> {conta_destinatario.titular}')
            conta_destinatario.historico_transacoes.append(f'PIX RECEBIDO +{valor} <- {self.titular}')

    
    def mostrar_historico(self):

        print(f'Historico da conta: {self.titular}\n')
        for numero, acao in enumerate(self.historico_transacoes, start=1):
            print(f'{numero} - {acao}')

'''==========================TESTES=========================='''

conta_felipe = ContaBancaria("Felipe", 12345, 1000, "felipe@email.com")
conta_kaio = ContaBancaria("Kaio", 54321, 500, "kaio@email.com")
conta_lucas = ContaBancaria("Lucas", 98765, 800, "lucas@email.com")

'''==========================OPERAÇÕES=========================='''

conta_felipe.depositar(500)
conta_felipe.sacar(200)
conta_felipe.pix(150, conta_kaio)
conta_felipe.depositar(300)
conta_felipe.pix(100, conta_lucas)
conta_felipe.sacar(50)
conta_felipe.depositar(400)
conta_felipe.pix(200, conta_kaio)
conta_felipe.sacar(100)
conta_felipe.depositar(250)

conta_felipe.mostrar_historico()

