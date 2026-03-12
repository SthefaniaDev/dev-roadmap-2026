class ContaBancaria:
    def __init__(self, numero, titular, saldo, limite, chave_pix):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.chave_pix = chave_pix
        self.historico_transacoes = []

    def depositar(self, valor):
        if valor <= 0:
            print("Operação inválida!")
        else:
            self.saldo += valor
            print(f"Depósito realizado no valor de {valor} na conta de {self.titular}")
            self.historico_transacoes.append(f"DEPOSITO +{valor}")

    def sacar(self, valor):
        if valor <= 0 or valor > (self.saldo + self.limite):
            print("Operação inválida!")
            return False
        else:
            self.saldo -= valor
            print(f"Saque realizado no valor de {valor} por {self.titular}")
            self.historico_transacoes.append(f"SAQUE -{valor}")
            return True

    def registrar_pix_enviado(self, valor, destinatario):
        print(f"PIX realizado com sucesso!\nPix realizado no valor de {valor} para {destinatario}")
        self.historico_transacoes.append(f"PIX ENVIADO -{valor} -> {destinatario}")

    def registrar_pix_recebido(self, valor, remetente):
        self.historico_transacoes.append(f"PIX RECEBIDO +{valor} <- {remetente}")

    def mostrar_historico(self):
        print(f"Historico da conta: {self.titular}\n")
        for numero, acao in enumerate(self.historico_transacoes, start=1):
            print(f"{numero} - {acao}")


class Banco:
    def __init__(self):
        self.contas = []

    def criar_conta(self, numero, titular, saldo_inicial, limite, chave_pix):
        for conta in self.contas:
            if conta.numero == numero:
                print("Conta com esse numero ja existe")
                return
            if conta.chave_pix == chave_pix:
                print("Chave PIX ja cadastrada")
                return

        nova_conta = ContaBancaria(numero, titular, saldo_inicial, limite, chave_pix)
        self.contas.append(nova_conta)

    def buscar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        print("Conta nao encontrada")

    def buscar_por_pix(self, chave_pix):
        for conta in self.contas:
            if conta.chave_pix == chave_pix:
                return conta
        print("Chave PIX nao encontrada")

    def transferir(self, numero_origem, numero_destino, valor):
        conta_origem = self.buscar_conta(numero_origem)
        conta_destino = self.buscar_conta(numero_destino)

        if conta_origem and conta_destino:
            if conta_origem.sacar(valor):
                conta_destino.depositar(valor)
                conta_origem.registrar_pix_enviado(valor, conta_destino.titular)
                conta_destino.registrar_pix_recebido(valor, conta_origem.titular)

    def listar_contas(self):
        print("=== LISTA DE CONTAS ===\n")
        for conta in self.contas:
            print(f"Conta: {conta.numero}")
            print(f"Titular: {conta.titular}")
            print(f"Saldo: {conta.saldo}")
            print(f"Limite: {conta.limite}")
            print(f"PIX: {conta.chave_pix}\n")


'''==========================TESTES=========================='''

banco = Banco()

banco.criar_conta(1001, "Felipe Kauã", 1000, 200, "felipe@email.com")
banco.criar_conta(1002, "Kaio Javã", 500, 100, "kaio@email.com")
banco.criar_conta(1003, "Jéssica Decarla", 800, 300, "jessica@email.com")

'''==========================LISTAGEM DE CONTAS=========================='''
banco.listar_contas()

'''========================== BUSCA DE CONTAS =========================='''
conta = banco.buscar_conta(1002)
print(conta.titular)
print(conta.saldo)

'''========================== BUSCA POR PIX ========================== '''
conta = banco.buscar_por_pix("jessica@email.com")
print(conta.numero)
print(conta.titular)

'''========================== TRANSFERENCIA =========================='''
banco.transferir(1002, 1003, 200)


'''========================== BUSCA DE CONTAS =========================='''
print(banco.buscar_conta(1002).saldo)
print(banco.buscar_conta(1003).saldo)

banco.buscar_conta(9999)

'''========================== BUSCA POR PIX ========================== '''
banco.buscar_por_pix("pix_inexistente@email.com")