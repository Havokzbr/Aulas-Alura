import re


class ExtratorURL:
    """Salva a url em um atributo do objeto (self.url)"""

    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    @staticmethod
    def sanitiza_url(url):
        """Remove espaços no início e no fim da url, faz a sanitização da url"""
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        """Valida se a url está vazia"""
        if not self.url:
            raise ValueError('A URL está vazia')

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida")

    def extrai_parametros(self):
        """Extrai os parâmetros da url"""
        indice_interrogacao = self.url.find('?')
        parametros = self.url[indice_interrogacao + 1:]
        return parametros

    def get_url_base(self):
        """Extrai a url base"""
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        """Retorna a url dos parâmetros"""
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        """Retorna o valor do parâmetro, se o parâmetro não existir, retorna vazio"""
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)

        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        """Retorna o tamanho da url, dando len no objeto"""
        return len(self.url)

    def __str__(self):
        """Retorna a url, dando print no objeto"""
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base() + "\n" + "O tamanho da URL é: " + str(
            len(extrator_url.url))

    def __eq__(self, other):
        """Compara se a url é igual a outra, dando == no objeto"""
        return self.url == other.url


url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url)

VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

if moeda_origem == "real" and moeda_destino == "dolar":
    valor_convertido = int(quantidade) / VALOR_DOLAR
    print(f"O valor de R$ {quantidade} em dólares é: U$ {valor_convertido}")
elif moeda_origem == "dolar" and moeda_destino == "real":
    valor_convertido = int(quantidade) * VALOR_DOLAR
    print(f"O valor de U$ {quantidade} em reais é: R$ {valor_convertido}")
else:
    print(f"Moeda de {moeda_origem} ou {moeda_destino} é inválida")



#url = "https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
#extrator_url = ExtratorURL(url)

# extrator_url_2 = ExtratorURL(url)

#print('A URL é: ', extrator_url)

# valor_quantidade = extrator_url.get_valor_parametro("quantidade")
# print(valor_quantidade)
# print(extrator_url == extrator_url_2) # extrator_url.__eq__(extrator_url_2) -> Comparação de objetos

# Método ID - Retorna o endereço de memória do objeto, para verificar se são o mesmo objeto, identicos ou apenas iguais
# print(id(extrator_url))
# print(id(extrator_url_2))



