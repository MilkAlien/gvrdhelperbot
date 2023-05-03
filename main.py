from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import speech_recognition as sr
import re
from fuzzywuzzy import fuzz
import uuid
import os
import msg


bot = Bot(token="5966383080:AAEuSbZUiPItzRtfohgIvVflRd1ZFd52d1Q")
dp = Dispatcher(bot, storage = MemoryStorage())

chat_id = "-973011111"

text_a = "Становясь верноподданным Его Величества Императора Драга Первого Великолепного я обязываюсь выполнять его поручения и поручения начальников Имперской гвардии. Также я заявляю о готовности пройти все тяготы службы и покинуть службу в любой момент по приказу Императора. Для меня будет честью служить Империи и я не просрамлю гордого знамени, которое мне доверил Император, искореняя как внешних, так и внутренних врагов режима, я с доблестью пройду предначертанный мне путь."
text_a = re.sub(r'[^\w\s]', '', text_a)
text_a = text_a.split()
text_a = ''.join(text_a)
text_a = text_a.lower()

class ProfileStatesGroup(StatesGroup):

    voice = State()
    state2 = State()
    state3 = State()
    state4 = State()
    sp_state1 = State()
    sp_state2 = State()
    sp_state3 = State()
    sp_state4 = State()
    sp_state5 = State()
    sp_state6 = State()
    sp_state7 = State()
    sp_state8 = State()
    sp_state9 = State()
    sp_state10 = State()
    sp_state11 = State()
    sp_state12 = State()
    sp_state13 = State()
    sp_state14 = State()
    sp_state15 = State()
    sp_state16 = State()
    sp_state17 = State()
    sp_state18 = State()
    sp_state19 = State()
    sp_state20 = State()
    sp_state21 = State()
    sp_state22 = State()
    sp_state23 = State()
    sp_state24 = State()
    sp_state25 = State()
    sp_state26 = State()
    sp_state27 = State()
    sp_state28 = State()
    sp_state29 = State()
    sp_state30 = State()

def rm_kb() -> ReplyKeyboardRemove:
    rkb = ReplyKeyboardRemove()
    return rkb
def get_kb2() -> ReplyKeyboardMarkup:
    kb2 = ReplyKeyboardMarkup(resize_keyboard=True)
    kb2.add(KeyboardButton("Начать курс модерации"))
    return kb2
def get_kb3() -> ReplyKeyboardMarkup:
    kb3 = ReplyKeyboardMarkup(resize_keyboard=True)
    kb3.add(KeyboardButton("Готов!"))
    return kb3
def get_kb4() -> ReplyKeyboardMarkup:
    kb4 = ReplyKeyboardMarkup(resize_keyboard=True)
    kb4.add(KeyboardButton("Перейти в четвертый этап"))
    return kb4
@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message) -> None:
    user = message.from_user
    first_name = user.first_name
    user_id = user.id
    username = user.username
    await message.answer(f"Добро пожаловать {first_name}\nТвой ID: {user_id}", reply_markup=rm_kb())
    with open("./data.py", "a+", encoding="utf-8") as data_file:
            await message.answer(f"Проверка базы...")
    with open("./data.py", "r", encoding="utf-8") as data_file:
        value_ok = f"{user_id}:voice_ok"
        text_data = data_file.read()
        if value_ok in text_data:
            await message.answer(f"✅Успех!", reply_markup=get_kb2())
            await ProfileStatesGroup.state2.set()
        else:
            await message.answer(f"❌Провал!")
            await message.answer(
                "<b>Гвардейцы</b> - <i>люди, охраняющие порядок и закон в чате. Если хочешь стать одним из них - пройди ряд процедур.</i>",
                parse_mode='HTML')
            await message.answer(
                "<b>Процедура 1.</b>\nПрисягни на верность нашему Императору.<i>Четко и без спешки запиши голосовым сообщением следующий текст:</i>",
                parse_mode='HTML')
            await message.answer(
                "<b>Становясь верноподданным Его Величества Императора Драга Первого Великолепного я обязываюсь выполнять его поручения и поручения начальников Имперской гвардии. Также я заявляю о готовности пройти все тяготы службы и покинуть службу в любой момент по приказу Императора. Для меня будет честью служить Империи и я не просрамлю гордого знамени, которое мне доверил Император, искореняя как внешних, так и внутренних врагов режима, я с доблестью пройду предначертанный мне путь.</b>",
                parse_mode='HTML')
            await ProfileStatesGroup.voice.set()


