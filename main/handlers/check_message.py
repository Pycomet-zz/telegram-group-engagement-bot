
message_format = "Dx15 @instatravel.lifestyle https://www.instagram.com/p/CCDc0kRMl_-/"


@bot.message_handler(regexp="^Dx15")
def group_echo(msg):
    """
    Checking The User's Message Within The Licensed Group
    """
    if msg.chat.type == "group" || msg.chat.type == "supergroup":

        #Check the message format
        message = msg.text
        if len(message.strip("/".split("/"))) == 5:

            username = message[1].strip("@")
            link = message[2]


        else:
            bot.reply_to(
                msg,
                f"Wrong Format! The right format is      {message_format}"
            )

        
        
        bot.delete_message(msg.chat.id, msg.message_id)

