from loader import db
from aiogram.types import Message,CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import bot
from state.state import States, Test_state, start_s
from datafetcher.data_fetcher import big,sec,vid
from keyboards.inline import inline_key
from keyboards.default import default_key
from datafetcher.data_fetcher import vid,test
from aiogram.types import ReplyKeyboardRemove
from second_bot.main import *
import random
admins = [981154238]

@db.callback_query_handler(inline_key.test.filter(),state='*')
async def tests_cal(msg:CallbackQuery,state:FSMContext,callback_data:dict):
    sanoq = callback_data.get('sanoq')
    right = callback_data.get('right')
    javob = callback_data.get('javob')
    id = callback_data.get('id')
    data = await test(id)
    text = f'Savol №{sanoq}\n\n'
    text += f'A  {data[0]["a"]}\n'
    text += f'B  {data[0]["b"]}\n'
    text += f'C  {data[0]["c"]}\n'
    text += f'D  {data[0]["d"]}\n'
    text += f'Javob: {javob.upper()}'
    await msg.message.edit_text(text=text)
    state_date =await state.get_data()
    try:
        await msg.message.edit_reply_markup(reply_markup=ReplyKeyboardRemove())
    except:
        pass
    if 'test' in state_date.keys():
        test1 = state_date['test']
        test1[f'{sanoq}']=[right,javob]
        await state.update_data({
            'test':test1
        })
    else:
        await state.update_data({
            'test':{
              f'{sanoq}':[right,javob]
            }})
# @db.message_handler(Command('orqaga'),state='*')
# async def  video_big(msg:Message,state:FSMContext):
#     a = await state.get_state()
#     if a[7:] == 'vid_state':
#         data = await state.get_data()
#         data1 = data['sec_data']
#         markup1 =await inline_key.sec_in(data1)
#         await bot.send_message(msg.chat.id,'nima keragligini tanlang', reply_markup= markup1)
#         await States.sec_state.set()
#     else:
#         await States.big_state.set()
#         markup1 = await inline_key.big_in()
#         await bot.send_message(msg.chat.id,'nima keragligini tanlang', reply_markup= markup1)
@db.message_handler(Command('test'), state=start_s.start)
async def start(msg:Message, state:FSMContext):
    mark = await default_key.test_key('key')
    await bot.send_message(msg.chat.id,'fani tanla',reply_markup=mark)
    await Test_state.name.set()
@db.message_handler(Command('video'), state=start_s.start)
async def start(msg:Message, state:FSMContext):
    markup =await inline_key.big_in()
    await bot.send_message(msg.chat.id,'NIMA KERAGLIGINI TANLANG!', reply_markup=markup)
    await States.big_state.set()

@db.message_handler(state=Test_state.name)
async def test_name(msg:Message, state:FSMContext):
    test_name1 = msg.text
    test_data1 = {'test':{}}
    tug_m =await default_key.tug()
    for data in await default_key.test_key('all'):
        ids = data['tests']
        if data['name'] == test_name1:
            if len(ids) <=30:
                e = 1
                for i in ids:
                    test_data = await test(i)
                    test_data1['test'][f'{e}'] = [test_data[0]['right'],'qilinmagan']
                    text = f'Savol  №{e} \n'

                    text += test_data[0]['test']
                    text += '\n'
                    text += f'A  {test_data[0]["a"]}'
                    text += '\n'
                    text += f'B  {test_data[0]["b"]}'
                    text += '\n'
                    text += f'C  {test_data[0]["c"]}'
                    text += '\n'
                    text += f'D  {test_data[0]["d"]}'
                    markup =await inline_key.inline_k(right=test_data[0]['right'],sanoq=e,id=test_data[0]['id'])
                    await bot.send_message(msg.chat.id,text=text,reply_markup=markup,parse_mode='html')
                    e += 1
                await bot.send_message(msg.chat.id,'tugatib bo`lgach tugatish tugmasini bosing',reply_markup=tug_m)
                await state.update_data(test_data1)
                await Test_state.test.set()
        else:
            new_ids = []
            for i in range(0,30):
                index = random(0,len(ids)-1)
                new_ids.append(ids[index])
                ids.pop(index)
            e = 1
            for i in new_ids:
                test_data1['test'][f'{e}'] = [test_data[0]['right'], 'qilinmagan']
                text = f'Savol  №{e} \n'
                test_data = await test(i)
                text += test_data[0]['test']
                text += '\n'
                text += f'A  {test_data[0]["a"]}'
                text += '\n'
                text += f'B  {test_data[0]["b"]}'
                text += '\n'
                text += f'C  {test_data[0]["c"]}'
                text += '\n'
                text += f'D  {test_data[0]["d"]}'
                markup = await inline_key.inline_k(right=test_data[0]['right'], sanoq=e, id=test_data[0]['id'])
                await bot.send_message(msg.chat.id, text=text, reply_markup=markup)
                e += 1
            await bot.send_message(msg.chat.id, 'tugatib bo`lgach tugatish tugmasini bosing', reply_markup=tug_m)
            await state.update_data(test_data1)
            await Test_state.test.set()
