# KIVY
## EXPLICAÇÃO:
Kivy é um framework de código aberto em Python para o desenvolvimento de aplicativos multi-toque, multi-plataforma e de interface gráfica (GUI). Ele permite que os desenvolvedores criem aplicativos com interfaces de usuário modernas e atraentes, compatíveis com uma variedade de dispositivos e sistemas operacionais, incluindo desktops, dispositivos móveis e até mesmo Raspberry Pi.

Aqui está um exemplo básico de como criar uma simples aplicação usando o Kivy:

```python
from kivy.app import App
from kivy.uix.button import Button

class MinhaApp(App):
    def build(self):
        return Button(text='Olá, Kivy!')

if __name__ == '__main__':
    MinhaApp().run()
```

Neste exemplo:

- Importamos as classes necessárias do Kivy.
- Criamos uma classe `MinhaApp` que herda da classe `App` do Kivy.
- Definimos o método `build`, que retorna um botão com o texto "Olá, Kivy!".
- No bloco `if __name__ == '__main__':`, instanciamos `MinhaApp()` e chamamos o método `run()` para iniciar a aplicação.

Ao executar este script Python, uma janela com um botão será aberta exibindo o texto "Olá, Kivy!". Você pode clicar no botão para interagir com ele.

O Kivy oferece muito mais do que apenas botões simples. Ele possui uma ampla gama de widgets e funcionalidades para criar interfaces gráficas complexas e interativas, incluindo layouts, gráficos, animações e muito mais. Recomendo explorar a documentação oficial do Kivy para aprender mais sobre seus recursos e como usá-los em seus próprios projetos.