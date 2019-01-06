import yaml
import logging

def get_logger():
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
    return log

def get_config(fname='config.yaml'):
    with open(fname) as f:
        config = yaml.load(f)
    return config
