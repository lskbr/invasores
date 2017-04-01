# -*- coding: cp1252 -*-
# Invasores
# Escrito por: Nilo Menezes (nilo at nilo dot pro dot br)

#	This file is part of Invasores.
#
#	Invasores is free software; you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation; either version 2 of the License, or
#	(at your option) any later version.
#
#	Invasores is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with Invasores; if not, write to the Free Software
#	Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import pygame.mixer

try:
    pygame.mixer.init()
    inicializado = 1
except:
    print("Sound initialization failure.")
    inicializado = 0

sons = {}

def carregue(nome,local):
  global sons
  if not sons.has_key(nome):
     try:
       sons[nome] = pygame.mixer.Sound(local)
       return sons[nome]
     except:
       return None

def reproduza(nome):
	global sons
	try:
		sons[nome].play()
	except:
		pass

def canais(nome=None):
    global sons
    if nome == None:
        try:
            return pygame.mixer.get_num_channels()
        except:
            return 0
    else:
        try:
            return sons[nome].get_num_channels()
        except:
            return 0

