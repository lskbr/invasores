#!/usr/bin/python
# Invasores
# Escrito por: Nilo Menezes (nilo at nilo dot pro dot br)
# Data: 21 de Setembro de 2003
# Versão 0.5 - 22/09/2003
#               Funcionamento básico
# Versão 0.6 - 23/09/2003
#               Ajuste e comentários
#               Adição de som
#               Melhoria das rotinas de impresão
#               Bugs de fechamento corrigidos
#               Tratamento de eventos melhorados
# Versão 0.7 - 24/09/2003
#               Melhoria nos gráficos
#               Acentuação do texto: contribuição de Luís Braga (SciTE)
#               Imagem de título e fim feitas no GIMP
#               Novos gráficos
#               Recarga de Mísseis
#               Recarga de Resistência
#               Nivel de dificuldade progressivo (mais inimigos a cada segundo a cada 10 segundos) :-)
#               Redutor de tiro (só se dispara uma vez a cada 3 frames ou 1/10 s
# Versão 0.8 -  12/04/2004
#               Suporte à Joystick (aceleracao fixa)
#               Suporte à Mouse (aceleracao variavel - max 15)
#               ESC sai
#               M misses (+1000)
#               R resistencia (+1000)
# Versão 0.9 - 05/03/2005
#               # Fazendo # Limpeza no código
#               # Fazendo # Isolamento da SDL em classes especificas
#               Divisão das classes em vários arquivos
#               # Fazendo # Classe de recursos (som e imagem)
#               Correção do bug de Joystick [1157541]
#               Correção do bug de Som (para micros sem som) [1157542]
#               Correção de erro de path no Linux [1157558]
#               * - Alterna FullScreen
#               + - Próximo modo de vídeo
#               - - Modo de vídeo anterior
#               Estrelas cintilantes
# Versão 0.9.1 - 12/11/2006
#              Controlador de jogo implementado
#              Resolvido bug de controle com mouse
#              Melhor jogabilidade
#              Resolvido bug ao iniciar nova partida
#              Primeiros testes com traducao
#              Implemenaçao basica de fases
# Versão 0.9.2 - 17/11/2006
#              Adicionado espanhol e francês a lista de traduçao
# Versão 0.9.3 - 04/2007
# Versão 0.9.4 - 24/11/2007
#              Modificada posição inicial das naves
# Versão 0.9.9 - 01/04/2017
#              Migração para Python 3.6 e GitHub
# Versão 0.9.10b - 12/01/2024
#              Migração para Python 3.12
#              Migração para pygame-ce
#              Formatação do código, limpeza e conformidade a pep-8
#              Resolução atualizada para começar com 1024x768 e novo modo HD
#              Atualização da Licença para GPL v3.0
#              13/01/2024
#              Refatoração, variáveis em português
#              Animação e movimentos baseada no delta t
#              Fases movidas da classe do jogo para um arquivo a parte.

# TODO: limpar o código
# TODO: reprojetar a engine de controle
# TODO: introduzir variabilidade de movimentos nos aliens
# TODO: criar telas de configuração
# TODO: níveis de dificuldade (fases)
# TODO: high score
# TODO: campo de força
# TODO: novas armas
# TODO: novos inimigos - boss

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

# Módulos do PyGame

import pygame
import pygame.joystick
import pygame.locals as pg

# Módulos do Python


# Módulos do jogo
import tradução
import video
import naleatorios
import fases

from universo import Universo

from nave import Nave
from objetos_bonus import ObjetosBonus
from laser import Laser
from alienigena import Alienigena
from score import ScoreComFPS, Texto
from objeto_do_jogo import Direção


