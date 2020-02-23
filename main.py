import telebot
from datetime import datetime
from datetime import date
from datetime import timedelta
import os

from constants import *

now = datetime.now()
list_user = []
quantity_users = 0
bot = telebot.TeleBot(Token)

print("Прога запущена")
infobot = bot.get_me()
print(f"id: {infobot.id} name: {infobot.first_name}")


def log(message):
    print("\n------")
    print(datetime.now().isoformat(timespec='minutes'))
    print(f"Сообщение от {message.from_user.first_name} {message.from_user.last_name}\nтекст = {message.text}")




@bot.message_handler(commands=['start'])
def handle_start(message):
    global quantity_users, list_user
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row(u'Следующая пара!\U000027A1')
    user_markup.row(u"Текущая пара!\U0001F55B", u"Сегоднешнее расписание!\U0001F558")
    user_markup.row(u"Завтрашнее расписание!\U0001F55B",
                    u"Полное расписание семестра!\U0001F4C5")
    bot.send_message(message.from_user.id, "Чего изволите, милорд?", reply_markup=user_markup)
    if not message.from_user.first_name in list_user:
        list_user.append(
                  (message.from_user.first_name,
                   message.from_user.last_name,
                   message.from_user.id))
        quantity_users += 1
    log(message)


@bot.message_handler(commands= ['stop'])
def handle_stop(message):
    hide_markup = telebot.types.ReplyKeyboardMarkup()
    bot.send_message(message.from_user.id,"Ваш слуга отключен!", reply_markup=hide_markup)
    log(message)

@bot.message_handler(commands=['statistics'])
def handle_statistics(message):
    text = ''
    for user in list_user:
        first_name, last_name, user_id = user
        text += f'Имя-{first_name} Фамилия-{last_name} id-{user_id}\n'
    bot.send_message(message.from_user.id,
    f"Ботом воспользовались: {quantity_users} человек\n\n{text}")
    log(message)

@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    print(message.sticker.file_id)
    log(message)

@bot.message_handler(content_types=['text'])
def handle_message(message):
    from datetime import time
    global now
    week = what_week(now.date())
    weekday = now.isoweekday()
    have_lessons = True

    if message.text == u"Следующая пара!\U000027A1":
        if week == 1 and weekday != 7:
            day = FTimetable[weekday]
            have_lessons = next_lesson(message, day, now)

        elif week == 2 and weekday != 7:
            day = STimetable[weekday]
            have_lessons = next_lesson(message, day, now)

        if weekday == 7: bot.send_message(message.from_user.id, u"Сегодня воскресенье! отдыхай ты заслужил! \U0001F60E")

    elif message.text == u"Текущая пара!\U0001F55B":
        if week == 1 and weekday != 7:
            day = FTimetable[weekday]
            have_lessons = current_lesson(message, day, now)

        elif week == 2 and weekday != 7:
            day = STimetable[weekday]
            have_lessons = current_lesson(message, day, now)

        if weekday == 7: bot.send_message(message.from_user.id, u"Сегодня воскресенье! отдыхай ты заслужил! \U0001F60E")

    elif message.text == u"Сегоднешнее расписание!\U0001F558":
        if week == 1 and weekday != 7:
            day = FTimetable[weekday]
            bot.send_message(message.from_user.id, string_message(day), parse_mode="Markdown")
        if week == 2 and weekday != 7:
            day = STimetable[weekday]
            bot.send_message(message.from_user.id, string_message(day), parse_mode="Markdown")
        if weekday == 7: bot.send_message(message.from_user.id, u"Сегодня воскресенье! Отдыхай, ты заслужил! \U0001F60E")

    elif message.text == u"Завтрашнее расписание!\U0001F55B":
        if week == 1 and weekday != 6 and weekday != 7:
            day = FTimetable[weekday+1]
            bot.send_message(message.from_user.id, string_message(day), parse_mode="Markdown")
        elif week == 1 and weekday ==  6 and weekday == 7:
            day = STimetable[1]
            bot.send_message(message.from_user.id, string_message(day), parse_mode="Markdown")
        elif week == 2 and weekday != 6 and weekday != 7:
            day = STimetable[weekday+1]
            bot.send_message(message.from_user.id, string_message(day), parse_mode="Markdown")
        elif week == 2 and (weekday == 6 or weekday == 7):
            day = FTimetable[1]
            bot.send_message(message.from_user.id, string_message(day), parse_mode="Markdown")

    elif message.text == u"Полное расписание семестра!\U0001F4C5":
        directory = os.getcwd()
        all_files_in_directory = os.listdir(f"{directory}\\resource")
        for file in all_files_in_directory:
            img = open(directory + '/resource' +'/' + file, 'rb')
            bot.send_photo(message.from_user.id, img)
            img.close()

    if have_lessons == False: bot.send_message(message.from_user.id, "Пар нет, можешь расслабиться!")
    log(message)



def what_week(now_date):
    zero_date = date(2020,2,17)
    week = 1
    num_day = abs(zero_date - now_date)
    week = (week + zero_date.toordinal() // 7) % 2

    return 1 if week == 1 else 2

def current_lesson(message ,day, now):
    for i in range(len(day)):
        TIME =time.fromisoformat(day[i]['time'])
        last_lesson_time = datetime.fromisoformat(f"0001-01-01 {day[-1]['time']}") + timedelta(hours=1,minutes=30)
        if day[i] != day[-1] and time.fromisoformat(day[i+1]['time']) >= now.time() > time.fromisoformat(day[i]['time']):
            bot.send_message(message.from_user.id,
            f"{i+1}) *{day[i]['time']}* - *{day[i]['lesson']}* - `{day[i]['cabinet']} каб`",parse_mode="Markdown")
            return True
        elif day[i] == day[-1] and last_lesson_time.time() >= now.time() > time.fromisoformat(day[-1]['time']):
            bot.send_message(message.from_user.id,
            f"{i+1}) *{day[i]['time']}* - *{day[i]['lesson']}* - `{day[i]['cabinet']} каб`", parse_mode="Markdown")
            return True
    return False


def next_lesson(message, day, now):
    for i in range(len(day)):
        TIME = time.fromisoformat(day[i]['time'])
        if now.time() < TIME:
            bot.send_message(message.from_user.id,
            f"{i+1}) *{day[i]['time']}* - *{day[i]['lesson']}* - `{day[i]['cabinet']} каб`", parse_mode="Markdown")
            return True
    return False

def string_message(day):
    result = ""
    for i in range(len(day)):
        result += f"{i+1}) *{day[i]['time']}* - *{day[i]['lesson']}* - `{day[i]['cabinet']} каб`\n"
    return result




bot.polling(none_stop=True, interval=0)
