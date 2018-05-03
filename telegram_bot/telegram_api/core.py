import json

import requests


class TelegramApi(object):
    """
    """

    URL = "https://api.telegram.org/bot"

    def __init__(self, token):
        self.token = token

    def get_me(self, save=False):
        """

        :param save:
        :return:
        """
        _url = self.URL + self.token + "/getMe"
        req = requests.get(_url)
        if save:
            save_json("telegram_get_me.json", req.json())
        return req.json()

    def get_updates(self, save=False):
        """

        :param save:
        :return:
        """
        _url = self.URL + self.token + "/getUpdates"
        req = requests.get(_url)
        if save:
            save_json("telegram_get_updates.json", req.json())
        return req.json()

    def send_message(self, chat_id, text, mode_html=False, save=False):
        """

        :param chat_id:
        :param text:
        :param mode_html:
        :param save:
        :return:
        """
        _url = self.URL + self.token + "/sendMessage"
        if mode_html:
            data = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
        else:
            data = {"chat_id": chat_id, "text": text}
        req = requests.post(_url, json=data)
        if save:
            save_json("telegram_send_message.json", req.json())
        return req.json()

    def set_webhook(self, url, save=False):
        """

        :param url:
        :param save:
        :return:
        """
        _url = self.URL + self.token + "/setWebhook"
        data = {"url": url}
        req = requests.post(_url, json=data)
        if save:
            save_json("telegram_set_webhook.json", req.json())
        return req.json()

    def delete_webhook(self, save=False):
        """

        :param save:
        :return:
        """
        _url = self.URL + self.token + "/deleteWebhook"
        req = requests.get(_url)
        if save:
            save_json("telegram_delete_webhook.json", req.json())
        return req.json()

    def get_webhook_info(self, save=False):
        """

        :param save:
        :return:
        """
        _url = self.URL + self.token + "/getWebhookInfo"
        req = requests.get(_url)
        if save:
            save_json("telegram_get_webhook_info.json", req.json())
        return req.json()


def save_json(file, json_data):
    """

    :param file:
    :param json_data:
    :return:
    """
    with open(file, "w", encoding="utf8") as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)