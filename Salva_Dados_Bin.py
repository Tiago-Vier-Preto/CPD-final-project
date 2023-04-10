import csv
import pickle
from classes import Aluno
database = open("database.bin", "wb")
arquivo = open("microdados_enem_2021\DADOS\MICRODADOS_ENEM_2021.csv", "r")
arquivo_csv = csv.reader(arquivo, delimiter=";")

j = 0
for linha in arquivo_csv:
    if (j != 0):
        notas = [linha[31], linha[32], linha[33], linha[34], linha[50]]
        i = 0
        while i < len(notas):
            if notas[i] == " " or notas[i] == "":
                notas[i] = 0
            else:
                notas[i] = float(notas[i])
                i += 1
        dict = {
            "inscricao": linha[0],
            "idade": linha[2],
            "Sexo": linha[3],
            "Cor": linha[5],
            "Nacionalidade": linha[9],
            "Treineiro": linha[11],
            "Municipio": linha[20],
            "estado": linha[22],
            "NotaCN": notas[0],
            "NotaCH": notas[1],
            "NotaLC": notas[2],
            "NotaMT": notas[3],
            "NotaRedacao": notas[4]
        }
        aluno = Aluno(dict)
        
        pickle.dump(aluno, database)
    j += 1
database.close()

