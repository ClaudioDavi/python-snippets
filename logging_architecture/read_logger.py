import os
import yaml

class LogReader():

    def __init__(self):
        pass

    def get_log(self):
        with open('log_config.yaml') as log:
            return yaml.load(log)['log']