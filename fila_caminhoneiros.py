class FilaCaminhoneiros:    # definindo uma classe cahamada FilaCaminhoneiros

    def __init__(self):     # definindo o método especial init, que é o constrututor da classe. ele é chamado quando um objeto da classe é criado
        self.fila = []      # criando um atributo chamado fila que é uma lista vazia. essa lista vai ser usada para armazenar os nomes dos caminhoneiros na fila

    def chegada_caminhoneiro(self, nome):   # definindo um método chamado chegada_caminhoneiro que permite que um caminhoneiro chegue e entre na fila. recebe o nome como argumento
        if len(self.fila) < 10:     # verifica se o tamanho da fila é menor que 10, para ver se ainda há espaço na fila para mais caminhoneiros
            self.fila.append(nome)      # adiciona o nome do caminhoneiro na fila usando o método append()
            print(f"{nome} chegou e entrou na fila.")   # mensagem indicando que o caminhoneiro chegou e entrou na fila
        else:       # se a fila estiver com mais de 10 caminhoneiros exibe a próxima mensagem
            print("A fila está cheia. Aguarde um caminhoneiro sair.")   # mensagem informando que a fila está cheia e o caminhoneiro deve esperar

    def atendimento_caminhoneiro(self):     # definindo um método que permite que o caminhoneiro seja atendido
        if self.fila:       # verifica se a fila não está vazia
            proximo = self.fila.pop(0)      # remove e armazena o primeiro da fila na variável "próximo" usando o método pop(0) para remover o primeiro da lista
            print(f"{proximo} está sendo atendido.")    # mostra uma mensagem que o caminhoneiro esta sendo atendido
        else:       # se a fila estiver vazia mostra a mensagem a seguir
            print("A fila está vazia. Nenhum caminhoneiro para atender.")   # mensagem informando que a fila esta vazia e que nao tem caminhoneiros pra atender

    def status_fila(self):      # definindo um método que exibe o status da fila
        print(f"Fila atual: {', '.join(self.fila)}")    # exibe uma mensagem com os nomes dos caminhoneiros na fila, usando o método join() para concatenar os elementos da lista

fila_caminhoneiros = FilaCaminhoneiros()    # criando uma instância da classe "FilaCaminhoneiros" chamada "fila_caminhoneiros"

while True:     # inicia um loop infinito pra exibir um menu e interagir com o usuário
    print("\n___________________MENU___________________")
    print("Digite o número conforme a opção desejada:")
    print("1 -> Chegada de caminhoneiro")
    print("2 -> Atendimento de caminhoneiro")
    print("3 -> Status da fila")
    print("4 -> Sair")

    opcao = input("Escolha uma opção: ")    # solicita ao usuário que escolha uma opção do menu e armazena a escolha na variável "opção"

    # as próximas linhas verificam a opção escolhida pelo usuário e chamam os métodos correspondentes da instâncias "fila_caminhoneiros" pra executar as ações desejadas

    if opcao == "1":
        nome = input("Digite o nome do caminhoneiro: ")
        fila_caminhoneiros.chegada_caminhoneiro(nome)
    elif opcao == "2":
        fila_caminhoneiros.atendimento_caminhoneiro()
    elif opcao == "3":
        fila_caminhoneiros.status_fila()
    elif opcao == "4":      # se o usuário escolher a opção 4 o loop "while" é interrompido, encerrando o programa
        break
    else:       # se o usuário escolher uma opção inválida o programa exibe a mensagem de opção inválida
        print("Opção inválida. Tente novamente.")
