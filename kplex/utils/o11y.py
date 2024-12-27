#Singleton class to implement a logger that can take the log level as a constructor argument and implements the debug, info, warning and error methods

import logging

#Singleton class to implement a logger that can take the log level as a constructor argument and implements the debug, info, warning and error methods
class Log:
    __instance = None

    def __new__(cls, log_level_str='INFO'):
        log_level = getattr(logging, log_level_str)
        if Log.__instance is None:
            Log.__instance = object.__new__(cls)
            Log.__instance.log_level = log_level
            Log.__instance.logger = logging.getLogger()
            Log.__instance.logger.setLevel(log_level)
            Log.__instance.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            Log.__instance.console_handler = logging.StreamHandler()
            Log.__instance.console_handler.setFormatter(Log.__instance.formatter)
            Log.__instance.logger.addHandler(Log.__instance.console_handler)
        else:
            Log.__instance.log_level = log_level
            Log.__instance.logger.setLevel(log_level)
            Log.__instance.console_handler.setLevel(log_level)
        return Log.__instance

    def debug(self, message):
        if self.log_level == logging.DEBUG:
            self.logger.debug(message)

    def info(self, message):
        if self.log_level <= logging.INFO:
            self.logger.info(message)

    def warning(self, message):
        if self.log_level <= logging.WARNING:
            self.logger.warning(message)

    def error(self, message):
        if self.log_level <= logging.ERROR:
            self.logger.error(message)
