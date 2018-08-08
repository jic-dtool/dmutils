
import os

import pytest
import dtoolcore

import numpy as np

from imageio import imread

from . import TEST_DATASET
from . import TEST_SAMPLE_DATA


def test_tile_generation():

	from dmlutils import tile_generator

	im = imread(os.path.join(TEST_SAMPLE_DATA, '000.png'))

	tgen = tile_generator(im)
	tile = next(tgen)
	assert tile.shape == (256, 256, 3)

	tgen = tile_generator(im, ts=512)
	tile = next(tgen)
	assert tile.shape == (512, 512, 3)

	tgen = tile_generator(im, ts=512)
	for x in range(15):
		next(tgen)

	with pytest.raises(StopIteration):
		next(tgen)


def test_dataset_tile_generation():

	from dmlutils import dataset_tile_generator

	dgen = dataset_tile_generator(TEST_DATASET)
	
	image, mask = next(dgen)
	assert image.shape == (256, 256, 3)
	assert mask.shape == (256, 256)
	im = imread(os.path.join(TEST_SAMPLE_DATA, '000.png'))
	assert np.array_equal(image, im[:256,:256,:])

