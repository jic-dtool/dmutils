import os

from dtoolcore import DataSet

_HERE = os.path.dirname(__file__)
TEST_SAMPLE_DATA = os.path.join(_HERE, "data")
ds_path = os.path.join(TEST_SAMPLE_DATA, 'test_tile_generator')
TEST_DATASET = DataSet.from_uri(ds_path)