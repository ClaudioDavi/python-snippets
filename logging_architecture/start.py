import logging
from read_logger import LogReader
from module import Module


class Starter():
    def __init__(self):
        self.__variable = 'value'

    def run(self):
        logger.info('Running on INFO')
        logger.error('Running on Error')
        print(f'Module Mean: {Module().get_mean()}')
        print(f'Self Variable: {self.__variable}')

log_info = LogReader().get_log()
logging.basicConfig(level=log_info['level'], format=log_info['formatter'])
logger = logging.getLogger('starter')

Starter().run()