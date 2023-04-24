import asyncio 
from telethon.sessions import StringSession
from telethon import TelegramClient, events, sync
from loguru import logger

from .config import settings
from .db import MongoDBManager

db = MongoDBManager(url, database)

class Telegram:

    def __init__(self,  authorized_string,
                        app_id,
                        app_hash):

        self.init = TelegramClient(
                StringSession(settings.authorized_string),
                settings.app_id,
                settings.app_hash)
        self.init.start()

    def send_message(self, channel_name, message):
        # retrieve channel from MongoDB
        channel = db.find_one({'name': channel_name})
        if not channel:
            raise ValueError(f'Channel "{channel_name}" not found.')

        # send message to channel
        self.client.send_message(channel['id'], message)
        
    def startListener(self, category="all"):

        channel_list = db.find({})
        if category != "all":
            channel_list = db.find({"category":category})
            
        with self.init as client:

            for channel in channel_list:

                logger.info(f"Listen on channel {channel.group_id}")

                @client.on(events.NewMessage(chats=channel.group_id))

                async def new_message_handler(event):

                    try:

                        if len(last_message) > 0 :
                            
                            cve_detail = await cve_info(event.text)
                            
                            for link in last_message:


                    except Exception as Error:

                        logger.warning(traceback.format_exc())

                        logger.warning(Error)

            
            with client:
                client.run_until_disconnected()

