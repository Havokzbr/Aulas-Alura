# Regular Expression - RegEx
import re


def inseri_texto():
    """Inicia a busca do CEP no texto"""
    print("Digite abaixo o texto que deseja buscar o CEP.\n")
    entrada = input("Digite o Endereço Completo: ")
    extrator_cep = ExtratorCEP(entrada)
    extrator_cep.exibi_dados()


class ExtratorCEP:
    """Classe para extrair o CEP do texto"""
    def __init__(self, texto):
        self.texto = texto

    def extrai_cep(self):
        """Extrair o CEP do texto"""
        padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
        return padrao.search(self.texto)

    def get_cep(self):
        """Retorna o CEP encontrado, se não encontrar, retorna aviso"""
        busca_cep = self.extrai_cep()
        if busca_cep:
            return busca_cep.group()
        else:
            return "Não encontrado o CEP no texto"

    def extrai_endereco(self):
        """Extrai o endereço do texto"""
        padrao = re.compile("[A-Za-z0-9 ]+")
        return padrao.search(self.texto)

    def get_endereco(self):
        """Retorna o endereço encontrado, se não encontrar, retorna aviso"""
        busca_endereco = self.extrai_endereco()
        if busca_endereco:
            return busca_endereco.group()
        else:
            return "Não encontrado o endereço no texto"

    def exibi_dados(self):
        """Exibe os dados"""
        print('Nome da rua: {}'.format(self.get_endereco()))
        print('CEP: {}'.format(self.get_cep()))


inseri_texto()

# Rua das Flores, 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120
