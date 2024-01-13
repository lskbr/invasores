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

import pygame.locals as pg
from typing import Dict, Tuple

pygame.init()
pygame.font.init()

imagens: Dict[str, object] = {}

modos = [[640, 480], [800, 600], [1024, 768], [1680, 1050], [1920, 1080]]

tela = None


def carregue(nome, local):
    global imagens, tela
    if nome not in imagens:
        imagens[nome] = pygame.image.load(local).convert(tela)
    return imagens[nome]


def imagem(nome):
    global imagens
    return imagens[nome]


class Imagem:
    def __init__(self, nome, local):
        self.carregue_imagem(nome, local)

    def ponto_croma(self, x, y):
        self.imagem.set_colorkey(self.imagem.get_at((x, y)), pg.RLEACCEL)

    def carregue_imagem(self, nome, local):
        self.imagem = carregue(nome, local)
        self.lx = self.imagem.get_width()
        self.ly = self.imagem.get_height()

    def altura(self):
        return self.ly

    def largura(self):
        return self.lx


class Video:
    def __init__(self, dimensao, tela_cheia=False):
        self.notifica = []
        self.modo(dimensao, tela_cheia)
        self.ifonte = pygame.font.Font(None, 24)
        self.modo_atual = 2

    def adicione(self, funcao):
        self.notifica.append(funcao)

    def notifique(self, mensagem):
        for m in self.notifica:
            m(mensagem)

    def modo(self, dimensao, tela_cheia=None):
        global tela
        self.dimensao: Tuple[int, int] = dimensao
        if tela_cheia is None:
            tela_cheia = self.tela_cheia
        else:
            self.tela_cheia = tela_cheia
        flags = pg.DOUBLEBUF | pg.HWSURFACE
        if tela_cheia:
            flags = flags | pg.FULLSCREEN
        self.tela = pygame.display.set_mode(dimensao, flags)
        tela = self.tela
        self.notifique(0)

    def proximo_modo(self):
        self.modo_atual = (self.modo_atual + 1) % len(modos)
        self.modo(modos[self.modo_atual])

    def anterior_modo(self):
        self.modo_atual -= 1
        if self.modo_atual < 0:
            self.modo_atual = len(modos) - 1
        self.modo(modos[self.modo_atual])

    def faz_tela_cheia(self, sim=None):
        if sim is None:
            sim = ~self.tela_cheia
        self.modo(self.dimensao, sim)

    def atualize(self):
        pygame.display.flip()

    def limpe(self, cor=(0, 0, 0, 0)):
        self.tela.fill(cor)

    def desenhe(self, imagem, posicao):
        self.tela.blit(imagem, posicao)

    def fonte(self, tamanho):
        self.ifonte = pygame.font.Font(None, tamanho)

    def texto(self, mensagem, cor):
        imagem = self.ifonte.render(mensagem, True, cor)
        return imagem

    def titulo(self, nome):
        pygame.display.set_caption(nome)

    def icone(self, imagem):
        pygame.display.set_icon(imagem)

    def rel_x(self, x: float) -> int:
        return int(x * self.dimensao[0])

    def rel_y(self, y: float) -> int:
        return int(y * self.dimensao[1])
