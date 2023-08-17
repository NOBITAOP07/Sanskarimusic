import os
import asyncio
from datetime import datetime
from time import sleep
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup
from pyrogram.errors import UserDeactivated, PeerIdInvalid, UserNotParticipant, FloodWait

from config import LOG_GROUP_ID, OWNER_ID, STRING1, STRING2, STRING3, STRING4, STRING5, LOG_FILE_NAME
from AnonX import app, userbot
from AnonX.misc import SUDOERS
from AnonX.utils.database import get_served_chats
from AnonX.utils.database.memorydatabase import (get_active_chats, get_active_video_chats)

from AnonX.utils import bot_sys_stats

MAINGROUP_ID = LOG_GROUP_ID

ub1 = userbot.one
ub2 = userbot.two
ub3 = userbot.three
ub4 = userbot.four
ub5 = userbot.five

#Check Every Userbots & Bot
@app.on_message(filters.command("check") & filters.user(OWNER_ID))
async def systest(client, message: Message):
	mys = await message.reply_text("**Please Wait•🚀**\nWe Are Checking Bot's Status...")
	suspendedacc = []
	await app.send_message(MAINGROUP_ID, "Main Bot Is Working Fine•✅")
	Coun = 0
	if bool(STRING1)==True:
		try:
			await ub1.send_message(MAINGROUP_ID, "Assistant 1 Is Working Fine•✅")
			Coun += 1
		except UserDeactivated:
			suspendedacc.append("Assistant 1")
	if bool(STRING2)==True:
		try:
			await ub2.send_message(MAINGROUP_ID, "Assistant 2 Is Working Fine•✅")
			Coun += 1
		except UserDeactivated:
			suspendedacc.append("Assistant 2")
	if bool(STRING3)==True:
		try:
			await ub3.send_message(MAINGROUP_ID, "Assistant 3 Is Working Fine•✅")
			Coun += 1
		except UserDeactivated:
			suspendedacc.append("Assistant 3")
	if bool(STRING4)==True:
		try:
			await ub4.send_message(MAINGROUP_ID, "Assistant 4 Is Working Fine•✅")
			Coun += 1
		except UserDeactivated:
			suspendedacc.append("Assistant 4")
	if bool(STRING5)==True:
		try:
			await ub5.send_message(MAINGROUP_ID, "Assistant 5 Is Working Fine•✅")
			Coun += 1
		except UserDeactivated:
			suspendedacc.append("Assistant 5")
	
	await mys.edit_text(f"**SYSTEM TEST COMPLETED•✅**\n**Bot** = __Working__ ✅\n**Total Assistants** = __{Coun}__\n**Suspended Assistant** = __{len(suspendedacc)}__\n**Suspended Acc Name** = __{suspendedacc}__")




#Active_VC plugin
@app.on_message(filters.command("ac") & SUDOERS)
async def littleac(_, message: Message):
    ac_audio = str(len(await get_active_chats()))
    ac_video = str(len(await get_active_video_chats()))
    UP, CPU, RAM, DISK = await bot_sys_stats()
    await message.reply_text(f"𝐁ᴏᴛ 𝐀ᴄᴛɪᴠᴇ 𝐂ʜᴀᴛs 𝐈ɴғᴏ • 🔊\n•━━━━━━━━━━━━━━━━━━•\n🎧 **𝐀ᴜᴅɪᴏ** 🎧 » {ac_audio} Active\n•───────•\n🎥 **𝐕ɪᴅᴇᴏ** 🎥 » {ac_video} Active\n•──────•\n\n🧭 **CPU** => {CPU}\n📟 **RAM** => {RAM}\n💽 **DISK** => {DISK}\n•───────•", quote=True)


#Logs, Temps Etc Cleaner Without Restarting Bot
@app.on_message(filters.command("clr") & SUDOERS)
async def clearLogs(_, message: Message):
    logsname = LOG_FILE_NAME[3]
    try:
	    os.system('rm -rf downloads/* cache/*')
	    os.system(f"rm -rf {logsname}*")
    except:
        await message.reply_text(f"**Failed To Delete Some Files !!**\nPlease Read\n{traceback.format_exc()}", quote=True)
    await message.reply_text(f"**Successfully Deleted Below Folders & Files**:\n -Downloads\n -Cache\n -Logs\n\n **PLUGIN MADE BY** - Ayush", quote=True)


