import string
from unicodedata import category
from aiogram import types
from dispatcher import dp
import config
import re
from bot import BotDB

@dp.message_handler(commands = "start")
async def start(message: types.Message):
    if(not BotDB.user_exists(message.from_user.id)):
        BotDB.add_user(message.from_user.id)

    await message.bot.send_message(message.from_user.id, "Приветствую тебя, я бот управления финансами, помогу контролировать доход/расход твоих средств.\n Список команд: /help")

@dp.message_handler(commands = ("spent", "earned", "s", "e"), commands_prefix = "/!")
async def start(message: types.Message):
    cmd_variants = (('/spent', '/s', '!spent', '!s'), ('/earned', '/e', '!earned', '!e'))
    operation = '-' if message.text.startswith(cmd_variants[0]) else '+'

    value = message.text
    for i in cmd_variants:
        for j in i:
            value = value.replace(j, '').strip()

    if(len(value)):
        x = re.findall(r"\d+(?:.\d+)?", value)
        if(len(x)):
            value = float(x[0].replace(',', '.'))

            

            if(operation == '-'):
                await message.reply("✅ Запись о <u><b>расходе</b></u> успешно внесена!")
                BotDB.add_record(message.from_user.id, operation, value)
            else:
                await message.reply("✅ Запись о <u><b>доходе</b></u> успешно внесена!")
                BotDB.add_record(message.from_user.id, operation, value)
        else:
            await message.reply("Не удалось определить сумму!")
    else:
        await message.reply("Не введена сумма!")

@dp.message_handler(commands = ("history", "h"), commands_prefix = "/!")
async def start(message: types.Message):
    cmd_variants = ('/history', '/h', '!history', '!h')
    within_als = {
        "day": ('today', 'day', 'сегодня', 'день'),
        "month": ('month', 'месяц'),
        "year": ('year', 'год'),
    }

    cmd = message.text
    for r in cmd_variants:
        cmd = cmd.replace(r, '').strip()

    within = 'day'
    if(len(cmd)):
        for k in within_als:
            for als in within_als[k]:
                if(als == cmd):
                    within = k

    records = BotDB.get_records(message.from_user.id, within)

    if(len(records)):
        answer = f"🕘 История операций за {within_als[within][-1]}\n\n"

        ea = 0
        sp = 0

        for r in records:
            answer += "<b>" + ("➖ Расход" if not r[2] else "➕ Доход") + "</b>"
            answer += f" - {r[3]}"
            answer += f" <i>({r[4]})</i>\n"
            if r[2] == 1:
                ea += r[3]
            if r[2] == 0:
                sp += r[3]
            
        answer += f"<i>Итог за {within_als[within][-1]}: {ea-sp}</i>"

        await message.reply(answer)
    else:
        await message.reply("Записей не обнаружено!")

