# -*- coding: utf8 -*- 

from datetime import datetime
import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import wikipedia as wiki
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import security
from character import get_random_character
from weather import Get_Weather

updater = Updater(token=security.api_key.get(security.TELEGRAM_KEY), use_context=True)
dispatcher = updater.dispatcher

symbols = 'йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+{}:"<>?,./\\\';]["№%'

# Обработка команд
def helpCommand(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text='/wiki -- поискать что-то на Википедии. \nФорма запроса /wiki <query>. \nПример: /wiki Гагарин\n\n/weather -- показать погоду. Пример запроса: /weather Казань\n\n/roll -- кинуть дайсы. По умолчанию, если не указать параметр границы, выдает рандмное число от 1 до 100.\nЧтобы бросить, например, d20, можно использовать команду /roll 20 (по аналогии /roll 2, /roll 6, /roll 12 и тд).\n\n/spoti -- искать трек на Spotify.\nФорма запроса /spoti <Artist> - <song name>. Если ввести в запросе только исполнителя, бот вернет ссылку на его самый популярный трек. \nПример: /spoti Sovvy - Vitrual Fatboy\n\n/spotiful -- тоже самое, что и /spoti, только вернет полную информацию о треке, исполнителе, а не только ссылку на него.\n\n/social -- показать меню социальных функций.')
    print('[' + str(datetime.now()) + '] BOT (/help): help for user [' +
          update.message.from_user.name + '], from chat [' + update.message.chat.link + ']')


def rollCommand(update, context):
    contain_symbol = False
    message = update.message.text
    if(message.startswith('/roll')):
        tag_index = message.find('@')
        if tag_index != -1:
            message = ''
        else:
            message = message[6:]

    for i in range(len(symbols)):
        if symbols[i] not in message:
            continue
        else:
            contain_symbol = True
            context.bot.send_message(chat_id=update.message.chat_id, text='' +
                             update.message.from_user.name + ', only numbers!')
            print('[' + str(datetime.now()) + '] BOT (/roll): roll INVALID for user [' +
                  update.message.from_user.name + '], from chat [' + update.message.chat.link + ']')
            return

    if message == '':
        roll = random.randint(1, 100)
        context.bot.send_message(chat_id=update.message.chat_id, text='Hey, ' +
                         update.message.from_user.name + ', your roll: [' + str(roll) + ']')
        print('[' + str(datetime.now()) + '] BOT (/roll): roll [' + str(roll) + '] out of [' + str(message) +
              '] for user [' + update.message.from_user.name + '], from chat [' + update.message.chat.link + ']')
    else:
        roll = random.randint(1, int(message))
        context.bot.send_message(chat_id=update.message.chat_id, text='Hey, ' +
                         update.message.from_user.name + ', your roll: [' + str(roll) + ']')
        print('[' + str(datetime.now()) + '] BOT (/roll): roll [' + str(roll) + '] out of [' + str(message) +
              '] for user [' + update.message.from_user.name + '], from chat [' + update.message.chat.link + ']')


def rollCharCommand(update, context):
    message = update.message.text
    if(message.startswith('/roll_char')):
        tag_index = message.find('@')
        if tag_index != -1:
            message = ''
        else:
            message = message[10:]

    for i in range(len(symbols)):
        if symbols[i] not in message:
            continue
        else:
            context.bot.send_message(chat_id=update.message.chat_id, text='' +
                             update.message.from_user.name + ', invalide generated... please sent only /roll_char')
            print('[' + str(datetime.now()) + '] BOT (/roll_char): roll INVALID for user [' +
                  update.message.from_user.name + '], from chat [' + update.message.chat.link + ']')
            return

    if message == '':
        chat_id = update.message.chat_id
        text = ("Hey, " + update.message.from_user.name +
                ", your character roll:\n\n")

        character = get_random_character()
        
        print(character)
        context.bot.send_message(chat_id,
                         text)
        context.bot.send_message(chat_id,
                         character.get('text'),
                         parse_mode="Markdown")
        context.bot.send_photo(chat_id, open(character.get('pic'), 'rb'))

        print('[' + str(datetime.now()) + '] BOT (/roll_char): roll new character for user [' +
              update.message.from_user.name + '], from chat [' + update.message.chat.link + ']')


