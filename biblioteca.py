class Aluno:
    def __init__(self, nome, sobrenome, ra):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__ra = ra

    # Métodos get e set para os atributos
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @sobrenome.setter
    def sobrenome(self, novo_sobrenome):
        self.__sobrenome = novo_sobrenome

    @property
    def ra(self):
        return self.__ra

    @ra.setter
    def ra(self, novo_ra):
        self.__ra = novo_ra

class Livro:
    def __init__(self, titulo, autor, codigo_identificacao):
        self.__titulo = titulo
        self.__autor = autor
        self.__codigo_identificacao = codigo_identificacao

    # Métodos get e set para os atributos
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        self.__titulo = novo_titulo

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, novo_autor):
        self.__autor = novo_autor

    @property
    def codigo_identificacao(self):
        return self.__codigo_identificacao

    @codigo_identificacao.setter
    def codigo_identificacao(self, novo_codigo):
        self.__codigo_identificacao = novo_codigo
        
        
# Criando um objeto da classe Aluno
aluno1 = Aluno("João", "Silva",12345)

# Acessando os atributos do aluno
print(aluno1.nome)  # Saída: João
print(aluno1.ra)     # Saída: 12345

# Criando um objeto da classe Livro
livro1 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "123-ABC")

# Acessando os atributos do livro
print(livro1.titulo)  # Saída: O Pequeno Príncipe
print(livro1.codigo_identificacao)  # Saída: 123-ABC   
