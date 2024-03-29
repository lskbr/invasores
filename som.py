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


import sys
import pygame.mixer
from typing import Dict


try:
    pygame.mixer.init()
    inicializado = 1
except Exception:
    print("Sound initialization failure.", file=sys.stderr)
    inicializado = 0

__sons: Dict[str, pygame.mixer.Sound] = {}


def carregue(nome: str, local: str):
    if nome not in __sons:
        try:
            __sons[nome] = pygame.mixer.Sound(local)
            return __sons[nome]
        except Exception:
            print(f"Erro carregando som: {nome}")


def reproduza(nome: str):
    try:
        __sons[nome].play()
    except Exception:
        print(f"Erro reproduzindo som: {nome}")


def canais(nome=None):
    try:
        if nome is None:
            return pygame.mixer.get_num_channels()
        else:
            return __sons[nome].get_num_channels()
    except Exception:
        return 0
