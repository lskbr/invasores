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

#import pygame
#import pygame.mixer

from objetodojogo import *

import som

class Laser(ObjetoDoJogo):
    """
        Classe Laser
        ------------
        Implementa os misseis do jogo.
    """

    def __init__(self, nome, pos, imagem=None, tipo="JOGADOR"):
        ObjetoDoJogo.__init__(self,nome, pos, imagem,tipo)
        self.velocidade = 15
        self.resistencia = 10
        self.dano = 50
        self.snd_disparo = som.carregue("LASER_DISPARO","sons/missile.wav")
        if som.canais("LASER_DISPARO")<4:
            self.som = som.reproduza("LASER_DISPARO")

    def move(self, direcao):
        pass

    def respire(self):
        ObjetoDoJogo.respire(self)
        self.pos[1] -= self.velocidade
        if self.pos[1]<0:
            self.visivel = False
            try:
                self.universo.remova(self)
            #self.som.stop()
            except:
               pass

    def teste_colisao(self):
        pass

    def colida(self, objeto):
        if objeto.nome != "Nave": #Evita colitir com a nave
            ObjetoDoJogo.colida(self,objeto)
