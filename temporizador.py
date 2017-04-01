import time
import sys


class Temporizador:
    def __init__(self,nome, descricao, cabecalho=""):
        self.arquivo = open(nome, "w")
        self.arquivo.write("%s - %s\n\n" % (cabecalho, time.ctime()))
        self.descricao = descricao
    
    def inicio(self,valores=[]):
        self.valores = valores
        self.tempo_i = time.time()
        
    def fim(self):
        self.tempo_f = time.time()
        linha = ""
        for x in range(len(self.descricao)):
            linha += "%s=%s " % (self.descricao[x], self.valores[x])
        self.arquivo.write(("%10.5f - " % (self.tempo_f - self.tempo_i)) + linha+"\n")
    
    def __del__(self):
        self.arquivo.close()

