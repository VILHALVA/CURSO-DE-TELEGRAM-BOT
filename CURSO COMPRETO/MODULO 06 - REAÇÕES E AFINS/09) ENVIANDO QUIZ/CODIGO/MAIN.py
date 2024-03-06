from TELEGRAM_BOT import telegramBot
from DB_CONECTION import databaseConnect
from CRENDECIAIS import update_URL, poll_URL,db_quiz,db_ids, db_database,client_url
from datetime import datetime

# current dateTime
if __name__ =="__main__":
    now = datetime.now()
    date_time_str = str(now.strftime("%d-%m-%Y"))
    # date_time_str = "27-04-2023"
    deepQuiz = databaseConnect(db_database, client_url)
    deepQuiz.collection_connect(db_quiz)
    data = deepQuiz.fetch_data(date_time_str)
    quiz_question =  {'question':data['question'],
                      'options':[data['option1'],data['option2'],data['option3'],data['option4']],
                      'correctOption':data['correct_answer'],'explaination':data['explaination']}
    
    # print(quiz_question)
    # groupid_db = databaseConnect(db_database, client_url)
    deepQuiz.collection_connect(db_ids)
    data = deepQuiz.fetch_data()
    group_ids = set(data['all_ids'])
    # print("group_ids:",group_ids)
    deepAIBot = telegramBot(update_URL,poll_URL)
    update_ids = set(deepAIBot.getChatIds())
    # print("Update Ids:",update_ids)
    
    if update_ids-group_ids:
        updated_data = data.copy()
        group_ids = set(group_ids.union(update_ids))
        updated_data['all_ids'] = list(map(str,group_ids))
        updated_data = {"$set":updated_data}
        deepQuiz.update_data(data,updated_data)

    if quiz_question:
        deepAIBot.sendPoll(group_ids,quiz_question)





