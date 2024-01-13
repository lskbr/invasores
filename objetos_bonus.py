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


from objeto_do_jogo import ObjetoDoJogo


class ObjetosBonus(ObjetoDoJogo):
    """
    Classe utilizada para representar os objetos de recarga de munição ou resistência
    """

    def __init__(self, nome, pos, imagem=None, tipo="INIMIGO"):
        super().__init__(nome, pos, imagem, tipo)
        self.iy = 250
        self.ix = 0
        self.resistência = 1000
        self.dano = 0
        self.carga = 0

    def respire(self, dt: float = 1.0):
        super().respire(dt)
        self.pos[1] += self.iy * dt
        if self.pos[1] > self.universo.altura:
            self.resistência = 0
            self.visível = 0
            try:
                self.universo.objetos.remove(self)
            except Exception:
                pass

    def colida(self, objeto):
        if objeto.nome == "Nave":
            self.resistência = 0