#Link Genrater
@app.on_message(
    filters.command("link")
    & filters.user(OWNER_ID)
    & ~filters.forwarded
    & ~filters.via_bot
)
async def link_getter(client, message):
    if len(message.command) < 2:
        return await edit_or_reply(
            message, text="**Did You Give Me Chat ID ?**"
            )
    try:
        cmd = message.text.split(" ", maxsplit=1)[1]
        ch_lid = int(cmd)
    except IndexError:
        return await message.delete()

    try:
        linkkk = await app.export_chat_invite_link(ch_lid)
        await message.reply_text(f"**Chat's Link** >>\n\n{linkkk}", quote=True)
    except:
        await message.reply_text(f"**Error**\nMaybe Bot Have No Permission Of Invite Users Permission OR Bot Removed!\n TRY /new_link", quote=True)


#Link Creater

@app.on_message(
    filters.command("new_link")
    & filters.user(OWNER_ID)
    & ~filters.forwarded
    & ~filters.via_bot
)
async def new_link_getter(client, message):
    if len(message.command) < 2:
        return await edit_or_reply(
            message, text="**Did You Give Me Chat ID ?**"
            )
    try:
        cmd = message.text.split(" ", maxsplit=1)[1]
        ch_lid = int(cmd)
    except IndexError:
        return await message.delete()

    try:
        linkkk = await app.create_chat_invite_link(ch_lid)
        await message.reply_text(f"Here Is This Chat's Link >>\n\n{linkkk}", quote=True)
    except:
        await message.reply_text(f"Maybe I'm Demoted There Or Removed From There!\n\n", quote=True)


#-------------Every_Plug-Ins are made by ayush---------------#


#--------------------Private_Plugins-------------------------#

@app.on_message(
    filters.command("track")
    & filters.user(OWNER_ID)
    & ~filters.forwarded
    & ~filters.via_bot
)
async def tracking_user(client, message: Message):
	if len(message.command) < 2:
		return await edit_or_reply(message, text="**Please Give User ID!**")
	try:
		banda = message.text.split(" ", maxsplit=1)[1]
		kimd = int(banda)
	except IndexError:
		return await message.delete()
	replyreport = await message.reply_text("🔄**Loading Databse...**")
	allchats = []
	addminfoundin = []
	foundin = []
	dbchat = await get_served_chats()
	await replyreport.edit_text("🏷**Trying To Validate The User...**")
	try:
		Validate_user = await app.resolve_peer(kimd)
	except PeerIdInvalid:
		return await replyreport.edit_text("❌**Bot Never Met This User!\nPlease Force That User To Start your bot even if bot is not online!\nFor Now,Stopping The Tracking!!**")
	await replyreport.edit_text("✅**User Validated!\nLoading Chats Now...**")
	for chts in dbchat:
		allchats.append(int(chts["chat_id"]))

	await asyncio.sleep(60)
	await replyreport.edit_text(f"✅**{len(allchats)} Chats Loaded!\nTracking Now!**")

	for cht_id in allchats:
		try:
			bnda = await app.get_chat_member(cht_id, kimd)
			chkstatus = str(bnda.status)
			if chkstatus=="administrator":
				addminfoundin.append(cht_id)
			elif chkstatus=="member":
				foundin.append(cht_id)
		except UserNotParticipant:
			continue
		except FloodWait as e:
			flood_time = int(e.x)
			if flood_time > 200:
				continue
			await asyncio.sleep(flood_time)
		except:
			continue
	await replyreport.edit_text(f"**Tracking Completed! ✅**\n**User ID** = <code>{kimd}</code>\n**Admin In** = {len(addminfoundin)} Groups\n**Member In** = {len(foundin)} Groups\n\n**AdminGroupsID**:\n<code>{addminfoundin}</code>\n\n**MemberGroupsID**:\n<code>{foundin}</code>\n\n\n**PLUGIN MADE BY**: Ayush")
