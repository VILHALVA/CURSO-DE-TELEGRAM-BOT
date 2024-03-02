import telebot

TOKEN = "TOKEN_AQUI"
bot = telebot.TeleBot(TOKEN)

def verificar(mensagem):
    return True

@bot.message_handler(commands=["teontologia"])
def teontologia(mensagem):
    bot.send_message(mensagem.chat.id, "Teologia própria, ou teologia propriamente dita, ou teontologia, é o locus (área de estudo) da teologia sistemática que trata do estudo de Deus e, especificamente, de Deus Pai. Suas áreas clássicas de investigação são a questão da existência de Deus, os atributos divinos, a Santíssima Trindade, a doutrina do decreto divino, criação, providência e teodiceia. 🌟SAIBA MAIS: https://pt.wikipedia.org/wiki/Teologia_pr%C3%B3pria")

@bot.message_handler(commands=["cristologia"])
def cristologia(mensagem):
    bot.send_message(mensagem.chat.id, "Cristologia é o estudo sobre Cristo; é uma parte da teologia cristã que estuda e define a natureza de Jesus, a doutrina da pessoa e da obra de Jesus Cristo, com uma particular atenção à relação com Deus, às origens, ao modo de vida de Jesus de Nazaré, visto que estas origens e o papel dentro da doutrina de salvação tem sido objeto de estudo e discussão desde os primórdios do cristianismo. 🌟SAIBA MAIS: https://pt.wikipedia.org/wiki/Cristologia")

@bot.message_handler(commands=["pneumatologia"])
def pneumatologia(mensagem):
    bot.send_message(mensagem.chat.id, "Na Teologia Cristã, pneumatologia se refere ao estudo do Espírito Santo. Na doutrina Cristã popular, o Espírito Santo é a terceira pessoa de Deus na Trindade. Algumas formas de Cristianismo negam que o Espírito Santo seja pessoal, embora assegurando que pode, em algumas ocasiões, influenciar as pessoas. No Evangelho de João, pneuma é unido a renascimento em água e espírito que foram sugeridos para ser o batismo. 🌟SAIBA MAIS: https://pt.wikipedia.org/wiki/Pneumatologia")

@bot.message_handler(commands=["angelologia"])
def angelologia(mensagem):
    bot.send_message(mensagem.chat.id, "No cristianismo, os anjos são agentes de Deus, baseados em anjos no judaísmo. A hierarquia angélica cristã mais influente foi a apresentada por Pseudo-Dionísio, o Areopagita, nos séculos IV ou V, em seu livro De Coelesti Hierarchia (Sobre a Hierarquia Celeste). Durante a Idade Média, muitos esquemas foram propostos sobre a hierarquia dos anjos, alguns recorrendo e expandindo o Pseudo-Dionísio, outros sugerindo classificações completamente diferentes. Segundo os teólogos cristãos medievais, os anjos estão organizados em várias ordens, ou coros angelicais. Pseudo-Dionísio (Sobre a Hierarquia Celestial) e Tomás de Aquino (Suma Teológica) inspiraram-se em passagens do Novo Testamento, especificamente em Gálatas 3:26-28,[carece de fontes] Mateus 22:24-33, Efésios 1:21-23 e Colossenses 1:16, para desenvolver um esquema de três hierarquias, esferas ou tríades de anjos, com cada hierarquia contendo três ordens ou coros. Embora ambos os autores tenham se inspirado no Novo Testamento, o cânone bíblico não é claro sobre o assunto, e essas hierarquias são consideradas menos definitivas do que o material bíblico. Conforme referido na doutrina teológica da comunhão dos santos, no Paraíso existe uma visão comum e única da verdade e contemplação do semblante divino, sem qualquer tipo de diferença entre anjos ou almas humanas. A Suma Teológica afirma que existe um grau diferente em relação à criação, sobre o poder da intercessão a Deus e da confiança direta nas vidas humanas. 🌟SAIBA MAIS: https://pt.wikipedia.org/wiki/Angelologia_crist%C3%A3")

@bot.message_handler(commands=["antropologia"])
def antropologia(mensagem):
    bot.send_message(mensagem.chat.id, "A antropologia (do grego ἄνθρωπος, anthropos, ser humano; e λόγος, logos, razão, pensamento, discurso, estudo) é a ciência que tem como objeto de estudo o ser humano e a humanidade de maneira totalizante, ou seja, abrangendo todas as suas dimensões. 🌟SAIBA MAIS: https://pt.wikipedia.org/wiki/Antropologia")

