
from . import TEST_DATASET


def test_tilegen_class():

	from dmlutils import ImageMaskGenerator

	imgen = ImageMaskGenerator(TEST_DATASET)

	assert len(imgen) == 70

	for x in range(75):
		X, Y = next(imgen)

		assert X.shape == (1, 256, 256, 3)
		assert Y.shape == (1, 256, 256, 1)

	# from imageio import imsave
	# imsave('t.png', X[0,:,:,:])