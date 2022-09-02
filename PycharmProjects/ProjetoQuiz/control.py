from model import model

class control:
    def __init__(self):
        self.opcao = -1
        self.modelo = model()
        self.opcao1 = 0

    def getOpcao1(self):
        return self.opcao1

    def setOpcao1(self, opcao1):
        self.opcao1 = opcao1

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def menu(self):
        print("\nEscolha uma das alternativas abaixo: "
              "\n0. Sair"  +
              "\n1. Jogar" +
              "\n2. Consultar"+
              "\n3. Atualizar Nome" +
              "\n4. Excluir")
        self.setOpcao(int(input()))

    def atualizarNome(self):
        print("Informe o código do dado que será atualizado!")
        codigo = int(input())
        print("Informe o novo nome")
        name = input()
        print(self.modelo.atualizar("nome", name, codigo))

    def excluir(self):
        print("Informe o código do dado que deseja excluir: ")
        cod = int(input())
        print(self.modelo.excluir(cod))

    def menuTema(self):
        print("Escolha o tema em qual deseja jogar: \n"
              "\n1.Futebol" +
              "\n2.Animais" +
              "\n3.Geografia")
        self.setOpcao1(int(input()))


    def operacao(self):
        while self.getOpcao() != 0:
            self.menu()
            if self.getOpcao() == 0:
                print("Obrigado.")
                break
            elif self.getOpcao() == 1:
                self.menuTema()
                if self.getOpcao1() == 1:
                    self.jogo()
                elif self.getOpcao1() == 2:
                    self.jogo1()
                elif self.getOpcao1() == 3:
                    self.jogo2()
                else:
                    print("Opção inválida!")

            elif self.getOpcao() == 2:
                print(self.modelo.selecionar())
            elif self.getOpcao() == 3:
                self.atualizarNome()

            elif self.getOpcao() == 4:
                self.excluir()

        else:
            print("Opção inválida.")

    def jogo2(self):
        tema = "Geografia"
        contador = 0
        print("Antes de começar o Quiz, informe seu nome: ")
        nome = input()
        print("1. A capital do Brasil é: \n"
              "\n1. Rio De Janeiro " +
              "\n2. Brasília" +
              "\n3. São Paulo" +
              "\n4. Brazilia")
        resposta = int(input())
        while resposta < 1 or resposta > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("1. A capital do Brasil é: \n"
                  "\n1. Rio De Janeiro " +
                  "\n2. Brasília" +
                  "\n3. São Paulo" +
                  "\n4. Brazilia")
            resposta = int(input())


        if resposta == 1:
            print("Resposta errada!")
        elif resposta == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta == 3:
            print("Resposta errada!")
        elif resposta == 4:
            print("Resposta errada!")

        #---------------------------------------------------------------------------------------------------------------


        print("2.A capital da russia é ? \n"
              "\n1. Moscou" +
              "\n2. Kiev" +
              "\n3. Texas" +
              "\n4. Caracas")
        resposta2 = int(input())
        while resposta2 < 1 or resposta2 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("2.A capital da russia é ? \n"
                  "\n1. Moscou" +
                  "\n2. Kiev" +
                  "\n3. Texas" +
                  "\n4. Caracas")
            resposta2 = int(input())

        if resposta2 == 1:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta2 == 2:
            print("Resposta errada!")
        elif resposta2 == 3:
            print("Resposta errada!")
        elif resposta2 == 4:
            print("Resposta errada!")

        #-----------------------------------------------------------------------------------------------------------------

        print("3.O estado do Brasil que tem maior números de habitantes é? \n" +
              "\n1. Ceará" +
              "\n2. Brasília" +
              "\n3. Amazonas" +
              "\n4. São Paulo")
        resposta3 = int(input())
        while resposta3 < 1 or resposta3 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("3.O estado do Brasil que tem maior números de habitantes é? \n" +
                  "\n1. Ceará " +
                  "\n2. Brasília" +
                  "\n3. Amazonas" +
                  "\n4. São Paulo")
            resposta3 = int(input())
        if resposta3 == 1:
            print("Resposta errada!")
        elif resposta3 == 2:
            print("Resposta errada!")
        elif resposta3 == 3:
            print("Resposta errada!")
        elif resposta3 == 4:
            print("Resposta correta!")
            contador = contador + 1
    #------------------------------------------------------------------------------------------------------------------------



        print("4.A frança fica no ? \n"
              "\n1. Hemisfério Sul" +
              "\n2. Hemisfério Norte" +
              "\n3. Hemisfério Leste" +
              "\n4. Hemisfério Oeste")
        resposta4 = int(input())



        while resposta4 < 1 or resposta4 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("4.A frança fica no ? \n"
                  "\n1. Hemisfério Sul" +
                  "\n2. Hemisfério Norte" +
                  "\n3. Hemisfério Leste"+
                  "\n4. Hemisfério Oeste")
            resposta4 = int(input())
        if resposta4 == 1:
            print("Resposta errada!")
        elif resposta4 == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta4 == 3:
            print("Resposta errada!")
        elif resposta4 == 4:
            print("Resposta errada!")

        #----------------------------------------------------------------------------------------------------------------------------


        print("5.A nação mais rica no mundo é? \n"
              "\n1. Brasil" +
              "\n2. Estados Unidos" +
              "\n3. China"+
              "\n4. Rússia")
        resposta5 = int(input())
        while resposta5 < 1 or resposta5 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("5.A nação mais rica no mundo é? \n"
                  "\n1. Brasil" +
                  "\n2. Estados Unidos" +
                  "\n3. China" +
                  "\n4. Rússia")
            resposta5 = int(input())

        if resposta5 == 1:
            print("Resposta Errada!")
        elif resposta5 == 2:
            print("Resposta Correta!")
            contador = contador + 1
        elif resposta5 == 3:
            print("Resposta Errada!")
        elif resposta5 == 4:
            print("Resposta Errada!")

    #------------------------------------------------------------------------------------------------------------------

        print("6.O clima do estado do amazonas é? \n"
              "\n1. Semi Árido" +
              "\n2. Sub Tropical" +
              "\n3. Tropical" +
              "\n4. Desértico")
        resposta6 = int(input())
        while resposta6 < 1 or resposta6 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("6.O clima do estado do amazonas é? \n"
                  "\n1. Semi Árido" +
                  "\n2. Sub Tropical" +
                  "\n3. Tropical" +
                  "\n4. Desértico")
            resposta6 = int(input())

        if resposta6 == 1:
            print("Resposta errada!")
        elif resposta6 == 2:
            print("Resposta errada!")
        elif resposta6 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta6 == 4:
            print("Resposta errada!")

    #-------------------------------------------------------------------------------------------------------------------------

        print("7.A África é ? \n"
              "\n1. País" +
              "\n2. Planeta" +
              "\n3. Estado" +
              "\n4. Continente")
        resposta7 = int(input())
        while resposta7 < 1 or resposta7 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("7.A África é ? \n"
                  "\n1. País" +
                  "\n2. Planeta" +
                  "\n3. Estado" +
                  "\n4. Continente")
            resposta7 = int(input())

        if resposta7 == 1:
            print("Resposta errada!")
        elif resposta7 == 2:
            print("Resposta errada!")
        elif resposta7 == 3:
            print("Resposta errada!")
        elif resposta7 == 4:
            print("Resposta correta!")
            contador = contador + 1

    #----------------------------------------------------------------------------------------------------------------------

        print("8.O bioma predominante no ceará é? \n"
              "\n1. Cerrado" +
              "\n2. Caatinga" +
              "\n3. Mata Atlântica" +
              "\n4. Amazônia")
        resposta8 = int(input())
        while resposta8 < 1 or resposta8 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("8.O bioma predominante no ceará é? \n"
                  "\n1. Cerrado" +
                  "\n2. Caatinga" +
                  "\n3. Mata Atlântica" +
                  "\n4. Amazônia")
            resposta8 = int(input())
        if resposta8 == 1:
            print("Resposta errada!")
        elif resposta8 == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta8 == 3:
            print("Resposta errada!")
        elif resposta8 == 4:
            print("Resposta errada!")

        #-------------------------------------------------------------------------------------------------------


        print("9.Qual o país mais populoso do hemisfério sul? \n"
              "\n1. Indonésia" +
              "\n2. Austrália" +
              "\n3. Brasil " +
              "\n4. África do Sul")
        resposta9 = int(input())
        while resposta9 < 1 or resposta9 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("9.Qual o país mais populoso do hemisfério sul? \n"
                  "\n1. Indonésia" +
                  "\n2. Austrália" +
                  "\n3. Brasil " +
                  "\n4. África do Sul")
            resposta9 = int(input())
        if resposta9 == 1:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta9 == 2:
            print("Resposta errada!")
        elif resposta9 == 3:
            print("Resposta errada!")
        elif resposta9 == 4:
            print("Resposta errada!")

    #--------------------------------------------------------------------------------------------------------------------

        print("10.Qual é o maior país do mundo ? \n"
              "\n1. Brasil" +
              "\n2. Rússia" +
              "\n3. Estados Unidos" +
              "\n4. Inglaterra")
        resposta10 = int(input())
        while resposta10 < 1 or resposta10 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("10.Qual é o maior país do mundo ? \n"
                  "\n1. Brasil" +
                  "\n2. Rússia" +
                  "\n3. Estados Unidos" +
                  "\n4. Inglaterra")
            resposta10 = int(input())
        if resposta10 == 1:
            print("Resposta errada!")
        elif resposta10 == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta10 == 3:
            print("Resposta correta!")
        elif resposta10 == 4:
            print("Resposta errada!")

        print("Sua pontuação foi: {}".format(contador))
        self.modelo.inserir(nome, contador, tema)
        #----------------------------------------------------------------------------------------------------------------------

    def jogo1(self):
        tema = "Animais"
        contador = 0
        print("Antes de começar o Quiz, informe seu nome: ")
        nome = input()
        print("1.Qual o maior animal do planeta? \n"
              "\n1. Tubarão Branco" +
              "\n2. Baleia Azul" +
              "\n3. Girafa" +
              "\n4. Rinoceronte")
        resposta = int(input())
        while resposta < 1 or resposta > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("1.Qual o maior animal do planeta? \n"
                  "\n1. Tubarão Branco" +
                  "\n2. Baleia Azul" +
                  "\n3. Girafa" +
                  "\n4. Rinoceronte")
            resposta = int(input())
        if resposta == 1:
            print("Resposta errada!")
        elif resposta == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta == 3:
            print("Resposta errada!")
        elif resposta == 4:
            print("Resposta errada!")


        print("2.Qual o animal mais rápido do mundo? \n"
              "\n1. Tigre" +
              "\n2. Leão" +
              "\n3. Guepardo" +
              "\n4. Cavalo")
        resposta2 = int(input())
        while resposta2 < 1 or resposta2 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("2.Qual o animal mais rápido do mundo? \n"
                  "\n1. Tigre" +
                  "\n2. Leão" +
                  "\n3. Guepardo" +
                  "\n4. Cavalo")
            resposta2 = int(input())
        if resposta2 == 1:
            print("Resposta errada!")
        elif resposta2 == 2:
            print("Resposta errada!")
        elif resposta2 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta2 == 4:
            print("Resposta errada!")

        print("3.Qual é o animal mais alto do mundo? \n" +
              "\n1. Elefante africano " +
              "\n2. Baleia Azul" +
              "\n3. Lula colossal" +
              "\n4. Girafa")
        resposta3 = int(input())
        while resposta3 < 1 or resposta3 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("3.Qual é o animal mais alto do mundo? \n" +
                  "\n1. Elefante africano "
                  "\n2. Baleia Azul"
                  "\n3. Lula colossal"
                  "\n4. Girafa")
            resposta3 = int(input())
        if resposta3 == 1:
            print("Resposta errada!")
        elif resposta3 == 2:
            print("Resposta errada!")
        elif resposta3 == 3:
            print("Resposta errada!")
        elif resposta3 == 4:
            print("Resposta correta!")
            contador = contador + 1
        print("4.Qual é o tempo médio de vida de um cão? \n"
              "\n1. 3-5 anos"+
              "\n2. 10-13 anos"+
              "\n3. 14-20 anos"+
              "\n4. 20-25 anos")
        resposta4 = int(input())
        while resposta4 < 1 or resposta4 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("4.Qual é o tempo médio de vida de um cão? \n"
                  "\n1. 3-5 anos" +
                  "\n2. 10-13 anos" +
                  "\n3. 14-20 anos"+
                  "\n4. 20-25 anos")
            resposta4 = int(input())
        if resposta4 == 1:
            print("Resposta errada!")
        elif resposta4 == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta4 == 3:
            print("Resposta errada!")
        elif resposta4 == 4:
            print("Resposta errada!")

        print("5.Qual o mecanismo de defesa de um gambá? \n"
              "\n1. Peidos com cheiro fétido" +
              "\n2. Mordidas Fatais" +
              "\n3. Saliva venenosa"+
              "\n4. Garras afiada")
        resposta5 = int(input())
        while resposta5 < 1 or resposta5 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("5.Qual o mecanismo de defesa de um gambá? \n"
                  "\n1. Peidos com cheiro fétido" +
                  "\n2. Mordidas Fatais" +
                  "\n3. Saliva venenosa" +
                  "\n4. Garras afiada")
            resposta5 = int(input())
        if resposta5 == 1:
            print("Resposta Correta!")
            contador = contador + 1
        elif resposta5 == 2:
            print("Resposta Errada!")
        elif resposta5 == 3:
            print("Resposta Errada!")
        elif resposta5 == 4:
            print("Resposta Errada!")

        print("6.Que animal pode viver por semanas sem cabeça ou cérebro? \n"
              "\n1. Aranha" +
              "\n2. Formigas" +
              "\n3. Barata" +
              "\n4. Gafanhoto")
        resposta6 = int(input())
        while resposta6 < 1 or resposta6 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("6.Que animal pode viver por semanas sem cabeça ou cérebro? \n"
                  "\n1. Aranha" +
                  "\n2. Formigas" +
                  "\n3. Barata" +
                  "\n4. Gafanhoto")
            resposta6 = int(input())
        if resposta6 == 1:
            print("Resposta errada!")
        elif resposta6 == 2:
            print("Resposta errada!")
        elif resposta6 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta6 == 4:
            print("Resposta errada!")

        print("7.Que animal não precisa beber água a vida inteira? \n"
              "\n1. Camelo" +
              "\n2. Pequeno rato canguru" +
              "\n3. Coruja" +
              "\n4. Elefante")
        resposta7 = int(input())
        while resposta7 < 1 or resposta7 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("7.Que animal não precisa beber água a vida inteira? \n"
                  "\n1. Camelo" +
                  "\n2. Pequeno rato canguru" +
                  "\n3. Coruja" +
                  "\n4. Elefante")
            resposta7 = int(input())
        if resposta7 == 1:
            print("Resposta errada!")
        elif resposta7 == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta7 == 3:
            print("Resposta errada!")
        elif resposta7 == 4:
            print("Resposta errada!")

        print("8.Que animal é o único que não consegue saltar? \n"
              "\n1. Suínos" +
              "\n2. Baleias" +
              "\n3. Girafas" +
              "\n4. Elefantes")
        resposta8 = int(input())
        while resposta8 < 1 or resposta8 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("8.Que animal é o único que não consegue saltar? \n"
                  "\n1. Suínos" +
                  "\n2. Baleias" +
                  "\n3. Girafas" +
                  "\n4. Elefantes")
            resposta8 = int(input())
        if resposta8 == 1:
            print("Resposta errada!")
        elif resposta8 == 2:
            print("Resposta errada!")
        elif resposta8 == 3:
            print("Resposta errada!")
        elif resposta8 == 4:
            print("Resposta correta!")
            contador = contador + 1

        print("9.Onde está o coração do camarão? \n"
              "\n1. Em seu peito" +
              "\n2. Em sua cabeça" +
              "\n3. Em suas caudas" +
              "\n4. Em suas pernas")
        resposta9 = int(input())
        while resposta9 < 1 or resposta9 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("9.Onde está o coração do camarão? \n"
                  "\n1. Em seu peito" +
                  "\n2. Em sua cabeça" +
                  "\n3. Em suas caudas" +
                  "\n4. Em suas pernas")
            resposta9 = int(input())
        if resposta9 == 1:
            print("Resposta errada!")
        elif resposta9 == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta9 == 3:
            print("Resposta errada!")
        elif resposta9 == 4:
            print("Resposta errada!")

        print("10.Qual dos seguintes animais pode voar ? \n"
              "\n1. Pinguins" +
              "\n2. Patos" +
              "\n3. Coruja" +
              "\n4. Foca")
        resposta10 = int(input())
        while resposta10 < 1 or resposta10 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("10.Qual dos seguintes animais pode voar ? \n"
                  "\n1. Pinguins" +
                  "\n2. Patos" +
                  "\n3. Coruja" +
                  "\n4. Foca")
            resposta10 = int(input())
        if resposta10 == 1:
            print("Resposta errada!")
        elif resposta10 == 2:
            print("Resposta errada!")
        elif resposta10 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta10 == 4:
            print("Resposta errada!")

        print("Sua pontuação foi: {}".format(contador))
        self.modelo.inserir(nome, contador, tema)



    def jogo(self):
        tema = "Futebol"
        contador = 0
        print("Antes de começar o Quiz, informe seu nome: ")
        nome = input()
        print("1.Em que ano nasceu o Corinthians?\n"
              "\n1. 1910"
              "\n2. 1934"
              "\n3. 1951"
              "\n4. 1850")
        resposta = int(input())
        while resposta < 1 or resposta > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("1.Em que ano nasceu o Corinthians?\n"
                  "\n1. 1910" +
                  "\n2. 1934" +
                  "\n3. 1951" +
                  "\n4. 1850")
            resposta = int(input())
        if resposta == 1:
            print("Resposta Correta!")
            contador = contador + 1
        elif resposta == 2:
            print("Resposta Errada!")
        elif resposta == 3:
            print("Resposta Errada!")
        elif resposta == 4:
            print("Resposta Errada!")

        print("2.Quantos Mundiais o Palmeiras tem?\n" +
              "\n1. Nenhum" +
              "\n2. Um" +
              "\n3. Dois" +
              "\n4. Cinco")
        resposta2 = int(input())
        while resposta2 < 1 or resposta2 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("2.Quantos Mundiais o Palmeiras tem?\n" +
                  "\n1. Nenhum" +
                  "\n2. Um" +
                  "\n3. Dois" +
                  "\n4. Cinco")
            resposta2 = int(input())
        if resposta2 == 1:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta2 == 2:
            print("Resposta Errada!")
        elif resposta2 == 3:
            print("Resposta Errada!")
        elif resposta2 == 4:
            print("Resposta Errada!")

        print("3.Quantas copas do mundo o Brasil conquistou? \n" +
              "\n1. Três" +
              "\n2. Duas" +
              "\n3. Cinco" +
              "\n4. Nenhuma")
        resposta3 = int(input())
        while resposta3 < 1 or resposta3 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("3.Quantas copas do mundo o Brasil conquistou? \n" +
                  "\n1. Três" +
                  "\n2. Duas" +
                  "\n3. Cinco" +
                  "\n4. Nenhuma")
            resposta3 = int(input())
        if resposta3 == 1:
            print("Resposta errada!")
        elif resposta3 == 2:
            print("Resposta errada!")
        elif resposta3 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta3 == 4:
            print("Resposta errada!")

        print("4.Qual foi o ano em que foi em que o Brasil conquistou a última copa do mundo? \n" +
              "\n1. 1994" +
              "\n2. 1998" +
              "\n3. 2002" +
              "\n4. 2010")
        resposta4 = int(input())

        while resposta4 < 1 or resposta4 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("4.Qual foi o ano em que foi em que o Brasil conquistou a última copa do mundo? \n" +
                  "\n1. 1994" +
                  "\n2. 1998" +
                  "\n3. 2002" +
                  "\n4. 2010")
            resposta4 = int(input())
        if resposta4 == 1:
            print("Resposta errada!")
        elif resposta4 == 2:
            print("Resposta errada!")
        elif resposta4 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta4 == 4:
            print("Resposta errada!")

        print("5. Quem foi o jogador mais jovem a ganhar uma copa do mundo: \n"
              "\n1. Cristiano Ronaldo" +
              "\n2. Pelé" +
              "\n3. Messi" +
              "\n4. Neymar")
        resposta5 = int(input())
        while resposta5 < 1 or resposta5 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("5. Quem foi o jogador mais jovem a ganhar uma copa do mundo? \n"
                  "\n1. Cristiano Ronaldo" +
                  "\n2. Pelé" +
                  "\n3. Messi" +
                  "\n4. Neymar")
            resposta5 = int(input())

        if resposta5 == 1:
            print("Resposta errada!")
        elif resposta5 == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta5 == 3:
            print("Resposta errada!")
        elif resposta5 == 4:
            print("Resposta errada!")

        print("6.Qual a maior torcida do Brasil? \n" 
              "\n1. Corinthians" +
              "\n2. Palmeiras" +
              "\n3. São Paulo" +
              "\n4. Flamengo")
        resposta6 = int(input())
        while resposta6 < 1 or resposta6 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("6.Qual a maior torcida do Brasil? \n"
                  "\n1. Corinthians" +
                  "\n2. Palmeiras" +
                  "\n3. São Paulo" +
                  "\n4. Flamengo")
            resposta6 = int(input())
        if resposta6 == 1:
            print("Resposta errada!")
        elif resposta6 == 2:
            print("Resposta errada!")
        elif resposta6 == 3:
            print("Resposta errada!")
        elif resposta6 == 4:
            print("Resposta correta!")
            contador = contador + 1

        print("7.Aonde foi disputada a última copa do mundo? \n"
              "\n1. França" +
              "\n2. Rússia" +
              "\n3. Japão" +
              "\n4. Espanha")
        resposta7 = int(input())
        while resposta7 < 1 or resposta7 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("7.Aonde foi disputada a última copa do mundo? \n"
                  "\n1. França" +
                  "\n2. Rússia" +
                  "\n3. Japão" +
                  "\n4. Espanha")
            resposta7 = int(input())
        if resposta7 == 1:
            print("Resposta errada!")
        elif resposta7 == 2:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta7 == 3:
            print("Resposta errada!")
        elif resposta7 == 4:
            print("Resposta errada!")

        print("8.Qual país conquistou a última copa do mundo? \n"
              "\n1. Brasil" +
              "\n2. Alemanha" +
              "\n3. Portugal" +
              "\n4. França")
        resposta8 = int(input())
        while resposta8 < 1 or resposta8 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("8.Qual país conquistou a última copa do mundo? \n"
                  "\n1. Brasil" +
                  "\n2. Alemanha" +
                  "\n3. Portugal" +
                  "\n4. França")
            resposta8 = int(input())
        if resposta8 == 1:
            print("Resposta errada!")
        elif resposta8 == 2:
            print("Resposta errada!")
        elif resposta8 == 3:
            print("Resposta errada!")
        elif resposta8 == 4:
            print("Resposta correta!")
            contador = contador + 1

        print("9.A copa do mundo é disputada a cada quantos anos? \n"
              "\n1. Três Anos" +
              "\n2. Dois Anos" +
              "\n3. Quatro Anos" +
              "\n4. Um Ano")
        resposta9 = int(input())
        while resposta9 < 1 or resposta9 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("9.A copa do mundo é disputada a cada quantos anos? \n"
                  "\n1. Três Anos" +
                  "\n2. Dois Anos" +
                  "\n3. Quatro Anos" +
                  "\n4. Um Ano")
            resposta9 = int(input())
        if resposta9 == 1:
            print("Resposta errada!")
        elif resposta9 == 2:
            print("Resposta errada!")
        elif resposta9 == 3:
            print("Resposta correta!")
            contador = contador + 1
        elif resposta9 == 4:
            print("Resposta errada!")

        print("10.Quais desses jogadores ainda não conquistaram a bola  de ouro\n"
              "(prêmio de jogador do ano)\n"
              "\n1. Neymar" +
              "\n2. Kaká" +
              "\n3. Ronaldinho Gaúcho" +
              "\n4. Ronaldo Fenômeno")
        resposta10 = int(input())
        while resposta10 < 1 or resposta10 > 4:
            print("Opção inválida! Digite somente as opções abaixo")
            print("10.Quais desses jogadores ainda não conquistaram a bola  de ouro\n"
                  "(prêmio de jogador do ano)\n"
                  "\n1. Neymar" +
                  "\n2. Kaká" +
                  "\n3. Ronaldinho Gaúcho" +
                  "\n4. Ronaldo Fenômeno")
            resposta10 = int(input())
        if resposta10 == 1:
            print("Resposta Correta!")
            contador = contador + 1
        elif resposta10 == 2:
            print("Resposta Errada!")
        elif resposta10 == 3:
            print("Resposta Errada!")
        elif resposta10 == 4:
            print("Resposta Errada!")

        print("sua pontuação foi: {}".format(contador))
        self.modelo.inserir(nome, contador, tema)



