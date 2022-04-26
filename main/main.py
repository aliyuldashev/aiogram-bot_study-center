from loader import db
from aiogram.types import Message,CallbackQuery
from aiogram.dispatcher.filters import Command
from state.state import  Test_state
from datafetcher.data_fetcher import big,sec,last
from datafetcher.data_fetcher import test,post
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

@db.message_handler(state=Test_state.name)
async def test_name(msg:Message, state:FSMContext):
    if msg.text == '⬅️orqaga':
        markup1 = await inline_key.big_in()
        await bot.send_message(msg.chat.id, 'nima keragligini tanlang', reply_markup=markup1)
        await States.big_state.set()
    else:
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

    if msg.text == '📜test':
        mark = await default_key.test_key('key')
        await bot.send_message(msg.chat.id, 'fani tanla', reply_markup=mark)
        await Test_state.name.set()
    else:
        data_bid = await big()
        for data in data_bid:
            if data['name'] == msg.text:
                dat = data['id']
        markup =await inline_key.sec_in(dat)
        await bot.send_message(msg.chat.id,'Nima keragligini tanlang',reply_markup=markup[1])
        await state.update_data({
            'first':dat,'ids':markup[0]
        })
        await States.sec_state.set()
@db.message_handler(state=States.sec_state)
async def  video_big(msg:Message,state:FSMContext):
    if msg.text == '🏠Asosiy menyu':
        markup1 = await inline_key.big_in()
        await bot.send_message(msg.chat.id, 'nima keragligini tanlang', reply_markup=markup1)
        await States.big_state.set()
    elif msg.text == '⬅️orqaga':
        markup1 = await inline_key.big_in()
        await bot.send_message(msg.chat.id, 'nima keragligini tanlang', reply_markup=markup1)
        await States.big_state.set()
    elif msg.text == '📜test':
        mark = await default_key.test_key('key')
        await bot.send_message(msg.chat.id, 'fani tanla', reply_markup=mark)
        await Test_state.name.set()
    else:
        data = await state.get_data()
        da = await sec(data['first'])
        second_count = 0
        for name , id in data['ids']['second'].items():
            if name == msg.text:
                data3 = id
                markup =await inline_key.last(first=data['first'],second=data3)
                await bot.send_message(msg.chat.id,'Nima keragligini tanlang', reply_markup=markup[1])
                second_count += 1
                await state.update_data({
                    'first': data['first'], 'second': data3
                })
                await States.last.set()
        if second_count ==0:
            for name, id in data['ids']['last'].items():
                if name == msg.text:
                    last1 =await last()
                    for i in last1:
                        if i['name'] == msg.text and i['firstfield'] == data['first'] and i['secondfield'] == None:
                            videos = i['dates']
                    for video in videos:
                        file = await post(video)
                        if file[0]['type'] == 'video':
                            file_name = open(f'E:/Новая_папка/telebot/telebot/django1{file[0]["File"]}', 'rb')
                            await bot.send_video(msg.chat.id, video=file_name, caption=file[0]['text'])
                        elif file[0]['type'] == 'pdf':
                            file_name = open(f'E:/Новая_папка/telebot/telebot/django1{file[0]["File"]}', 'rb')
                            print({file[0]["File"][-3:]},)
                            await bot.send_document(msg.chat.id,document=file_name)
                        elif file[0]['type'] == 'post':
                            await bot.send_message(msg.chat.id, file[0]['text'])
                        else:
                            file_name = open(f'E:/Новая_папка/telebot/telebot/django1{file[0]["File"]}', 'rb')
                            await bot.send_photo(msg.chat.id, photo=file_name, caption=file[0]['text'])

            await States.send.set()

@db.message_handler(state=States.last)
async def last_cl(msg:Message,state:FSMContext):
    data = await state.get_data()
    if msg.text == '🏠Asosiy menyu':
        markup1 = await inline_key.big_in()
        await bot.send_message(msg.chat.id, 'nima keragligini tanlang', reply_markup=markup1)
        await States.big_state.set()
    elif msg.text == '⬅️orqaga':
        markup = await inline_key.sec_in(data['first'])
        await bot.send_message(msg.chat.id, 'Nima keragligini tanlang', reply_markup=markup[1])
        await state.update_data({
            'first': data["first"], 'ids': markup[0]
        })
        await States.sec_state.set()
    else:
        last1 =await last()
        for i in last1:
            if i['name'] == msg.text and i['firstfield'] == data['first'] and i['secondfield'] == data['second']:
                videos = i['dates']
        for video in videos:
            file =await post(video)
            if file[0]['type'] == 'video':
                file_name = open(f'study_center_bot/django1/{file[0]["File"]}', 'rb')
                await bot.send_video(msg.chat.id, video=file_name, caption=file[0]['text'])
            elif file[0]['type'] == 'pdf':
                file_name = open(f'study_center_bot/django1/{file[0]["File"]}', 'rb')
                await bot.send_file(msg.chat.id, file_type=f'{file[0]["File"][-3:]}', file=file_name)
            elif file[0]['type'] == 'post':
                await bot.send_message(msg.chat.id, file[0]['text'])
            else:
                file_name = open(f'study_center_bot/django1/{file[0]["File"]}', 'rb')
                await bot.send_photo(msg.chat.id, photo=file_name, caption=file[0]['text'])
        await States.send.set()

@db.message_handler(state=States.send)
async def send_video(msg:Message,state:FSMContext):
    data = await state.get_data()
    if msg.text == '🏠Asosiy menyu':
        markup1 = await inline_key.big_in()
        await bot.send_message(msg.chat.id, 'nima keragligini tanlang', reply_markup=markup1)
        await States.big_state.set()
    elif msg.text == '⬅️orqaga':
        try:
            await States.last.set()
            markup = await inline_key.last(first=data['first'], second=data['second'])
            await bot.send_message(msg.chat.id, 'Nima keragligini tanlang1', reply_markup=markup[1])
            await state.update_data({
                'first': data['first'], 'second': data['second']
            })
        except:
            await States.sec_state.set()
            markup = await inline_key.sec_in(big_id=data['first'])
            await bot.send_message(msg.chat.id, 'Nima keragligini tanlang', reply_markup=markup[1])
            await state.update_data({
                'first': data['first']})
