from app import *
from main.functions import Action

@bot.message_handler(regexp="^Dx15")
def echo(msg):
    """
    Checking The User's Message Within The Licensed Group
    """

    message_format = "Dx15 @instatravel.lifestyle https://www.instagram.com/p/CCDtc0kRMl_-/"

    if msg.chat.type == "group" or msg.chat.type == "supergroup":

        #Check the message format
        text = msg.text

        try:
            message = text.split(" ")

            username = message[1].strip("@")

            if len(message[2].strip("/").split("/")) == 5:

                link = message[2]

                action = Action(username, link)
                
                action.get_user_id()
                post = action.get_media_id()

                if post is None:
                    bot.reply_to(
                        msg,
                        f"This post was not found in @{username}'s timeline feed"
                    )
                else:
                    pass
                    ####CHECK IF USER HAS PERFORMED LIKE ACTIONS



            else:
                bot.reply_to(
                    msg,
                    f"""
Wrong Format! The right format is
{message_format}
                    """
                )
        except:
            bot.reply_to(
                msg,
                f"""
Invalid Format! The right format is
{message_format}
                """
            )
            
        bot.delete_message(msg.chat.id, msg.message_id)
        time.sleep(5)

        #delete the next message
        msg.message_id += 1
        bot.delete_message(msg.chat.id, msg.message_id)

    else:

        bot.reply_to(
            msg,
            "You are not authorized to use this endpoint directly! Please go to your referenced Engagment Group"
        )
        
        
        bot.delete_message(msg.chat.id, msg.message_id)
        time.sleep(5)

        #delete the next message
        msg.message_id += 1
        bot.delete_message(msg.chat.id, msg.message_id)