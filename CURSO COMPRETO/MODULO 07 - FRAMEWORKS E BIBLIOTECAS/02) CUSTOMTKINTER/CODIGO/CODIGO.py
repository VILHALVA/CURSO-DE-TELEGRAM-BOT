import os
import json
import telebot
import customtkinter as ctk

class TelegramBotApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("BOT DE RECADOS")
        self.geometry("600x400")

        self.token_label = ctk.CLabel(self, text="TOKEN DO BOT:")
        self.token_label.grid(row=0, column=0, padx=10, pady=10, sticky=ctk.E)

        self.token_entry = ctk.CEntry(self)
        self.token_entry.grid(row=0, column=1, padx=10, pady=10, sticky=ctk.W)

        self.group_label = ctk.CLabel(self, text="ID DO GRUPO/CANAL:")
        self.group_label.grid(row=1, column=0, padx=10, pady=10, sticky=ctk.E)

        self.group_entry = ctk.CEntry(self)
        self.group_entry.grid(row=1, column=1, padx=10, pady=10, sticky=ctk.W)

        self.message_label = ctk.CLabel(self, text="MENSAGEM:")
        self.message_label.grid(row=2, column=0, padx=10, pady=10, sticky=ctk.E)

        self.message_entry = ctk.CText(self, width=50, height=5)  
        self.message_entry.grid(row=2, column=1, padx=10, pady=10, sticky=ctk.W)

        self.media_button = ctk.CButton(self, text="SELECIONE A MÍDIA", command=self.select_media)
        self.media_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.send_button = ctk.CButton(self, text="ENVIAR", command=self.send_message)
        self.send_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.clear_button = ctk.CButton(self, text="LIMPAR", command=self.clear_fields)
        self.clear_button.grid(row=5, column=0, columnspan=2, pady=10)
        
        self.footer_label = ctk.CLabel(
            self, text="APP CRIADO PELO VILHALVA\nGITHUB: @VILHALVA",
            bg="gray", fg="white", height=2
        )
        self.footer_label.grid(row=6, column=0, columnspan=2, sticky=ctk.W+ctk.E)   

        self.load_settings()

    def load_settings(self):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(script_dir, "settings.json")
        try:
            with open(file_path, "r") as f:
                settings = json.load(f)
                self.token_entry.insert(ctk.END, settings.get("token", ""))
                self.group_entry.insert(ctk.END, settings.get("chat_id", ""))
        except FileNotFoundError:
            pass

    def save_settings(self):
        settings = {
            "token": self.token_entry.get().strip(),
            "chat_id": self.group_entry.get().strip()
        }
        script_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(script_dir, "settings.json")
        with open(file_path, "w") as f:
            json.dump(settings, f)

    # Outros métodos (select_media, send_message, clear_fields) Você deve adaptar.

if __name__ == "__main__":
    app = TelegramBotApp()
    app.mainloop()
