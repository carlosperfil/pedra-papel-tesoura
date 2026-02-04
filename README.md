# 🎮 Jogo Pedra Papel Tesoura

Um jogo clássico de Pedra, Papel e Tesoura desenvolvido em Python com interface gráfica usando Tkinter. Jogue contra o computador e acompanhe suas estatísticas em tempo real!

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Regras do Jogo](#regras-do-jogo)
- [Estrutura do Código](#estrutura-do-código)
- [Screenshots](#screenshots)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Melhorias Futuras](#melhorias-futuras)

## 🎯 Sobre o Projeto

Este é um jogo interativo de Pedra, Papel e Tesoura desenvolvido como projeto educacional em Python. O jogo apresenta uma interface gráfica intuitiva, sistema completo de pontuação e estatísticas detalhadas para acompanhar o desempenho do jogador.

## ✨ Funcionalidades

### 🏆 Sistema de Pontuação Completo
- **Rastreamento de vitórias** do jogador
- **Rastreamento de vitórias** do computador
- **Contador de empates**
- **Total de rodadas** jogadas

### 📊 Estatísticas Detalhadas
- Taxa de vitória do jogador em porcentagem
- Taxa de vitória do computador em porcentagem
- Histórico visual das últimas 5 jogadas
- Símbolos visuais para resultado (✓ vitória, ✗ derrota, = empate)

### 🎨 Interface Moderna
- **Design colorido e intuitivo**
- **Emojis** para melhor visualização (🪨 📄 ✂️)
- **Feedback visual por cores**:
  - 🟢 Verde para vitórias
  - 🔴 Vermelho para derrotas
  - 🟠 Laranja para empates
- **Botões interativos** com cursor pointer
- **Placar destacado** com borda e cores diferenciadas

### 🔧 Controles
- Botão de **reset** para reiniciar o placar
- Botão de **sair** para fechar o jogo
- Interface responsiva e amigável

## 💻 Requisitos

- Python 3.7 ou superior
- Tkinter (geralmente já incluído na instalação padrão do Python)

### Verificar se o Tkinter está instalado

```bash
python -m tkinter
```

Se uma janela aparecer, o Tkinter está instalado corretamente.

## 🚀 Instalação

1. **Clone o repositório ou baixe o arquivo**

```bash
git clone https://github.com/[seu-usuario]/pedra-papel-tesoura.git
cd pedra-papel-tesoura
```

2. **Execute o jogo**

```bash
python pedra_papel_tesoura.py
```

## 🎮 Como Usar

1. **Inicie o jogo** executando o arquivo Python
2. **Escolha sua jogada** clicando em um dos três botões:
   - 🪨 Pedra
   - 📄 Papel
   - ✂️ Tesoura
3. **Veja o resultado** imediatamente na tela
4. **Acompanhe suas estatísticas** no placar superior
5. **Visualize o histórico** das últimas jogadas
6. **Reset o placar** quando quiser recomeçar
7. **Saia do jogo** clicando no botão "Sair"

## 📖 Regras do Jogo

O jogo segue as regras clássicas de Pedra, Papel e Tesoura:

| Jogada 1 | vs | Jogada 2 | Resultado |
|----------|:--:|----------|-----------|
| 🪨 Pedra | vs | ✂️ Tesoura | ✓ Pedra vence |
| 📄 Papel | vs | 🪨 Pedra | ✓ Papel vence |
| ✂️ Tesoura | vs | 📄 Papel | ✓ Tesoura vence |
| Iguais | vs | Iguais | = Empate |

### 🎯 Objetivo
Vencer o máximo de rodadas possível contra o computador!

## 🏗️ Estrutura do Código

### Constantes Globais
```python
ESCOLHAS = ["pedra", "papel", "tesoura"]
EMOJIS = {"pedra": "🪨", "papel": "📄", "tesoura": "✂️"}
CORES = {...}  # Cores para feedback visual
```

### Funções Principais

#### `obter_escolha_computador()`
Gera aleatoriamente a escolha do computador.

#### `decidir_vencedor(jogador, computador)`
Determina o vencedor da rodada com base nas regras do jogo.

#### `atualizar_placar()`
Atualiza a interface com os pontos atuais e estatísticas.

#### `atualizar_historico()`
Mantém o histórico visual das últimas 5 jogadas.

#### `ao_jogar(escolha_jogador)`
Função principal que processa cada jogada e atualiza a interface.

#### `resetar_pontos()`
Reseta todos os contadores e o histórico.

### Estrutura de Dados
```python
pontos = {
    "jogador": 0,
    "computador": 0,
    "empates": 0,
    "historico": []
}
```

## 📸 Screenshots

```
🎮 Pedra Papel Tesoura 🎮
━━━━━━━━━━━━━━━━━━━━━━━━━
🏆 PLACAR 🏆
Você: 5  |  Computador: 3  |  Empates: 2
━━━━━━━━━━━━━━━━━━━━━━━━━
Total de rodadas: 10
Taxa de vitória: 5/10 (50.0%)  |  Computador: 30.0%

[🪨 Pedra]  [📄 Papel]  [✂️ Tesoura]

━━━━━━━━━━━━━━━━━━━━━━━━━
🪨 Você: Pedra  VS  Computador: Tesoura ✂️
Você venceu! 🎉
━━━━━━━━━━━━━━━━━━━━━━━━━

📜 Últimas jogadas:
🪨✓✂️ | 📄✗🪨 | ✂️=✂️ | 🪨✓✂️ | 📄✗🪨

[🔄 Resetar]  [❌ Sair]
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.x** - Linguagem de programação
- **Tkinter** - Biblioteca para interface gráfica
- **Random** - Geração de escolhas aleatórias para o computador

## 🚀 Melhorias Futuras

- [ ] Adicionar sons para vitória/derrota
- [ ] Implementar diferentes níveis de dificuldade
- [ ] Adicionar modo multiplayer (2 jogadores)
- [ ] Salvar estatísticas em arquivo
- [ ] Adicionar gráficos de desempenho
- [ ] Implementar sistema de conquistas
- [ ] Adicionar animações nas jogadas
- [ ] Modo dark/light theme
- [ ] Tradução para outros idiomas
