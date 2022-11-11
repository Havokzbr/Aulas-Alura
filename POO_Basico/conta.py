"""
Quando há dois underscores à frente de um atributo, não deve-se acessá-lo diretamente, se torna um método privado.
Para ler um atributo, cria-se um getter para ele, e para modificar um atributo, cria-se um setter para ele.
"""


class Conta:
    """Classe criadora dos objetos da conta"""

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de: {} reais do titular: {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        """Método privado, não deve ser acessado diretamente"""
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    # Pegar o saldo da conta
    """Métodos Getters e Setters"""
    @property
    def saldo(self):
        return self.__saldo

    # Pegar o titular da conta
    @property
    def titular(self):
        return self.__titular

    # Pegar o limite da conta
    """Método property"""
    @property
    def limite(self):
        return self.__limite

    # Alterar o novo valor de limite
    """Método setter, acessar o atributo privado"""
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    # Função para pegar o código do banco
    """Método estático, não precisa de self"""
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_todos_bancos():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}     # Dicionário
