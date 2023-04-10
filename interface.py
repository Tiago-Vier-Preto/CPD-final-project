from src.bplustree import bplus_tree
import pickle
import os
import math

def calcula_media(notas):
    soma = 0
    for nota in notas:
        soma = soma + nota
    media = soma / len(notas)
    return media


def ordena_por_nota(inicio, forma):
    if (forma == "C"):
        forma = False
    elif forma == "D":
        forma = True
    else: 
        forma = False

    arq = open("database.bin", "rb")
    arq.seek(inicio)
    lista_alunos_notas = []
    j = 0
    while True:
        try:
            offset = arq.tell()
            obj = pickle.load(arq)
            notas = [obj.dict["NotaCN"], obj.dict["NotaCH"], obj.dict["NotaCN"], obj.dict["NotaLC"], obj.dict["NotaCN"], obj.dict["NotaRedacao"]]
            media = calcula_media(notas)
            media = round(media, 2)
            tupla = (offset, media)
            lista_alunos_notas.append(tupla)
            j += 1
        except(EOFError):
            break

    lista_ordenada = sorted(lista_alunos_notas, key = lambda x:x[1], reverse = forma)
    arq.close()
    return lista_ordenada

def ordena_por_municipio():
    arq = open("database.bin", "rb")
    dicionario_municipios = {}
    j = 0
    while True:
        try:
            offset = arq.tell()
            obj = pickle.load(arq)
            municipio = obj.dict["Municipio"]
            if municipio not in dicionario_municipios:
                dicionario_municipios[municipio] = []
                dicionario_municipios[municipio].append(offset)
            else:
                dicionario_municipios[municipio].append(offset)
            j += 1
        except(EOFError):
            break

    arq.close()
    return dicionario_municipios

def ordena_por_estado():
    arq = open("database.bin", "rb")
    dicionario_estados = {}
    j = 0
    while True:
        try:
            offset = arq.tell()
            obj = pickle.load(arq)
            estado = obj.dict["estado"]
            if estado not in dicionario_estados:
                dicionario_estados[estado] = []
                dicionario_estados[estado].append(offset)
            else:
                dicionario_estados[estado].append(offset)
            j += 1
        except(EOFError):
            break
    arq.close()
    return dicionario_estados

def ordena_por_genero(genero):
    arq = open("database.bin", "rb")
    lista_offset = []
    j = 0
    while True:
        try:
            offset = arq.tell()
            obj = pickle.load(arq)
            sexo = obj.dict["Sexo"]
            if sexo == genero:
                lista_offset.append(offset)
            j += 1
        except(EOFError):
            break

    arq.close()
    return lista_offset

    

def salva_arquivo_invertido(path, dicionario):
    arq = open(path, "wb")
    pickle.dump(dicionario, arq)

def imprime_em_paginas(lista, num_elementos, arq):
    num_paginas = math.ceil(len(lista) / num_elementos)
    pag_atual = 1
    ultimo = 0
    fim = False
    while fim == False:
        print(f'\nExibindo {num_elementos} elementos. Página {pag_atual}/{num_paginas}\n')
        j = ultimo
        while j < num_elementos + ultimo:
            try:
                offset = lista[j]
            except(IndexError):
                break
            arq.seek(offset)
            obj = pickle.load(arq)
            print(obj)
            print("\n")
            j += 1
          
        prox = input("Proxima Pagina (P) - Pagina Anterior (A) - Inserior Página (I) - Sair (S)")
        prox = prox.upper()
        if (prox == "S"):
            fim = True
        elif prox == "P":
            if (pag_atual < num_paginas):
                pag_atual += 1
                ultimo = j
            else:
                ultimo = (num_paginas - 1) * num_elementos
            os.system('cls' if os.name == 'nt' else 'clear')
        elif prox == "A":
            if (pag_atual != 1):
                pag_atual -= 1
                ultimo = j - 2*num_elementos
            else:
                pag_atual = 1
                ultimo = 0
            os.system('cls' if os.name == 'nt' else 'clear')

        elif prox == "I":
            pag_desejada = int(input("Insira a Página:"))
            if (pag_desejada < 1):
                pag_desejada = 1
            if pag_desejada > num_paginas:
                pag_desejada = num_paginas
            ultimo = j + (pag_desejada - pag_atual - 1) * num_elementos
            pag_atual = pag_desejada
            os.system('cls' if os.name == 'nt' else 'clear')

