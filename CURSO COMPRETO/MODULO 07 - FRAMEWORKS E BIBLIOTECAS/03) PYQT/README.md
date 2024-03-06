# PYQT
## EXPLICAÇÃO:
PyQt é um conjunto de ferramentas para criar aplicativos GUI usando o Qt toolkit. Ele fornece uma ampla variedade de widgets e funcionalidades para criar interfaces gráficas ricas e interativas.

Aqui está um exemplo básico de como você pode criar uma janela simples usando PyQt:

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget

# Classe da janela principal
class MinhaJanela(QWidget):
    def __init__(self):
        super().__init__()

        # Definindo título e geometria da janela
        self.setWindowTitle('Minha Janela PyQt')
        self.setGeometry(100, 100, 300, 200)

        # Exibindo a janela
        self.show()

# Função principal
def main():
    # Criando a aplicação Qt
    app = QApplication(sys.argv)

    # Criando uma instância da janela
    janela = MinhaJanela()

    # Executando o loop de eventos da aplicação
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
```

Este é um exemplo muito simples de uma janela criada com PyQt. PyQt possui uma variedade de widgets e recursos que podem ser usados para criar interfaces gráficas mais complexas e interativas. Recomendo explorar a documentação oficial do PyQt para aprender mais sobre seus recursos e como usá-los em seus próprios projetos.