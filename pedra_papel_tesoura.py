import random
import tkinter as tk
from tkinter import font

ESCOLHAS = ["pedra", "papel", "tesoura"]
EMOJIS = {"pedra": "🪨", "papel": "📄", "tesoura": "✂️"}
CORES = {
    "vitoria": "#4CAF50",
    "derrota": "#F44336",
    "empate": "#FF9800",
    "neutro": "#2196F3"
}

def obter_escolha_computador():
    return random.choice(ESCOLHAS)

def decidir_vencedor(jogador, computador):
    if jogador == computador:
        return "empate"
    if (
        (jogador == "pedra" and computador == "tesoura")
        or (jogador == "tesoura" and computador == "papel")
        or (jogador == "papel" and computador == "pedra")
    ):
        return "jogador"
    return "computador"

def atualizar_placar():
    """Atualizar a exibição detalhada do placar"""
    label_placar.config(
        text=f"🏆 PLACAR 🏆\n"
             f"Você: {pontos['jogador']}  |  Computador: {pontos['computador']}  |  Empates: {pontos['empates']}"
    )
    
    total_rodadas = pontos['jogador'] + pontos['computador'] + pontos['empates']
    if total_rodadas > 0:
        taxa_vitoria = (pontos['jogador']/total_rodadas*100)
        taxa_computador = (pontos['computador']/total_rodadas*100)
        label_estatisticas.config(
            text=f"Total de rodadas: {total_rodadas}\n"
                 f"Taxa de vitória: {pontos['jogador']}/{total_rodadas} ({taxa_vitoria:.1f}%)  |  "
                 f"Computador: {taxa_computador:.1f}%"
        )

def resetar_pontos():
    """Resetar todos os pontos para zero"""
    pontos['jogador'] = 0
    pontos['computador'] = 0
    pontos['empates'] = 0
    pontos['historico'] = []
    atualizar_placar()
    atualizar_historico()
    label_resultado.config(
        text="Placar resetado! Faça sua jogada!",
        bg="#f0f0f0",
        fg="black"
    )

def atualizar_historico():
    """Atualizar o histórico das últimas 5 jogadas"""
    if not pontos['historico']:
        label_historico.config(text="📜 Histórico: Nenhuma jogada ainda")
        return
    
    ultimas = pontos['historico'][-5:]
    texto_historico = "📜 Últimas jogadas:\n" + " | ".join(ultimas)
    label_historico.config(text=texto_historico)

def ao_jogar(escolha_jogador):
    escolha_computador = obter_escolha_computador()
    vencedor = decidir_vencedor(escolha_jogador, escolha_computador)

    emoji_j = EMOJIS[escolha_jogador]
    emoji_c = EMOJIS[escolha_computador]
    
    if vencedor == "empate":
        pontos["empates"] += 1
        texto_resultado = "Empate! 🤝"
        cor_fundo = CORES["empate"]
        simbolo_resultado = "="
    elif vencedor == "jogador":
        pontos["jogador"] += 1
        texto_resultado = "Você venceu! 🎉"
        cor_fundo = CORES["vitoria"]
        simbolo_resultado = "✓"
    else:
        pontos["computador"] += 1
        texto_resultado = "Computador venceu! 🤖"
        cor_fundo = CORES["derrota"]
        simbolo_resultado = "✗"

    pontos['historico'].append(f"{emoji_j}{simbolo_resultado}{emoji_c}")
    
    label_resultado.config(
        text=f"{emoji_j} Você: {escolha_jogador.capitalize()}  VS  "
             f"Computador: {escolha_computador.capitalize()} {emoji_c}\n"
             f"{texto_resultado}",
        bg=cor_fundo,
        fg="white"
    )
    atualizar_placar()
    atualizar_historico()


janela = tk.Tk()
janela.title("🎮 Pedra Papel Tesoura")
janela.geometry("450x420")
janela.resizable(False, False)
janela.configure(bg="#ffffff")

