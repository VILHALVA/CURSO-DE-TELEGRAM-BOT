# CONVERSA.py

class ConversationHandler:
    @staticmethod
    def generate_response(input_text):
        responses = {
            "Olá": "Olá! Como posso ajudar?",
            "Qual é o seu nome?": "Meu nome é Botinho.",
            "Como você está?": "Estou bem, obrigado por perguntar!",
            "O que você pode fazer?": "Posso fornecer informações básicas, contar piadas e muito mais!",
            "Tchau": "Até logo! Se precisar de mais alguma coisa, estarei aqui.",
            "Qual é a sua idade?": "Sou um bot e não tenho idade.",
            "Você é humano?": "Não, sou um bot.",
            "Onde você mora?": "Moro na internet!",
            "Você gosta de música?": "Como sou um bot, não posso ouvir música, mas posso te ajudar a encontrar algumas!",
            "Você pode me contar uma piada?": "Claro! Por que o programador foi para o bar? Porque precisava de um byte!",
            "Você pode me ajudar com matemática?": "Sim, posso ajudar com problemas simples de matemática!",
            "Como posso aprender programação?": "Existem muitos recursos online gratuitos, como tutoriais e cursos, para aprender programação!",
            "Qual é o seu filme favorito?": "Como sou um bot, não assisto filmes, mas posso recomendar alguns!",
            "Você pode me ajudar a encontrar um restaurante?": "Sim, posso te ajudar a encontrar um restaurante próximo!",
            "Você pode me dizer uma curiosidade?": "Claro! Sabia que o DNA humano é aproximadamente 99,9% idêntico em todas as pessoas?",
            "Como eu posso te chamar?": "Você pode me chamar de Botinho!",
            "Você sabe falar outros idiomas?": "Sim, posso entender e responder em vários idiomas!",
            "Você gosta de jogos?": "Como sou um bot, não posso jogar, mas posso te ajudar a encontrar alguns jogos divertidos!",
            "Você pode me ajudar a encontrar informações sobre um tópico específico?": "Sim, posso ajudar a encontrar informações sobre uma variedade de tópicos!",
            "Você é inteligente?": "Sou programado para fornecer respostas úteis e precisas, mas você pode me chamar de inteligente se quiser!"
            # Adicione mais perguntas e respostas conforme necessário!
        }

        return responses.get(input_text, "Desculpe, não entendi. Tente outra pergunta!")
