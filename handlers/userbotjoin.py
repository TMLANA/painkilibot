from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["ujoin"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>അഡ്മിൻ ആക്കട തെണ്ടി ..  അല്ലെങ്കിൽ ഞാൻ പാടൂല.... </b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "painkilibot"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"I joined here as you requested")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>ഞാൻ ഇവിടെ ഉണ്ട് ...</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n User {user.first_name} couldn't join your group due to heavy join requests for userbot! Make sure user is not banned in group."
            "\n\nOr manually add @VCPlayRobot to your Group and try again</b>",
        )
        return
    await message.reply_text(
            "<b>അതാണു..... ഞാൻ ഈ കളിക്ക് ഇല്ല</b>",
        )
    
@USER.on_message(filters.group & filters.command(["uleave"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>User couldn't leave your group! May be floodwaits."
            "\n\nOr manually kick me from to your Group</b>",
        )
        return
