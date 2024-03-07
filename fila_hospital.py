class ElementoDaListaSimples:   # definindo uma classe chamada "ElementoDaListaSimples" para representar os elementos individuais em sua lista encadeada simples...
                                # onde cada elemento possui um dado (que é o número do paciente) e uma cor (V para verde e A para amarelo)
    def __init__(self, dado,cor):   # criando o construtor da classe "ElementoDaListaSimples" que é chamado quando você cria um novo elemento da lista
        self.dado = dado            # ele recebe dois parâmetros (dado e cor) que são usados para inicializar os atributos do objeto
        self.cor = cor
        self.proximo = None #  inicializa o atributo proximo com None, indicando que este elemento ainda não esta vinculado a nenhum outro elemento na lista

class ListaEncadeadaSimples:    # definindo uma classe chamada "ListaEncadeadaSimples" que representa a lista encadeada em si. Ela contém métodos para gerenciar a lista
    def __init__(self, nodos=None): # esse é o construtor da classe ListaEncadeadaSimples, ele pode receber uma lista de nodos opcionalmente ao ser criado
                                    # se nodos for fornecido, a lista encadeada será inicializada com os elementos dessa lista
        self.head = None    # inicializa o atributo head como None, indicando que a lista está vazia no início
        if nodos is not None:   #  verificando se "nodos" foi fornecido ao criar a lista encadeada
            nodo = ElementoDaListaSimples(dado=nodos.pop(0))    #  cria um primeiro elemento na lista com o valor do primeiro elemento da lista "nodos"
            self.head = nodo    # define o head como o primeiro elemento da lista
            for elem in nodos:  # itera sobre os elementos restantes na lista nodos
                nodo.proximo = ElementoDaListaSimples(dado=elem)    # cria um novo elemento na lista encadeada para cada elemento restante em nodos e liga ao último elemento
                nodo = nodo.proximo

    def inserirNoFinal(self, nodo): # este método insere um elemento nodo no final da lista encadeada. Se a lista estiver vazia, o elemento se torna o primeiro
        if self.head is None:
            self.head = nodo
            return

        nodo_atual = self.head
        while nodo_atual.proximo != None:
            nodo_atual = nodo_atual.proximo

        nodo_atual.proximo = nodo
        return

    def inserirPrioridade(self, nodo):  # este método insere um elemento nodo na lista com prioridade no início da fila. Se o primeiro paciente na fila tiver um cartão verde...
                                        # o paciente com prioridade é inserido antes dele, caso contrário o paciente com prioridade é inserido após o último paciente com cartão verde
        if self.head.cor == "V":
            # Se o primeiro paciente na fila tiver cartão verde, insira o paciente com prioridade antes dele.
            nodo.proximo = self.head
            self.head = nodo
        else:
            # Caso contrário, encontre o último paciente com cartão verde na fila e insira o paciente com prioridade após ele.
            nodo_atual = self.head
            while nodo_atual.proximo is not None and nodo_atual.proximo.cor == "V":
                nodo_atual = nodo_atual.proximo
            nodo.proximo = nodo_atual.proximo
            nodo_atual.proximo = nodo

    def inserir(self, dado,cor): # esse método insere um novo elemento na lista com base no valor de cor, se a cor for "V" (verde), o paciente é inserido no final da fila usando "inserirNoFinal"
                                # se a cor for "A" (amarelo), o paciente é inserido com prioridade no início da fila usando "inserirPrioridade"
        nodo = ElementoDaListaSimples(dado,cor)

        if self.head is None:
            self.head = nodo
            return
        else:
            if nodo.cor == "V":
                self.inserirNoFinal(nodo)
            else:
                self.inserirPrioridade(nodo)
        return

lista = ListaEncadeadaSimples() # criando uma instância da lista encadeada
# inserindo pacientes declarando o número e a cor
lista.inserir(10, "V")
lista.inserir(11, "V")
lista.inserir(5, "A")
lista.inserir(12, "V")
lista.inserir(6, "A")

# Vericando o status da fila
nodo_atual = lista.head     # inicializa uma variável "nodo_atual" para rastrear o elemento atual da lista, começando pelo primeiro elemento (head)
while nodo_atual is not None:   # inicia um loop para percorrer a lista encadeada
    print(f"{nodo_atual.dado}-{nodo_atual.cor}")    # imprime o número do paciente e a cor do cartão do paciente atua
    nodo_atual = nodo_atual.proximo     # move para o próximo elemento da lista