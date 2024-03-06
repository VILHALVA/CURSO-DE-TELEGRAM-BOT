from flask import Flask, render_template, request
import telebot
import json

app = Flask(__name__)

# Carrega as configurações do arquivo JSON
def load_settings():
    try:
        with open("settings.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Salva as configurações no arquivo JSON
def save_settings(settings):
    with open("settings.json", "w") as f:
        json.dump(settings, f)

# Página inicial
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        token = request.form["token"]
        chat_id = request.form["chat_id"]

        # Salva as configurações
        settings = {"token": token, "chat_id": chat_id}
        save_settings(settings)

        return "Configurações salvas com sucesso!"

    # Carrega as configurações atuais
    settings = load_settings()
    return render_template("INDEX.html", settings=settings)

if __name__ == "__main__":
    app.run(debug=True)
