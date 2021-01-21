import pandas as pd
import pytest
from extract import CargoData
from datetime import datetime, timedelta

@pytest.fixture()
def cargo_movements(tmpdir):
    df = pd.DataFrame({
        "start_timestamp": [datetime(2000, 1, 1, 1, 1, 1), datetime(2000, 1, 1, 1, 1, 1), datetime(2000, 1, 1, 1, 1, 1)],
        "end_timestamp": [datetime(2000, 1, 1, 1, 1, 2), datetime(2000, 1, 1, 1, 1, 3), datetime(2000, 1, 1, 1, 1, 5)],
        "vessel_class": ["test_class_1", "test_class_1", "test_class_2"],
        "id": ["test_id_1", "test_id_2", "test_id_3"]
    })

    filename = tmpdir + 'test.parquet'
    df.to_parquet(filename)

    return filename


def test_get_duration(cargo_movements):
    cargo_data = CargoData(cargo_movements)
    actual = cargo_data.get_duration().to_dict()
    expected = {
        0: timedelta(0,1),
        1: timedelta(0,2),
        2: timedelta(0,4)
    }

    assert actual == expected

def test_get_duration_per_class(cargo_movements):
    cargo_data = CargoData(cargo_movements)
    actual = cargo_data.get_duration_per_class().to_dict()
    expected = {
        "test_class_1": timedelta(0,3),
        "test_class_2": timedelta(0,4)
    }

    assert actual == expected
