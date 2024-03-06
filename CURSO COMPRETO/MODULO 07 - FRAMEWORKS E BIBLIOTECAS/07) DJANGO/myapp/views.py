from django.shortcuts import render
from django.http import HttpResponse
import json

def load_settings():
    try:
        with open("settings.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_settings(request):
    if request.method == "POST":
        token = request.POST["token"]
        chat_id = request.POST["chat_id"]

        settings = {"token": token, "chat_id": chat_id}
        with open("settings.json", "w") as f:
            json.dump(settings, f)

        return HttpResponse("Configurações salvas com sucesso!")

def index(request):
    settings = load_settings()
    return render(request, 'myapp/index.html', {'settings': settings})