@dp.message_handler(content_types=['voice'], state=ProfileStatesGroup.voice)
async def handle_voice_message(message: types.Message, state: FSMContext) -> None:
    await message.answer("Идет распознавание голоса...")
    # os.mkdir("./voice/")
    # os.mkdir("./ready/")
    filename = str(uuid.uuid4())
    file_name_full="./voice/"+filename+".ogg"
    file_name_full_converted="./ready/"+filename+".wav"
    file_info = await bot.get_file(message.voice.file_id)
    downloaded_file = await bot.download_file(file_info.file_path)
    with open(file_name_full, 'wb') as new_file:
        new_file.write(downloaded_file.getvalue())
    os.system("ffmpeg -i "+file_name_full+"  "+file_name_full_converted)
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_name_full_converted) as source:
        audio = recognizer.record(source)
    try:
        text_b = recognizer.recognize_google(audio, language='ru-RU')
    except sr.UnknownValueError:
        await message.answer("Не удалось распознать речь")
    except sr.RequestError:
        await message.answer("Ошибка при обращении к API распознавания речи")
    text_b = re.sub(r'[^\w\s]','', text_b)
    text_b = text_b.split()
    text_b = ''.join(text_b)
    text_b = text_b.lower()
    text_fw1 = fuzz.ratio(text_a, text_b)
    text_fw2 = fuzz.partial_ratio(text_a, text_b)
    text_fw3 = fuzz.token_sort_ratio(text_a, text_b)
    text_fw4 = fuzz.token_set_ratio(text_a, text_b)
    text_fw5 = fuzz.WRatio(text_a, text_b)
    if (text_fw1 >= 90):
        if (text_fw2 >= 90):
            if (text_fw3 >= 90):
                if (text_fw4 >= 90):
                    if (text_fw5 >= 90):
                        await message.answer(f"✅Успех!\nСовпадение: {text_fw1}%", reply_markup=get_kb2())
                        user = message.from_user
                        first_name = user.first_name
                        user_id = user.id
                        username = user.username
                        await bot.send_message(chat_id, f"Имя: {first_name}\nНик: @{username}\nID: {user_id}\n✅Успех!\nПростое сравнение: {text_fw1}%\nЧастичное сравнение: {text_fw2}%\nСравнение по токену(по словам): {text_fw3}%\nСравнение по токену(по словам игнорируя повторы): {text_fw4}%\nПродвинутое сравнение: {text_fw5}%")
                        with open(r"./voice/"+filename+".ogg", "rb") as audio:
                            await bot.send_audio(chat_id, audio)
                        with open("./data.py", "a+", encoding="utf-8") as data_file:
                            data_file.write(f'{first_name}:{username}:{user_id}:voice_ok\n')
                        await ProfileStatesGroup.next()
    else:
        await message.answer(f"❌Провал!\nПовтори еще раз!")
        user = message.from_user
        first_name = user.first_name
        user_id = user.id
        username = user.username
        await bot.send_message(chat_id, f"Имя: {first_name}\nНик: @{username}\nID: {user_id}\n❌Провал!\nПростое сравнение: {text_fw1}%\nЧастичное сравнение: {text_fw2}%\nСравнение по токену(по словам): {text_fw3}%\nСравнение по токену(по словам игнорируя повторы): {text_fw4}%\nПродвинутое сравнение: {text_fw5}%")
        with open(r"./voice/" + filename + ".ogg", "rb") as audio:
            await bot.send_audio(chat_id, audio)

@dp.message_handler(state=ProfileStatesGroup.state2)
async def handle_state2_message(message: types.Message, state: FSMContext) -> None:
    await message.answer(f"Процедура 3\nДобро пожаловать в курс модерации!\nТебе нужно ..... готов?", reply_markup=get_kb3())
    await ProfileStatesGroup.next()

@dp.message_handler(state=ProfileStatesGroup.state3)
async def handle_state3_message(message: types.Message, state: FSMContext) -> None:
    await message.answer("3333333333...")
    await ProfileStatesGroup.next()

@dp.message_handler(state=ProfileStatesGroup.state4)
async def handle_state4_message(message: types.Message, state: FSMContext) -> None:
    await message.answer("44444444...")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)