@bot.message_handler(commands=["hamartiologia"])
def hamartiologia(mensagem):
    bot.send_message(mensagem.chat.id, "Hamartiologia (do grego transliterado hamartia = erro, pecado + logós = estudo), como sugere o próprio nome, é a ciência que estuda o pecado e as suas origens e consequências, ou — se preferível — o estudo sistematizado daquele tema (pecado). Referir, pois, hamartia como pecado no sentido espiritual judaico-cristão justifica-se por sua comprovada presença nos textos do Novo Testamento, da Bíblia Sagrada judaico-cristã, fato comprovável por várias traduções/versões de renome mundial, embora a concepção (logo, o conceito) de pecado, em si, variem com as culturas, posto que com as variadas concepções de espiritualidade e/ou religiosidade. O estudo do pecado e sua origem inevitavelmente incorre na questão da natureza do mal, assim como da relação deste com o homem. Conquanto usualmente concebido como ramo da teologia cristã, não é necessariamente a esta vinculado, pois esse conceito, em sua abrangência, complexidade e diversidade de entendimentos culturais enseja também, necessariamente, várias concepções em seu estudo. É, assim, legítimo investigar a gênese e a dinâmica desse conceito e dos seus valores também sob outras ópticas, como a filosófica e a científica e, neste domínio, a médico-psicológica, todas elas necessariamente entrelaçadas pela ideia comum do pecado, como quer que isso signifique ou importe em particular para cada pessoa, per se e no seu núcleo vivencial. 🌟SAIBA MAIS: https://pt.wikipedia.org/wiki/Hamartiologia")

@bot.message_handler(commands=["soteriologia"])
def soteriologia(mensagem):
    bot.send_message(mensagem.chat.id, "A soteriologia é o estudo da salvação humana. A palavra é formada a partir de dois termos gregos σωτήριος [Soterios], que significa salvação e λόγος [logos], que significa palavra, princípio, ou ensino. Cada religião oferece um tipo diferente de salvação e possui sua própria soteriologia, algumas dão ênfase ao relacionamento do homem em unidade com Deus, outras dão ênfase ao aprimoramento do conhecimento humano como forma de se obter a salvação. O tema da soteriologia é a área da Teologia Sistemática que trata da doutrina da salvação humana.🌟SAIBA MAIS: https://pt.wikipedia.org/wiki/Soteriologia")

@bot.message_handler(commands=["bibliologia"])
def bibliologia(mensagem):
    bot.send_message(mensagem.chat.id, "Bibliologia é a ciência da história e composição dos livros. É o conjunto de conhecimentos e técnicas que abrangem a história do livro, a bibliotecnia, a bibliografia, a bibliotecologia, a biblioteconomia, e a bibliofilia, e se relacionam com a origem, evolução, produção, publicação, descrição, enumeração, conservação, e restauração dos livros, e a organização deles em coleções gerais ou especiais para uso público ou privado. O profissional dessa área é o bibliólogo.🌟SAIBA MAIS: https://pt.wikipedia.org/wiki/Bibliologia")

@bot.message_handler(commands=["eclesiologia"])
def eclesiologia(mensagem):
    bot.send_message(mensagem.chat.id, "Eclesiologia (do grego ekklesia e logos) é o ramo da teologia cristã que trata da doutrina da Igreja: origem, características, marcas, função, organização, forma de governo, disciplina, confessionalidade, ecumenismo com outras igrejas, mudanças temporais, relacionamento com o mundo, papel social etc. 🌟SAIBA MAIS: https://pt.wikipedia.org/wiki/Eclesiologia")

@bot.message_handler(commands=["escatologia"])
def escatologia(mensagem):
    bot.send_message(mensagem.chat.id, "Escatologia (do grego antigo εσχατος, último, mais o sufixo -λόγια, estudo) é uma parte da teologia e filosofia que trata dos últimos eventos na história do mundo ou do destino final do gênero humano, comumente denominado como fim do mundo. Em muitas religiões, o fim do mundo é um evento futuro profetizado no texto sagrado ou no folclore. De forma ampla, escatologia costuma relacionar-se com conceitos tais como Messias ou Era Messiânica, a pós-vida, e a alma. 🌟SAIBA MAIS: https://pt.wikipedia.org/wiki/Escatologia")

@bot.message_handler(func=verificar, commands=["start", "menu"])
def responder(mensagem):
    texto = '''
🖥PRINCIPAIS PROLEGOMENOS:

/teontologia > Doutrina de Deus
/cristologia > Doutrina de Cristo
/pneumatologia > Doutrina do Espirito
/angelologia > Doutrina dos Anjos
/antropologia > Doutrina do Homem
/hamartiologia > Doutina do Pecado
/soteriologia > Doutrina da Salvação
/bibliologia > Doutrina da Bíblia
/eclesiologia > Doutrina da Igreja
/escatologia > Doutrina das ultimas coisas

🌝BASTA APENAS CLICAR EM CIMA DE UMA OPÇÃO!'''
    bot.reply_to(mensagem, texto)
    
bot.polling()