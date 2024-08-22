#CLASSE ENDERECO
from datetime import date


class Endereco: 
    def __init__(self, logradouro='', numero='', endereco_Comercial=False):
        #Inicializar os atributos com valores padrao
        self.logradouro = logradouro
        self.numero = numero
        self.endereco_Comercial = endereco_Comercial

#CLASSE PESSOA
class Pessoa: 
    def __init__(self, nome='', rendimento=0.0, endereco=None):
        self.nome = nome
        self.rendimento = rendimento
        self.endereco = endereco

    def calcular_imposto(self, rendimento):
        return rendimento

#CLASSE PESSOA FISICA
class PessoaFisica(Pessoa):
    def __init__(self, nome="", redimento=0.0, endereco=None, cpf="", dataNascimento=None):
        #atribitos da propria classe
        self.cpf = cpf
        self.dataNascimento = dataNascimento
        
        if endereco is None:
            #se nenhum endereço for fornecido, crie um objeto de endereço padrão
            endereco = Endereco()

        if dataNascimento is None:
            dataNascimento = date.today()
            #Validando se a data é diferente da data de hoje

        super().__init__(nome, redimento, endereco)
        #chamando o contrutotor de superclasse pessoa para iniciar os atributos herdados
    
    def calcular_imposto(self, rendimento: float) -> float:
        #verificando se paga imposto 
        if rendimento <= 1500:
            return 0
        elif 1500 < rendimento <= 3500:
            return rendimento * 0.2
            #retornanndo o taltal de imposto a pagar
        elif 3500 < rendimento <= 6000:
            return(rendimento /100)*3.5
        else:
            return rendimento * 0.5
        
#CLASSE PESSOA JURIDICA
class PessoaJuridica(Pessoa): 
    #Inicializar os atributos que foram herdados e proprios atributos da classe
    def __init__(self, nome = "", rendimento=0.0, endereco=None, cnpj=""):
        if endereco is None:
            # Se nenhum endereco for fornecido, cria um objeto Endereco padrao
            endereco = Endereco()
        super().__init__(nome, rendimento, endereco)
        self.cnpj = cnpj
     
        
    def calcular_imposto(self, rendimento: float) -> float:
        # Sem imposto para rendimentos ate 10500
        if rendimento <= 10500:
            return 0
        # 2% de imposto para rendimento entre 10500 e 30500
        elif 10500 < rendimento <= 30500:
            return (rendimento / 100) * 5
            # return rendimento * 0.2
        # 3.5% de imposto para rendimentos entre 30500 e 60000   
        elif 30500 < rendimento <= 60000:
            return (rendimento / 100) * 8   
        # 5% de imposto para rendimentos acima de 60000     
        else: 
            return (rendimento / 100) * 12   
