import requests, json

class telegramBot:
  def __init__(self,update_url,poll_url):
     self.update_url = update_url
     self.poll_url = poll_url
  
  def getChatIds(self):
    response = requests.get(self.update_url)
    response.raise_for_status()

    # Extract the chat IDs from the updates
    updates = response.json()['result']
    chat_ids = set()
    print("Updates:",updates)
    for update in updates:
        print(update)
        if 'message' in update and 'chat' in update['message']:
            chat_id = update['message']['chat']['id']
            chat_type = update['message']['chat']['type']
            if chat_type == 'group' or chat_type == 'supergroup':
                chat_ids.add(chat_id)

    # Print the chat IDs
    print('Group chat IDs:')
    allChatIds = []
    for chat_id in chat_ids:
        print(chat_id)
        allChatIds.append(chat_id)
    return allChatIds

  def sendPoll(self,chatIds,quiz):
    for chatId in chatIds:
      parameters = {
          "chat_id":chatId,
          "question":quiz['question'],
          "options":json.dumps(quiz['options']),
          "correct_option_id":quiz['correctOption'],
          "explaination":quiz['explaination'],
          "type":"quiz",
      }
      resp = requests.get(self.poll_url, data=parameters)