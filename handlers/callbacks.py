from app import *
from main.functions import Subscriber


@bot.callback_query_handler(func=lambda call: True)
def callback_answer(call):
    """
    Button Response
    """
    if call.data == "list":

        # Fetch List
        data = [i for i in sessions_db.find()][-10:]

        try:
            reply = bot.send_message(
                call.message.chat.id,
                f"""
        <b>Dx50 INSTAGRAM LIST</b>

    1)  {data[0].get("media_url")}

    2)  {data[1].get("media_url")}

    3)  {data[2].get("media_url")}

    4)  {data[3].get("media_url")}

    5)  {data[4].get("media_url")}

    6)  {data[5].get("media_url")}

    7)  {data[6].get("media_url")}

    8)  {data[7].get("media_url")}

    9)  {data[8].get("media_url")}

    10)  {data[9].get("media_url")}
        
                """,
                parse_mode=telegram.ParseMode.HTML,
                disable_web_page_preview=True
            )
        except Exception as e:
            reply = bot.send_message(
                call.message.chat.id,
                f"<b>The Dx50 engagement list({len(data)} users) is almost complete! Contact the engagement bot pod to get on the list.</b>",
                parse_mode=telegram.ParseMode.HTML,
                disable_web_page_preview=True
            )

            
        time.sleep(20)
        bot.delete_message(call.message.chat.id, reply.message_id)

    elif call.data == "ad":
        question = bot.send_message(
            call.from_user.id,
            "Paste your advestisement writing below to post to Dx50 Engagement Group....",
            reply_markup=force_reply
        )
        
        bot.register_next_step_handler(question, send_ad)


    elif call.data == "activate":

        subscriber = Subscriber().activate
        question = bot.send_message(
            int(ADMIN_ID),
            "To add a new subscriber, paste the instagram username below",
            reply_markup=force_reply
        )
        
        bot.register_next_step_handler(question, subscriber)

    elif call.data == "deactivate":
        subscriber = Subscriber().deactivate
        question = bot.send_message(
            int(ADMIN_ID),
            "To deactivate a subscriber, paste the instagram username below",
            reply_markup=force_reply
        )
        
        bot.register_next_step_handler(question, subscriber)

    else:
        pass








def send_ad(msg):
    "Sends Add Message To Group"
    message = msg.text
    
    bot.send_message(
        int(GROUP_ID),
        f"""
<b>{message}</b>
        """,
        parse_mode=telegram.ParseMode.HTML,
        disable_web_page_preview=True
    )