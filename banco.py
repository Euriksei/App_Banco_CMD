import os

def limpar_tela():
    os.system('cls')

class cliente:
    def __init__(self, nome, cpf, saldo):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo

    def cadastro(self):
        print(f"O nome do cliente é: {self.nome}")
        print(f'O CPF é: {self.cpf}')
        print(f'O saldo atual é de: R${self.saldo:.2f}\n')

    def pagamento(self):
        valor = float(input('\nQual valor do pagamento?\n'))
        self.saldo = self.saldo - valor
        limpar_tela()
    
    def receber(self):
        valor = float(input('Qual valor voce esta recebendo?\n'))
        self.saldo += valor
        limpar_tela()

clientes = [
    cliente('João', '14526597854', 1200),
    cliente('Marco', '14318963478', 2000),
    cliente('Júlia', '25649768314', 4580),
    cliente('Ana', '49768315428', 6972)
]

def selecionar_cliente():
    while True:
        print('Bem vindo ao Banco!')
        print('Sobre qual cliente você quer tratar ?\n')
        try:
            tran = int(input('1-Joao\n2-Marco\n3-Julia\n4-Ana\n0-Sair\n'))
            limpar_tela()
            if tran == 0:
                return None
            elif 1 <= tran <=4:
             return tran - 1
            
            else:
                print('Escolha um valor valido')    
        except ValueError:
            print('Insira um valor válido')
        
        
def main():
    while True:
        cliente_index = selecionar_cliente()
        if cliente_index is None:
                limpar_tela()
                print("Saindo...")
                break
        cliente_selecionado = clientes[cliente_index]
        cliente_selecionado.cadastro()
        while True:
            try:
                print('qual operação voce quer realizar?')
                movi = int(input('1-Pagar\n2-Receber\n3-Outro cliente\n0-Sair\n'))
                if movi == 1:
                    cliente_selecionado.pagamento()
                    limpar_tela()
                    print('\nTransação realizada')
                    print(f'O saldo atual é de {cliente_selecionado.saldo}\n\n')
                elif movi == 2:
                    cliente_selecionado.receber()
                    limpar_tela()
                    print('\nTransação realizada')
                    print(f'O saldo atual é de {cliente_selecionado.saldo}\n\n')
                elif movi == 3:
                    limpar_tela()
                    main()
                elif movi == 0:
                    limpar_tela()
                    print('saindo')
                    return
            except ValueError:
                print('Digite uma opção valida')


if __name__ == "__main__":
    main()