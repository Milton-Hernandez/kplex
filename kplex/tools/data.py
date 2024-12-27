from typing import Set
import pandas as pd 
import pandasgui as pg
import json

from kplex.utils.settings import Settings

 
        

class DataTable:
    cols = {}
    _parent = None

    def _reset_cols(self):
        cols = {}
        if(self.df is not None):
            for col in self.df.columns:
                self.cols[col] = self.df[col]

    def __init__(self, name, data=None):
        if data is not None:
            self.df = data
        else:
            self.df = pd.DataFrame()
        self.name = name
        self.cfg = Settings()
        self._reset_cols()

    def add_row(self, row: dict) -> None:
        self.df = self.df.append(row, ignore_index=True)

    def remove_row(self, index: int) -> None:
        self.df = self.df.drop(index)
    
    def rename(self, new_name: str) -> None:
        old_name = self.name
        self.name = new_name
        if(self._parent is not None):
            self._parent.rename_table(old_name, self.name)

    def get_row(self, index: int) -> pd.Series:
        return self.df.iloc[index]

    def add_column(self, column_name: str, data: list) -> None:
        self.df[column_name] = data
        self._reset_cols()

    def remove_column(self, column_name: str) -> None:
        self.df = self.df.drop(columns=[column_name])
        self._reset_cols()

    def get_column(self, column_name: str) -> pd.Series:
        return self.df[column_name]

    def filter_rows(self, condition: pd.Series) -> pd.DataFrame:
        return self.df[condition]

    def sort_by_column(self, column_name: str, ascending: bool = True) -> None:
        self.df = self.df.sort_values(by=column_name, ascending=ascending)

    def to_csv(self) -> None:
        self.df.to_csv(self.cfg.full_path(self.cfg.data_dir, self.name + '.csv'))

    def from_csv(self) -> None:
        self.df = pd.read_csv(self.cfg.full_path(self.cfg.data_dir, self.name + '.csv'))
        self._reset_cols()

    def to_json(self, file_path: str) -> None:
        self.df.to_json(file_path, orient='records')

    def view(self) -> None:
        pg.show(self.df)

    def set_parent(self, parent) -> None:
        self._parent = parent


#class DataBook is a named collection of DataTable objects.  It contains a dictionary of DataTable objects, where the keys are the names of the tables.
class DataBook:
 
    tables = {}

    def add_table(self, table) -> None:
        setattr(self, table.name, table)
        self.tables[table.name] = table
        table.set_parent(self)
  
    def remove_table(self, table_name: str) -> None:
        self.tables[table_name].set_parent(None)
        self.tables.pop(table_name)
        delattr(self,table_name)

    def rename_table(self, old_name: str, new_name: str) -> None:
        self.tables[new_name] = self.tables.pop(old_name)
        setattr(self, new_name, self.tables[new_name])

    def to_json(self, file_path: str) -> None:
        '''Serialize the DataBook object to a JSON file.'''
        data = {}
        for name, table in self.tables.items():
            data[name] = table.df.to_dict(orient='records')
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def from_json(self, file_path: str) -> None:
        '''Deserialize the DataBook object from a JSON file.'''
        with open(file_path, 'r') as f:
            data = json.load(f)
        for name, records in data.items():
            self.tables[name] = DataTable(records, name)

    def view_tables(self) -> None:
        '''Visualize all tables in the DataBook in a GUI window using the PandasGUI library.'''
        dfs = []
        for t in self.tables.values():
            dfs.append(t.df)
        pg.show(dfs)