@db.message_handler(state=Test_state.test)
async def tugatish(msg:Message, state:FSMContext):
    if msg.text == 'tugatish':
        ism = f'{await state.get_data()["ism"]}\n'
        markup =await default_key.staert()
        data = await state.get_data()
        text = ''
        right_ans = 0
        for i in range(1,len(data['test'])+1):
             try:
                 data_s = data['test'][f'{i}']
                 if data_s[0] == data_s[1]:
                    text += f'{i} {data_s[0]}✔\n'
                    right_ans += 1
                 else:
                     text += f'{i} {data_s[1]}❌ to`grsi: {data_s[0]}\n'
             except Exception as ex:
                 print(ex, i)
                 text += f'{i}\n'
        text += f'javob {len(data["test"])}dan {right_ans}ta to`gri'
        await bot.send_message(msg.chat.id,text=text)
        await msg.reply('/start tugmasini bosing',reply_markup= markup)
        ism += text
        for admin in admins:
            try:
                await bot.send_message(admin,ism)
            except:
                pass
@db.message_handler(state=States.big_state)
async def  video_big(msg:Message,state:FSMContext):
    data_bid = await big()
    for data in data_bid:
        if data['name'] == msg.text:
            dat = data['id']
    markup =await inline_key.sec_in(dat)
    await bot.send_message(msg.chat.id,'Nima keragligini tanlang',reply_markup=markup)
    await States.next()
@db.message_handler(state=States.sec_state)
async def  video_big(msg:Message,state:FSMContext):
    if msg.text =='⬅️orqaga':
        await States.big_state.set()
        markup1 = await inline_key.big_in()
        await bot.send_message(msg.chat.id, 'nima keragligini tanlang', reply_markup=markup1)
    else:
        da = await sec()
        for data2 in da:
            if data2['name'] == msg.text:
                data3 = data2['id']
                data1 = data2['bigfield_id']
        markup =await inline_key.vid_in(data3)
        await bot.send_message(msg.chat.id,'Nima keragligini tanlang', reply_markup=markup)
        await state.update_data({'sec_data':f'{data1}'})
        await States.next()

@db.message_handler(state=States.vid_state)
async def  video_big(msg:Message,state:FSMContext):
    if msg.text =='⬅️orqaga':
        data = await state.get_data()
        data1 = data['sec_data']
        markup1 = await inline_key.sec_in(data1)
        await bot.send_message(msg.chat.id, 'nima keragligini tanlang', reply_markup=markup1)
        await States.sec_state.set()
    id = msg.text
    der = await vid()
    a = 1
    for data in der:
        if (data['name']) == (id):
            video = open(f'D:/programing/telebot/telebot/django1{data["Video"]}','rb')
            await bot.send_video(msg.chat.id,video=video, caption=f'{data["character"]}')
        a += 1
    if a ==0:
        await bot.send_message(msg.message.chat.id,'video xozircha mavjud emas')