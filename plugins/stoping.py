#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) hsk the editor

import os
import sys
import asyncio
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery

@Client.on_callback_query(filters.regex(r'^stop_btn$'))
async def stop_button(c: Client, cb: CallbackQuery):
    await cb.message.delete()
    await cb.answer()
    msg = await c.send_message(
        text="<i>Trying To Stop Forwarding.....</i>",
        chat_id=cb.message.chat.id
    )
    await asyncio.sleep(5)
    await msg.edit("<i>File Forword Stoped Successfully കഴിഞ്ഞു😁👍</i>")
    os.execl(sys.executable, sys.executable, *sys.argv)
    
@Client.on_callback_query(filters.regex(r'^close_btn$'))
async def close(bot, update):
    await update.answer()
    await update.message.delete()
