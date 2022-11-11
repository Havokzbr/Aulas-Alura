class Cliente:
    def __init__(self, nome):
        self.__nome = nome


    """ Este método representa uma propriedade, desta forma, indicaremos ao 
    Python nossa intenção de ter acesso ao objeto. """
    @property
    def nome(self):
        print("Chamando @property nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("Chamando setter nome()")
        self.__nome = nome

    @nome.deleter
    def nome(self):
        print("Chamando deleter nome()")
        del self.__nome

