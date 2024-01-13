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

import som


class Laser(ObjetoDoJogo):
    """
    Implementa os misseis do jogo.
    """

    def __init__(self, nome, pos, imagem=None, tipo="JOGADOR"):
        ObjetoDoJogo.__init__(self, nome, pos, imagem, tipo)
        self.velocidade = 1000.0
        self.resistência = 10
        self.dano = 50
        self.snd_disparo = som.carregue("LASER_DISPARO", "sons/missile.wav")
        if som.canais("LASER_DISPARO") < 4:
            self.som = som.reproduza("LASER_DISPARO")

    def move(self, direcao):
        pass

    def respire(self, dt: float = 1.0):
        super().respire()
        self.pos[1] -= self.velocidade * dt
        if self.pos[1] < 0:
            self.visível = False
            try:
                self.universo.remova(self)
            except Exception:
                pass

    def colida(self, objeto):
        if objeto.nome != "Nave":  # Evita colidir com a nave
            super().colida(objeto)
