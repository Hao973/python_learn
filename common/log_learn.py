# -*- coding: utf-8 -*- 
# @Time : 2019/7/10 20:15 
# @Author : FengHao 
# @Site :  
# @File : log_learn.py
# @Software: PyCharm Community Edition

import logging
import logging.handlers
DEFAULT_LOG_FORMAT = '%(asctime)-15s %(levelname)s %(process)d %(name)s %(funcName)s %(message)s'

class LogHelper(object):

    def __init__(self, logfile, logger, level=logging.DEBUG, fmt=DEFAULT_LOG_FORMAT):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(level)
        handler = logging.handlers.TimedRotatingFileHandler(logfile, 'midnight', 1, 10)
        handler.setLevel(level)
        handler.setFormatter(logging.Formatter(fmt=fmt, datefmt='%Y-%m-%d %H:%M:%S'))
        self.logger.addHandler(handler)

    def getlog(self):
        return self.logger

if __name__ == '__main__':
    pass
