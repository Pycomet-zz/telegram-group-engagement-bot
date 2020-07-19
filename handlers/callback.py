from app import *
from main.functions import Subscriber


@bot.callback_query_handler(func=lambda call: True)
def callback_answer(call):
    """
    Button Response
    """
    if call.data == "list":

        # Fetch List
        file = open("main/list.json", 'rb')
        data = pickle.load(file)
        file.close()
        
        message = bot.send_message(
            call.message.chat.id,
            f"""
<b>Dx30 INSTAGRAM LIST</b>

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
11)  {data[10].get("media_url")}        
12)  {data[11].get("media_url")}        
13)  {data[12].get("media_url")}        
14)  {data[13].get("media_url")}        
15)  {data[14].get("media_url")}
16)  {data[15].get("media_url")}
17)  {data[16].get("media_url")}
18)  {data[17].get("media_url")}
19)  {data[18].get("media_url")}
20)  {data[19].get("media_url")}
21)  {data[20].get("media_url")}
22)  {data[21].get("media_url")}
23)  {data[22].get("media_url")}
24)  {data[23].get("media_url")}
25)  {data[24].get("media_url")}
26)  {data[25].get("media_url")}
27)  {data[26].get("media_url")}
28)  {data[27].get("media_url")}
29)  {data[28].get("media_url")}
30)  {data[29].get("media_url")}


            """,
            parse_mode=telegram.ParseMode.HTML,
            disable_web_page_preview=True
        )

        time.sleep(20)
        bot.delete_message(message.chat.id, message.message_id)

    elif call.data == "ad":
        question = bot.send_message(
            call.from_user.id,
            "Paste your advestisement writing below to post to Dx30 Engagement Group....",
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

    # Fetch List
    file = open("main/list.json", 'rb')
    data = pickle.load(file)
    file.close()
    
    bot.send_message(
        int(GROUP_ID),
        f"""
<b>{message}</b>

--------------------------
<b>Dx30 INSTAGRAM LIST</b>
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
11)  {data[10].get("media_url")}        
12)  {data[11].get("media_url")}        
13)  {data[12].get("media_url")}        
14)  {data[13].get("media_url")}        
15)  {data[14].get("media_url")}
16)  {data[15].get("media_url")}
17)  {data[16].get("media_url")}
18)  {data[17].get("media_url")}
19)  {data[18].get("media_url")}
20)  {data[19].get("media_url")}
21)  {data[20].get("media_url")}
22)  {data[21].get("media_url")}
23)  {data[22].get("media_url")}
24)  {data[23].get("media_url")}
25)  {data[24].get("media_url")}
26)  {data[25].get("media_url")}
27)  {data[26].get("media_url")}
28)  {data[27].get("media_url")}
29)  {data[28].get("media_url")}
30)  {data[29].get("media_url")}
    
        """,
        parse_mode=telegram.ParseMode.HTML,
        disable_web_page_preview=True
    )