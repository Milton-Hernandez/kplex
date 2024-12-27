

from kplex.utils.settings import Settings
from kplex.tools.data import DataBook, DataTable
from kplex.utils.o11y import Log




if __name__ == '__main__':
    log = Log('debug')
    settings = Settings()
    settings.base_dir = 'd:/data/titanic'
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

    dt = DataTable('train')
    dt.from_csv()
    dt2 = DataTable('test')
    dt2.from_csv()
    db = DataBook()
    db.add_table(dt)
    db.add_table(dt2)
    db.train.df.info()  
    db.train.rename('train_data')
    db.train_data.df.info()


    api = KaggleApi()
    api.authenticate()

