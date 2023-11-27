def construir_linguagem(A, B):
    conjunto_A = set(A) #converte A e B em conjuntos para a manipulação
    conjunto_B = set(B)
    
    # constrói a linguagem conforme os conjuntos são definidos
    C = (conjunto_A.intersection(conjunto_B.symmetric_difference(conjunto_A))) | (conjunto_B.intersection(conjunto_A.symmetric_difference(conjunto_B))) 
    
    return C 

def executar_MT(linguagem):
    if len(linguagem) == 0: #executa a maquina de turing conferindo a linguagem e assim gerando a saída "aceita" ou "rejeita"
        return "Aceita"
    else:
        return "Rejeita"

# definir a "palavra" AB para a entrada do algoritmo 
A = "wwraaaabbrcaaba"  
B = "adbabaeaaa"


linguagem = construir_linguagem(A, B) #construtor da palavra para enviar a linguagem para as funções

resultado_MT = executar_MT(linguagem) #gera o resultado "aceita" ou "rejieta"

print("resultado da MT:", resultado_MT) 
