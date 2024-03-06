# CUSTOMTKINTER
## EXPLICAÇÃO:
Para criar uma interface gráfica personalizada usando Tkinter para um bot do Telegram, você pode estender as capacidades do Tkinter para criar uma experiência mais elaborada e atraente para os usuários. Aqui está um exemplo básico de como você pode criar uma interface personalizada usando Tkinter:

```python
import tkinter as tk
from tkinter import messagebox
import telebot

# Função para enviar mensagem quando o botão for pressionado
def enviar_mensagem():
    mensagem = entrada_texto.get()
    bot.send_message(chat_id='ID_DO_CHAT', text=mensagem)
    messagebox.showinfo("Envio de Mensagem", "Mensagem enviada com sucesso!")

# Configurações iniciais do bot Telegram
TOKEN = 'TOKEN_DO_SEU_BOT'
bot = telebot.TeleBot(TOKEN)

# Configurações da interface gráfica
root = tk.Tk()
root.title("Bot do Telegram")

# Estilo personalizado para o botão
botao_estilo = {
    'bg': 'blue',            # Cor de fundo
    'fg': 'white',           # Cor do texto
    'font': ('Helvetica', 12),  # Fonte e tamanho do texto
    'relief': 'raised',      # Estilo da borda
    'width': 15              # Largura do botão
}

# Campo de entrada de texto
entrada_texto = tk.Entry(root, width=50, font=('Helvetica', 14))
entrada_texto.grid(row=0, column=0, padx=10, pady=10)

# Botão para enviar mensagem
botao_enviar = tk.Button(root, text="Enviar Mensagem", command=enviar_mensagem, **botao_estilo)
botao_enviar.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()
```

Neste exemplo, usei o método `grid()` para organizar os widgets na janela Tkinter. Além disso, personalizei o estilo do botão usando um dicionário para configurar cores, fonte e largura. Você pode ajustar esses parâmetros conforme necessário para atender ao design desejado.

Não se esqueça de substituir `'ID_DO_CHAT'` pelo ID do chat para o qual você deseja enviar mensagens e `'TOKEN_DO_SEU_BOT'` pelo token do seu bot do Telegram. Certifique-se também de ter instalado as bibliotecas necessárias, como Tkinter e telebot.

Este é apenas um exemplo básico para começar. Você pode expandir e personalizar ainda mais a interface gráfica conforme suas necessidades e preferências de design.