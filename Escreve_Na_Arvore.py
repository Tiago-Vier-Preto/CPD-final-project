import pickle
from classes import Aluno
from src.bplustree import bplus_tree

arq = open("database.bin", "rb")
tree = bplus_tree()
tree.open("./")

while True:
    try:
        offset = arq.tell()
        obj = pickle.load(arq)
        inscricao = obj.getInscricao()
        tree.insert(int(inscricao), offset)
    except (EOFError):
        break

arq.close()