class Invasores:
    """
    Esta classe é responsável pelo jogo em si.
    Toda customização deve ser feita aqui
    """

    def __init__(self, tela):
        self.tamanho = tela
        self.eventos = {}
        self.comandos = {}
        self.universo = Universo(tela)
        self.video = self.universo.video
        self.carregue_imagens()
        self.sair = None
        self.jogador = Nave(
            "Nave",
            pos=[self.video.rel_x(0.5), self.video.rel_y(0.8)],
            imagem=self.iJogador,
            posicao_centro=True,
        )
        self.placar = ScoreComFPS("Placar", [0, 0], self.universo)
        self.placar.jogador = self.jogador
        self.universo.quadros = 60
        self.universo.calcule_pontos = self.calcula_pontos
        self.video.titulo("Invasores")
        self.video.icone(video.carregue("ICONE", "img/nave2.bmp"))
        self.fases = (fases.fase1, fases.fase2)
        self.nova_partida()
        self.inicializa_joystick()
        self.sensibilidade_mouse = 5
        self.inicializa_eventos()
        self.inicializa_comandos()

    def inicializa_joystick(self):
        try:
            pygame.joystick.init()
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
        except Exception:
            print("No joystick detected")

    def carregue_imagens(self):
        self.iJogador = video.carregue("NAVE", "img/nave.png")
        self.iMissil = video.carregue("TIRO", "img/laser.png")
        self.iInimigo = video.carregue("INIMIGO", "img/inimigo.png")
        self.iCaixaDeMisseis = video.carregue("CMISSIL", "img/caixademisseis.png")
        self.iCaixaDeResistencia = video.carregue(
            "CRESITENCIA", "img/caixaderesistencia.png"
        )
        self.logo = video.Imagem("LOGO", "img/Invasoreslogo.png")
        self.logo.ponto_croma(0, 0)
        self.fim_de_jogo = video.Imagem("FIMDEJOGO", "img/fimdejogo.png")
        self.fim_de_jogo.ponto_croma(0, 0)

    def mostra_texto(self, ttexto):
        texto = Texto("Texto", [-1, -1], ttexto, 80, 3, self.universo, (255, 0, 0))
        self.universo.adicione(texto)

    def cria_alienigena(self, xi, yi, coluna, linha, script, xl=60, yl=60):
        for y in range(linha):
            for x in range(coluna):
                a = Alienigena("Inimigo", [xi + x * xl, yi + y * yl], self.iInimigo)
                a.set_script(script)
                self.universo.adicione(a)

    def para_tempo_script(self, motivo):
        self.estado_tempo_script = motivo

    def incrementa_tempo_script(self):
        if self.estado_tempo_script == 0:
            self.tempo_script += 1
        elif self.estado_tempo_script == 1:
            if Alienigena.alienigenas_vivos == 0:
                self.estado_tempo_script = 0

    def nova_partida(self):
        self.jogador.resistência = 300
        self.jogador.misseis = 300
        self.jogador.pos = [400, 400]
        self.jogador.ix = 0
        self.jogador.iy = 0
        self.universo.score = 0
        self.universo.objetos = []
        self.universo.colisoes = {}
        self.universo.adicione(self.jogador)
        self.universo.adicione(self.placar)
        self.placar.respire()
        self.fase = 0
        self.frame = 0
        self.tempo_script = 0
        Alienigena.alienigenas_vivos = 0

    def calcula_pontos(universo, a, b):
        if a.nome != b.nome:
            a.colida(b)
            b.colida(a)
            return a.valor + b.valor
        else:
            return 0

    def atira(self, evento=None):
        if self.jogador.misseis > 0 and self.frame - self.ultimo_tiro >= 5:
            self.universo.adicione(
                Laser(
                    "tiro",
                    [self.jogador.pos[0] + 5, self.jogador.pos[1] - 30],
                    self.iMissil,
                )
            )
            self.universo.adicione(
                Laser(
                    "tiro",
                    [
                        self.jogador.pos[0] + self.jogador.lx - 15,
                        self.jogador.pos[1] - 30,
                    ],
                    self.iMissil,
                )
            )
            self.jogador.misseis -= 2
            self.ultimo_tiro = self.frame

    def cria_munição(self, carga=100):
        caixa_m = ObjetosBonus(
            "CaixaDeMisseis",
            [naleatorios.faixa(self.tamanho[0]), 10],
            self.iCaixaDeMisseis,
        )
        caixa_m.carga = carga
        self.universo.adicione(caixa_m)

    def cria_resistência(self, carga=100):
        caixa_r = ObjetosBonus(
            "CaixaDeResistencia",
            [naleatorios.faixa(self.tamanho[0]), 10],
            self.iCaixaDeResistencia,
        )
        caixa_r.carga = carga
        self.universo.adicione(caixa_r)

    def tela_inicial(self):
        self.universo.desenhe_fundo()
        self.universo.desenhe([-1, -1], self.logo.imagem)
        self.universo.escreva(
            [-1, 450], tradução.pega("pressionequalquertecla"), (255, 255, 0), 24
        )
        self.universo.escreva(
            [-1, 200],
            "[P]Português [E]English [S]Spañol [F]Français",
            (255, 255, 0),
            24,
        )
        self.universo.atualize()
        while True:
            for event in pygame.event.get():
                if event.type == pg.QUIT:
                    return 1
                if event.type == pg.KEYDOWN or event.type == pg.JOYBUTTONDOWN:
                    teclas = pygame.key.get_pressed()
                    if teclas[pg.K_p]:
                        tradução.dicionario("pt_br")
                    if teclas[pg.K_e]:
                        tradução.dicionario("en")
                    if teclas[pg.K_s]:
                        tradução.dicionario("es")
                    if teclas[pg.K_f]:
                        tradução.dicionario("fr")
                    self.nova_partida()
                    return 0

    def tela_fim_de_jogo(self):
        self.universo.desenhe([-1, -1], self.fim_de_jogo.imagem)
        self.universo.escreva(
            [-1, 450], tradução.pega("pressionexour"), (255, 255, 0), 24
        )
        self.universo.atualize()
        while True:
            for event in pygame.event.get():
                if event.type == pg.QUIT:
                    return True
                if event.type == pg.KEYDOWN:
                    teclas = pygame.key.get_pressed()
                    if teclas[pg.K_r]:
                        return 0
                    elif teclas[pg.K_x]:
                        return True
                if event.type == pg.JOYBUTTONDOWN:
                    if event.button % 2 == 0:
                        return False
                    else:
                        return True

    def move_mouse(self, evento):
        if evento.rel[0] < -self.sensibilidade_mouse:
            self.jogador.move(Direção.ESQUERDA)
        elif evento.rel[0] > self.sensibilidade_mouse:
            self.jogador.move(Direção.DIREITA)
        if evento.rel[1] < -self.sensibilidade_mouse:
            self.jogador.move(Direção.CIMA)
        elif evento.rel[1] > self.sensibilidade_mouse:
            self.jogador.move(Direção.BAIXO)
        if evento.buttons[0] == 1:  # and c % 3 == 0:
            self.atira(evento)

    def move_joystick(self, event):
        if event.axis == 0:
            if event.value > 0.0:
                self.jogador.ix = 5
            elif event.value < -1.0:
                self.jogador.ix = -5
        elif event.axis == 1:
            if event.value > 0.0:
                self.jogador.iy = 5
            elif event.value < -1.0:
                self.jogador.iy = -5

    def inicializa_eventos(self):
        self.eventos[pg.MOUSEBUTTONDOWN] = self.atira
        self.eventos[pg.MOUSEMOTION] = self.move_mouse
        self.eventos[pg.JOYAXISMOTION] = self.move_joystick
        self.eventos[pg.MOUSEBUTTONDOWN] = self.atira
        self.eventos[pg.QUIT] = self.saida
        self.eventos[pg.JOYBUTTONDOWN] = self.atira

    def esquerda(self):
        self.jogador.move(Direção.ESQUERDA)

    def direita(self):
        self.jogador.move(Direção.DIREITA)

    def cima(self):
        self.jogador.move(Direção.CIMA)

    def baixo(self):
        self.jogador.move(Direção.BAIXO)

    def aumenta_misseis(self):
        """Cheat para aumentar o número de mísseis do jogador em 1000"""
        self.jogador.misseis += 1000

    def aumenta_resistencia(self):
        """Cheat para aumentar a resistência do jogador em 1000 pontos"""
        self.jogador.resistência += 1000

    def inicializa_comandos(self):
        self.comandos[pg.K_LEFT] = self.esquerda
        self.comandos[pg.K_RIGHT] = self.direita
        self.comandos[pg.K_UP] = self.cima
        self.comandos[pg.K_DOWN] = self.baixo
        self.comandos[pg.K_SPACE] = self.atira
        self.comandos[pg.K_x] = self.saida
        self.comandos[pg.K_ESCAPE] = self.saida
        self.comandos[pg.K_m] = self.aumenta_misseis
        self.comandos[pg.K_r] = self.aumenta_resistencia
        self.comandos[pg.K_KP_PLUS] = self.video.proximo_modo
        self.comandos[pg.K_PLUS] = self.video.proximo_modo
        self.comandos[pg.K_EQUALS] = self.video.proximo_modo
        self.comandos[pg.K_KP_MINUS] = self.video.anterior_modo
        self.comandos[pg.K_MINUS] = self.video.anterior_modo
        self.comandos[pg.K_KP_MULTIPLY] = self.video.faz_tela_cheia
        self.comandos[pg.K_ASTERISK] = self.video.faz_tela_cheia
        self.comandos[pg.K_8] = self.video.faz_tela_cheia

    def saida(self, evento=None):
        self.sair = True

    def carrega_fase(self):
        self.frame = 0
        self.estado_tempo_script = 0
        self.tempo_script = 0
        self.ultimo_tiro = 0
        self.fases[self.fase](self)

    def avanca_fase(self):
        self.fase += 1
        if self.fase == len(self.fases):
            return False
        else:
            self.carrega_fase()
            return True

    def repeticao_do_jogo(self):
        """
        Loop principal do jogo.
        Apaga a tela, carrega a fase e repete até o jogador morrer ou escolher para sair.

        """
        self.universo.desenhe_fundo()
        self.sair = False
        self.carrega_fase()
        pos_script = 0
        while self.jogador.resistência > 0 and not self.sair:
            self.frame += 1
            self.incrementa_tempo_script()
            while True:
                event = pygame.event.poll()
                if event.type == pg.NOEVENT:
                    break
                if event.type in self.eventos:
                    self.eventos[event.type](event)

            # Pega todas as teclas pressionadas no momento
            teclas = pygame.key.get_pressed()
            # Verifica se cada tecla com comando foi pressionada
            for comando in self.comandos.keys():
                if teclas[comando]:
                    # Chama o gerenciador da tecla
                    self.comandos[comando]()
            # Processa as instruções da fase
            tempo, funcao, *parametros = self.script[pos_script]
            if self.script[pos_script][0] <= self.tempo_script:
                if funcao:
                    funcao(*parametros)
                pos_script += 1
                if pos_script == len(self.script):
                    pos_script = 0
                    if not self.avanca_fase():
                        return 0

            self.universo.desenhe_fundo()
            self.universo.desenhe_objetos()
            self.universo.atualize()
            self.universo.finalize_sincronia()

        self.universo.desenhe_fundo()
        self.placar.respire()
        self.universo.desenhe_objetos()
        self.universo.atualize()
        return self.sair


# Jogo - Principal
def jogo():
    """
    Cria o loop do jogo. Alterna entre os três estados principais do invasores:

    - :meth:`Invasores.tela_inicial`

    - :meth:`Invasores.repeticao_do_jogo`

    - :meth:`Invasores.tela_fim_de_jogo`

    O usuário pode pressionar X para sair em qualquer tela.
    """
    try:
        # Cria o jogo em uma janela de 1024x768
        jogo = Invasores([1024, 768])
        # Esconde o mouse
        pygame.mouse.set_visible(0)
        # Loop principal do Jogo
        while True:
            if jogo.tela_inicial():
                break
            # Ativa captura eventos
            pygame.event.set_grab(1)
            jogo.nova_partida()
            if jogo.repeticao_do_jogo():
                break
            # Desativa captura eventos
            pygame.event.set_grab(0)
            if jogo.tela_fim_de_jogo():
                break
    finally:
        pygame.display.quit()


if __name__ == "__main__":
    # Carrega o dicionário padrão, no caso, Português do Brasil
    tradução.dicionario("pt_br")
    # traducao.dicionario("en")

    jogo()
    # profile.run("jogo()")
