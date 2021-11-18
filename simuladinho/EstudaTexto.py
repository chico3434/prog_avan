class EstudaTexto:

    def __init__(self, texto):
        self.palavras = texto.strip(',?!').replace(',','').split(' ')



et = EstudaTexto("família, família, cachorro, gato, galinha, oh yeah yeah yeah!")
print(et.palavras)
