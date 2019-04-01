#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from rasa_core.channels.telegram import TelegramOutput


class TelegramBot(TelegramOutput):
    @classmethod
    def name(cls):
        return "telegram_bot"

    def __init__(self, access_token):
        super(TelegramBot, self).__init__(access_token)

    def send_file(self, chat_id, document):
        self.send_document(chat_id, document)
