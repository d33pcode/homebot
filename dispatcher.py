import datetime
import random
import subprocess


def ping():
    return 'PONG'

def help_message():
    return "Command list:\n" + ''.join([c + '\n' for c in cmap])

def not_found():
    return "Command not found.\nType help for a command list."


def echo_date():
    return datetime.datetime.now()


def roll_dice():
    return random.randint(1, 6)


def uptime():
    p = subprocess.Popen(['uptime'], stdout=subprocess.PIPE)
    out, err = p.communicate()
    return out


cmap = {
    'help': help_message,
    '/roll': roll_dice,
    '/time': echo_date,
    'ping': ping,
    'uptime': uptime,
}


def dispatch(c):
    return cmap[c]() if c in cmap else not_found()
