import pandas as pd
import pytest

@pytest.fixture()
def cargo_movements(tmpdir):
    df = pd.DataFrame({
        "start_timestamp": ['2000-01-01T00:00:00+0000', '2000-01-01T00:00:00+0000', '2000-01-01T00:00:00+0000'],
        "end_timestamp": ['2000-01-02T00:02:00+0000', '2000-01-02T00:02:00+0000', '2000-01-02T00:02:00+0000'],
        "vessel_class": ["test_class_1", "test_class_1", "test_class_2"],
        "id": ["test_id_1", "test_id_2", "test_id_3"]
    })

    filename = tmpdir + 'test.parquet'
    df.to_parquet(filename)

    return filename


def test_print_movements(cargo_movements):
    pd.read_parquet(cargo_movements)

    assert False
