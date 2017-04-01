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

class ObjetosBonus(ObjetoDoJogo):
    """
        Classe utilizada para representar os objetos de recarga de munição ou resistência
    """
    def __init__(self, nome, pos, imagem=None,tipo="INIMIGO"):
        ObjetoDoJogo.__init__(self,nome, pos, imagem,tipo)
        self.iy = 5
        self.ix = 0
        self.resistencia = 1000
        self.dano = 0
        self.carga = 0
        
    def respire(self):
        ObjetoDoJogo.respire(self)
        self.pos[1] += self.iy
        if self.pos[1]>self.universo.altura:
            self.resistencia = 0
            self.visivel = 0
            try:
                self.universo.objetos.remove(self)
            except:
                pass
                
    def colida(self, objeto):
        if objeto.nome == "Nave":
            self.resistencia = 0
