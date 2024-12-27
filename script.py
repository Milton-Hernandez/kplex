
import logging
import sys

from config.settings import Settings
from data import DataBook, DataTable
from util import Log

if __name__ == '__main__':
    log = Log(logging.DEBUG)
    settings = Settings()
    settings.init_fs()
    settings.addtional = 'additional'
    print(settings.base_dir)
    print(settings.data_dir)
    print(settings.log_dir)
    print(settings.model_dir)
    print(settings.app_name)
    print(settings.addtional)
    print(settings.any_var)
    print(settings.all_vars)

    dt = DataTable({'A': [1, 2, 3], 'B': [4, 5, 6]},'tbl1')
    db = DataBook()
    db.add_table(dt)
   # db.tbl1.view_table() # I want to be able to use the table name as an attribute
