# FLASK
## EXPLICAÇÃO:
Flask é um framework web leve e flexível para Python. Ele foi projetado para ser simples e fácil de usar, permitindo que os desenvolvedores criem aplicativos web rapidamente com menos boilerplate code.

Aqui está um exemplo básico de como criar um aplicativo web simples usando Flask:

```python
from flask import Flask

# Criando uma instância do aplicativo Flask
app = Flask(__name__)

# Definindo uma rota para a página inicial
@app.route('/')
def index():
    return 'Olá, mundo! Este é o meu primeiro aplicativo Flask.'

# Rodando o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True)
```

Neste exemplo:

- Importamos a classe Flask do módulo flask.
- Criamos uma instância do aplicativo Flask.
- Definimos uma rota para a página inicial ('/'), que retorna uma mensagem de saudação.
- Finalmente, executamos o aplicativo Flask com `app.run()`.

Ao executar este script Python, um servidor web local será iniciado e você poderá acessar o aplicativo Flask no navegador visitando `http://localhost:5000`.

O Flask oferece muito mais do que isso, incluindo suporte para roteamento avançado, templates Jinja2 para renderização HTML, manipulação de formulários, suporte a banco de dados e muito mais. É altamente recomendável explorar a documentação oficial do Flask para aprender mais sobre suas capacidades e como usá-lo para desenvolver aplicativos web mais complexos.