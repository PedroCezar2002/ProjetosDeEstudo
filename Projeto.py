

class Usuario:

    usuarios = []

    def listarUsuario(self,nome,idade,email):
        novoUsuario = Usuario(nome, idade, email)
        usuarios.append(novoUsuario)
        print("contato adicionado com sucesso {novoUsuario}")

    def __init__(self, nome , idade , email):                         #Informações que um usuário deve fornecer
        self.__nome = nome
        self.__idade = idade
        self.__email = email

    def __str__(self):
        return "Nome: {__nome}, Idade: {__idade}, E-mail: {__email}"

            # ------------ Getters e Setters das informações fornecidas do usuário-----------------

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome):
        __nome = nome
    
    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self,idade):
        __idade = idade
    
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,email):
        __email = email

    @property
    def dominio(self):
        return self.__dominio
    
    def pegarDominio(self):
        self.__dominio = self.__email ['@': ]

# ---------------------------------------------------------------------------


    def verificaIdade(self):                        # Sistema para verificar se a idade fornecida é um Int maior que zero
        while(self.__idade < 0):
            self.__idade = int(self.__idade)
            if (self.__idade < 0):
                print("Por favor, digite uma idade válida!")
                self.__idade = input("Idade: ")
    
    def verificaEmail(self):                        # Sistema para verificar se E-mail fornecido é válido
        if (self.__dominio == None):
            print("Achamos um erro! Digite um email válido.")
            self.__email = input("E-mail: ")
            self.__dominio = self.__email.find['@':]

    def comparaIdade(self, outroUsuario):           # Sistema para comparar as Idades entre dois usuários
        if(self.idade == outroUsuario.idade):
            print("Ambos usuários possuem a mesma idade.")
        elif(self.idade > outroUsuario.idade):  
            print("Esse usuário é mais velho que o outro usuário em {} anos".format(self.idade - outroUsuario.idade))
        else:
            print("Esse usuário é mais novo que o outro usuário em {} anos".format(outroUsuario.idade - self.idade))
    
#------------------------------------------------------------------------------------------------------------------------------


    contadorint = 0

    while(contadorint <=4):
        print("1 - Criar usuário")
        print("2 - Informações do usuário")
        print("3 - Saber o dominio de E-mail do usuário")
        print("4 - Comparar idades entre usuários")
        print("5 ou mais - Fechar aplicação")
        contador = input("Qual opção você deseja realizar?")
        contadorint = int(contador)
        print("")
        
        if(contadorint == 1):
            nome = input("Nome do usuário: ")
            idade = input("Idade: ")
            email = input("E-mail: ")
            listarUsuario(nome,idade,email)
            
            
                
            

        elif(contadorint == 2):
            # numero = input("Qual usuário quer acessar as informações? ")
            print()

        elif(contadorint ==3):
            print(Usuario.dominio)