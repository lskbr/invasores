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


import pygame

import traducao
from objetodojogo import *

clock = pygame.time.Clock()


class Score(ObjetoDoJogo):
    """
        Utilizada para exibir o score do jogo.
        Implementada como um objeto normal, podendo inclusive suportar
        animação.
    """

    def __init__(self, nome, pos=[0, 0]):
        super().__init__(nome, pos)
        self.fonte = pygame.font.Font(None, 30)
        self.fonte.set_bold(True)
        self.jogador = None

    def respire(self):
        # ObjetoDoJogo.respire(self)
        self.imagem = self.fonte.render(traducao.pega("score") %
                                        (self.universo.score,
                                         self.jogador.resistencia,
                                         self.jogador.misseis),
                                        True, (255, 255, 0, 0))


class Texto(ObjetoDoJogo):
    """
        Utilizada para exibir o score do jogo.
        Implementada como um objeto normal, podendo inclusive suportar
        animação.
    """

    def __init__(self, nome, pos, texto, tamanho, tempo, universo, cor):
        ObjetoDoJogo.__init__(self, nome, pos)
        self.fonte = pygame.font.Font(None, tamanho)
        self.fonte.set_bold(True)
        self.jogador = None
        self.resistencia = tempo
        self.universo = universo
        self.texto = texto
        self.cor = cor
        self.imagem = self.fonte.render(traducao.pega(self.texto), True, self.cor)
        if self.pos == [-1, -1]:
            self.pos = [(self.universo.largura - self.imagem.get_width()) / 2,
                        (self.universo.altura - self.imagem.get_height()) / 2]

    def respire(self):
        """Decrementa a resistência a cada frame.
           Com objetivo de fazer o texto sumir após x frames"""
        self.resistencia -= 1
        super().respire()


class ScoreComFPS(Score):
    def __init__(self, nome, pos):
        super().__init__(nome, pos)

    def respire(self):
        clock.tick(60)
        self.imagem = self.fonte.render(traducao.pega("scorefps") %
                                        (self.universo.score,
                                         self.jogador.resistencia,
                                         self.jogador.misseis, clock.get_fps()),
                                        True, (255, 255, 0, 0))
