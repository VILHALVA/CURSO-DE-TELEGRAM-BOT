import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from toga.widgets import Label, TextInput, Button
import telebot
import json

class TelegramBotApp(toga.App):
    def startup(self):
        self.settings = self.load_settings()

        main_box = toga.Box(style=Pack(direction=COLUMN))

        token_label = Label('TOKEN DO BOT:', style=Pack(padding=(0, 5)))
        self.token_entry = TextInput(placeholder='Insira o token do bot', initial=self.settings.get('token', ''), style=Pack(flex=1, padding=(0, 5)))

        group_label = Label('ID DO GRUPO/CANAL:', style=Pack(padding=(0, 5)))
        self.group_entry = TextInput(placeholder='Insira o ID do grupo/canal', initial=self.settings.get('chat_id', ''), style=Pack(flex=1, padding=(0, 5)))

        self.save_button = Button('Salvar Configurações', on_press=self.save_settings, style=Pack(padding=5))

        main_box.add(token_label)
        main_box.add(self.token_entry)
        main_box.add(group_label)
        main_box.add(self.group_entry)
        main_box.add(self.save_button)

        main_box.app = self
        main_box.show()

    def load_settings(self):
        try:
            with open("settings.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_settings(self, widget):
        token = self.token_entry.value
        chat_id = self.group_entry.value

        settings = {"token": token, "chat_id": chat_id}
        with open("settings.json", "w") as f:
            json.dump(settings, f)

        self.settings = settings
        print("Configurações salvas com sucesso!")

if __name__ == '__main__':
    app = TelegramBotApp('Telegram Bot', 'org.example.telegrambot')
    app.main_loop()
