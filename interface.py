from src.bplustree import bplus_tree
import pickle

arvore = bplus_tree()
print("\n********** Bem vindo ao Banco de Dados do ENEM 2021/2 **********\n")
arvore = arvore.open("./")
sair = False

while sair == False:
    print("1 - Consultar Informações")
    print("0 - Sair")
    opcode = int(input("Escolha uma Opção:"))

    if opcode == 1:
        inscricao = int(input("Insira o número de matrícula:"))
        offset = arvore.get(inscricao)
        if offset == None:
            print("Número de matrícula não encontrado!")

        else:
            arq = open("database.bin", "rb")
            arq.seek(offset)
            obj = pickle.load(arq)
            print(obj)
            escolha = input("Deseja voltar ao menu? (S/N)")
            escolha = escolha.upper()
            if escolha == "S":
                pass
            elif escolha == "N":
                sair = True

    elif opcode == 0:
        sair = True
    

    

    

