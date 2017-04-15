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


import naleatorios

from video import *
from typing import List, Dict, Tuple, Callable
from objetodojogo import ObjetoDoJogo


class Universo:
    """
        Responsável pela manutenção do conjunto de objetos do jogo (:py:class:`objetodojogo.ObjetoDoJogo`).
        Esta classe varre sua lista de objetos, chamando o método de respiração
        de cada objeto, rotina de cálculo de pontos e também gerando o fundo de estrelas.

    """
    def __init__(self, dimensao: Tuple[int, int], quadros: int=60) -> None:
        """
        Inicializa o universo com valores
        :param tuple dimensao: tupla com a largura e altura da tela em pixels
        :param int quadros: quadros por segundo
        """
        #: lista de objetos do jogo
        self.objetos = []  # type: List[ObjetoDoJogo]
        self.colisoes = {}  # type: Dict[str,List]
        self.video = Video(dimensao)
        self.video.adicione(self.reconfigura_video)
        self.quadros = quadros
        self.largura = dimensao[0]
        self.altura = dimensao[1]
        self.score = 0
        self.calcule_pontos = None  # type: Callable[[ObjetoDoJogo, ObjetoDoJogo], int]
        self.gere_estrelas()
        self.intensidade_estrelas = 0
        self.clock = pygame.time.Clock()

    def reconfigura_video(self, mensagem: int):
        """Usado para trocar de resolução. Atualiza os limites do universo,
           gera novas estrelas."""
        if mensagem == 0:
            # Mudança de resolução
            self.largura = self.video.dimensao[0]
            self.altura = self.video.dimensao[1]
            self.gere_estrelas()

    def gere_estrelas(self) -> None:
        """Gera aleatoriamente as estrelas do fundo.
           As coordenadas x e y de cada estrela são escolhidas aleatoriamente e representão a posição da estrela.
           z é o tamanho da estrela.
        """
        self.estrelas = []  # type: pygame.Rect
        for i in range(60):
            x = naleatorios.faixa(1, self.largura)
            y = naleatorios.faixa(1, self.altura)
            z = naleatorios.faixa(2, 6)
            rect = pygame.Rect(x, y, z, z)
            self.estrelas.append(rect)

    def adicione(self, objeto: ObjetoDoJogo):
        """Adiciona um objeto à lista de desenho."""
        self.objetos.append(objeto)
        objeto.universo = self
        if objeto.tipo is not None:
            if objeto.tipo in self.colisoes:
                self.colisoes[objeto.tipo].append(objeto)
            else:
                self.colisoes[objeto.tipo] = [objeto]

    def remova(self, objeto: ObjetoDoJogo):
        """Retira um objeto da lista de desenho e da lista de colisões"""
        if objeto.tipo is not None:
            self.colisoes[objeto.tipo].remove(objeto)
        self.objetos.remove(objeto)

    def __centraliza_x(self, imagem) -> int:
        """Centraliza imagem na tela"""
        return (self.largura - imagem.get_width()) / 2

    def __centraliza_y(self, imagem) -> int:
        """Centraliza imagem verticalmente na tela"""
        return (self.altura - imagem.get_height()) / 2

    def desenhe(self, posicao: List[int], imagem):
        """Desenha a imagem na posição x, y indicada"""
        if posicao[0] == -1:
            posicao[0] = self.__centraliza_x(imagem)
        if posicao[1] == -1:
            posicao[1] = self.__centraliza_y(imagem)
        self.video.desenhe(imagem, posicao)

    def escreva(self, posicao: List[int], texto, cor, tamanho=None):
        """Escreve uma mensagem de texto na posição x, y passada.
           Se uma das posições for igual a -1, centraliza no eixo específico"""
        if tamanho is not None:
            self.video.fonte(tamanho)
        imagem = self.video.texto(texto, cor)
        if posicao[0] == -1:
            posicao[0] = self.__centraliza_x(imagem)
        if posicao[1] == -1:
            posicao[1] = self.__centraliza_y(imagem)
        self.desenhe(posicao, imagem)

    def desenhe_fundo(self):
        """Apaga a tela e desenha as estrelas"""
        self.video.limpe()
        for estrela in self.estrelas:
            intensidade = 100 + self.intensidade_estrelas * 2 % 50
            cor = [intensidade, intensidade, intensidade]
            # (255,255,100)
            pygame.draw.rect(self.video.tela, cor, estrela, 0)
            # Mode a estrela para baixo para dar ideia de movimento
            estrela.y += 3
            # Se a estrela estiver fora da tela, reposiciona na primeira linha
            if estrela.y > self.altura:
                estrela.y = 0
            self.intensidade_estrelas = self.intensidade_estrelas + 1

    def desenhe_objetos(self):
        """Desenha a lista de objetos na tela"""
        [self.video.tela.blit(objeto.imagem, objeto.pos)
            for objeto in self.objetos if objeto.visivel]
        self.teste_colisao()

    def atualize(self):
        """Atualiza o estado do jogo, chamando o método :meth:`ObjetoDoJogo.respire`
           de todos os objetos na lista de desenho."""
        [objeto.respire() for objeto in self.objetos]
        self.video.atualize()

    def finalize_sincronia(self):
        """Espera o fim do frame atual."""
        self.clock.tick_busy_loop(self.quadros)

    def teste_colisao(self):
        """Verifica se objetos de classes diferentes colidem uns com os outros"""
        colisoes = list(self.colisoes.keys())
        while colisoes:
            A = colisoes.pop()
            for objetoA in self.colisoes[A]:
                for B in colisoes:
                    for objetoB in self.colisoes[B]:
                        if objetoA.rect.colliderect(objetoB.rect):
                            self.score += self.calcule_pontos(objetoA, objetoB)
