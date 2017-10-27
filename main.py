"""
Simple telegram bot
"""

import asyncio

import telepot
from telepot.aio.delegate import per_inline_from_id, create_open, pave_event_space
from telepot.aio.helper import InlineUserHandler, AnswererMixin
from telepot.aio.loop import MessageLoop
from telepot.namedtuple import InlineQueryResultCachedAudio

from __TOKEN__ import TOKEN
from soundids import FILE_ARRAY, NAMES, MP3FILE_ARRAY, MP3NAMES

__author__ = "Franco Cruces Ayala"


class InlineHandler(InlineUserHandler, AnswererMixin):
    """
    Handler for the inline bot.
    """

    def __init__(self, *args, **kwargs):
        super(InlineHandler, self).__init__(*args, **kwargs)

    def on_inline_query(self, msg):
        """
        How to handle an inline query.
        :param msg: Telegram message. It's expected to be an inline_query
        :return: Results for the inline query
        """

        def compute_answer():
            """
            Function generating the answer for the handler.
            :return: Lyrics as articles
            """
            print(msg)
            query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
            print(self.id, ':', 'Inline Query:', query_id, from_id, query_string)
            sounds = get_sound(query_string)
            return sounds

        self.answerer.answer(msg, compute_answer)


def get_sound(query_string):
    if query_string != "":
        number = int(query_string)
        print("Getting sound " + str(number))
        print("Name: " + NAMES[number - 1])
        print("Id: " + FILE_ARRAY[number - 1])
        result = []
        if number >= 1 or number <= 42:
            voice_message = InlineQueryResultCachedAudio(
                id=str(MP3NAMES[number - 1]),
                audio_file_id=str(MP3FILE_ARRAY[number - 1]),
            )
            print(voice_message)
            result.append(voice_message)
        return result


bot = telepot.aio.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_inline_from_id(), create_open, InlineHandler, timeout=20)
])

loop = asyncio.get_event_loop()

loop.create_task(MessageLoop(bot).run_forever())
print('Listening ...')

loop.run_forever()
