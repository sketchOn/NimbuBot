import telebot
import requests
import json
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import nekobin
from nekobin import NekoBin, errors
uHelp = '''Oh! so you want help? 
Here are some of my commads you can use!
My Commads preifix starts from "/"

/start : check whether I am alive!
/help : The command is self exlanatory
/code : Get my precious code!

Below are some of my more commads: 
'''
codeHelp= '''wanna run code snippets?
/charp <code>
/vbnet <code>
/f# <code>
/java <code>
/python <code>
/c <code>
/c++ <code>
/php <code>
/pascal <code>
/objective-c <code>
/haskell <code>
/ruby <code>
/javascript <code>
/swift <code>
/kotlin <code>

'''

# replace with your token
bot = telebot.TeleBot("1690932998:AAHDJIQSfLRBI8iFBDI4TdUeUnSSLNLmCJo")


def gen_markup_welcome():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("🧬 Updates Channel", url='t.me/nethchannel'),
                               InlineKeyboardButton("❤️ Source Code", url='https://github.com/AdityaGupta345/Tg-Sketchware-Bot'))
    return markup

def gen_markup_help():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("🧬 Code Runner", callback_data="run"),
                            InlineKeyboardButton("🧬 Github", callback_data="github"))
    
    return markup

def gen_markup_help_back():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('🔙 Back',callback_data='help_back'))
    return markup

# On inline help click
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
        if (call.data.startswith('run')):
            bot.edit_message_text(chat_id=call.message.chat.id,
                                text=codeHelp,
                                message_id=call.message.message_id,
                                reply_markup=gen_markup_help_back())

        if (call.data.startswith('github')):
            bot.edit_message_text(chat_id=call.message.chat.id,
                                text="Works for github tooo",
                                message_id=call.message.message_id,
                                reply_markup=gen_markup_help_back(),
                                parse_mode='HTML')

        if (call.data.startswith('help_back')):
            bot.edit_message_text(chat_id=call.message.chat.id,
                                text=uHelp,
                                message_id=call.message.message_id,
                                reply_markup=gen_markup_help(),
                                parse_mode='HTML')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    photo = open('images\coder.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
    photo.close()
    bot.send_message(message.chat.id, 'Hello My name is bruh, I can execute your small codes :) . Send /help to knoe more ', reply_markup=gen_markup_welcome())


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, uHelp , reply_markup=gen_markup_help())


@bot.message_handler(commands=['code'])
def send_code_link(message):
    bot.send_message(message.chat.id, 'https://github.com/AdityaGupta345/Tg-Sketchware-Bot')

#################*******#####
def justToMakeCodegood():
    def run(langcode,msgUn,chatID):
        bot.send_chat_action(chatID,'typing')
        langcode = int(langcode)
        search = msgUn.split(" ", maxsplit=1)[1]
        dicte = {
            'languageChoice':langcode,
            'Program': search
        }
        x = requests.post('https://rextester.com/rundotnet/api',dicte)
        result = x.json()
        if (not(result['Result']==None) and len(result['Result'])>=100):
                key = (
                requests.post("https://nekobin.com/api/documents", json={"content": result['Result']})
                .json()
                .get("result")
                .get("key")
                )
                url = "https://nekobin.com/"+key
                reply_text = "Too long result! so Pasted to Nekobin : " + url
                return reply_text

        elif (result['Errors']==None):
            exect = '''*Your result is*

            '''+ '```' + result['Result'] + '```'
            return exect
        else:
            exect = ''' *Errors*

            '''+ '```' + result['Errors'] + '```'

            return exect

    @bot.message_handler(commands=['csharp','C#'])
    def run_csharp(message):
        bot.send_message(message.chat.id,run(1,message.text,message.chat.id), parse_mode='markdown')


    @bot.message_handler(commands=['vbnet'])
    def run_vbNEtmessage(message):
        bot.send_message(message.chat.id,run(2,message.text,message.chat.id), parse_mode='markdown')

    @bot.message_handler(commands=['f#'])
    def fhash(message):
        bot.send_message(message.chat.id,run(3,message.text,message.chat.id), parse_mode='markdown')

    @bot.message_handler(commands=['java'])
    def java(message):
        bot.send_message(message.chat.id,run(4,message.text,message.chat.id) , parse_mode='markdown')

    @bot.message_handler(commands=['python'])
    def python(message):
        bot.send_message(message.chat.id,run(24,message.text,message.chat.id), parse_mode='markdown')

    @bot.message_handler(commands=['c'])
    def c(message):
        bot.send_message(message.chat.id,run(6,message.text,message.chat.id), parse_mode='markdown')


    @bot.message_handler(commands=['c++'])
    def CPLUsPLUS(message):
        bot.send_message(message.chat.id,run(7,message.text,message.chat.id), parse_mode='markdown')

    @bot.message_handler(commands=['php'])
    def php(message):
        bot.send_message(message.chat.id,run(8,message.text,message.chat.id), parse_mode='markdown')

    @bot.message_handler(commands=['pascal'])
    def pascal(message):
        bot.send_message(message.chat.id,run(9,message.text,message.chat.id) , parse_mode='markdown')

    @bot.message_handler(commands=['objective-c'])
    def objectivec(message):
        bot.send_message(message.chat.id,run(10,message.text,message.chat.id),  parse_mode='markdown')

    @bot.message_handler(commands=['haskell'])
    def haskell(message):
        
        bot.send_message(message.chat.id,run(11,message.text,message.chat.id) , parse_mode='markdown')

    @bot.message_handler(commands=['ruby'])
    def ruby(message):
        
        bot.send_message(message.chat.id,run(12,message.text,message.chat.id) , parse_mode='markdown')

    @bot.message_handler(commands=['javascript'])
    def javascript(message):
        
        bot.send_message(message.chat.id,run(17,message.text,message.chat.id) , parse_mode='markdown')

    @bot.message_handler(commands=['swift'])
    def swift(message):
        
        bot.send_message(message.chat.id,run(37,message.text,message.chat.id),parse_mode='markdown')

    @bot.message_handler(commands=['kotlin'])
    def kotlin(message):
        
        bot.send_message(message.chat.id,run(43,message.text,message.chat.id), parse_mode='markdown')
################********#####

justToMakeCodegood()
bot.polling()