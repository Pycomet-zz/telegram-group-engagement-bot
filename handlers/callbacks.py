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


    elif call.data == "rules":
        reply = bot.send_message(
            call.from_user.id,
            f"""
Hey {call.from_user.first_name}, I am guessing this is your first attempting to join Dx50 enagagement bot list. Here are the steps you should follow;

<b>STEP 1</b> ➡️ Send /start to @Instgramgfluencerbot to get the current list

<b>STEP 2</b> ➡️ Like and comment on at least 10 posts from the list gotten from the bot in <b>STEP 1</b>

<b>STEP 3</b> ➡️ Goto t.me/instagramgrowthg and join the engagement with your instagram post in the following format - "Dx50 @instatravel.lifestyle https://www.instagram.com/p/CCk4PN9sz4S/"

Just these three steps and you are actively part of the engagement pod. Relax and watch your account grow naturally. 😊

Contact @theoneknow for inquiries of the <b>Premium Plan</b> to join the engagement pod without having to like or comment from list...
            """,
            parse_mode=telegram.ParseMode.HTML,
            disable_web_page_preview=True
        )
   
        time.sleep(60)
        bot.delete_message(call.message.chat.id, reply.message_id)


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