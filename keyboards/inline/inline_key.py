from aiogram.types import ReplyKeyboardMarkup,KeyboardButton, InlineKeyboardButton,InlineKeyboardMarkup
from datafetcher.data_fetcher import big,sec
from datafetcher.data_fetcher import last as last1
from aiogram.utils.callback_data import CallbackData
test = CallbackData('test','id','javob','right','sanoq')
asosiy = KeyboardButton(text='🏠Asosiy menyu')
async def big_in():
    data_big =await big()
    mark_up = ReplyKeyboardMarkup(row_width=4 , resize_keyboard=True)
    for data in data_big:
        mark_up.insert(KeyboardButton(text=data['name']))
    kitob = KeyboardButton(text='📜test')
    mark_up.add(kitob)
    return mark_up
async def sec_in(big_id):
    to_return =[]
    last_name = {'last':{},
                 'second':{}}
    data_sec =await  sec(big_id)
    last_data = await last1()
    mark_up = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    for data in data_sec:
        mark_up.insert(KeyboardButton(text=data['name']))
        last_name['second'][f'{data["name"]}'] = data['id']
    for data in last_data:
        if data['firstfield'] == big_id and data['secondfield'] ==None:
            mark_up.insert(KeyboardButton(text=data['name']))
            last_name['last'][f'{data["name"]}'] = data['id']
    to_return.append(last_name)
    mark_up.insert(KeyboardButton(text='⬅️orqaga'))
    mark_up.insert(asosiy)
    to_return.append(mark_up)
    return to_return


async def last(first,second):
    to_return = []
    mark_up = ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    data_vid = await last1()
    a =0
    for data in data_vid:
        if first == data['firstfield'] and second == data['secondfield']:
            mark_up.insert(KeyboardButton(text=f'{data["name"]}'))
            a += 1
    to_return.append(a)
    mark_up.insert(KeyboardButton(text='⬅️orqaga'))
    mark_up.insert(asosiy)
    to_return.append(mark_up)
    return to_return

async def  inline_k(right,sanoq,id):
    mark_up = InlineKeyboardMarkup(row_width=2)
    a = InlineKeyboardButton(text='A', callback_data=f'test:{id}:a:{right}:{sanoq}')
    b = InlineKeyboardButton(text='B', callback_data=f'test:{id}:b:{right}:{sanoq}')
    c = InlineKeyboardButton(text='C', callback_data=f'test:{id}:c:{right}:{sanoq}')
    d = InlineKeyboardButton(text='D', callback_data=f'test:{id}:d:{right}:{sanoq}')
    mark_up.add(a,b,c,d)
    return mark_up