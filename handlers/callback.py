from app import *


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
        
        bot.send_message(
            call.message.chat.id,
            f"""
<b>Dx15 INSTAGRAM LIST</b>

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
       
            """,
            parse_mode=telegram.ParseMode.HTML,
            disable_web_page_preview=True
        )

    elif call.data == "send_ad":
        question = bot.send_message(
            msg.from_user.id,
            "Paste your advestisement writing below to post to Dx15 Engagement Group...."
        )
        bot.register_next_step_handler(question, send_ad)


    elif call.data == "premium":
        ### ADD AND REMOVE PREMIUM USERS
        pass

    else:
        pass






def send_ad(msg):
    "Sends Add Message To Group"
    message = msg.text

    bot.send_message(
        GROUP_ID,
        f"<b>{message}</b>",
        parse_mode=telegram.ParseMode.HTML
    )

    # Fetch List
    file = open("main/list.json", 'rb')
    data = pickle.load(file)
    file.close()
    
    bot.send_message(
        GROUP_ID,
        f"""
<b>Dx15 INSTAGRAM LIST</b>

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
    
        """,
        parse_mode=telegram.ParseMode.HTML,
        disable_web_page_preview=True
    )