@dp.message_handler(commands = ("vl", "valute"), commands_prefix = "/!")
async def vl(message: types.Message):
    cmd_variants = ('/valute', '/vl', '!valute', '!vl')
    text = message.text
    summ1 = text[text.find(" "):text.find(";")]
    summ1 = int(summ1)
    val1 = text[text.find(";")+1: text.rfind(";")]
    val2 = text[text.rfind(";")+1: len(text)]

    if val1 == "RUB":
        if val2 == "USD":
            summ2 = summ1*0.013199
            answer = f"{summ1} RUB = {summ2} USD"
            await message.bot.send_message(message.from_user.id, answer)
        elif val2 == "EUR":
            summ2 = summ1*0.011608
            answer = f"{summ1} RUB = {summ2} EUR"
            await message.bot.send_message(message.from_user.id, answer)
        elif val2 == "KZT":
            summ2 = summ1*5.65
            answer = f"{summ1} RUB = {summ2} KZT"
            await message.bot.send_message(message.from_user.id, answer)
        elif val2 == "UAH":
            summ2 = summ1*0.37416
            answer = f"{summ1} RUB = {summ2} UAH"
            await message.bot.send_message(message.from_user.id, answer)
        elif val2 == "BYN":
            summ2 = summ1*0.0339
            answer = f"{summ1} RUB = {summ2} BYN"
            await message.bot.send_message(message.from_user.id, answer)
        else:
            answer = "Данный бот пока не может перевести деньги в данную валюту"
            await message.bot.send_message(message.from_user.id, answer)

    elif val1 == "USD":
        if val2 == "RUB":
            summ2 = summ1*75.76
            answer = f"{summ1} USD = {summ2} RUB"
            await message.bot.send_message(message.from_user.id, answer)
        elif val2 == "EUR":
            summ2 = summ1*0.88324
            answer = f"{summ1} USD = {summ2} EUR"
            await message.bot.send_message(message.from_user.id, answer)
        elif val2 == "KZT":
            summ2 = summ1*428.28
            answer = f"{summ1} USD = {summ2} KZT"
            await message.bot.send_message(message.from_user.id, answer)
        elif val2 == "UAH":
            summ2 = summ1*28.38
            answer = f"{summ1} USD = {summ2} UAH"
            await message.bot.send_message(message.from_user.id, answer)
        elif val2 == "BYN":
            summ2 = summ1*2.57
            answer = f"{summ1} USD = {summ2} BYN"
            await message.bot.send_message(message.from_user.id, answer)
        else:
            answer = "Данный бот пока не может перевести деньги в данную валюту"
            await message.bot.send_message(message.from_user.id, answer)

    elif val1 == "EUR":
        if val2 == "RUB":
            summ2 = summ1*86.15
            answer = f"{summ1} EUR = {summ2} RUB"
            await message.bot.send_message(message.from_user.id, answer)
        elif val2 == "USD":
            summ2 = summ1*1.13
            answer = f"{summ1} EUR = {summ2} USD"
            await message.bot.send_message(message.from_user.id, answer)
        elif val2 == "KZT":
            summ2 = summ1*486.98
            answer = f"{summ1} EUR = {summ2} KZT"
            await message.bot.send_message(message.from_user.id, answer)
        elif val2 == "UAH":
            summ2 = summ1*32.26
            answer = f"{summ1} EUR = {summ2} UAH"
            await message.bot.send_message(message.from_user.id, answer)
        elif val2 == "BYN":
            summ2 = summ1*2.92
            answer = f"{summ1} EUR = {summ2} BYN"
            await message.bot.send_message(message.from_user.id, answer)
        else:
            answer = "Данный бот пока не может перевести деньги в данную валюту"
            await message.bot.send_message(message.from_user.id, answer)

    elif val1 == "KZT":
        if val2 == "RUB":
            summ2 = summ1*0.1769
            answer = f"{summ1} KZT = {summ2} RUB"
            await message.bot.send_message(message.from_user.id, answer)
        elif val2 == "USD":
            summ2 = summ1*0.002335
            answer = f"{summ1} KZT = {summ2} USD"
            await message.bot.send_message(message.from_user.id, answer)
        elif val2 == "EUR":
            summ2 = summ1*0.002054
            answer = f"{summ1} KZT = {summ2} EUR"
            await message.bot.send_message(message.from_user.id, answer)
        elif val2 == "UAH":
            summ2 = summ1*0.066289
            answer = f"{summ1} KZT = {summ2} UAH"
            await message.bot.send_message(message.from_user.id, answer)
        elif val2 == "BYN":
            summ2 = summ1*0.00599
            answer = f"{summ1} KZT = {summ2} BYN"
            await message.bot.send_message(message.from_user.id, answer)
        else:
            answer = "Данный бот пока не может перевести деньги в данную валюту"
            await message.bot.send_message(message.from_user.id, answer)

    elif val1 == "UAH":
        if val2 == "RUB":
            summ2 = summ1*2.67
            answer = f"{summ1} UAH = {summ2} RUB"
            await message.bot.send_message(message.from_user.id, answer)
        elif val2 == "USD":
            summ2 = summ1*0.035241
            answer = f"{summ1} UAH = {summ2} USD"
            await message.bot.send_message(message.from_user.id, answer)
        elif val2 == "EUR":
            summ2 = summ1*0.030993
            answer = f"{summ1} UAH = {summ2} EUR"
            await message.bot.send_message(message.from_user.id, answer)
        elif val2 == "KZT":
            summ2 = summ1*15.09
            answer = f"{summ1} UAH = {summ2} KZT"
            await message.bot.send_message(message.from_user.id, answer)
        elif val2 == "BYN":
            summ2 = summ1*0.0906
            answer = f"{summ1} UAH = {summ2} BYN"
            await message.bot.send_message(message.from_user.id, answer)
        else:
            answer = "Данный бот пока не может перевести деньги в данную валюту"
            await message.bot.send_message(message.from_user.id, answer)

    elif val1 == "BYN":
        if val2 == "RUB":
            summ2 = summ1*29.5
            answer = f"{summ1} BYN = {summ2} RUB"
            await message.bot.send_message(message.from_user.id, answer)
        elif val2 == "USD":
            summ2 = summ1*0.38947
            answer = f"{summ1} BYN = {summ2} USD"
            await message.bot.send_message(message.from_user.id, answer)
        elif val2 == "EUR":
            summ2 = summ1*0.34244
            answer = f"{summ1} BYN = {summ2} EUR"
            await message.bot.send_message(message.from_user.id, answer)
        elif val2 == "KZT":
            summ2 = summ1*166.83
            answer = f"{summ1} BYN = {summ2} KZT"
            await message.bot.send_message(message.from_user.id, answer)
        elif val2 == "UAH":
            summ2 = summ1*11.04
            answer = f"{summ1} BYN = {summ2} UAH"
            await message.bot.send_message(message.from_user.id, answer)
        else:
            answer = "Данный бот пока не может перевести деньги в данную валюту"
            await message.bot.send_message(message.from_user.id, answer)

    else:
        answer = "Данный бот пока не может перевести деньги в данную валюту"
        await message.bot.send_message(message.from_user.id, answer)

@dp.message_handler(commands = ("hl", "help"), commands_prefix = "/!")
async def help(message: types.Message):
    cmd_variants = ('/help', '/hl', '!help', '!hl')
    answer = f"Список всех команд:\n /e *сумма* - запись дохода\n/s *сумма* - запись расхода\n/h *день, месяц, год* - история операций\n/vl *сумма;валюта из которой переводить;валюта в которую переводить* - перевод валюты (например: 1;USD;RUB)\n(Расчет валюты производится исходя из курса валют на момент 20.02.2022, доступные валюты: RUB, BYN, KZT, USD, EUR, UAH)"
    await message.bot.send_message(message.from_user.id, answer)
