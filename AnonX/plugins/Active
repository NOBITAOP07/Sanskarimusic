from pyrogram import Client, filters
from pyrogram.types import Message
from AnonX import app
from AnonX.utils.database.memorydatabase import active, activevideo
from config import OWNER_ID

@app.on_message(filters.command("ac") & filters.user(OWNER_ID))
async def start(client: Client, message: Message):
    ac_audio = str(len(active))
    ac_video = str(len(activevideo))
    await message.reply_text(f"✫ <b><u>ᴀᴄᴛɪᴠᴇ ᴄʜᴀᴛs ɪɴғᴏ</u></b> :\n\nᴠᴏɪᴄᴇ : {ac_audio}\nᴠɪᴅᴇᴏ  : {ac_video}", quote=True)