label_titulo = tk.Label(
    janela, 
    text="🎮 Pedra Papel Tesoura 🎮", 
    font=("Segoe UI", 16, "bold"),
    bg="#ffffff",
    fg="#1976D2"
)
label_titulo.pack(pady=(15, 8))

label_placar = tk.Label(
    janela, 
    text="🏆 PLACAR 🏆\nVocê: 0  |  Computador: 0  |  Empates: 0", 
    font=("Segoe UI", 10, "bold"),
    bg="#E3F2FD",
    fg="#0D47A1",
    relief="solid",
    borderwidth=1,
    padx=10,
    pady=8
)
label_placar.pack(pady=(0, 4), fill="x", padx=20)

label_estatisticas = tk.Label(
    janela, 
    text="Total de rodadas: 0\nTaxa de vitória: 0/0 (0.0%)  |  Computador: 0.0%", 
    font=("Segoe UI", 9),
    bg="#ffffff",
    fg="#555"
)
label_estatisticas.pack(pady=(0, 8))

frame_botoes = tk.Frame(janela, bg="#ffffff")
frame_botoes.pack(pady=8)

pontos = {"jogador": 0, "computador": 0, "empates": 0, "historico": []}

estilo_botao = {
    "font": ("Segoe UI", 11),
    "width": 12,
    "height": 2,
    "relief": "raised",
    "borderwidth": 2,
    "cursor": "hand2"
}

botao_pedra = tk.Button(
    frame_botoes, 
    text="🪨 Pedra", 
    command=lambda: ao_jogar("pedra"),
    bg="#90A4AE",
    fg="white",
    activebackground="#78909C",
    **estilo_botao
)
botao_papel = tk.Button(
    frame_botoes, 
    text="📄 Papel", 
    command=lambda: ao_jogar("papel"),
    bg="#42A5F5",
    fg="white",
    activebackground="#1E88E5",
    **estilo_botao
)
botao_tesoura = tk.Button(
    frame_botoes, 
    text="✂️ Tesoura", 
    command=lambda: ao_jogar("tesoura"),
    bg="#66BB6A",
    fg="white",
    activebackground="#43A047",
    **estilo_botao
)

botao_pedra.grid(row=0, column=0, padx=5, pady=5)
botao_papel.grid(row=0, column=1, padx=5, pady=5)
botao_tesoura.grid(row=0, column=2, padx=5, pady=5)

label_resultado = tk.Label(
    janela, 
    text="Faça sua jogada!", 
    font=("Segoe UI", 11),
    bg="#f0f0f0",
    fg="black",
    justify="center",
    relief="groove",
    borderwidth=2,
    padx=15,
    pady=10
)
label_resultado.pack(pady=(10, 8), padx=20, fill="x")

label_historico = tk.Label(
    janela, 
    text="📜 Histórico: Nenhuma jogada ainda", 
    font=("Segoe UI", 9),
    bg="#ffffff",
    fg="#666",
    justify="center"
)
label_historico.pack(pady=(0, 10))

frame_controles = tk.Frame(janela, bg="#ffffff")
frame_controles.pack(pady=(5, 15))

botao_resetar = tk.Button(
    frame_controles, 
    text="🔄 Resetar", 
    width=14,
    font=("Segoe UI", 9),
    command=resetar_pontos,
    bg="#FF9800",
    fg="white",
    activebackground="#F57C00",
    cursor="hand2"
)
botao_resetar.grid(row=0, column=0, padx=5)

botao_sair = tk.Button(
    frame_controles, 
    text="❌ Sair", 
    width=12,
    font=("Segoe UI", 9),
    command=janela.destroy,
    bg="#F44336",
    fg="white",
    activebackground="#D32F2F",
    cursor="hand2"
)
botao_sair.grid(row=0, column=1, padx=5)

janela.mainloop()
