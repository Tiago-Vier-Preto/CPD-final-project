import csv
import pickle
from classes import Aluno
database = open("database.bin", "wb")
arquivo = open("microdados_enem_2021\DADOS\MICRODADOS_ENEM_2021.csv", "r")
arquivo_csv = csv.reader(arquivo, delimiter=";")

j = 0
for linha in arquivo_csv:
    if (j != 0):
        dict = {
            "inscricao": linha[0],
            "idade": linha[2],
            "Sexo": linha[3],
            "Cor": linha[5],
            "Nacionalidade": linha[9],
            "Treineiro": linha[11],
            "Municipio": linha[20],
            "estado": linha[22],
            "NotaCN": linha[31],
            "NotaCH": linha[32],
            "NotaLC": linha[33],
            "NotaMT": linha[34],
            "NotaRedacao": linha[50]
        }
        aluno = Aluno(dict)
        
        pickle.dump(aluno, database)
    j += 1
database.close()

