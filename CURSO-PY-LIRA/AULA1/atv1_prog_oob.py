# -*- coding: utf-8 -*-
"""
Atividade 1 progração orinetada a objeto
Prof: LEANDRO OLIVEIRA DA SILVA

Aluno: Guglielmo H T
"""

class ContaBancaria:
    def __init__(self, titular, saldo, numero_conta):
        self.titular = titular
        self.saldo = saldo
        self.numero_conta = numero_conta

    def mostrardados(self):
        print(f"Titular: {self.titular}")
        print(f"Número da conta: {self.numero_conta}")
        print(f"Saldo: R$ {self.saldo:.2f}")
        print("-" * 30)


# Criando dois objetos (contas bancárias diferentes)
conta1 = ContaBancaria("Maria Tavares Silva", 1000.75, "001234")
conta2 = ContaBancaria("João Souza Cintra", 1200.50, "005678")

# Exibindo as informações das contas
conta1.mostrardados()
conta2.mostrardados()
