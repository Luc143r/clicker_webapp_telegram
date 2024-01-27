import asyncio

from aiogram import Router, Bot, Dispatcher, F
from aiogram.types import Message, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import token


def webapp_builder() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(text='Сюда тыкай да', web_app=WebAppInfo(
        url='https://52ds1b7g-8000.euw.devtunnels.ms/',
    ))
    return builder.as_markup()

router = Router()

@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.reply('Здарова заебал!',
                        reply_markup=webapp_builder())
    
async def main() -> None:
    bot = Bot(token=token, parse_mode=ParseMode.HTML)
    
    dp = Dispatcher()
    dp.include_router(router)
    
    await bot.delete_webhook(True)
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    try:
        text = 'Bot started'
        print(f'{text:*^30}')
        asyncio.run(main())
    except:
        text = 'Bot not stated'
        print(f'{text:*^30}')
