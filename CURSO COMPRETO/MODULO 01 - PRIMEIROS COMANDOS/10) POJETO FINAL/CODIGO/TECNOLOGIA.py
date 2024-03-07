from telebot import types

def submenu_tecnologia():
    markup = types.InlineKeyboardMarkup(row_width=2)
    python_button = types.InlineKeyboardButton("PYTHON", callback_data='python')
    java_button = types.InlineKeyboardButton("JAVA", callback_data='java')
    javascript_button = types.InlineKeyboardButton("JAVASCRIPT", callback_data='javascript')
    c_button = types.InlineKeyboardButton("C", callback_data='c')
    cpp_button = types.InlineKeyboardButton("C++", callback_data='cpp')
    swift_button = types.InlineKeyboardButton("SWIFT", callback_data='swift')
    
    markup.add(python_button, java_button, javascript_button, c_button, cpp_button, swift_button)
    
    return markup

# Handler para os callbacks dos botões do submenu de Tecnologia
def callback_query(bot, call):
    if call.data == 'python':
        bot.send_message(call.message.chat.id, "Python é uma linguagem de programação de alto nível, interpretada e de script, amplamente utilizada para desenvolvimento web, científico e de software em geral.")
    elif call.data == 'java':
        bot.send_message(call.message.chat.id, "Java é uma linguagem de programação de propósito geral, projetada para ser executada em uma máquina virtual Java (JVM). É amplamente utilizada para desenvolvimento de aplicativos empresariais.")
    elif call.data == 'javascript':
        bot.send_message(call.message.chat.id, "JavaScript é uma linguagem de programação de alto nível, interpretada e orientada a objetos, amplamente utilizada para desenvolvimento web, principalmente para adicionar interatividade às páginas.")
    elif call.data == 'c':
        bot.send_message(call.message.chat.id, "C é uma linguagem de programação de propósito geral que foi desenvolvida originalmente por Dennis Ritchie para o desenvolvimento do sistema operacional Unix.")
    elif call.data == 'cpp':
        bot.send_message(call.message.chat.id, "C++ é uma linguagem de programação de propósito geral, derivada de C, com suporte a programação orientada a objetos. É amplamente utilizada para desenvolvimento de sistemas e aplicativos de alto desempenho.")
    elif call.data == 'swift':
        bot.send_message(call.message.chat.id, "Swift é uma linguagem de programação desenvolvida pela Apple para desenvolvimento de aplicativos para iOS, macOS, watchOS e tvOS. É projetada para ser segura, rápida e moderna.")
    else:
        pass
