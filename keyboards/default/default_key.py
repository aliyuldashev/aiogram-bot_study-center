from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from datafetcher.data_fetcher import tests

async def test_key(a):
    mark =ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
    orqaga = KeyboardButton(text='⬅️orqaga')
    if a =='key':
        for data in await tests():
            key = KeyboardButton(text=f'{data["name"]}')
            mark.add(key)

        mark.add(orqaga)
        return mark
    else:
        data = await tests()
        return data
async def tug():
    tugma = ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    k = KeyboardButton(text='tugatish')
    tugma.add(k)
    return tugma
async def staert():
    mark = ReplyKeyboardMarkup(resize_keyboard=True)
    mark.add(KeyboardButton(text='/start'))
    return mark


