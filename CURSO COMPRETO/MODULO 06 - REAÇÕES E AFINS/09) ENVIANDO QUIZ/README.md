# ENVIANDO QUIZ
## DESCRIÇÃO:
Este é um bot que automatiza o envio de perguntas de quiz para grupos no Telegram. Ele recupera as perguntas do banco de dados, atualiza os grupos no banco de dados, se necessário, e envia as perguntas para os grupos.

## EXPLICAÇÃO 
### MAIN.PY:
1. **Importações:**
   ```python
   from TELEGRAM_BOT import telegramBot
   from DB_CONECTION import databaseConnect
   from CRENDECIAIS import update_URL, poll_URL, db_quiz, db_ids, db_database, client_url
   from datetime import datetime
   ```
   - Importa várias classes, funções e módulos necessários para o funcionamento do script, incluindo uma classe `telegramBot`, uma função `databaseConnect`, algumas URLs de banco de dados e outras credenciais, bem como a classe `datetime`.

2. **Obtenção da Data Atual:**
   ```python
   now = datetime.now()
   date_time_str = str(now.strftime("%d-%m-%Y"))
   ```
   - Obtém a data e hora atuais em formato de string no padrão "dia-mês-ano" (por exemplo, "27-04-2023").

3. **Conexão com o Banco de Dados:**
   ```python
   deepQuiz = databaseConnect(db_database, client_url)
   deepQuiz.collection_connect(db_quiz)
   ```
   - Estabelece uma conexão com o banco de dados usando as credenciais fornecidas.

4. **Recuperação dos Dados do Quiz para o Dia Atual:**
   ```python
   data = deepQuiz.fetch_data(date_time_str)
   quiz_question = {
       'question': data['question'],
       'options': [data['option1'], data['option2'], data['option3'], data['option4']],
       'correctOption': data['correct_answer'],
       'explaination': data['explaination']
   }
   ```
   - Recupera os dados da pergunta do quiz para o dia atual do banco de dados.

5. **Recuperação dos IDs dos Grupos:**
   ```python
   deepQuiz.collection_connect(db_ids)
   data = deepQuiz.fetch_data()
   group_ids = set(data['all_ids'])
   ```
   - Recupera os IDs dos grupos que receberam as perguntas do quiz anteriormente.

6. **Inicialização do Bot do Telegram:**
   ```python
   deepAIBot = telegramBot(update_URL, poll_URL)
   ```
   - Cria uma instância do bot do Telegram, fornecendo as URLs de atualização e de enquete.

7. **Recuperação dos IDs de Atualização dos Grupos:**
   ```python
   update_ids = set(deepAIBot.getChatIds())
   ```
   - Obtém os IDs dos grupos que estão atualmente ativos e prontos para receber atualizações.

8. **Atualização dos IDs dos Grupos no Banco de Dados:**
   ```python
   if update_ids - group_ids:
       updated_data = data.copy()
       group_ids = set(group_ids.union(update_ids))
       updated_data['all_ids'] = list(map(str, group_ids))
       updated_data = {"$set": updated_data}
       deepQuiz.update_data(data, updated_data)
   ```
   - Se houver novos grupos ativos, atualiza a lista de IDs de grupo no banco de dados.

9. **Envio da Pergunta do Quiz para os Grupos:**
   ```python
   if quiz_question:
       deepAIBot.sendPoll(group_ids, quiz_question)
   ```
   - Se houver uma pergunta de quiz disponível para o dia atual, envia-a para os grupos.

### DB_CONECTION.PY:
Este é um conjunto de funções para facilitar o upload e busca de dados em um banco de dados MongoDB. 

#### Função upload_data
```python
def upload_data(db_collection, db_database):
    """
    Uploads data to specified MongoDB collection and database.
    
    Parameters:
        db_collection (str): Name of the collection in MongoDB.
        db_database (str): Name of the database in MongoDB.
        
    Returns:
        result: Result of the data insertion operation.
    """
    client = pymongo.MongoClient('mongodb+srv://shubhamagnihotri:test@telegrambot.fdd25em.mongodb.net/test')
    db = client.get_database(db_database)
    col = db.get_collection(db_collection)
    df = pd.read_csv('questions.csv')
    data = json.loads(df.to_json(orient='records'))
    result = col.insert_many(data)
```

#### Função upload_ids
```python
def upload_ids(db_collection, db_database, group_ids):
    """
    Uploads group IDs to specified MongoDB collection and database.
    
    Parameters:
        db_collection (str): Name of the collection in MongoDB.
        db_database (str): Name of the database in MongoDB.
        group_ids (pandas.DataFrame): DataFrame containing group IDs.
        
    Returns:
        result: Result of the data insertion operation.
    """
    client = pymongo.MongoClient('mongodb+srv://shubhamagnihotri:test@telegrambot.fdd25em.mongodb.net/test')
    db = client.get_database(db_database)
    col = db.get_collection(db_collection)
    data = json.loads(group_ids.to_json(orient='records'))
    result = col.insert_many(data)
```

#### Função fetch_data
```python
def fetch_data(query_string, db_collection, db_database):
    """
    Fetches data from specified MongoDB collection and database based on a query string.
    
    Parameters:
        query_string (str): Query string to search data.
        db_collection (str): Name of the collection in MongoDB.
        db_database (str): Name of the database in MongoDB.
        
    Returns:
        dict: Data fetched from the database.
    """
    client = pymongo.MongoClient('mongodb+srv://shubhamagnihotri:test@telegrambot.fdd25em.mongodb.net/test')
    db = client.get_database(db_database)
    col = db.get_collection(db_collection)
    data = col.find_one({"date": query_string})
    if data:
        return {'question': data['question'], 'options': [data['option1'], data['option2'], data['option3'], data['option4']],
                'correctOption': data['correct_answer'], 'explanation': data['explanation']}
    return ""
```

#### Função fetch_ids
```python
def fetch_ids(query_string, db_collection, db_database):
    """
    Fetches IDs from specified MongoDB collection and database based on a query string.
    
    Parameters:
        query_string (str): Query string to search IDs.
        db_collection (str): Name of the collection in MongoDB.
        db_database (str): Name of the database in MongoDB.
        
    Returns:
        dict: IDs fetched from the database.
    """
    client = pymongo.MongoClient('mongodb+srv://shubhamagnihotri:test@telegrambot.fdd25em.mongodb.net/test')
    db = client.get_database(db_database)
    col = db.get_collection(db_collection)
    data = col.find_one({"value": query_string})
    return data
```

Estas funções podem ser usadas para interagir com um banco de dados MongoDB de forma simples e eficiente. Certifique-se de ter as bibliotecas `pandas` e `pymongo` instaladas para executar estas funções corretamente.

## CREDITOS:
* [ESSE BOT FOI CRIADO PELO "KillerStrike17"](https://github.com/KillerStrike17/DeepQuiz-Telegram-Bot)
* [ESSE BOT FOI EDITADO PELO VILHALVA](https://github.com/VILHALVA)