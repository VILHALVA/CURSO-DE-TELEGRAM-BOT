import pymongo
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

class Bot:
    def __init__(self, token, db_uri):
        self.token = token
        self.db_uri = db_uri
        self.updater = Updater(token)
        self.dispatcher = self.updater.dispatcher

        # Handlers
        self.dispatcher.add_handler(CommandHandler("start", self.start))
        self.dispatcher.add_handler(CommandHandler("test_db", self.test_db))

    def start(self, update: Update, context: CallbackContext):
        update.message.reply_text("Olá! Eu sou um bot para testar conexão com MongoDB. Use /test_db para verificar a conexão.")

    def test_db(self, update: Update, context: CallbackContext):
        try:
            # Conecta ao banco de dados MongoDB
            client = pymongo.MongoClient(self.db_uri)
            db = client.test_database
            collection = db.test_collection
            collection.insert_one({"message": "Teste de conexão com MongoDB"})
            update.message.reply_text("Conexão com o MongoDB bem-sucedida!")
        except Exception as e:
            update.message.reply_text(f"Erro ao conectar ao MongoDB: {e}")

    def start_bot(self):
        self.updater.start_polling()
        self.updater.idle()

if __name__ == "__main__":
    # Substitua "TOKEN_DO_SEU_BOT" pelo token do seu bot e "URI_DO_SEU_MONGODB" pela URI de conexão do seu MongoDB
    token = "TOKEN_DO_SEU_BOT"
    db_uri = "URI_DO_SEU_MONGODB"
    bot = Bot(token, db_uri)
    bot.start_bot()
