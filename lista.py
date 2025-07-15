from enum import Enum
from datetime import datetime, date

class paciente:
    def __init__(self, nome, cpf, telefone, data):
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_data(data)

    def set_nome(self, valor):
        if valor == "":
            raise ValueError("valor invalido")
        self.__nome = valor

    def set_cpf(self, valor):
        if len(valor) != 11:
            raise ValueError("valor invalido")
        self.__cpf = valor

    def set_telefone(self, valor):
        if len(valor) != 11:
            raise ValueError("valor invalido")
        self.__telefone = valor

    def set_data(self, valor):
        if valor == "":
            raise ValueError("valor invalido")
        self.__data = datetime.strptime(valor, "%d/%m/%Y").date()

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_telefone(self):
        return self.__telefone

    def get_data(self):
        return self.__data

    def calc_idade(self):
        hoje = date.today()
        anos = hoje.year - self.__data.year
        meses = hoje.month - self.__data.month
        if hoje.day < self.__data.day:
            meses -= 1
        if meses < 0:
            anos -= 1
            meses += 12
        return anos, meses

    def __str__(self):
        anos, meses = self.calc_idade()
        return f"{self.__nome} tem {anos} anos e {meses} meses"

class paciente_UI:
    def main():
        while paciente_UI.menu() == 1:
            paciente_UI.executar()
    def menu():
        print("1 - calcular | 2 - fim")
        return int(input(""))
    def executar():
        nome = input("nome: ")
        cpf = input("cpf: ")
        telefone = input("telefone: ")
        data = input("data de nascimento (dd/mm/aaaa): ")
        x = paciente(nome, cpf, telefone, data)
        print(x)

paciente_UI.main()

class Pagamento(Enum):
    EM_ABERTO = "Em Aberto"
    PAGO_PARCIAL = "Pago Parcial"
    PAGO = "Pago"

class Boleto:
    def __init__(self, cod_barras, data_emissao, data_vencimento, valor_total):
        self.set_cod_barras(cod_barras)
        self.set_data_emissao(data_emissao)
        self.set_data_vencimento(data_vencimento)
        self.set_valor_total(valor_total)
        self.__valor_pago = 0.0

    def set_cod_barras(self, valor):
        if valor == "":
            raise ValueError("valor inválido")
        self.__cod_barras = valor

    def set_data_emissao(self, valor):
        self.__data_emissao = datetime.strptime(valor, "%d/%m/%Y").date()

    def set_data_vencimento(self, valor):
        self.__data_vencimento = datetime.strptime(valor, "%d/%m/%Y").date()

    def set_valor_total(self, valor):
        valor = float(valor)
        if valor <= 0:
            raise ValueError("Valor inválido")
        self.__valor_total = valor

    def get_cod_barras(self):
        return self.__cod_barras

    def get_data_emissao(self):
        return self.__data_emissao

    def get_data_vencimento(self):
        return self.__data_vencimento

    def get_valor_total(self):
        return self.__valor_total

    def get_valor_pago(self):
        return self.__valor_pago

    def pagar(self, valor):
        valor = float(valor)
        if valor < 0 or self.__valor_pago + valor > self.__valor_total:
            raise ValueError("Valor de pagamento inválido")
        self.__valor_pago += valor

    def situacao(self):
        if self.__valor_pago == 0:
            return Pagamento.EM_ABERTO
        elif self.__valor_pago < self.__valor_total:
            return Pagamento.PAGO_PARCIAL
        else:
            return Pagamento.PAGO

    def __str__(self):
        return (f"Boleto: {self.get_cod_barras()}\n"
                f"Emissão: {self.get_data_emissao().strftime('%d/%m/%Y')}\n"
                f"Vencimento: {self.get_data_vencimento().strftime('%d/%m/%Y')}\n"
                f"Valor Total: R$ {self.get_valor_total():.2f}\n"
                f"Valor Pago: R$ {self.get_valor_pago():.2f}\n"
                f"Situação: {self.situacao().value}")

