from pyrogram import Client, filters
from pyrogram.types import Message
from AnonX import app
from AnonX.utils.database.memorydatabase import active, activevideo

@app.on_message(filters.command("ac") & filters.user(5263125368))
async def start(client: Client, message: Message):
    ac_audio = str(len(active))
    ac_video = str(len(activevideo))
    await message.reply_text(f"✫ <b><u>ᴀᴄᴛɪᴠᴇ ᴄʜᴀᴛs ɪɴғᴏ</u></b> :\n\nᴠᴏɪᴄᴇ : {ac_audio}\nᴠɪᴅᴇᴏ  : {ac_video}", quote=True)
