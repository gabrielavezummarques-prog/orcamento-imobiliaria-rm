import csv

# ============================
# CLASSES DOS IMÓVEIS
# ============================

class Imovel:
    def __init__(self, tipo, valor_base):
        self.tipo = tipo
        self.valor_base = valor_base

    def calcular_valor_aluguel(self):
        return self.valor_base


class Apartamento(Imovel):
    def __init__(self, quartos, garagem, tem_criancas):
        super().__init__("Apartamento", 700)
        self.quartos = quartos
        self.garagem = garagem
        self.tem_criancas = tem_criancas

    def calcular_valor_aluguel(self):
        valor = self.valor_base

        if self.quartos == 2:
            valor += 200

        if self.garagem:
            valor += 300

        if not self.tem_criancas:
            valor *= 0.95  # desconto de 5%

        return valor


class Casa(Imovel):
    def __init__(self, quartos, garagem):
        super().__init__("Casa", 900)
        self.quartos = quartos
        self.garagem = garagem

    def calcular_valor_aluguel(self):
        valor = self.valor_base

        if self.quartos == 2:
            valor += 250

        if self.garagem:
            valor += 300

        return valor


class Estudio(Imovel):
    def __init__(self, vagas_estacionamento):
        super().__init__("Estúdio", 1200)
        self.vagas_estacionamento = vagas_estacionamento

    def calcular_valor_aluguel(self):
        valor = self.valor_base

        if self.vagas_estacionamento >= 2:
            valor += 250  # valor para 2 vagas

            if self.vagas_estacionamento > 2:
                vagas_extra = self.vagas_estacionamento - 2
                valor += vagas_extra * 60

        return valor


# ============================
# CLASSE ORÇAMENTO
# ============================

class Orcamento:
    def __init__(self, imovel):
        self.imovel = imovel
        self.valor_contrato = 2000

    def calcular_mensalidade(self):
        return self.imovel.calcular_valor_aluguel()

    def mostrar_orcamento(self):
        mensalidade = self.calcular_mensalidade()

        print("\n===============================")
        print("      ORÇAMENTO DE ALUGUEL")
        print("===============================")
        print(f"Tipo de imóvel: {self.imovel.tipo}")
        print(f"Valor do aluguel mensal: R$ {mensalidade:.2f}")
        print(f"Contrato imobiliário: R$ {self.valor_contrato:.2f}")
        print("\nParcelamento do contrato (até 5x):")

        for i in range(1, 6):
            print(f"{i}x de R$ {self.valor_contrato / i:.2f}")

        print("===============================\n")

    def gerar_csv_12_parcelas(self, nome_arquivo="parcelas_orcamento.csv"):
        mensalidade = self.calcular_mensalidade()

        with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo, delimiter=";")
            escritor.writerow(["Parcela", "Valor (R$)"])

            for parcela in range(1, 13):
                escritor.writerow([parcela, f"{mensalidade:.2f}"])

        print(f"Arquivo CSV gerado com sucesso: {nome_arquivo}")


# ============================
# FUNÇÃO PRINCIPAL
# ============================

def menu():
    print("===================================")
    print(" SISTEMA DE ORÇAMENTO IMOBILIÁRIA R.M")
    print("===================================")
    print("1 - Apartamento")
    print("2 - Casa")
    print("3 - Estúdio")
    print("0 - Sair")
    print("===================================")


def main():
    while True:
        menu()
        opcao = input("Escolha o tipo de imóvel: ")

        if opcao == "0":
            print("Encerrando sistema... Até logo!")
            break

        elif opcao == "1":
            quartos = int(input("Quantos quartos? (1 ou 2): "))
            garagem = input("Deseja vaga de garagem? (s/n): ").lower() == "s"
            tem_criancas = input("Possui crianças? (s/n): ").lower() == "s"

            imovel = Apartamento(quartos, garagem, tem_criancas)

        elif opcao == "2":
            quartos = int(input("Quantos quartos? (1 ou 2): "))
            garagem = input("Deseja vaga de garagem? (s/n): ").lower() == "s"

            imovel = Casa(quartos, garagem)

        elif opcao == "3":
            vagas = int(input("Quantas vagas de estacionamento deseja? (0 ou mais): "))

            imovel = Estudio(vagas)

        else:
            print("Opção inválida! Tente novamente.\n")
            continue

        orcamento = Orcamento(imovel)
        orcamento.mostrar_orcamento()

        gerar = input("Deseja gerar arquivo CSV com 12 parcelas? (s/n): ").lower()

        if gerar == "s":
            orcamento.gerar_csv_12_parcelas()

        print("\nOrçamento finalizado.\n")


if __name__ == "__main__":
    main()
