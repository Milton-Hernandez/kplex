
import logging
import sys

from kplex.utils.settings import Settings
from kplex.tools.data import DataBook, DataTable
from kplex.utils.o11y import Log

if __name__ == '__main__':
    log = Log('debug')
    settings = Settings()
    settings.init_fs()
    settings.additional = 'additional'
    log.info('This is an info message')
    set2 = Settings()
    log.info(set2.base_dir)
    log.info(set2.data_dir)
    log.info(set2.log_dir)
    log.info(set2.model_dir)
    log.info(set2.app_name)
    log.debug(set2.additional)

    dt = DataTable({'A': [1, 2, 3], 'B': [4, 5, 6]},'tbl1')
    db = DataBook()
    db.add_table(dt)
   # db.tbl1.view_table() # I want to be able to use the table name as an attribute
