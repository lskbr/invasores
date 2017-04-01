# -*- coding: cp1252 -*-
# Invasores
# Escrito por: Nilo Menezes (nilo at nilo dot pro dot br)

#   This file is part of Invasores.
#
#   Invasores is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
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

from objetodojogo import *

# Retorna o sinal de um nimero
def sinal(x):
    if x != 0:
        return x/abs(x)
    else:
        return 1


class Nave(ObjetoDoJogo):
    """
        Classe Nave
        -----------
        Implementa a nave com aceleração vetorial (x,y)
        Faz o tratamento de colisão e evita objetos chamados "tiro"
    """
    def __init__(self, nome, pos, imagem=None, tipo="JOGADOR"):
        ObjetoDoJogo.__init__(self,nome, pos, imagem, tipo)
        self.resistencia = 300
        self.dano = 10
        self.misseis = 300

    def move(self, direcao):
        if direcao == 0:
            self.ix+=3
        elif direcao == 1:
            self.ix-=3
        elif direcao == 2:
            self.iy+=3
        elif direcao == 3:
            self.iy-=3
        if abs(self.ix) > 15:
            self.ix = sinal(self.ix) * 15
        if abs(self.iy) > 15:
            self.iy = sinal(self.iy) * 15

    def colida(self, objeto):
        if objeto.nome == "CaixaDeMisseis":
            self.misseis += objeto.carga
        elif objeto.nome == "CaixaDeResistencia":
            self.resistencia += objeto.carga
        elif objeto.nome != "tiro": #Evita colidir com os próprios mísseis
            ObjetoDoJogo.colida(self,objeto)

    def respire(self):
        ObjetoDoJogo.respire(self)
        self.pos[0] += self.ix
        self.pos[1] += self.iy
        if self.pos[0]+self.lx > self.universo.largura or self.pos[0]<0:
            if self.pos[0]<0:
                self.pos[0]=0
            else:
                self.pos[0] = self.universo.largura-self.lx
            self.ix = 0
        if self.pos[1]+self.ly > self.universo.altura or self.pos[1]<0:
            if self.pos[1]<0:
                self.pos[1]=0
            else:
                self.pos[1] = self.universo.altura-self.ly
            self.iy = 0
