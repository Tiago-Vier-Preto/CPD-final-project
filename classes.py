class Aluno:
    def __init__(self, dicionario = {}):
        self.dict = dicionario
        self.arruma_valores()

    def arruma_valores(self):
        self.arruma_idade()
        self.arruma_sexo()
        self.arruma_cor()
        self.arruma_nacionalidade()
        self.arruma_treineiro()
        

    def arruma_idade(self):
        if self.dict["idade"] == "1":
            self.dict["idade"] = "Menor de 17 anos"

        elif self.dict["idade"] == "2":
            self.dict["idade"] = "17 anos"

        elif self.dict["idade"] == "3":
            self.dict["idade"] = "18 anos" 

        elif self.dict["idade"] == "4":
            self.dict["idade"] = "19 anos"

        elif self.dict["idade"] == "5":
            self.dict["idade"] = "20 anos"
        
        elif self.dict["idade"] == "6":
            self.dict["idade"] = "21 anos"

        elif self.dict["idade"] == "7":
            self.dict["idade"] = "22 anos"

        elif self.dict["idade"] == "8":
            self.dict["idade"] = "23 anos"

        elif self.dict["idade"] == "9":
            self.dict["idade"] = "24 anos"

        elif self.dict["idade"] == "10":
            self.dict["idade"] = "25 anos"
        
        elif self.dict["idade"] == "11":
            self.dict["idade"] = "Entre 26 e 30 anos"

        elif self.dict["idade"] == "12":
            self.dict["idade"] = "Entre 31 e 35 anos"

        elif self.dict["idade"] == "13":
            self.dict["idade"] = "Entre 36 e 40 anos"

        elif self.dict["idade"] == "14":
            self.dict["idade"] = "Entre 41 e 45 anos"

        elif self.dict["idade"] == "15":
            self.dict["idade"] = "Entre 46 e 50 anos"
        
        elif self.dict["idade"] == "16":
            self.dict["idade"] = "Entre 51 e 55 anos"

        elif self.dict["idade"] == "17":
            self.dict["idade"] = "Entre 56 e 60 anos"

        elif self.dict["idade"] == "18":
            self.dict["idade"] = "Entre 61 e 65 anos"

        elif self.dict["idade"] == "19":
            self.dict["idade"] = "Entre 66 e 70 anos"

        elif self.dict["idade"] == "20":
            self.dict["idade"] = "Maior de 70"
    
    def arruma_nacionalidade(self):
        if self.dict["Nacionalidade"] == "0":
            self.dict["Nacionalidade"] = "Não informado"

        elif self.dict["Nacionalidade"] ==  "1":
            self.dict["Nacionalidade"] = "Brasileiro(a)"
        
        elif self.dict["Nacionalidade"] ==  "2":
            self.dict["Nacionalidade"] = "Brasileiro(a) Naturalizado(a)"
        
        elif self.dict["Nacionalidade"] ==  "3":
            self.dict["Nacionalidade"] = "Estrangeiro(a)"

        elif self.dict["Nacionalidade"] ==  "4":
            self.dict["Nacionalidade"] = "Brasileiro(a) Nato(a), nascido(a) no exterior"
        
    def arruma_treineiro(self):
        if self.dict["Treineiro"] == "1":
            self.dict["Treineiro"] = "Sim"

        if self.dict["Treineiro"] == "0":
            self.dict["Treineiro"] = "Não"

    def arruma_sexo(self):
        if self.dict["Sexo"] == "M":
            self.dict["Sexo"] = "Masculino"

        elif self.dict["Sexo"] ==  "F":
            self.dict["Sexo"] = "Feminino"
    
    def arruma_cor(self):
        if self.dict["Cor"] == "0":
            self.dict["Cor"] = "Não Declarado"

        elif self.dict["Cor"] == "1":
            self.dict["Cor"] = "Branca"

        elif self.dict["Cor"] == "2":
            self.dict["Cor"] = "Preta"

        elif self.dict["Cor"] == "3":
            self.dict["Cor"] = "Parda"

        elif self.dict["Cor"] == "4":
            self.dict["Cor"] = "Amarela"

        elif self.dict["Cor"] == "5":
            self.dict["Cor"] = "Indígena"

        elif self.dict["Cor"] == "6":
            self.dict["Cor"] = "Não dispõe da informação"


    def getDicionario(self):
        return self.dict

    def getInscricao(self):
        return self.dict["inscricao"]

    def __str__(self):
        return f'Inscricao:{self.dict["inscricao"]}\nIdade:{self.dict["idade"]}\nSexo:{self.dict["Sexo"]}\nCor:{self.dict["Cor"]}\nNacionalidade:{self.dict["Nacionalidade"]}\nTreineiro:{self.dict["Treineiro"]}\nHumanas:{self.dict["NotaCN"]}\nNaturezas:{self.dict["NotaCH"]}\nLinguagens:{self.dict["NotaLC"]}\nMatematica:{self.dict["NotaMT"]}\nRedacao:{self.dict["NotaRedacao"]}'
