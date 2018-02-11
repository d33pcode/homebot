#!/usr/bin/env python

import logging
import os
import time

import telepot

import dispatcher


def handle(msg):
    log.debug(msg)
    chat_id = msg['chat']['id']
    username = msg['from']['username']

    if 'text' in msg:
        log.debug('command received from ' + username)
        command = msg['text'].lower()
        result = dispatcher.dispatch(command)
        homebot.sendMessage(chat_id, str(result))

    elif 'document' in msg:
        log.debug('document received from ' + username)
        download_path = downloads_dir + msg['document']['file_name']
        homebot.sendMessage(chat_id, 'Document received. Starting download...')
        res = homebot.download_file(
            file_id=msg['document']['file_id'], dest=download_path)
        log.debug(res)
        homebot.sendMessage(chat_id, 'Download completed.')

    elif 'audio' in msg:
        log.debug('audio received from ' + username)
        download_path = downloads_dir + (msg['audio']['performer'] + '_' + msg['audio']['title']).replace(' ', '_')
        homebot.sendMessage(chat_id, 'Audio received. Starting download...')
        res = homebot.download_file(
            file_id=msg['audio']['file_id'], dest=download_path)
        homebot.sendMessage(chat_id, 'Download completed.')


my_id = 5778849
downloads_dir = './downloads/'
homebot = telepot.Bot('346659556:AAHJmpdZ4eN5inoKug_WOnvJFjZ0XApLDGQ')
# logging.basicConfig(level=logging.DEBUG,
#                     format='[%(asctime)s] %(levelname)s:\t %(message)s',
#                     filename='bot.log')


log = logging.getLogger('homebot')
log.setLevel(logging.DEBUG)
fh = logging.FileHandler('bot.log')
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s] %(levelname)s:\t %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
log.addHandler(fh)
log.addHandler(ch)


homebot.sendMessage(my_id, 'homebot started.')
homebot.message_loop(handle)
log.info('I am listening ...')
while 1:
    time.sleep(10)
log.info('homebot stopped.')
