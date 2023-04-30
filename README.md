# Documentação do Detetive Bot
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

<p align="center">
  <img src="https://github.com/ViniciusHora1009/detetive_bot/blob/main/imagens/logo.png">
</p>

## Sobre o Detetive Bot

O Detetive Bot é um bot de Discord desenvolvido para que os usuários possam jogar uma versão adaptada do jogo Detetive da Estrela pelo Discord. O bot realiza tarefas esseciais para o jogo como distribuir as cartas, escolher o assassino e rolar o dado. A função de tabuleiro é feita pelo tabuleiro oficial do Detetive Bot no Roll20.

[Convidar o detetive Bot ao meu servidor](https://discord.com/api/oauth2/authorize?client_id=753686837117059162&permissions=8&scope=bot)

<h1 align="center">
  Regras
</h1>

<p align="center">
  <img img width="200" height="200" src="https://github.com/ViniciusHora1009/detetive_bot/blob/main/imagens/rules.png">
</p>

[Guia explicativo das regras](https://www.bananaquantica.com.br/como-jogar-detetive/)

<h1 align="center">
  Tabuleiro
</h1>

<p align="center">
  <img img width="200" height="200" src="https://github.com/ViniciusHora1009/detetive_bot/blob/main/imagens/table.png">
</p>

Para o tabuleiro virtual, você precisará ter uma baixar o mapa em [link](https://drive.google.com/file/d/1q1OGmuhr5y3aaVVLe-eDj1PJ0PpsSm87/view?usp=sharing). Depois deve utilizar algo serviço de tabuleiro online, como o Roll20, por exemplo. Ao usar o mapa com tabuleiro, a proporção deve ser de 1:1, sendo cada quadrado da imagem, um quadrado do tabuleiro na plataforma escolhida. Em seguida, crie os personagens de cada jogador, convide-os para seu jogo e dê-os o controle da peça.

<h1 align="center">
  Cartas
</h1>

<p align="center">
  <img img width="200" height="200" src="https://github.com/ViniciusHora1009/detetive_bot/blob/main/imagens/cards.png">
</p>

As cartas são necessárias para que os jogadores possam eliminar os suspeitos e que o assassino seja definido. Dentre as cartas que estarão no jogo estão:<br>

| Locais          | Armas        | Personagens                 |
|:---------------:|:------------:|:---------------------------:|
| Restaurante     | Faca         | Sargento Bigode             |
| Prefeitura      | Soco Inglês  | Florista Dona Branca        |
| Banco           | Pé de Cabra  | Advogado Senhor Marinho     |
| Hospital        | Tesoura      | Chef de Cozinha Tony Gourmet|
| Floricultura    | Pá           | Dançarina Srta Rosa         |
| Praça Central   | Arma Química | Médica Dona Violeta         |
| Mansão          | Veneno       | Coveiro Sérgio Noturno      |
| Hotel           | Espingarda   | Mordomo James               |
| Cemitério       |     ---      |             ---             |
| Estação de Trem |     ---      |             ---             |
| Boate           |     ---      |             ---             |

## Como utilizar o bot

**Prefixo: det!**

### Iniciando o jogo

Utilize o comando: **det!jogar**<br>

![Alt text](https://github.com/ViniciusHora1009/detetive_bot/blob/main/imagens/print1.PNG "Comando Jogar")<br>

Todos os jogadores que forem participar da partida devem reagir com o emote de verificado. Após todos terem reagido, clique no emote de ok.

### Selecionando o assassino e distribuindo as cartas

Depois de ter sido confirmada a partida o bot avisará que as cartas foram entregadas aos participantes e o assassino foi definido.<br>

![Alt text](https://github.com/ViniciusHora1009/detetive_bot/blob/main/imagens/print2.PNG "Trabalhando com as cartas")<br>

O bot entregará as cartas no privado:<br>

![Alt text](https://github.com/ViniciusHora1009/detetive_bot/blob/main/imagens/print3.PNG "Suas cartas")<br>

### Revelando o assassino

Para revelar o assassino digite o comando **det!assasssino**:<br>

![Alt text](https://github.com/ViniciusHora1009/detetive_bot/blob/main/imagens/print4.PNG "Revelado o assassino")<br>

### Resetando o jogo

Para reiniciar o jogo digite o comando **det!resetar**:<br>

![Alt text](https://github.com/ViniciusHora1009/detetive_bot/blob/main/imagens/print5.PNG "Jogo resetado")<br>

Para iniciar uma nova partida é só utilizar o comando **det!jogar** novamente.



