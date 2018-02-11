#!/usr/bin/env python

import os
import time

import telepot
import logging
import dispatcher


def handle(msg):
    print(msg)
    chat_id = msg['chat']['id']
    username = msg['from']['username']

    if 'text' in msg:
        command = msg['text'].lower()
        print('command received from ' + username)
        result = dispatcher.dispatch(command)
        homebot.sendMessage(chat_id, str(result))

    elif 'document' in msg:
        download_path = os.path.curdir + '/' + msg['document']['file_name']
        print('document received from ' + username)
        homebot.sendMessage(chat_id, 'Document received. Starting download...')
        res = homebot.download_file(file_id=msg['document']['file_id'], dest=download_path)
        print(res)
        homebot.sendMessage(chat_id, 'Download completed.')

    elif 'audio' in msg:
        download_path = os.path.curdir + '/' + (msg['audio']['performer'] + '_' + msg['audio']['title']).replace(' ', '_')
        print('audio received from ' + username)
        homebot.sendMessage(chat_id, 'Audio received. Starting download...')
        res = homebot.download_file(file_id=msg['audio']['file_id'], dest=download_path)
        homebot.sendMessage(chat_id, 'Download completed.')

homebot = telepot.Bot('346659556:AAHJmpdZ4eN5inoKug_WOnvJFjZ0XApLDGQ')
my_id = 5778849

homebot.sendMessage(my_id, 'homebot started.')

homebot.message_loop(handle)
print('I am listening ...')
while 1:
    time.sleep(10)
print('homebot stopped.')
