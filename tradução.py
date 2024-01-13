#   This file is part of Invasores.
#
#   Invasores is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 3 of the License, or
#   (at your option) any later version.
#
#   Invasores is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Invasores; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA


from typing import Dict


class Traducao:
    lingua = "pt"
    dicionario: Dict[str, str] = {}

    def __init__(self, prefixo):
        self.lingua = prefixo
        self.carregaDicionario("lang/%s.lang" % self.lingua)

    def carregaDicionario(self, nome):
        with open(nome, "r", encoding="utf-8") as f:
            for e in f.readlines():
                x = e.split("=")
                self.dicionario[x[0]] = x[1].rstrip()

    def pega(self, chave):
        return self.dicionario[chave]


dic = None


def pega(chave):
    return dic.pega(chave)


def dicionario(lingua):
    global dic
    dic = Traducao(lingua)
