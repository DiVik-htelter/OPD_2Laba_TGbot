from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os 


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handlers()
async def echo_send(message : types.Message):
	#что делает бот при получении сообщения?
	await message.answer(message.text)
	#await message.reply(message.text) #Тоже самое, только бот отвечает на сообщение
	#await bot.send_message(message.from_user.id,message.text)# jnghfdkztn cjj,otybt d kbxre? yj ,eltn jib,rf tckb gjkmpjdfntkm ybxtuj yt gbcfk? n?r? ,jn gthdsv yfgbcfnm yt vj;tn



executor.start_polling(dp, skip_updates = True)
