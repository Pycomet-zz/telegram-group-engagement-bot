from app import *


message = """
<b>:bangbang: STOP Liking & Commenting :bangbang:</b>

:raising_hand: Join the Premium Subscribers and post without engaging back or get auto comments every time you post to our pods :raising_hand:

:point_right: Contact admin:
 @codefred :phone:
"""

keyboard = types.InlineKeyboardMarkup(row_width=2)
# a = types.InlineKeyboardButton(text=emoji.emojize(":memo: Check :memo:", use_aliases=True), callback_data="check")
a = types.InlineKeyboardButton(text=emoji.emojize(":scroll: Dx15 List", use_aliases=True), callback_data="list")
keyboard.add(a)


@bot.message_handler(commands=['start'])
def start(msg):
    
    bot.reply_to(
        msg,
        emoji.emojize(message, use_aliases=True),
        parse_mode=telegram.ParseMode.HTML,
        reply_markup=keyboard
    )

    time.sleep(5)
    bot.delete_message(msg.chat.id, msg.message_id)

    #delete the next message
    # msg.message_id += 1
    # bot.delete_message(msg.chat.id, msg.message_id)


    