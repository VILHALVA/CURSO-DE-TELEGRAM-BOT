import wx
import telebot
import json
import os

class TelegramBotApp(wx.Frame):
    def __init__(self):
        super().__init__(None, title="BOT DE RECADOS", size=(700, 400))
        self.panel = wx.Panel(self)

        self.token_label = wx.StaticText(self.panel, label="TOKEN DO BOT:")
        self.token_entry = wx.TextCtrl(self.panel)
        self.group_label = wx.StaticText(self.panel, label="ID DO GRUPO/CANAL:")
        self.group_entry = wx.TextCtrl(self.panel)
        self.message_label = wx.StaticText(self.panel, label="MENSAGEM:")
        self.message_entry = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
        self.media_button = wx.Button(self.panel, label="SELECIONE A MÍDIA")
        self.send_button = wx.Button(self.panel, label="ENVIAR")
        self.clear_button = wx.Button(self.panel, label="LIMPAR")

        self.init_ui()
        self.load_settings()

    def init_ui(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.token_label, 0, wx.ALL, 5)
        sizer.Add(self.token_entry, 0, wx.EXPAND|wx.ALL, 5)
        sizer.Add(self.group_label, 0, wx.ALL, 5)
        sizer.Add(self.group_entry, 0, wx.EXPAND|wx.ALL, 5)
        sizer.Add(self.message_label, 0, wx.ALL, 5)
        sizer.Add(self.message_entry, 1, wx.EXPAND|wx.ALL, 5)
        sizer.Add(self.media_button, 0, wx.ALL, 5)
        sizer.Add(self.send_button, 0, wx.ALL, 5)
        sizer.Add(self.clear_button, 0, wx.ALL, 5)
        
        self.panel.SetSizer(sizer)

        self.media_button.Bind(wx.EVT_BUTTON, self.select_media)
        self.send_button.Bind(wx.EVT_BUTTON, self.send_message)
        self.clear_button.Bind(wx.EVT_BUTTON, self.clear_fields)

    def load_settings(self):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(script_dir, "settings.json")
        try:
            with open(file_path, "r") as f:
                settings = json.load(f)
                self.token_entry.SetValue(settings.get("token", ""))
                self.group_entry.SetValue(settings.get("chat_id", ""))
        except FileNotFoundError:
            pass

    # Outros métodos (select_media, send_message, clear_fields) Você deve adaptar.

if __name__ == "__main__":
    app = wx.App(False)
    frame = TelegramBotApp()
    frame.Show(True)
    app.MainLoop()
