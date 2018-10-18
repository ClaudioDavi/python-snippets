import numpy as np
import logging


class Module():

    def __init__(self):
        self.__values = [3,4,5,6,7,8]
        self.logger = logging.getLogger('module')

    def get_mean(self):
        self.logger.info('Calculating the mean')
        return np.mean(self.__values)