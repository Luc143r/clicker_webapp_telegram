import asyncio

from aiogram import Router, Bot, Dispatcher, F
from aiogram.types import Message, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder

from configs.config_reader import Config


def webapp_builder() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(text='Сюда тыкай да', web_app=WebAppInfo(
        url=Config.get_config('config').API_URL,
    ))
    return builder.as_markup()

router = Router()

@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.reply('Здарова заебал!',
                        reply_markup=webapp_builder())
    
async def main() -> None:
    bot = Bot(token=Config.get_config('config').TOKEN, parse_mode=ParseMode.HTML)
    
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
