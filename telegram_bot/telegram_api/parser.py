import telegram_bot.libs_api.core as libs


def parse_text(message_text, first_name, language_code):
    """

    :param message_text:
    :param first_name:
    :param language_code:
    :return:
    """
    if "/launches" in message_text:
        launches = libs.upcoming_launches(6)
        text = ""
        for launch in launches:
            if launch["tbd"]:
                tbd = "(<b>TBD</b>)"
            else:
                tbd = ""
            text += "<b>{}</b>\n{}\n<i>{}</i> {}\n\n".format(launch["name"], launch["location"], launch["net"], tbd)
        return text
    elif "/weather" in message_text:
        return "weather"
    elif "/money" in message_text:
        return "money"
    elif "/hello" in message_text:
        return "Hello {}!".format(first_name)
    elif "/help" in message_text:
        return "<b>Commands</b>\n" \
               "/launches - <b>Upcoming Launches</b>\n" \
               "/weather - <b>Weather on your place</b>\n" \
               "/money - <b>Exchange Rates</b>\n" \
               "/hello - <b>Hello test message</b>\n" \
               "/help - <b>This message</b>"
    else:
        return None
