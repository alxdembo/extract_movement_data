import pandas as pd


class CargoData:
    """
    Class to perform various calculations over Cargo Data
    """
    def __init__(self, source_file):
        self.source_file = source_file

        # Rows containing NA values are dropped due to unsuitability for the calculations required
        self.source_df = pd.read_parquet(source_file, engine='pyarrow', use_nullable_dtypes=True, columns=[
            "start_timestamp",
            "end_timestamp",
            "vessel_class",
            "id"
        ]).dropna()

    def get_duration(self):
        """
        Returns movement duration time
        :return: Pandas series of movement duration time deltas
        """
        return self.source_df.end_timestamp.astype("datetime64") - self.source_df.start_timestamp.astype("datetime64")

    def get_duration_per_class(self):
        """
        Returns movement duration time per class
        :return: Pandas series of movement duration time deltas with class as an index
        """
        duration_per_class_df = self.source_df[["id", "vessel_class"]].copy()

        duration_per_class_df["duration"] = self.get_duration()

        return duration_per_class_df.groupby("vessel_class")["duration"].sum()

    def print_movements(self):
        """
        Prints movement durations and movement durations per class
        """
        duration_df = self.source_df
        duration_df["duration"] = self.get_duration()

        print("\nMovement duration: \n", duration_df.to_string())
        print("\nMovement duration per class: \n", self.get_duration_per_class().to_string())


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="A source file to extract movements from.")
    args = parser.parse_args()
    #
    cargo_data = CargoData(args.source)
    cargo_data.print_movements()
