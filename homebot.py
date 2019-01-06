#!/usr/bin/env python

import logging
import os
import time

import yaml

import telepot
from botlib import dispatcher, utils


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


conf = utils.get_config()

# my_id = 5778849
downloads_dir = conf.get('download_dir')
botconf = conf.get('bot', {})
homebot = telepot.Bot('{k}:{s}'.format(k=botconf.get('key'),
                                       s=botconf.get('secret')))

log = utils.get_logger()

# homebot.sendMessage(my_id, 'homebot started.')
homebot.message_loop(handle)
log.info('I am listening ...')
while 1:
    time.sleep(10)
log.info('homebot stopped.')
