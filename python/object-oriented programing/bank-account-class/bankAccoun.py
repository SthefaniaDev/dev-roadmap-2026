'''
- adicionar um historico de transacoes do tipo lista
- registrar todas as operalões
- criar um método chamado mostrar histotico
- não permitir operações negativos


mostrar histórico da conta 
depositar 
sacar
pix mostrar histórico
'''
class ContaBancaria:
    def __init__(self, titular, numeroconta, saldo, chavepix):
        self.titular = titular
        self.numeroconta = numeroconta
        self.saldo = saldo
        self.chavepix = chavepix
        self.historico = []
        
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito realizado no valor de {valor} por {self.titular}')
            self.historico.append(f'Depósito ------------ +{valor}')
        else:
            print("Digite um valor válido")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque realizado no valor de {valor} por {self.titular}')
            self.historico.append(f'Saque realizado ------------ -{valor}')
        else:
            print("Valor insuficiente para realizar saque")

    def exibirSaldo(self):
        print(f'Titular: {self.titular} \n Saldo: {self.saldo}' )

    def mostrarDados(self):
        print("==========================================")
        print("Titular:", self.titular)
        print("Numero da conta: ", self.numeroconta)
        print("Saldo: ", self.saldo)
        print("chave pix cadastrada: ", self.chavepix)
        print("==========================================")


    def pix(self, valor, chave_destinatario, contas):
        for conta in contas:
            if chave_destinatario == conta.chavepix:
                if valor <= self.saldo :
                    self.saldo -= valor
                    conta.saldo += valor
                    print(f'Pix realizado no valor de {valor} para {conta.titular}')
                    self.historico.append(f'Pix enviado ------------ -{valor} --> {conta.titular}')

                    conta.historico.append(f'Pix recebido')
                else:
                    print("Saldo insuficiente")
                    print("Chave PIX não encontrada")
    
    def mostrarHistorico(self):
        for acao in self.historico:
            print(acao)

conta1 = ContaBancaria("Felipe", 1, 1000, "felipe@email.com")
conta2 = ContaBancaria("Kaio", 2, 2000, "kaio@email.com")
conta3 = ContaBancaria("Nathan", 3, 3000, "nathan@email.com")
contas = [conta1, conta2]

'''print("\n--- Dados iniciais ---")
conta1.mostrarDados()
conta2.mostrarDados()

print("\n--- Teste de Depósito ---")
conta1.depositar(500)

print("\n--- Teste de Saque ---")
conta1.sacar(200)

print("\n--- Exibir saldo ---")
conta1.exibirSaldo()

print("\n--- Teste PIX (Felipe -> Kaio) ---")
conta1.pix(300, "kaio@email.com", contas)

print("\n--- Teste PIX com chave inexistente ---")
conta2.pix(100, "nathan@gmail.com", contas)

print("\n--- Dados finais das contas ---")
conta1.mostrarDados()
conta2.mostrarDados()

print("=================================")
print(f'saldo de {conta1.titular}: {conta1.saldo}')
print(f'saldo de {conta2.titular}: {conta2.saldo}')
print(f'saldo de {conta3.titular}: {conta3.saldo}')
print("=================================")'''
conta1.depositar(100)
conta1.pix(20, "kaio@email.com", contas)