arvore = bplus_tree()
print("\n********** Bem vindo ao Banco de Dados do ENEM 2021 **********\n")
arvore = arvore.open("./")
sair = False

while sair == False:
    print("1 - Consultar Informações")
    print("2 - Ordenar por Nota")
    print("3 - Mostrar as provas feitas em um Municipio")
    print("4 - Mostrar as provas feitas em um Estado")
    print("5 - Mostrar as provas feitas por um determinado gênero")
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
    elif opcode == 2:
        print("C - Crescente")
        print("D - Decrescente")
        forma = input("Insira a forma de ordenacao:")
        forma = forma.upper()
        
        arq = open("database.bin", "rb")

        lista_ordenada = ordena_por_nota(0, forma)

        num_elementos = 4
        num_paginas = math.ceil(len(lista_ordenada) / num_elementos)
        pag_atual = 1
        ultimo = 0
        fim = False
        while fim == False:
            print(f'\nExibindo {num_elementos} elementos. Página {pag_atual}/{num_paginas}\n')
            j = ultimo
            while j < num_elementos + ultimo:
                try:
                    offset = lista_ordenada[j][0]
                except(IndexError):
                    break
                arq.seek(offset)
                obj = pickle.load(arq)
                print(obj)
                print(f'Nota Média:{lista_ordenada[j][1]}')
                print("\n")
                j += 1
            prox = input("Proxima Pagina (P) - Pagina Anterior (A) - Inserior Página (I) - Sair (S)")
            prox = prox.upper()
            if (prox == "S"):
                fim = True
            elif prox == "P":
                if (pag_atual < num_paginas):
                    pag_atual += 1
                    ultimo = j
                else:
                    ultimo = (num_paginas - 1) * num_elementos
                os.system('cls' if os.name == 'nt' else 'clear')
            elif prox == "A":
                if (pag_atual != 1):
                    pag_atual -= 1
                    ultimo = j - 2*num_elementos
                else:
                    pag_atual = 1
                    ultimo = 0
                os.system('cls' if os.name == 'nt' else 'clear')

            elif prox == "I":
                pag_desejada = int(input("Insira a Página:"))
                if (pag_desejada < 1):
                    pag_desejada = 1
                if pag_desejada > num_paginas:
                    pag_desejada = num_paginas
                ultimo = j + (pag_desejada - pag_atual - 1) * num_elementos
                pag_atual = pag_desejada
                os.system('cls' if os.name == 'nt' else 'clear')
    elif opcode == 3:
        arq = open("database.bin", "rb")
        try:
            arq2 = open("ArquivoMunicipio.bin", "rb")
            dicionario_municipios = pickle.load(arq2)
        except(FileNotFoundError):
            dicionario_municipios = ordena_por_municipio()
            salva_arquivo_invertido("ArquivoMunicipio.bin", dicionario_municipios)

        municipio = input("Insira o municipio:")
        if municipio not in dicionario_municipios:
            print(f'Municipio {municipio} não encontrado!')
        else:
            lista_offset = dicionario_municipios[municipio]
            imprime_em_paginas(lista_offset, 4, arq)  
    elif opcode == 4:
        arq = open("database.bin", "rb")
        try:
            arq2 = open("ArquivoEstado.bin", "rb")
            dicionario_estados = pickle.load(arq2)
        except(FileNotFoundError):
            dicionario_estados = ordena_por_estado()
            salva_arquivo_invertido("ArquivoEstado.bin", dicionario_estados)

        estado = input("Insira o estado:")
        estado = estado.upper()
        if estado not in dicionario_estados:
            print(f'Estado {estado} não encontrado!')
        else:
            lista_offset = dicionario_estados[estado]
            imprime_em_paginas(lista_offset, 4, arq)
    elif opcode == 5:
        genero = input("Masculino (M) ou Feminino (F):")
        genero = genero.upper()
        if genero != "M" and genero != "F":
            print("Gênero não encontrado!")
        else:
            if genero == "M":
                genero = "Masculino"
            elif genero == "F":
                genero = "Feminino"
            arq = open("database.bin", "rb")
            lista_offset_genero = ordena_por_genero(genero)
            imprime_em_paginas(lista_offset_genero, 4, arq)
    elif opcode == 0:
        sair = True