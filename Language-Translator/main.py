from googletrans import Translator
import asyncio

async def main():
    translator = Translator()
    src_lang = 'Hello Sai Charan Sir, How are you. You are looking very handsome today.'
    out = await translator.translate(src_lang, dest='or')
    print(out.text)

asyncio.run(main())