class boleto_UI:
    def main():
        while boleto_UI.menu() == 1:
            boleto_UI.executar()
    def menu():
        print("1 - Registrar boleto | 2 - Fim")
        return int(input("Escolha: "))
    def executar():
        cod = input("Código de barras: ")
        emissao = input("Data de emissão (dd/mm/aaaa): ")
        venc = input("Data de vencimento (dd/mm/aaaa): ")
        valor = input("Valor do boleto: ")

        boleto = Boleto(cod, emissao, venc, valor)

        pagar = input("Deseja realizar um pagamento? (s/n): ")
        if pagar == "s":
            valor_pago = input("Valor a pagar: ")
            boleto.pagar(valor_pago)

        print("\n--- Dados do Boleto ---")
        print(boleto)

boleto_UI.main()

class Contato:
    def __init__(self, id, nome, email, telefone, data_nascimento):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_telefone(telefone)
        self.set_data_nascimento(data_nascimento)

    def set_id(self, valor):
        valor = int(valor)
        if valor <= 0:
            raise ValueError("valor inválido")
        self.__id = valor

    def set_nome(self, valor):
        if valor == "":
            raise ValueError("valor inválido")
        self.__nome = valor

    def set_email(self, valor):
        if valor == "":
            raise ValueError("valor inválido")
        self.__email = valor

    def set_telefone(self, valor):
        if len(valor) != 11:
            raise ValueError("valor inválido")
        self.__telefone = valor

    def set_data_nascimento(self, valor):
        if valor == "":
            raise ValueError("valor inválido")
        self.__data_nascimento = datetime.strptime(valor, "%d/%m/%Y").date()

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_telefone(self):
        return self.__telefone

    def get_data_nascimento(self):
        return self.__data_nascimento

    def __str__(self):
        return (f"ID: {self.get_id()} | Nome: {self.get_nome()} | Email: {self.get_email()} | "
                f"Telefone: {self.get_telefone()} | Nascimento: {self.get_data_nascimento().strftime('%d/%m/%Y')}")
class ContatoUI:
    contatos = []
    def main():
        while True:
            op = ContatoUI.menu()
            if op == 1:
                ContatoUI.inserir()
            elif op == 2:
                ContatoUI.listar()
            elif op == 3:
                ContatoUI.atualizar()
            elif op == 4:
                ContatoUI.excluir()
            elif op == 5:
                ContatoUI.pesquisar()
            elif op == 6:
                ContatoUI.aniversariantes()
            elif op == 7:
                break
            else:
                print("Opção inválida")
    def menu():
        print("\n--- MENU AGENDA ---")
        print("1 - Inserir Contato")
        print("2 - Listar Contatos")
        print("3 - Atualizar Contato")
        print("4 - Excluir Contato")
        print("5 - Pesquisar por Iniciais")
        print("6 - Aniversariantes do Mês")
        print("7 - Sair")
        return int(input("Escolha: "))
    def inserir():
        id = input("ID: ")
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        data_nasc = input("Data de nascimento (dd/mm/aaaa): ")
        c = Contato(id, nome, email, telefone, data_nasc)
        ContatoUI.contatos.append(c)
        print("Contato inserido com sucesso!")
    def listar():
        print("\n--- Lista de Contatos ---")
        for c in ContatoUI.contatos:
            print(c)
        if not ContatoUI.contatos:
            print("Nenhum contato cadastrado.")
    def atualizar():
        id = int(input("Informe o ID do contato a atualizar: "))
        for c in ContatoUI.contatos:
            if c.get_id() == id:
                nome = input("Novo nome: ")
                email = input("Novo email: ")
                telefone = input("Novo telefone: ")
                data_nasc = input("Nova data de nascimento (dd/mm/aaaa): ")
                c.set_nome(nome)
                c.set_email(email)
                c.set_telefone(telefone)
                c.set_data_nascimento(data_nasc)
                print("Contato atualizado com sucesso!")
                return
        print("Contato não encontrado.")
    def excluir():
        id = int(input("Informe o ID do contato a excluir: "))
        for c in ContatoUI.contatos:
            if c.get_id() == id:
                ContatoUI.contatos.remove(c)
                print("Contato excluído.")
                return
        print("Contato não encontrado.")
    def pesquisar():
        iniciais = input("Iniciais do nome: ").lower()
        for c in ContatoUI.contatos:
            if iniciais in c.get_nome().lower():
                print(c)
    def aniversariantes():
        mes = int(input("Digite o mês (1 a 12): "))
        achou = False
        for c in ContatoUI.contatos:
            if c.get_data_nascimento().month == mes:
                print(c)
                achou = True
        if not achou:
            print("Nenhum aniversariante neste mês.")
ContatoUI.main()