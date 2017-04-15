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

import pygame.mixer
import naleatorios


from objetodojogo import *

import som


class Alienigena(ObjetoDoJogo):
    alienigenas_vivos = 0

    def __init__(self, nome, pos, imagem, tipo="INIMIGO"):
        super().__init__(nome, [pos[0], pos[1] - 200], imagem, tipo)
        self.iy = 3 + naleatorios.faixa(0, 5)
        self.ix = 3 + naleatorios.faixa(0, 5)
        self.posical_final = pos[1]
        self.resistencia = 50
        self.dano = 50
        self.valor = 10
        self.script_movimento = None
        self.pos_script = 0
        self.qmov = 0
        Alienigena.alienigenas_vivos += 1

        som.carregue("ALIENIGENA_EXP", "sons/boom.wav")

    def move(self, direcao):
        pass

    def set_script(self, script):
        self.script_movimento = script
        self.ix = self.script_movimento[self.pos_script][0]
        self.iy = self.script_movimento[self.pos_script][1]

    def respire(self):
        super().respire()
        if self.resistencia <= 0:
            som.reproduza("ALIENIGENA_EXP")
            Alienigena.alienigenas_vivos -= 1

        if self.pos[1] < self.posical_final:
            self.iy = 10
        else:
            if self.iy == 10:
                self.iy = self.script_movimento[self.pos_script][1]
        if self.script_movimento is not None:
            self.qmov += 1
            if self.qmov >= self.script_movimento[self.pos_script][2]:
                self.pos_script += 1
                self.qmov = 0
                self.pos_script = self.pos_script % len(self.script_movimento)
                self.ix = self.script_movimento[self.pos_script][0]
                self.iy = self.script_movimento[self.pos_script][1]

        self.pos[0] += self.ix
        self.pos[1] += self.iy

        if self.pos[0] + self.lx > self.universo.largura or self.pos[0] < 0:
            if self.pos[0] < 0:
                self.pos[0] = 0
            else:
                self.pos[0] = self.universo.largura - self.lx
            self.ix *= -1
        if self.pos[1] + self.ly > self.universo.altura:  # or self.pos[1]<0:
            self.pos[1] = self.universo.altura - self.ly
            if self.iy == 0:
                self.iy = 2
            self.iy *= -1
