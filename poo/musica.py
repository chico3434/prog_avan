class Musica:

    def __init__(self, nome, artista, estilos):
        self.nome = nome
        self.artista = artista
        self.estilos = estilos

    def tocar(self, comentarios=None):
        if comentarios:
            return "Tocando {} por {} - {}.".format(self.nome, self.artista, comentarios)
        else:
            return "Tocando {} por {}.".format(self.nome, self.artista)