import os
import sys
import tempfile

class Settings:

    base_dir = '~/kplex'
    app_name = 'default'
    @property
    def data_dir(self):
        return self.base_dir + self._data_dir

    @property
    def log_dir(self):
        return self.base_dir + self._log_dir

    @property
    def model_dir(self):
        return self.base_dir + self._model_dir

    _data_dir = '/data'
    _log_dir = '/log'
    _model_dir = '/models'

    def load_props(self):
        if len(sys.argv) > 0:
            self.app_name = sys.argv[0].replace('.py', '')
        for i in range(1, len(sys.argv), 2):
            token = sys.argv[i]
            if token[0] == '-':
                token = token.replace('-', '')
                setattr(self, token, sys.argv[i+1])
                print(self.base_dir)

    def init_fs(self):
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        if not os.path.exists(self.model_dir):
            os.makedirs(self.model_dir)

    def __init__(self, base_dir=None):
        if base_dir is not None:
            self.base_dir = base_dir  
        self.load_props()
 
          
