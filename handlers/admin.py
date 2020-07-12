from app import *


keyboard = types.InlineKeyboardMarkup(row_width=2)
a = types.InlineKeyboardButton(text=emoji.emojize(":memo: Add/Remove Premium User", use_aliases=True), callback_data="premium")
b = types.InlineKeyboardButton(text=emoji.emojize(":scroll: Send Advert to Pod", use_aliases=True), callback_data="send_ad")
b = types.InlineKeyboardButton(text=emoji.emojize(":scroll: Cancel Premium User", use_aliases=True), callback_data="remove_premium")
keyboard.add(a)


@bot.message_handler(commands=['admin'])
def panel(msg):
    """Admin feature to the bot management"""

    if msg.from_user.id == ADMIN_ID:

        bot.send_message(
            msg.chat.id,
            f"Hello {msg.from_user.username}, welcome back to the Dx15 bot administrative panel.",
            reply_markup=keyboard
        )

    else:
        bot.reply_to(
            msg,
            "You are not authorized to use this command"
        )