def spotifulCommand(update, context):
    message = update.message.text
    if(message.startswith('/spotiful')):
        message = message[10:]
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    result = sp.search(message)

    if len(result.get('tracks').get('items')) > 0:
        artist_dict = result.get('tracks').get('items')[0]
        album_dict = result.get('tracks').get('items')[0].get('album')

        artist_name = album_dict.get('artists')[0].get('name')
        artist_link = album_dict.get('artists')[0].get(
            'external_urls').get('spotify')

        album_name = album_dict.get('name')
        album_release_date = album_dict.get('release_date')
        album_link = album_dict.get('external_urls').get('spotify')

        track_name = artist_dict.get('name')
        track_number = artist_dict.get('track_number')
        track_popularity = artist_dict.get('popularity')
        track_link = artist_dict.get('external_urls').get('spotify')

        result_text = ('[ARTIST:]\nArtist Name: ' + artist_name +
                       '\nArtist Link: ' + artist_link +
                       '\n\n[ALBUM:]\nAlbum Name: ' + album_name +
                       '\nRelease Date: ' + str(album_release_date) +
                       '\nAlbum Link: ' + album_link +
                       '\n\n[SONG:]\nTrack Name: ' + str(track_name) +
                       '\nTrack Number: ' + str(track_number) +
                       '\nTrack popularity: ' + str(track_popularity) + '%' +
                       '\nTrack Link: ' + track_link)

        context.bot.send_message(chat_id=update.message.chat_id, text=result_text)
        print('[' + str(datetime.now()) + '] BOT (/spotiful): search result send for user [' +
              update.message.from_user.name + '], from chat [' + update.message.chat.link + ']')
    else:
        context.bot.send_message(chat_id=update.message.chat_id,
                         text='invalid request')
        print('[' + str(datetime.now()) + '] BOT (/spotiful): INVALID REQUEST for user [' +
              update.message.from_user.name + '], from chat [' + update.message.chat.link + ']')


def spotiCommand(update, context):
    message = update.message.text
    if(message.startswith('/spoti')):
        message = message[7:]

    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    result = sp.search(message)

    if len(result.get('tracks').get('items')) > 0:
        artist_dict = result.get('tracks').get('items')[0]
        track_link = artist_dict.get('external_urls').get('spotify')

        context.bot.send_message(chat_id=update.message.chat_id, text=track_link)
        print('[' + str(datetime.now()) + '] BOT (/spoti): search result send for user [' +
              update.message.from_user.name + '], from chat [' + update.message.chat.link + ']')
    else:
        context.bot.send_message(chat_id=update.message.chat_id,
                         text='invalid request')
        print('[' + str(datetime.now()) + '] BOT (/spoti): INVALID REQUEST for user [' +
              update.message.from_user.name + '], from chat [' + update.message.chat.link + ']')


def weatherCommand(update, context):
    message = update.message.text
    if(message.startswith('/weather')):
        tag_index = message.find('@')
        if tag_index != -1:
            message = ''
        else:
            message = message[9:]

    collback = Get_Weather(message)

    chat_id = update.message.chat_id
    username = update.message.from_user.name
    text = 'Хэй, ' + username + ', вот твоя погода в городе ' + collback

    context.bot.send_message(chat_id, text)
    print('[' + str(datetime.now()) + '] BOT (/weather): [' + str(message) + '] from user [' +
          update.message.from_user.name + '], from chat [' + update.message.chat.link + ']')


def wikiCommand(update, context):
    message = update.message.text
    if(message.startswith('/wiki')):
        page = get_wiki(message[6:])

        if(page != 'Not Found'):
            url = page.url
            title = page.title
            content = page.content
            search_index = content.find('\n\n\n')

            context.bot.send_message(chat_id=update.message.chat_id, text='link: ' +
                             url + '\n\nTitle: ' + title + '\n\nContent:\n' + content[:search_index])
            print('[' + str(datetime.now()) + '] BOT (/wiki): Wikipedia summery of [' + message[6:] +
                  '] for user [' + update.message.from_user.name + '], from chat [' + update.message.chat.link + ']')
        else:
            context.bot.send_message(chat_id=update.message.chat_id, text='Not Found')
            print('[' + str(datetime.now()) + '] BOT (/wiki): Wikipedia... Not Found for user [' +
                  update.message.from_user.name + '], from chat [' + update.message.chat.link + ']')
    else:
        context.bot.send_message(
            chat_id=update.message.chat_id, text="{}, Invalid command".format(update.message.from_user.first_name))
        print('[' + str(datetime.now()) + '] BOT (/spoti): Invalid command for user [' +
              update.message.from_user.name + '], from chat [' + update.message.chat.link + ']')


def get_wiki(word):
    try:
        wiki.set_lang('ru')
        return wiki.page(word)
    except:
        return "Not Found"


def snippetCommand(update, context):
    chat_id = update.message.chat_id
    username = update.message.from_user.name
    path = './resources/Bar_Two-D-Bot--Snippet.mp3'
    context.bot.send_audio(chat_id, audio=open(path, 'rb'))


# Добавляем хендлеры в диспетчер
dispatcher.add_handler(CommandHandler('help', helpCommand))
dispatcher.add_handler(CommandHandler('spoti', spotiCommand))
dispatcher.add_handler(CommandHandler('spotiful', spotifulCommand))
dispatcher.add_handler(CommandHandler('snippet', snippetCommand))
dispatcher.add_handler(CommandHandler('roll', rollCommand))
dispatcher.add_handler(CommandHandler('roll_char', rollCharCommand))
dispatcher.add_handler(CommandHandler('wiki', wikiCommand))
dispatcher.add_handler(CommandHandler('weather', weatherCommand))
# Начинаем поиск обновлений
updater.start_polling(clean=True)
print('[' + str(datetime.now()) + '] BOT: bot is up!')
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
