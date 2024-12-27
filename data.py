import pandas as pd # type: ignore
import pandasgui as pg
import json

class DataTable:
    def __init__(self, data: dict, name: str) -> None:
        self.df = pd.DataFrame(data)
        self.df.name = name

    def add_row(self, row: dict) -> None:
        self.df = self.df.append(row, ignore_index=True)

    def remove_row(self, index: int) -> None:
        self.df = self.df.drop(index)

    def get_row(self, index: int) -> pd.Series:
        return self.df.iloc[index]

    def add_column(self, column_name: str, data: list) -> None:
        self.df[column_name] = data

    def remove_column(self, column_name: str) -> None:
        self.df = self.df.drop(columns=[column_name])

    def get_column(self, column_name: str) -> pd.Series:
        return self.df[column_name]

    def filter_rows(self, condition: pd.Series) -> pd.DataFrame:
        return self.df[condition]

    def sort_by_column(self, column_name: str, ascending: bool = True) -> None:
        self.df = self.df.sort_values(by=column_name, ascending=ascending)

    def to_csv(self, file_path: str) -> None:
        self.df.to_csv(file_path, index=False)

    def from_csv(self, file_path: str) -> None:
        self.df = pd.read_csv(file_path)

    def to_json(self, file_path: str) -> None:
        self.df.to_json(file_path, orient='records')

    def view_table(self) -> None:
        pg.show(self.df)


#class DataBook is a named collection of DataTable objects.  It contains a dictionary of DataTable objects, where the keys are the names of the tables.
class DataBook:


    def add_table(self, table) -> None:
        setattr(self, table.df.name, table)

    def add_table_fromcsv(self, file_path: str, name: str) -> None:
        setattr(self, name, DataTable(pd.read_csv(file_path), name))    

    def remove_table(self, table_name: str) -> None:
        delattr(self,table_name)

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
        dfs = {name: table.df for name, table in self.tables.items()}
        pg.show(dfs)
