class Transicao:
    def __init__(self,estado_origem,simbolo,estado_destino):
        self.estado_origem = estado_origem
        self.simbolo = simbolo
        self.estado_destino = estado_destino

class AFD:
    def __init__(self):
        self.transicoes = []
        self.estados_finais = []
        self.estado_inicial = 0
        self.estados = []
        self.estado_atual = 0
        self.alfabeto = []

    def adicionar_estado(self,estado):
        self.estados.append(estado)

    def adicionar_transicao(self,estado_origem,simbolo,estado_destino):
        transicao = Transicao(estado_origem,simbolo,estado_destino)
        self.transicoes.append(transicao)
    
    def adicionar_estado_final(self,estado_final):
        self.estados_finais.append(estado_final)

    def adicionar_alfabeto(self,simbolo):
        self.alfabeto.append(simbolo)
    
    def inicializar_estados(self,quantidade_estados):
        for i in range(quantidade_estados):
            self.adicionar_estado(i)

    def inicializar_alfabeto(self,entrada):
        entrada = entrada.split()
        numero_de_simbolos = int(entrada[0])

        for i in range(numero_de_simbolos):
            self.adicionar_alfabeto(entrada[i+1])

    def inicializar_estados_finais(self,entrada):
        entrada = entrada.split()
        numero_estados_finais = int(entrada[0])

        for i in range(numero_estados_finais):
            self.adicionar_estado_final(int(entrada[i+1]))
    
    def set_estado_inicial(self,estado_inicial):
        self.estado_inicial = estado_inicial

    def set_estado_atual(self,estado_atual):
        self.estado_atual = int(estado_atual)
    
    def get_estado_atual(self):
        return self.estado_atual
    
    def get_numero_transicoes(self):
        return len(self.transicoes)
    
    def get_numero_estados(self):
        return len(self.estados)
    
    def get_tamanho_alfabeto(self):
        return len(self.alfabeto)
    
    def consumir_simbolo(self,estado_atual,simbolo):
        for transicao in self.transicoes:
            if int(transicao.estado_origem) == estado_atual and transicao.simbolo == simbolo:
             return transicao.estado_destino
            
        return None
    
    def consumir_palavra(self,palavra):
        palavra = list(palavra)
        self.set_estado_atual(self.estado_inicial)
        for simbolo in palavra:
            estado = self.consumir_simbolo(self.estado_atual,simbolo)
            self.set_estado_atual(estado)
        return self.get_estado_atual()
            
    def pertence_a_linguagem(self,palavra):
        self.consumir_palavra(palavra)
        if self.get_estado_atual() in self.estados_finais:
            return True
        else:
            return False
        
    def __str__(self):
        transicoes_str = "\n".join(
            f"({t.estado_origem}) --[{t.simbolo}]--> ({t.estado_destino})" for t in self.transicoes
        )
        return (
            f"AFD:\n"
            f"Estados: {self.estados}\n"
            f"Alfabeto: {self.alfabeto}\n"
            f"Estado Inicial: {self.estado_inicial}\n"
            f"Estados Finais: {self.estados_finais}\n"
            f"Transições:\n{transicoes_str}\n"
        )
    


class Solucao:
    def __init__(self,numero_estados,input_simbolos,afd):   
        self.numero_estados = numero_estados
        self.input_simbolos = input_simbolos
        self.afd = afd

    def resolve(self):
        self.afd.inicializar_estados(self.numero_estados)
        self.afd.inicializar_alfabeto(self.input_simbolos)

        for i in range(self.afd.get_tamanho_alfabeto() * self.afd.get_numero_estados()):
            self.afd.adicionar_transicao(*input().split())
        
        self.afd.set_estado_inicial(int(input()))
        self.afd.inicializar_estados_finais(input())

        if self.afd.pertence_a_linguagem(input()):
            print('Aceito')
        else:
            print('Rejeito')
    
    

afd = AFD()
solucao = Solucao(int(input()),input(),afd)
solucao.resolve()



    

