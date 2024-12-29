import logging
from kplex.utils.settings import Settings
from kplex.tools.data import DataBook, DataTable

def test_fun1():
    from kplex.utils.o11y import Log
    Log.to.error('function 1')
    set2 = Settings.props
    Log.to.info(set2.base_dir)
    Log.to.info(set2.data_dir)
    Log.to.info(set2.log_dir)
    Log.to.info(set2.model_dir)
    Log.to.info(set2.app_name)
    Log.to.debug(set2.additional)

def test_fun2():
    from kplex.utils.o11y import Log
    set2 = Settings.props
    Log.to.error('Function 2')
    Log.to.info(set2.base_dir)
    Log.to.info(set2.data_dir)
    Log.to.info(set2.log_dir)
    Log.to.info(set2.model_dir)
    Log.to.info(set2.app_name)
    Log.to.debug(set2.additional)

if __name__ == '__main__':
    settings = Settings()
    settings.base_dir = 'd:/data/titanic'
    settings.init_fs()
    settings.additional = 'additional'
    
    test_fun1()
    from kplex.utils.o11y import Log
    Log.to.set_level(Log.DEBUG)
    test_fun2() 

'''
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
'''


