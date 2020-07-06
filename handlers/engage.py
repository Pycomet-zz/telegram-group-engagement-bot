from app import *

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

                bot.send_message(
                    msg.chat.id,
                    f"""
    Username - instagram.com/{username}
    Picture url - {link}
                    """
                )


            ###################################ADD LISTING BUSINESS LOGIC
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

    else:

        bot.reply_to(
            msg,
            "You are not authorized to use this endpoint directly! Please go to your referenced Engagment Group"
        )
        
        
        bot.delete_message(msg.chat.id, msg.message_id)
