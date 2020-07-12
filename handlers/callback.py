from app import *


@bot.callback_query_handler(func=lambda call: True)
def callback_answer(call):
    """
    Button Response
    """
    if call.data == "list":

        # Fetch List
        file = open("list.json", 'rb')
        data = pickle.load(file)
        file.close()
        
        bot.reply_to(
            msg,
            """
Dx15 INSTAGRAM LIST
1)  {data[0]['media_url']}
2)  {data[1]['media_url']}
3)  {data[2]['media_url']}
4)  {data[3]['media_url']}
5)  {data[4]['media_url']}
6)  {data[5]['media_url']}
7)  {data[6]['media_url']}
8)  {data[7]['media_url']}
9)  {data[8]['media_url']}        
10)  {data[9]['media_url']}        
11)  {data[10]['media_url']}        
12)  {data[11]['media_url']}        
13)  {data[12]['media_url']}        
14)  {data[13]['media_url']}        
15)  {data[14]['media_url']}        
            """
        )

    elif call.data == "send_ad":
        pass


    elif call.data == "premium":
        pass

    else:
        pass