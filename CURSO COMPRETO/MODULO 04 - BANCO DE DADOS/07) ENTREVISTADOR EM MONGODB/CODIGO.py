from pymongo import MongoClient
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

class GerenciadorUsuarios:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["cadastro"]
        self.collection = self.db["usuarios"]

    def adicionar_usuario(self, nome, idade):
        usuario = {"nome": nome, "idade": idade}
        self.collection.insert_one(usuario)

    def listar_usuarios(self):
        usuarios = self.collection.find()
        return usuarios

    def atualizar_usuario(self, nome_antigo, novo_nome, nova_idade):
        query = {"nome": nome_antigo}
        new_values = {"$set": {"nome": novo_nome, "idade": nova_idade}}
        self.collection.update_one(query, new_values)

    def excluir_usuario(self, nome):
        query = {"nome": nome}
        self.collection.delete_one(query)

def start(update, context):
    keyboard = [
        [InlineKeyboardButton("ADICIONAR", callback_data='add')],
        [InlineKeyboardButton("EXIBIR A LISTA", callback_data='list')],
        [InlineKeyboardButton("ATUALIZAR", callback_data='update')],
        [InlineKeyboardButton("EXCLUIR", callback_data='delete')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('👋OLÁ! EU SOU UM BOT BÁSICO DE CRUD. MINHA PRINCIPAL FUNCIONALIDADE É GERENCIAR USUÁRIOS COM DATABASE. \n🤖CLIQUE EM UMA OPÇÃO:', reply_markup=reply_markup)

    context.user_data['gerenciador'] = GerenciadorUsuarios()

def button(update, context):
    query = update.callback_query
    data = query.data

    if data == 'add':
        query.message.reply_text('Digite o nome do usuário:')
        context.user_data['action'] = 'add_name'
    elif data == 'list':
        gerenciador = context.user_data['gerenciador']
        usuarios = gerenciador.listar_usuarios()
        if usuarios:
            response = "LISTA DE USUÁRIOS:\n"
            cont = 1
            for usuario in usuarios:
                response += f"{cont} - 👥NOME: {usuario['nome']}, 👁IDADE: {usuario['idade']}\n"
                cont += 1
            query.message.reply_text(response)
        else:
            query.message.reply_text('Nenhum usuário cadastrado.')
    elif data == 'update':
        query.message.reply_text('Digite o nome do usuário a ser atualizado:')
        context.user_data['action'] = 'update_name'
    elif data == 'delete':
        query.message.reply_text('Digite o nome do usuário a ser excluído:')
        context.user_data['action'] = 'delete_name'

def message(update, context):
    text = update.message.text
    user_data = context.user_data

    if 'action' in user_data:
        action = user_data['action']
        if action == 'add_name':
            user_data['nome'] = text
            update.message.reply_text('Digite a idade do usuário:')
            user_data['action'] = 'add_age'
        elif action == 'add_age':
            nome = user_data['nome']
            idade = text
            gerenciador = user_data['gerenciador']
            gerenciador.adicionar_usuario(nome, idade)
            update.message.reply_text('Usuário adicionado com sucesso.')
            del user_data['action']
            del user_data['nome']
            start(update, context)
        elif action == 'update_name':
            user_data['nome_antigo'] = text
            update.message.reply_text('Digite o novo nome do usuário:')
            user_data['action'] = 'update_new_name'
        elif action == 'update_new_name':
            user_data['novo_nome'] = text
            update.message.reply_text('Por favor, envie a idade do usuário para atualizá-lo.')
            user_data['action'] = 'update_age'
        elif action == 'update_age':
            novo_nome = user_data['novo_nome']
            nova_idade = text
            gerenciador = user_data['gerenciador']
            gerenciador.atualizar_usuario(user_data['nome_antigo'], novo_nome, nova_idade)
            update.message.reply_text('Usuário atualizado com sucesso.')
            del user_data['nome_antigo']
            del user_data['novo_nome']
            del user_data['action']
            start(update, context)
        elif action == 'delete_name':
            nome = text
            gerenciador = user_data['gerenciador']
            gerenciador.excluir_usuario(nome)
            update.message.reply_text('Usuário excluído com sucesso.')
            del user_data['action']
            start(update, context)
    else:
        update.message.reply_text('Por favor, inicie o bot usando /start.')

def main():
    TOKEN = 'SEU_TOKEN'  # Substitua pelo token do seu bot

    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(button, pattern='^add$|^list$|^update$|^delete$'))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
