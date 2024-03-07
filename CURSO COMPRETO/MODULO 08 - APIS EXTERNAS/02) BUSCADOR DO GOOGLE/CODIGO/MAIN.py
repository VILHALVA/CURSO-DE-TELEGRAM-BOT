from bs4 import BeautifulSoup
import requests
import telebot
from TOKEN import TOKEN

bot = telebot.TeleBot(TOKEN)

def busar_google(texto):
    lista = []
    user_agent = 'mozilla/5.0 (Windows NT 10; win64 x64) Applewebkit/537.36(KHTML, like)'
    headers = {
        "User_Agent": user_agent,
        'referer': 'https://www.google.com/' 
    }
    
    texto_url = texto.replace(" ", "+")
    url = f'https://www.google.com/search?q={texto_url}&num=50'
    r = requests.get(url, headers=headers, timeout=10)
    if r.ok:
        soup = BeautifulSoup(r.text, "html.parser")
        elementos = soup.find_all("div", {"class": "g"})
        for e in elementos:
            try:
                titulo = e.find_all("h3")[-1].text.split()
            except:
                continue
            
            descricao = e.find_all("span")[-1].text.split() 
            enlace = e.find("a").attrs.get("href")
            if titulo and enlace and not(titulo, descricao, enlace) in lista:
                lista.append((titulo, descricao, enlace))

    print(f"ENCONTRADOR {len(lista)} RESULTADOS!")
    return lista

@bot.message_handler(commands=["start"])
def start(m):
    bot.send_message(m.chat.id, "Olá! Para pesquisar no Google, envie /google seguido do assunto.")

@bot.message_handler(commands=["google"])
def google(m):
    if not m.text.split()[1]:
        bot.send_message(m.chat.id, "Por favor, envie o assunto da sua pesquisa.")
        return
    texto = m.text.split()[1]
    res = busar_google(texto)
    if not res:
        bot.send_message(m.chat.id, "Nenhum resultado encontrado.")
        return
    bot.send_message(m.chat.id, "Resultados da pesquisa:")
    for titulo, descricao, url in res:
        bot.send_message(m.chat.id, f"**Título:** {titulo}\n**Descrição:** {descricao}\n**Link:** {url}")
        
if __name__ == "__main__":
    bot.polling()
