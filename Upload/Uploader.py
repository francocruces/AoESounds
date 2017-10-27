"""
Simple telegram bot
"""

import asyncio
import os

import telepot
from telepot.aio.delegate import per_inline_from_id, per_chat_id, create_open, pave_event_space, \
    intercept_callback_query_origin
from telepot.aio.helper import AnswererMixin, InterceptCallbackQueryMixin, ChatHandler
from telepot.aio.loop import MessageLoop

from __TOKEN__ import TOKEN

__author__ = "Franco Cruces Ayala"


class Handler(ChatHandler, AnswererMixin, InterceptCallbackQueryMixin):
    """
    Handler for the inline bot.
    """
    def __init__(self, *args, **kwargs):
        super(Handler, self).__init__(*args, **kwargs)
        self.files = os.listdir(os.getcwd()+"\\sounds")
        self.count = 0
        self.dict = {}

    def on_chat_message(self, msg):
        """
        How to handle an inline query.
        :param msg: Telegram message. It's expected to be an inline_query
        :return: Results for the inline query
        """
        print(msg)
        print(msg['audio']['file_id'])
        print("Count: " + str(self.count))
        print("Writing " + str(self.count) + "file: " + self.files[self.count])
        self.dict[self.files[self.count]] = msg['audio']['file_id']
        self.count = self.count + 1
        print(self.dict)


    def on_chosen_inline_result(self, msg):
        """
        Console printing for debugging.
        :param msg: Telegram message. It's expected to be a chosen_inline_result
        """
        print(msg)
        print('inline_message_id' in msg)
        result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
        print(from_id, ",", self.id, ':', 'Chosen Inline Result:', result_id, from_id, query_string)
        print("Message sent to " + str(from_id))


### ASYNC MAIN
bot = telepot.aio.DelegatorBot(TOKEN, [intercept_callback_query_origin(
    pave_event_space())(
    per_chat_id(), create_open, Handler, timeout=20)
])

loop = asyncio.get_event_loop()

loop.create_task(MessageLoop(bot).run_forever())
print('Listening ...')

loop.run_forever()


