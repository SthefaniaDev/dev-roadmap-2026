class Curso:
    def __init__(self, titulo, carga_horaria, preco):
        self.titulo = titulo
        self._carga_horaria = carga_horaria
        self.__preco = preco
    
    def exibir_dados(self):
        print(
            "============================ Dados do curso ============================\n"
            f"Título: {self.titulo}\n"
            f"Carga horária: {self._carga_horaria}\n"
            f"Preço: {self.__preco}"
        )
    
    def get_preco(self):
        return self.__preco

curso = Curso("Python OO", 40, 200.0)
curso.exibir_dados()
curso.get_preco()