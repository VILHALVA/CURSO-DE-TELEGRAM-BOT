from pyscript import tk
import telebot
import json
import os

def load_settings():
    try:
        with open("settings.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_settings(settings):
    with open("settings.json", "w") as f:
        json.dump(settings, f)

def select_media():
    # Implemente a seleção de mídia aqui
    pass

def send_message():
    # Implemente o envio de mensagem aqui
    pass

def clear_fields():
    # Implemente a limpeza dos campos aqui
    pass

def main():
    root = tk.Tk()
    root.title("BOT DE RECADOS")

    token_label = tk.Label(root, text="TOKEN DO BOT:")
    token_label.grid(row=0, column=0, padx=10, pady=10)

    token_entry = tk.Entry(root)
    token_entry.grid(row=0, column=1, padx=10, pady=10)

    group_label = tk.Label(root, text="ID DO GRUPO/CANAL:")
    group_label.grid(row=1, column=0, padx=10, pady=10)

    group_entry = tk.Entry(root)
    group_entry.grid(row=1, column=1, padx=10, pady=10)

    message_label = tk.Label(root, text="MENSAGEM:")
    message_label.grid(row=2, column=0, padx=10, pady=10)

    message_entry = tk.Text(root, width=50, height=5)
    message_entry.grid(row=2, column=1, padx=10, pady=10)

    media_button = tk.Button(root, text="SELECIONE A MÍDIA", command=select_media)
    media_button.grid(row=3, column=0, columnspan=2, pady=10)

    send_button = tk.Button(root, text="ENVIAR", command=send_message)
    send_button.grid(row=4, column=0, columnspan=2, pady=10)

    clear_button = tk.Button(root, text="LIMPAR", command=clear_fields)
    clear_button.grid(row=5, column=0, columnspan=2, pady=10)

    footer_label = tk.Label(
        root, text="APP CRIADO PELO VILHALVA\nGITHUB: @VILHALVA",
        bg="gray", fg="white", height=2
    )
    footer_label.grid(row=6, column=0, columnspan=2, sticky=tk.W+tk.E)

    settings = load_settings()
    token_entry.insert(tk.END, settings.get("token", ""))
    group_entry.insert(tk.END, settings.get("chat_id", ""))

    root.mainloop()

if __name__ == "__main__":
    main()
