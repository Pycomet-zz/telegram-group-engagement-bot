from config import *

server = Flask(__name__)

import importdir
importdir.do("handlers", globals())

@server.route('/' + TOKEN, methods=['POST', 'GET'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL + TOKEN)
    return "Application Running", 200


if __name__ == "__main__":

    if DEBUG == True:
        print("bot polling...")

        bot.remove_webhook()
        bot.polling(none_stop=True)
    else:
        server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))



