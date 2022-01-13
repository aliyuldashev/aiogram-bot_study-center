from aiogram.types import ReplyKeyboardMarkup,KeyboardButton, InlineKeyboardButton,InlineKeyboardMarkup
from datafetcher.data_fetcher import big,sec,vid
from aiogram.utils.callback_data import CallbackData
test = CallbackData('test','id','javob','right','sanoq')
async def big_in():
    data_big =await big()
    mark_up = ReplyKeyboardMarkup(row_width=4 , resize_keyboard=True)
    for data in data_big:
        mark_up.insert(KeyboardButton(text=data['name']))
    return mark_up
async def sec_in(big_id):
    data_sec =await  sec()
    mark_up = ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
    for data in data_sec:
        if int(data["bigfield_id"]) == int(big_id):
            mark_up.insert(KeyboardButton(text=data['name']))
    mark_up.insert(KeyboardButton(text='⬅️orqaga'))

    return mark_up

async def vid_in(sec_id):
    mark_up = ReplyKeyboardMarkup(row_width=4,resize_keyboard=True)
    a =1
    data_vid = await vid()
    for data in data_vid:
        if int(sec_id) == int(data['secondfield_id']):
            mark_up.insert(KeyboardButton(text=f'{data["name"]}'))
            a += 1
    mark_up.insert(KeyboardButton(text='⬅️orqaga'))
    return mark_up

async def  inline_k(right,sanoq,id):
    mark_up = InlineKeyboardMarkup(row_width=2)
    a = InlineKeyboardButton(text='A', callback_data=f'test:{id}:a:{right}:{sanoq}')
    b = InlineKeyboardButton(text='B', callback_data=f'test:{id}:b:{right}:{sanoq}')
    c = InlineKeyboardButton(text='C', callback_data=f'test:{id}:c:{right}:{sanoq}')
    d = InlineKeyboardButton(text='D', callback_data=f'test:{id}:d:{right}:{sanoq}')
    mark_up.add(a,b,c,d)
    return mark_up