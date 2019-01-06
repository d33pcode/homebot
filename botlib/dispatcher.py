import datetime
import random
import subprocess
import pydoc

def ping():
    """Ping the bot."""
    return '`PONG`'


def help_message(command=None):
    """Print the help message.

    :param command: if specified, prints the help message of command."""
    if command:
        if command in cmap:
            return command + ':\n' + ''.join(pydoc.render_doc(cmap[command]).splitlines()[3:])
        else:
            return not_found()
    return "Command list:\n" + ''.join([c + '\n' for c in cmap])


def not_found():
    return "Command not found.\nType __help__ for a command list."


def uptime():
    """Print the current server's uptime."""
    return run_proc('uptime')


def get_ip():
    """Return the current IP address of the server."""
    return run_proc('curl ifconfig.co')


def run_proc(command):
    """Runs a command as a subprocess.

    :param command: a list containing the command and its args
    :return: the command output
    """
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         shell=True)
    out, err = p.communicate()
    if err:
        logging.err(err)
    return out.decode('utf-8').replace('\n', chr(10))


cmap = {'help': help_message,
        'ping': ping,
        'uptime': uptime,
        'ip': get_ip}

def dispatch(command):
    clist = command.split()
    if len(clist) > 1:
        return cmap.get(clist[0], help_message)(*clist[1:]) # call function in cmap with arguments
    else:
        return cmap.get(command, help_message)()
