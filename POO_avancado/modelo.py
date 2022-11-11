class Programa:
    def __init__(self, nome, ano):
        """Método mágico __init__, construtor da classe"""
        self._nome = nome.title()
        self.ano = ano
        self._curtidas = 0

    @property
    def nome(self):
        """Método mágico @property, retorna o valor do atributo, nome do programa"""
        return self._nome

    @nome.setter
    def nome(self, nome):
        """Método mágico @setter, altera o valor do atributo, nome do programa"""
        self._nome = nome.title()

    @property
    def likes(self):
        """Método mágico @property, retorna o valor do atributo, curtidas do programa"""
        return self._curtidas

    def dar_curtidas(self):
        """Método dar_curtidas, adiciona uma curtida ao programa"""
        self._curtidas += 1

    def __str__(self):
        """Método mágico __str__, representação textual do objeto"""
        return f'{self._nome} - {self.ano} - {self._curtidas} curtidas'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        """Class Filme herda de Programa, super() chama o construtor da classe pai"""
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Filme: {self._nome} - {self.ano} - {self.duracao} min - {self._curtidas} curtidas'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        """Class Serie herda de Programa, super() chama o construtor da classe pai"""
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Série: {self._nome} - {self.ano} - {self.temporadas} temporadas - {self._curtidas} curtidas'


class Playlist(list):
    """Class Playlist, herda de list"""
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        """Método mágico __getitem__, define o comportamento do objeto
        quando for acessado como uma lista, aquele que é interável"""
        return self._programas[item]

    @property
    def listagem(self):
        """Retorna a lista de programas da playlist"""
        return self._programas

    @property
    def tamanho(self):
        """Retorna o tamanho (len) dos programas da playlist"""
        return len(self._programas)

    def __len__(self):
        """Método mágico __len__, retorna o tamanho da playlist"""
        return len(self._programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atantla = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

vingadores.dar_curtidas()
vingadores.dar_curtidas()
tmep.dar_curtidas()
tmep.dar_curtidas()
tmep.dar_curtidas()
demolidor.dar_curtidas()
demolidor.dar_curtidas()
demolidor.dar_curtidas()
atantla.dar_curtidas()
atantla.dar_curtidas()

filmes_e_series = [vingadores, atantla, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana.listagem:
    print(programa)


