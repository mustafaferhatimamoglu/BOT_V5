import asyncio
import telegram


async def main():
    bot = telegram.Bot("6474533873:AAEUK4AtkTfJr3eghfSGM1Y_4di_vW7kIkI")
    async with bot:
        updates = (await bot.get_updates())[0]
        print(updates)


if __name__ == '__main__':
    asyncio.run(main())
    
    
    
import asyncio
import telegram


async def main():
    bot = telegram.Bot("6474533873:AAEUK4AtkTfJr3eghfSGM1Y_4di_vW7kIkI")
    async with bot:
        print(await bot.get_me())


if __name__ == '__main__':
    asyncio.run(main())