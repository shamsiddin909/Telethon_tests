from telethon import TelegramClient, events

api_id = ''
api_hash = ''

client = TelegramClient('hello', api_id, api_hash)

async def main():
    await client.start()
    
    list = ["ndos","ndodass","ndodaksndks","ndoioneowinois","ndiefnwoinewoos","ndooidfnasnosians","nofidsnoinfdsodos","ndsdfofinsoinos","ndos","ndos","ndos","ndos","ndos","ndos","ndos","ndos","ndos","ndos","ndos","ndos","ndos","ndos","ndos","ndos","ndos","ndos","ndos","ndos","ndos",]
    
    for i in list:
       await client.send_message('S1mple_T', i)
with client:
    client.loop.run_until_complete(main())
