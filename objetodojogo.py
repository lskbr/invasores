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

from pygame.locals import *

class ObjetoDoJogo:
    """
        Classe ObjetoDoJogo
        -------------------
        Implementa os objetos do universo.
        nome é utilizada para identificar um grupo de objetos
        pos é a posicao inicial do objeto
        imagem é a figura que representara este objeto.
        ix, iy são o incremento x e y aplicados durante a respiração
        lx, ly é a largura e altura da imagem em pontos
        dano é o valor subtraido quando algo colide com este objeto
        resistencia é o valor que quando zerado retira o objeto do jogo
        estado variável utilizada para controlar estados e principalmente
            troca de imagens
        visivel indica se o objeto deve ou não ser desenhado
        universo aponta para o universo ao qual este objeto pertence
            seu valor é setado pela classe Universo no momento da inclusão
    """
    def __init__(self, nome, pos, imagem=None, tipo=None):
        self.nome = nome
        self.pos = pos
        if imagem is not None:
            self.set_imagem(imagem)
        else:
            self.lx = 0
            self.ly = 0
        self.ix = 0
        self.iy = 0
        self.visivel = True
        self.resistencia = 0
        self.dano = 0
        self.estado = 0
        self.valor = 0
        self.universo = None
        self.tipo = tipo

    def set_imagem(self, imagem):
        self.imagem = imagem
        self.imagem.set_colorkey(self.imagem.get_at((0,0)), RLEACCEL)
        self.lx = self.imagem.get_width()
        self.ly = self.imagem.get_height()

    def __str__(self):
        return "[%s] x = %d y = %d ix = %d iy=%d res=%d dano=%d\nL=%d\nA=%d" % \
            (self.nome, self.pos[0], self.pos[1], self.ix, self.iy,
                self.resistencia, self.dano, self.lx, self.ly)

    def respire(self):
        #print "RObj %d" % self.resistencia
        if self.resistencia <=0:
            #self.universo.objetos.remove(self)
            if self.universo is not None:
                self.universo.remova(self)

    def carregue_imagem(self,nome):
        self.imagem = pygame.image.load(nome).convert()

    def move(self, direcao):
        pass

    def teste_colisao(self):
        pass

    def colida(self, objeto):
        if objeto.nome != self.nome:
            self.resistencia -= objeto.dano
            pass

    def rect(self):
        return (Rect(self.pos[0], self.pos[1], self.lx, self.ly))

    def retangulo(self):
        return (self.pos[0], self.pos[1],
                self.pos[0]+self.lx, self.pos[1]+self.ly)

