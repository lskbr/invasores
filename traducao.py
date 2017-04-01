# -*- coding: cp1252 -*-

class traducao:
    lingua = "pt"
    dicionario = {}
    def __init__(self, prefixo):
        self.lingua = prefixo
        self.carregaDicionario("lang/%s.lang" % self.lingua)

    def carregaDicionario(self, nome):
        f =open(nome,"r")

        for e in f.readlines():
            x = e.split("=")
            self.dicionario[x[0]] = x[1].rstrip()
        f.close()

    def pega(self, chave):
        return self.dicionario[chave]

dic = None


def pega(chave):
    global dic
    return dic.pega(chave)

def dicionario(lingua):
    global dic
    dic = traducao(lingua)

