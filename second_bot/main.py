from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram import types
from keyboards.default import default_key
from aiogram.dispatcher import FSMContext
from .keyboard import inlin_k,cal,admin
from loader import db as dp
from loader import bot
from state.state import start_s, Admin
# kurslar
global users
users = ['1999579475']
KURS = ['BIOLOGIYA','KIMYO','ONATILI VA ADABIYOT','TARIX','MATEMATIKA','INGLIZ-TILI','RUS-TILI']
#bo`limlar
class state1(StatesGroup):
    ism = State()
    kurs = State()
    nomer = State()
    manzil = State()
    maktab = State()
    vaqt = State()
    yuborish = State()
admins = [981154238]
@dp.callback_query_handler(cal.filter(),state='*')
async def qab(msg:types.CallbackQuery,state: FSMContext,callback_data: dict):
    if callback_data.get('qabul') == 'qb':
        await bot.send_message(chat_id=callback_data.get('id'),text='siz yuborgan so`rov qabul qilindi')
        users.append(callback_data.get('id'))
    if callback_data.get('qabul') == 'rd':
        await bot.send_message(chat_id=callback_data.get('id'),text='siz yuborgan so`rov RAD qilindi')
        if callback_data.get('id') in users:
            users.remove(callback_data.get('id'))
@dp.message_handler(commands=['start'],state='*')
async def start(msg:types.Message,state: FSMContext):

    await state.update_data({'ism':'ali'})
    data = await state.get_data()
    print(data, users, msg.chat.id)
    if len(data)>0 and str(msg.chat.id) in users:
        markup = await default_key.start()
        await bot.send_message(msg.chat.id, 'NIMA KERAGLIGINI TANLANG!', reply_markup=markup)
        await start_s.start.set()
    elif msg.chat.id in admins:
        markup = await admin()
        await bot.send_message(msg.chat.id,'Malumot kelishini kuting',reply_markup=markup)
        await Admin.kutish.set()
    else:
        await msg.reply('ism sharifingizni kriting')
        await state1.ism.set()
@dp.message_handler(state=Admin.kutish)
async def ism(msg:types.Message, state: FSMContext):
    if msg.text == 'Elon yuborish':
        await Admin.elon.set()
        await msg.reply('Eloni yuboring')
    else:
        await bot.send_message(msg.chat.id, 'Malumot kelishini kuting')
@dp.message_handler(state=Admin.elon)
async def ism(msg:types.Message, state: FSMContext):
    markup = await admin()
    try:
        for user in users:
            await bot.send_message(user,msg.text, reply_markup='html')
    except Exception as ex:
        print(ex)
    await msg.reply('Elon yuborildi',reply_markup=markup)
    await Admin.kutish.set()
@dp.message_handler(state=state1.ism)
async def ism(msg:types.Message, state: FSMContext):
    k_tugma = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    for i in KURS:
        tugma_b = KeyboardButton(text=i)
        k_tugma.insert(tugma_b)
    ism = msg.text
    await state.update_data(
        {'ism':ism}
    )
    await bot.send_message(msg.chat.id,'kursni tanlang', reply_markup=k_tugma)
    await state1.kurs.set()

@dp.message_handler(state=state1.kurs)
async def kurs(msg:types.Message, state: FSMContext):
    await state.update_data(
        {'kurs': msg.text}
    )
    k_tugma = ReplyKeyboardMarkup( resize_keyboard=True)
    b_tugma = KeyboardButton(text='telefon raqam', request_contact=True)
    k_tugma.insert(b_tugma)
    await bot.send_message(msg.chat.id,'no`meringni krit', reply_markup=k_tugma)
    await state1.next()
@dp.message_handler(state=state1.nomer,content_types=['contact'])
async def nomer(msg:types.Message, state: FSMContext):
    await state.update_data(
        {'nomer': msg.contact.phone_number}
    )
    k_tugma = ReplyKeyboardMarkup(resize_keyboard=True)
    b_tugma = KeyboardButton(text='manzil', request_location=True)
    k_tugma.insert(b_tugma)
    await bot.send_message(msg.chat.id, 'manzilni krit', reply_markup=k_tugma)
    await state1.next()
@dp.message_handler(state=state1.nomer)
async def nomer(msg:types.Message, state: FSMContext):
    if len(msg.text) == 13 and msg.text[0] =='+':
        await state.update_data(
            {'nomer': msg.text}
        )
        k_tugma = ReplyKeyboardMarkup(resize_keyboard=True)
        b_tugma = KeyboardButton(text='manzil', request_location=True)
        k_tugma.insert(b_tugma)
        await bot.send_message(msg.chat.id, 'manzilni krit', reply_markup=k_tugma)
        await state1.next()
    else:
        await bot.send_message(msg.chat.id, 'raqamni no`tog`ri kritingiz qaytadan kriting')

@dp.message_handler(state=state1.manzil,content_types=['location'])
async def manzil(msg:types.Message, state: FSMContext):
    await state.update_data(
        {'manzil': [msg.location.latitude,msg.location.longitude] }
    )
    await bot.send_message(msg.chat.id, 'maktabingni krit', reply_markup=ReplyKeyboardRemove())
    await state1.next()
@dp.message_handler(state=state1.manzil)
async def manzil(msg:types.Message, state: FSMContext):
    if len(msg.text) >15:
        await state.update_data(
                {'manzil': msg.text }
            )
        await bot.send_message(msg.chat.id, 'maktabingni krit', reply_markup=ReplyKeyboardRemove())
        await state1.next()
    else:
        await bot.send_message(msg.chat.id, 'manzilni xato kritingiz qayta kriting')

@dp.message_handler(state=state1.maktab)
async def maktab(msg:types.Message, state: FSMContext):
    await state.update_data(
        {'maktab': msg.text}
    )
    k_tugma = ReplyKeyboardMarkup(resize_keyboard=True)
    b_tugma1 = KeyboardButton(text='ertalab')
    b_tugma = KeyboardButton(text='kechki payt')
    k_tugma.insert(b_tugma)
    k_tugma.insert(b_tugma1)
    await bot.send_message(msg.chat.id, 'vaqtingni krit', reply_markup=k_tugma)
    await state1.next()
@dp.message_handler(state=state1.vaqt)
async def vaqt(msg:types.Message, state: FSMContext):

    await state.update_data(
        {'vaqt': msg.text}
    )
    malumot = await state.get_data()
    if len(malumot['manzil']) == 2:
        lat = malumot['manzil'][0]
        lon = malumot['manzil'][1]
        print(lon,lat)
    else:
        pass
    tugma = await inlin_k(kurs=malumot['kurs'],nomer=malumot['nomer'],vaqt=malumot['vaqt'],id=msg.chat.id)
    await bot.send_message(msg.chat.id, 'qabul qilindi. menejerimiz siz bilan yaqin orada aloqaga chiqadi')
    text = f'''
YANGI O`QUVCHI
ISM: {malumot['ism']}
KURS: {malumot['kurs']}
NOMER: {malumot['nomer']}
VAQTI: {malumot['vaqt']}
MAKTABI: {malumot['maktab']}

'''
    for admin in admins:
        try:
            await bot.send_location(chat_id=admin,longitude=lon,latitude=lat)
        except:
            text += f'MANZIL: {malumot["manzil"]}'
        await bot.send_message(admin, text, reply_markup=tugma)