import pandas as pd


class CargoData:
    def __init__(self, source_file):
        self.source_file = source_file
        self.source_df = pd.read_parquet(source_file)

    def print_movements(source_file):
        raise NotImplementedError


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="A source file to extract movements from.")
    args = parser.parse_args()

    print_movements(args.source)
