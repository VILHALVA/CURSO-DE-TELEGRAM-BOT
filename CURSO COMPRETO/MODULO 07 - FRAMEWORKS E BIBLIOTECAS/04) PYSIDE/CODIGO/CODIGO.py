import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox, QVBoxLayout, QHBoxLayout, QFileDialog
import telebot
import json
import os

class TelegramBotApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BOT DE RECADOS")
        self.initUI()
        self.load_settings()

    def initUI(self):
        layout = QVBoxLayout()

        token_layout = QHBoxLayout()
        token_label = QLabel("TOKEN DO BOT:")
        self.token_entry = QLineEdit()
        token_layout.addWidget(token_label)
        token_layout.addWidget(self.token_entry)

        group_layout = QHBoxLayout()
        group_label = QLabel("ID DO GRUPO/CANAL:")
        self.group_entry = QLineEdit()
        group_layout.addWidget(group_label)
        group_layout.addWidget(self.group_entry)

        message_layout = QHBoxLayout()
        message_label = QLabel("MENSAGEM:")
        self.message_entry = QTextEdit()
        message_layout.addWidget(message_label)
        message_layout.addWidget(self.message_entry)

        media_layout = QHBoxLayout()
        self.media_button = QPushButton("SELECIONE A MÍDIA")
        self.media_button.clicked.connect(self.select_media)
        media_layout.addWidget(self.media_button)

        send_layout = QHBoxLayout()
        self.send_button = QPushButton("ENVIAR")
        self.send_button.clicked.connect(self.send_message)
        send_layout.addWidget(self.send_button)

        clear_layout = QHBoxLayout()
        self.clear_button = QPushButton("LIMPAR")
        self.clear_button.clicked.connect(self.clear_fields)
        clear_layout.addWidget(self.clear_button)

        layout.addLayout(token_layout)
        layout.addLayout(group_layout)
        layout.addLayout(message_layout)
        layout.addLayout(media_layout)
        layout.addLayout(send_layout)
        layout.addLayout(clear_layout)

        self.setLayout(layout)

    def load_settings(self):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(script_dir, "settings.json")
        try:
            with open(file_path, "r") as f:
                settings = json.load(f)
                self.token_entry.setText(settings.get("token", ""))
                self.group_entry.setText(settings.get("chat_id", ""))
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
    app = QApplication(sys.argv)
    window = TelegramBotApp()
    window.show()
    sys.exit(app.exec_())
