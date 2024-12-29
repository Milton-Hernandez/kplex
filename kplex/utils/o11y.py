from enum import Enum
import logging

class Log:  
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL    

    to = None
    def all_off(self):
        self._debug_on = False
        self._info_on = False
        self._warning_on = False
        self._error_on = False
  
    def set_level(self,log_level):
        self.all_off()
        if(log_level == logging.DEBUG):
            self._debug_on = self.info_on = self.warning_on = self.error_on = True
        if (log_level == logging.INFO):
            self._info_on = self.warning_on = self.error_on = True
        if (log_level == logging.WARNING):    
            self._warning_on = self.error_on = True
        if (log_level == logging.ERROR):  
            self._error_on = True
        self.logger.setLevel(log_level)    

    def debug(self, message):
        if self._debug_on:
            self.logger.debug(message)

    def info(self, message):
        if self._info_on:
            self.logger.info(message)

    def warning(self, message):
        if self.log_level <= logging.WARNING:
            self.logger.warning(message)

    def error(self, message):
        if self.log_level <= logging.ERROR:
           self.logger.error(message)

class SimpleLog(Log):
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
  
    def __init__(self, log_level_str='INFO'):
        self.log_level = getattr(logging, log_level_str.upper())  
        self.logger = logging.getLogger()
        self.set_level(self.log_level)
        self.logger.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.logger.console_handler = logging.StreamHandler()
        self.logger.console_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.logger.console_handler)

if Log.to == None:
    Log.to = SimpleLog()