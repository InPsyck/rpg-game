# EldoriaRPG - Um RPG de Aventura Baseado em Texto

## Visão Geral

͏Eldori͏aRPG é um jogo de R͏P͏G f͏eito com tex͏to que foi cr͏iado todo em ͏Pytho͏n.

## Funcionalidades

- **Criação de Personagem**: Escolha entre três classes (Guerreiro, Arqueiro, Mago) e três raças (Humano, Elfo, Demônio), cada uma com atributos e habilidades únicas.
- **Sistema de Combate Dinâmico**: Participe de batalhas por turnos com ataques físicos e mágicos, com a opção de fugir do perigo.
- **Missões**: Enfrente missões principais e secundárias, como combater um Dragão das Sombras, explorar ruínas ou resolver enigmas.
- **Gerenciamento de Inventário**: Coletar e usar itens como poções de vida, poções de mana e armas para auxiliar na aventura.
- **Loja**: Gaste ouro para comprar poções e armas que aprimoram as habilidades do seu personagem.
- **Sistema de Salvamento/Carregamento**: Salve seu progresso em um arquivo JSON e carregue-o depois para continuar sua jornada.
- **Sistema de Níveis**: Ganhe experiência em missões e batalhas para subir de nível, aumentando os pontos de vida (HP) e mana (MP) do personagem.
- **Interface Colorida**: Utiliza a biblioteca `colorama` para uma saída de texto vibrante e envolvente.

## Requisitos

Para rodar o EldoriaRPG, você precisa de:

- **Python 3.6 ou superior**
- Biblioteca **colorama** (`pip install colorama`)

## Instalação

1. **Faça o download**:

   - Baixe o arquivo `Eldoria.py` para sua máquina local.

2. **Instalar Dependências**:

   - Certifique-se de que o Python está instalado no seu sistema.
   - Instale a biblioteca `colorama` executando:

     ```bash
     pip install colorama
     ```

3. **Executar o Jogo**:

   - Navegue até o diretório que contém o arquivo `Eldoria.py`.
   - Execute o script com:

     ```bash
     python Eldoria.py
     ```

## Como Jogar

1. **Iniciar o Jogo**:

   - Execute o script e você verá o menu principal.
   - Escolha entre iniciar um novo jogo, carregar um jogo salvo, ver informações sobre o jogo ou sair.

2. **Criação de Personagem**:

   - Ao iniciar um novo jogo, insira o nome do seu personagem, selecione uma classe (Guerreiro, Arqueiro ou Mago) e escolha uma raça (Humano, Elfo ou Demônio).
   - Cada combinação de classe e raça oferece atributos e habilidades únicas, exibidos durante a seleção.

3. **Jogabilidade**:

   - Navegue pelo menu do jogo para ver estatísticas, visitar a loja, realizar missões, gerenciar o inventário ou salvar seu progresso.
   - Em combates, escolha entre ataques físicos, ataques mágicos (se tiver mana suficiente) ou fugir.
   - Complete missões para ganhar experiência, ouro e itens, e suba de nível para melhorar os atributos do seu personagem.

4. **Salvamento e Carregamento**:

   - Salve seu progresso a qualquer momento pelo menu do jogo. O estado do jogo é armazenado em um arquivo `save_game.json`.
   - Carregue um jogo salvo a partir do menu principal para continuar de onde parou.

## Mecânicas do Jogo

### Classes

- **Guerreiro**: Alta força de ataque e defesa, com habilidades como Frenesi, Golpe Sísmico e Pele de Ferro.
- **Arqueiro**: Excelente em velocidade e precisão, com habilidades como Tiro Rápido e Flecha Fantasma.
- **Mago**: Forte em poder arcano, com feitiços como Bola de Fogo, Chama Gélida e Raio.

### Raças

- **Humano**: Atributos equilibrados em todas as áreas.
- **Elfo**: Alta destreza, inteligência e sabedoria, com imunidade a venenos e resistência elemental.
- **Demônio**: Forte em resistência e inteligência, com resistência ao fogo, mas vulnerável a luz sagrada.

### Atributos

- **HP**: Pontos de vida, determinam quanto dano seu personagem pode suportar.
- **MP**: Pontos de mana, usados para ataques mágicos e habilidades.
- **Ataque, Defesa, Velocidade**: Modificados pela classe e raça, afetam o desempenho em combate.

### Missões

- **Missão Principal**: Enfrente o Dragão das Sombras em uma batalha desafiadora.
- **Missões Secundárias**: Explore ruínas, salve aldeias, resolva enigmas ou aceite tarefas arriscadas, como contrabando.

## Estrutura de Arquivos

- `Eldoria.py`: O script principal do jogo, contendo toda a lógica.
- `save_game.json`: Gerado ao salvar o jogo, armazena dados do jogador (nome, classe, raça, atributos, inventário, etc.).

## Créditos

Desenvolvido por:

- Pablo Silva
- Thiago Guimarães
- Vitor Hugo
- Fábio Luiz
- Diogo Lourenço
- Marli
- Angelo Rocha
- Kadu Luis
- Rayan Roque
