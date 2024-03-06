from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import telebot
import json

class TelegramBotApp(App):
    def build(self):
        self.settings = self.load_settings()

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='TOKEN DO BOT:'))
        self.token_entry = TextInput(text=self.settings.get('token', ''))
        layout.add_widget(self.token_entry)

        layout.add_widget(Label(text='ID DO GRUPO/CANAL:'))
        self.group_entry = TextInput(text=self.settings.get('chat_id', ''))
        layout.add_widget(self.group_entry)

        self.save_button = Button(text='Salvar Configurações')
        self.save_button.bind(on_press=self.save_settings)
        layout.add_widget(self.save_button)

        return layout

    def load_settings(self):
        try:
            with open("settings.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_settings(self, instance):
        token = self.token_entry.text
        chat_id = self.group_entry.text

        settings = {"token": token, "chat_id": chat_id}
        with open("settings.json", "w") as f:
            json.dump(settings, f)

        self.settings = settings
        print("Configurações salvas com sucesso!")

if __name__ == "__main__":
    TelegramBotApp().run()
