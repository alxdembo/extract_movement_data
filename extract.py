import pandas as pd


class CargoData:
    def __init__(self, source_file):
        self.source_file = source_file
        self.source_df = pd.read_parquet(source_file)


def print_movements(source_file):
    raise NotImplementedError
