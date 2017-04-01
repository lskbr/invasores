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


from video import *

import naleatorios

#import temporizador


#tcolide = temporizador.Temporizador("colide.log",[], "Colisao com Colliderect")

#tcolisoes = temporizador.Temporizador("lista.log",["N"], "Colisao de objetos")


# Verifica a colisao de dois retangulos
def colide(a,b):
    #tcolide.inicio()
    ##ret = a.colliderect(b)

    ##return ret
    if a[0]>b[0]:
        a,b = b,a
    if a[2]>b[0] and (a[2]>b[0] or a[2]>b[2]):
        if a[1]>b[1]:
            a,b=b,a
        if a[3]>b[1] or a[3]>b[3]:
            #tcolide.fim()
            return True
    #tcolide.fim()
    return False

class Universo:
    """
        Classe Universo
        ============
        Responsável pela manutenção do conjunto de objetos do jogo.
        Esta classe varre sua lista de objetos, chamando o método de respiração
        de cada objeto, rotina de cálculo de pontos e também gerando o fundo de estrelas.
    """
    def __init__(self, dimensao):
        self.objetos = []
        self.colisoes = {}
        self.video = Video(dimensao)
        self.video.adicione(self.reconfigura_video)
        self.quadros=30
        self.largura = dimensao[0]
        self.altura = dimensao[1]
        self.score = 0
        self.calcule_pontos=None
        self.gere_estrelas()
        self.intensidade_estrelas = 0

    def reconfigura_video(self, mensagem):
        if mensagem == 0:
            # Mudança de resolução
            self.largura = self.video.dimensao[0]
            self.altura = self.video.dimensao[1]
            self.gere_estrelas()

    def gere_estrelas(self):
        self.estrelas = []
        for i in range(60):
            x = naleatorios.faixa(1, self.largura)
            y = naleatorios.faixa(1, self.altura)
            z = naleatorios.faixa(2, 6)
            rect = pygame.Rect(x,y,z,z)
            self.estrelas.append( rect )

    def adicione(self, objeto):
        self.objetos.append(objeto)
        objeto.universo=self
        if objeto.tipo is not None:
            if objeto.tipo in self.colisoes:
                self.colisoes[ objeto.tipo ].append(objeto)
            else:
                self.colisoes[ objeto.tipo ] = [ objeto ]

    def remova(self, objeto):
            if objeto.tipo is not None:
                self.colisoes[objeto.tipo].remove(objeto)
            self.objetos.remove(objeto)

    def desenhe(self, posicao, imagem):
        if posicao[0] == -1: posicao[0] = (self.largura - imagem.get_width()) /2
        if posicao[1] == -1: posicao[1] = (self.altura - imagem.get_height()) /2
        self.video.desenhe(imagem, posicao)

    def escreva(self, posicao, texto, cor, tamanho=None):
        if tamanho is not None:
            self.video.fonte(tamanho)
        imagem = self.video.texto(texto,cor)
        if posicao[0] == -1: posicao[0] = (self.largura - imagem.get_width()) /2
        if posicao[1] == -1: posicao[1] = (self.altura - imagem.get_height()) /2
        self.desenhe(posicao, imagem)

    def desenhe_fundo(self):
        self.video.limpe()
        for estrela in self.estrelas:
            intensidade = 100 + self.intensidade_estrelas * 2 % 50
            cor = [ intensidade ,intensidade , intensidade  ]
            #(255,255,100)
            pygame.draw.rect(self.video.tela, cor , estrela, 0)
            estrela[1]+=3
            if estrela[1]>self.altura:
                estrela[1]=0
            self.intensidade_estrelas = self.intensidade_estrelas + 1


    def desenhe_objetos(self):
        for objeto in self.objetos:
            if objeto.visivel:
                self.video.tela.blit(objeto.imagem, objeto.pos)
        self.teste_colisao()

    def atualize(self):
        for objeto in self.objetos:
            objeto.respire()
        self.video.atualize()

    def inicie_sincronia(self):
        self.inicio = pygame.time.get_ticks()

    def finalize_sincronia(self):
        pygame.time.delay(1000/self.quadros - (pygame.time.get_ticks() - self.inicio))

    def teste_colisao(self):
##      c = 1
##        tcolisoes.inicio( [len(self.objetos)])
##        for objetoA in self.objetos:
##            for objetoB in self.objetos[c:]:
##                if colide(objetoA.retangulo(), objetoB.retangulo()):
##                    self.score += self.calcule_pontos(objetoA,objetoB)
##            c+=1
        c=1
        #tcolisoes.inicio( [len(self.objetos)])
        colisoes = self.colisoes.keys()
        for x in range(len(colisoes)-1):
            for objetoA in self.colisoes[colisoes[x]]:
                for y in range(x+1,len(colisoes)):
                    for objetoB in self.colisoes[colisoes[y]]:
                        if colide(objetoA.retangulo(), objetoB.retangulo()):
                            self.score += self.calcule_pontos(objetoA,objetoB)
                c+=1
        #tcolisoes.fim()


