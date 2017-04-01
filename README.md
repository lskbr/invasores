# Invasores

Abaixo a página original da Wiki, portada para o GitHub.

O projeto continua vivo. A versão atual foi testada com Python 3.6.


## Situação do Projeto

Mudanças estão sendo feitas para a realização da versão 1.0. Veremos muitas versões 0.9x por que o target da versão 1.0 é possuir fases. O jogo foi planejado para ter 5 fases. Otimizações ainda estão pendentes.

## Instalação

Faça o download do jogo no GitHub.

Invasores utiliza Python e PyGame sendo multiplataforma por definição. O jogo já foi testado nas seguintes plataformas:

* Instalação Windows

* Instalação Linux

* Instalação Mac OS X

* Instalação FreeBSD

## Ajuda

O Invasores nasceu de um grupo de amigos programadores. Infelizmente ninguém sabia desenhar. Se você é um artista gráfico ou entusiasta e gostaria de ver sua arte no jogo, não hesite em me contactar. LSK-BR
Isto é sério, programas livres são feitos pela e para a comunidade. Existem vários planos para Invasores parados por falta de desenhistas e pessoas que possam contribuir com sons e efeitos.

## Implementação

Invasores foi inteiramente desenvolvido utilizando-se Python e Pygame.

A implementação atual divide o jogo num loop de eventos principal e em várias classes. Basicamente, o jogo é composto de uma instância da classe Universo, populada por instâncias de objeto do jogo. Como o objetivo era fazer o jogo mais rápido que os demais, diversos assassinatos em relação a otimização e organização de código/uso de OO foram cometidas. Com o tempo, vários problemas foram resolvidos e as classes foram isoladas em arquivos independentes.

Diversas mudanças estão ocorrendo no código. Verifique o GIT.

### Metas

Para a versão 1.0, a principal meta seria a divisão do jogo em fases.
No entanto, outras metas surgiram antes disso:

* Detecção de colisão fina, com quadrados internos
* Desacoplar o jogo do loop principal
* Redividir os módulos
* Controles: otimizar, permitir customização
* Score em barra
* Log de eventos, permitir playback e save-games
* Inimigos que atiram, com inteligência, linha de visão
* Obstáculos
* Menu
* Textos introdutórios
* Gravar em filme
* Pacotes .deb, .rpm, .ebuild, ports e .exe
* 2 jogadores
* Versão em rede
* Novas armas
* Aumentar a equipe

## História

O jogo começou a ser desenvolvido em 2002, quando um grupo de colegas da Fundação Paulo Feitoza resolveu fazer jogos. Eu criei um grupo no Yahoo, chamado Gamessa (07/02/2002).

Como era nosso primeiro projeto, publicamos regras e as esperanças foram grandes. Várias pessoas contribuiram para o grupo, mas na realidade jogo nenhum surgira.

Em 2003, a FPF começou a trabalhar com J2ME e com isso mais pessoas se juntaram ao grupo. Começamos então a discutir em que linguagem fazer o jogo. Abrimos votação e não chegamos a nenhum consenso. Para resolver este problema, cada um escolheu a linguagem que mais gosta e um projeto piloto. O resultado seria avaliado para a escolha final do grupo. Assim nasceu o Invasores.

Eu escolhi Python e fiz o primeiro release, a versão 0.5, em 22/09/2003. De lá para cá, o jogo melhorou bastante, principalmente os gráficos e a própria engine. Observando o processo de desenvolvimento, fica claro que o uso da Pygame foi melhorando com o tempo, a cada versão novas funcionalidades da biblioteca foram sendo utilizadas.

Em 2005, um processo de divulgação foi iniciado, visando atrair colaboradores. Invasores é cadastrado no diretório de software da FSF [1]. Todo lançamento é divulgado também no Freshmeat [2]. Uma notícia também foi divulgada no Notícias Linux [3]. Também houve uma apresentação sobre o jogo no III ESLAM (Encontro de Software Livre do Amazonas) que poder ser baixada PythonEPygame.pdf.

Ainda há muito por vir...

## Python & Pygame

Python foi escolhida por ser fácil de usar e de prototipar. Eu já havia tentado fazer muita coisa em DirectX com o Visual C++ e em Delphi. Além disso, criar um jogo que só rodava em Windows gerava um problema ideológico muito grande para um defensor do Linux. O problema é que não era tão divertido. Com Python a prototipação ficou mais rápida e a solução é multiplataforma.

Eu já programava em Python antes, utilizando-a como linguagem script no Linux, para automatizar tarefas repetitivas do sistema. Pygame permitiu a velocidade que eu precisava com a Linguagem que eu havia escolhido.

## Equipe

Atualmente a equipe é composta por: Nilo Menezes - LSKBR Programador, sonoplasta, desenhista, autor da história, webmaster deste site, tradutor, etc.

## Agradecimentos

Não poderia faltar uma série de agradecimentos:

* Lúis Braga - por emprestar seus filhos e os ensinar a jogar o Invasores.

* Edson César - por emprestar o notebook e deixar eu instalar o Invasores no Mac OS X.

* Clebson Derivan - por instalar e testar o jogo no OpenBSD.

* Pablo Godoy - tradução para espanhol.

* Xavier Ricco - tradução para francês.

## Pendências do site

* Trocar as imagens

* Adicionar mais informações sobre o projeto

* Links para download
