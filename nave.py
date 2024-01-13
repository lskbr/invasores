# Invasores
# Escrito por: Nilo Menezes (nilo at nilo dot pro dot br)

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

import math
from objeto_do_jogo import ObjetoDoJogo, Direção


def sinal(x):
    """Retorna o sinal de um número"""
    return math.copysign(1, x)


class Nave(ObjetoDoJogo):
    """
    Implementa a nave com aceleração vetorial (x,y)
    Faz o tratamento de colisão e evita objetos chamados "tiro"
    """

    def __init__(self, nome, pos, imagem=None, tipo="JOGADOR", posicao_centro=False):
        super().__init__(nome, pos, imagem, tipo, posicao_centro)
        self.resistência = 300
        self.dano = 100
        self.misseis = 300
        self.velocidade_x = 50.0
        self.velocidade_y = 50.0
        self.max_velocidade_x = 500.0
        self.max_velocidade_y = 500.0

    def move(self, direção: Direção):
        if direção == Direção.DIREITA:
            self.ix += self.velocidade_x
        elif direção == Direção.ESQUERDA:
            self.ix -= self.velocidade_x
        elif direção == Direção.BAIXO:
            self.iy += self.velocidade_y
        elif direção == Direção.CIMA:
            self.iy -= self.velocidade_y
        if abs(self.ix) > self.max_velocidade_x:
            self.ix = math.copysign(self.max_velocidade_x, self.ix)
        if abs(self.iy) > self.max_velocidade_y:
            self.iy = math.copysign(self.max_velocidade_y, self.iy)
        # print(self.ix, self.iy)

    def colida(self, objeto):
        if objeto.nome == "CaixaDeMisseis":
            self.misseis += objeto.carga
        elif objeto.nome == "CaixaDeResistencia":
            self.resistência += objeto.carga
        elif objeto.nome != "tiro":  # Evita colidir com os próprios mísseis
            super().colida(objeto)

    def respire(self, dt):
        super().respire(dt)
        self.pos[0] += self.ix * dt
        self.pos[1] += self.iy * dt
        if self.pos[0] + self.lx > self.universo.largura or self.pos[0] < 0:
            if self.pos[0] < 0:
                self.pos[0] = 0
            else:
                self.pos[0] = self.universo.largura - self.lx
            self.ix = 0
        if self.pos[1] + self.ly > self.universo.altura or self.pos[1] < 0:
            if self.pos[1] < 0:
                self.pos[1] = 0
            else:
                self.pos[1] = self.universo.altura - self.ly
            self.iy = 0
