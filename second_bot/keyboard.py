from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton, KeyboardButton,ReplyKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
cal = CallbackData('by','kurs','nomer','vaqt','id','qabul')
async def inlin_k(kurs,nomer,vaqt,id):
    tuga = InlineKeyboardMarkup(row_width=2)
    tugma_k1 = InlineKeyboardButton(text='QABUL QILISH',callback_data=f'by:{kurs}:{nomer}:{vaqt}:{id}:qb')
    tugma_k2 = InlineKeyboardButton(text='RAD ETISH',callback_data=f'by:{kurs}:{nomer}:{vaqt}:{id}:rd')
    tuga.insert(tugma_k1)
    tuga.insert(tugma_k2)
    return tuga
async def admin():
    tugma = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    tugma_k = KeyboardButton(text='Elon yuborish')
    tugma.add(tugma_k)
    return tugma