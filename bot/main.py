import telebot
import news

TOKEN = '1640582466:AAHo8fSHkLrikM3j5rGJbCFjGoXc4QjiOHQ'

bot = telebot.TeleBot(TOKEN, parse_mode='html')

# Main Markup
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Показать новые новости')
# Category Markup
keyboard2 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
for category in news.CATEGORIES:
    keyboard2.row(category)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'показать новые новости':
        bot.send_message(message.chat.id, 'Choose category:',
                         reply_markup=keyboard2)
    elif message.text.lower() in news.CATEGORIES:
        loadedNews = news.loadTopNews(message.text.lower())
        for article in loadedNews:
            bot.send_message(
                message.chat.id, 
                '<b>' + article['title'] + '</b>\n\n' + 
                article['content'] + '\n\n' + 
                '<a href="' + article['url'] + '">Подробнее</a>', reply_markup=keyboard1)

print('Starting Bot')        
bot.polling()

