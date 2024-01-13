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


import pygame
import enum
import pygame.locals as pg
from typing import Tuple


class Direção(enum.Enum):
    CIMA = 3
    BAIXO = 2
    DIREITA = 0
    ESQUERDA = 1


class Posicao2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, ix, iy):
        self.x += ix
        self.y += iy

    def tuple(self):
        return (self.x, self.y)


class ObjetoDoJogo:
    """
    Implementa os objetos do universo.
    Um objeto do jogo representa uma imagem que será desenhada a cada frame.
    Para mudar o estado do objeto, o universo chama o método :py:meth:`respire`
    a cada frame.

    Quando dois objetos colidem, o valor de dano é utilizado para subtrair
    um valor da resistência do outro objeto.

    Quando a resistência chega a zero, o objeto é removido do universo
    """

    def __init__(self, nome, pos, imagem=None, tipo=None, posição_centro=False):
        #: nome é utilizada para identificar um grupo de objetos
        self.nome = nome
        #: pos é a posição inicial do objeto
        self.pos = pos
        if imagem is not None:
            self.imagem = imagem
        else:
            #: lx é a largura da imagem em pontos
            self.lx = 0
            #: ly é a altura da imagem em pontos
            self.ly = 0
            self.__imagem = None
        if posição_centro:
            self.pos[0] -= self.lx // 2
            self.pos[1] -= self.ly // 2
        #: ix é o incremento x aplicado durante a respiração
        self.ix = 0
        #: iy é o incremento y aplicado durante a respiração
        self.iy = 0
        #: visível indica se o objeto deve ou não ser desenhado
        self.visível = True
        #: resistencia é o valor que quando zerado retira o objeto do jogo
        self.resistência = 0
        #: dano é o valor subtraído quando algo colide com este objeto
        self.dano = 0
        #: estado variável utilizada para controlar estados e principalmente
        #: troca de imagens
        self.estado = 0
        self.valor = 0
        #: universo aponta para o universo ao qual este objeto pertence
        #: seu valor é setado pela classe Universo no momento da inclusão
        self.universo = None
        self.tipo = tipo
        self.rect = self.makeRect()

    @property
    def imagem(self):
        """Bitmap usado para desenhar este objeto"""
        return self.__imagem

    @imagem.setter
    def imagem(self, imagem):
        #: imagem é a figura que representara este objeto.
        self.__imagem = imagem
        self.__imagem.set_colorkey(self.imagem.get_at((0, 0)), pg.RLEACCEL)
        self.lx = self.__imagem.get_width()
        self.ly = self.__imagem.get_height()

    def __str__(self):
        return "[%s] x = %d y = %d ix = %d iy=%d res=%d dano=%d\nL=%d\nA=%d" % (
            self.nome,
            self.pos[0],
            self.pos[1],
            self.ix,
            self.iy,
            self.resistência,
            self.dano,
            self.lx,
            self.ly,
        )

    def respire(self, dt=1.0):
        """
        Chamado a cada frame. Utilizado para modificar o estado do objeto.
        """
        if self.resistência <= 0:
            if self.universo is not None:
                self.universo.remova(self)
        self.rect = self.makeRect()

    def carregue_imagem(self, nome: str) -> None:
        self.imagem = pygame.image.load(nome).convert()

    def move(self, direcao: Direção):
        """
        Move o objeto, na direção indicada.
        A implementação deste método é responsável por fazer os ajustes de velocidade
        e posição necessários.
        """
        pass

    def colida(self, objeto):
        """Chamado quando dois objetos colidem no jogo.
        Para evitar que os inimigos colidam entre si, apenas objetos com nomes
        diferentes podem colidir entre si.

        Em caso de colisão, retira da resistência do objeto atual o dano
        causado pelo outro objeto.
        """
        if objeto.nome != self.nome:
            self.resistência -= objeto.dano

    def makeRect(self) -> pygame.Rect:
        """Retorna um retângulo com as dimensões deste objeto"""
        return pygame.Rect(self.pos[0], self.pos[1], self.lx, self.ly)

    def retangulo(self) -> Tuple[int, int, int, int]:
        return (self.pos[0], self.pos[1], self.pos[0] + self.lx, self.pos[1] + self.ly)
