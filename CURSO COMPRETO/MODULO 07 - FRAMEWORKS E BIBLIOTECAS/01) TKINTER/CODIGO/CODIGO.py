import telebot
import tkinter as tk
from tkinter import messagebox, filedialog
import json
import os

class TelegramBotApp:
    def __init__(self, master):
        self.master = master
        self.master.title("BOT DE RECADOS")

        self.token_label = tk.Label(master, text="TOKEN DO BOT:")
        self.token_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)

        self.token_entry = tk.Entry(master)
        self.token_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        self.group_label = tk.Label(master, text="ID DO GRUPO/CANAL:")
        self.group_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

        self.group_entry = tk.Entry(master)
        self.group_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        self.message_label = tk.Label(master, text="MENSAGEM:")
        self.message_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

        self.message_entry = tk.Text(master, width=50, height=5)  
        self.message_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        self.media_button = tk.Button(master, text="SELECIONE A MÍDIA", command=self.select_media)
        self.media_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.send_button = tk.Button(master, text="ENVIAR", command=self.send_message)
        self.send_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.clear_button = tk.Button(master, text="LIMPAR", command=self.clear_fields)
        self.clear_button.grid(row=5, column=0, columnspan=2, pady=10)
        
        self.footer_label = tk.Label(
        master, text="APP CRIADO PELO VILHALVA\nGITHUB: @VILHALVA",
        bg="gray", fg="white", height=2
        )
        self.footer_label.grid(row=6, column=0, columnspan=2, sticky=tk.W+tk.E)   

        self.load_settings()

    def load_settings(self):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(script_dir, "settings.json")
        try:
            with open(file_path, "r") as f:
                settings = json.load(f)
                self.token_entry.insert(tk.END, settings.get("token", ""))
                self.group_entry.insert(tk.END, settings.get("chat_id", ""))
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

    def select_media(self):
        media_path = filedialog.askopenfilename(title="Selecionar Mídia", filetypes=[("Arquivos de Mídia", "*.jpg;*.jpeg;*.png;*.mp4;*.avi")])
        if media_path:
            messagebox.showinfo("Sucesso", f"Mídia selecionada: {media_path}")
            self.media_path = media_path
        else:
            messagebox.showwarning("Aviso", "Nenhum arquivo de mídia selecionado.")

    def send_message(self):
        token = self.token_entry.get().strip()
        chat_id = self.group_entry.get().strip()
        message_text = self.message_entry.get("1.0", tk.END).strip()  
        send_media = hasattr(self, 'media_path') and self.media_path

        if not token or not chat_id:
            messagebox.showerror("Erro", "Preencha todos os campos obrigatórios!")
            return

        try:
            bot = telebot.TeleBot(token)
            if send_media:
                caption_text = f"\n{message_text}" if message_text else ""
                with open(self.media_path, 'rb') as media_file:
                    bot.send_media_group(chat_id, [telebot.types.InputMediaPhoto(media_file, caption=caption_text)])
            elif message_text:
                bot.send_message(chat_id, message_text)
            else:
                messagebox.showwarning("Aviso", "Nada para enviar. Preencha a mensagem ou selecione uma mídia.")
                return

            messagebox.showinfo("Sucesso", "Mensagem enviada com sucesso!")

            self.save_settings()

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao enviar mensagem:\n{str(e)}")

    def clear_fields(self):
        self.token_entry.delete(0, tk.END)
        self.group_entry.delete(0, tk.END)
        self.message_entry.delete("1.0", tk.END)
        if hasattr(self, 'media_path'):
            delattr(self, 'media_path')

if __name__ == "__main__":
    root = tk.Tk()
    app = TelegramBotApp(root)
    root.mainloop()