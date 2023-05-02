from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import User, message
from aiogram.contrib.fsm_storage import memory
import speech_recognition as sr
import re
from fuzzywuzzy import fuzz
import uuid
import os

bot = Bot(token="5966383080:AAEuSbZUiPItzRtfohgIvVflRd1ZFd52d1Q")
dp = Dispatcher(bot)

text_a = "Становясь верноподданным Его Величества Императора Драга Первого Великолепного я обязываюсь выполнять его поручения и поручения начальников Имперской гвардии. Также я заявляю о готовности пройти все тяготы службы и покинуть службу в любой момент по приказу Императора. Для меня будет честью служить Империи и я не просрамлю гордого знамени, которое мне доверил Император, искореняя как внешних, так и внутренних врагов режима, я с доблестью пройду предначертанный мне путь."

text_a = re.sub(r'[^\w\s]', '', text_a)
text_a = text_a.strip()
text_a = text_a.lower()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user = message.from_user
    first_name = user.first_name
    user_id = user.id
    username = user.username
    await message.answer(f"Добро пожаловать {first_name}\nТвой ID: {user_id}")
    await message.answer("<b>Гвардейцы - люди, охраняющие порядок и закон в чате. Если хочешь стать одним из них - пройди ряд процедур.</b>", parse_mode='HTML')
    await message.answer("<b>Процедура 1.</b>\nПрисягни на верность нашему Императору.<i>Четко и без спешки запиши голосовым сообщением следующий текст:</i>", parse_mode='HTML')
    await message.answer("<b>Становясь верноподданным Его Величества Императора Драга Первого Великолепного я обязываюсь выполнять его поручения и поручения начальников Имперской гвардии. Также я заявляю о готовности пройти все тяготы службы и покинуть службу в любой момент по приказу Императора. Для меня будет честью служить Империи и я не просрамлю гордого знамени, которое мне доверил Император, искореняя как внешних, так и внутренних врагов режима, я с доблестью пройду предначертанный мне путь.</b>", parse_mode='HTML')

@dp.message_handler(content_types=['voice'])
async def handle_voice_message(message):
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
        # await message.answer(f"Текст сообщения: {text_b}")
    except sr.UnknownValueError:
        await message.answer("Не удалось распознать речь")
    except sr.RequestError:
        await message.answer("Ошибка при обращении к API распознавания речи")
    text_b = re.sub(r'[^\w\s]','', text_b)
    text_b = text_b.strip()
    text_b = text_b.lower()
    text_fw1 = fuzz.ratio(text_a, text_b)
    text_fw2 = fuzz.partial_ratio(text_a, text_b)
    text_fw3 = fuzz.token_sort_ratio(text_a, text_b)
    text_fw4 = fuzz.token_set_ratio(text_a, text_b)
    text_fw5 = fuzz.WRatio(text_a, text_b)
    await message.answer(f"Текст голоса: {text_b}")
    await message.answer(f"Текст оригинала: {text_a}")
    await message.answer(f"Простое сравнение: {text_fw1}%")
    await message.answer(f"Частичное сравнение: {text_fw2}%")
    await message.answer(f"Сравнение по токену(по словам): {text_fw3}%")
    await message.answer(f"Сравнение по токену(по словам игнорируя повторы): {text_fw4}%")
    await message.answer(f"Продвинутое сравнение: {text_fw5}%")
    new_file.close()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)