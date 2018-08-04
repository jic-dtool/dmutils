
import os

from imageio import imread


_HERE = os.path.dirname(__file__)
TEST_SAMPLE_DATA = os.path.join(_HERE, "data")


def test_tile_generation():

	from dmlutils import tile_generator

	im = imread(os.path.join(TEST_SAMPLE_DATA, '000.png'))

	tgen = tile_generator(im)
	tile = next(tgen)
	assert tile.shape == (256, 256, 3)

	tgen = tile_generator(im, ts=512)
	tile = next(tgen)
	assert tile.shape == (512, 512, 3)
