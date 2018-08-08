
from imageio import imread


def identifiers_where_overlay_is_true(dataset, overlay_name):

    overlay = dataset.get_overlay(overlay_name)

    selected = [identifier
                for identifier in dataset.identifiers
                if overlay[identifier]]

    return selected


def tile_generator(im, ts=256):

    rows, cols = im.shape[0], im.shape[1]

    nr = rows//ts
    nc = cols//ts

    for r in range(nr):
        for c in range(nc):
            tile = im[r*ts:(r+1)*ts,c*ts:(c+1)*ts]
            yield tile


def dataset_tile_generator(dataset, ts=256):

    mask_ids = dataset.get_overlay("mask_ids")
    for imid in identifiers_where_overlay_is_true(dataset, "is_image"):
        im = imread(dataset.item_content_abspath(imid))
        mask = imread(dataset.item_content_abspath(mask_ids[imid]))

        imgen = tile_generator(im, ts=ts)
        maskgen = tile_generator(mask, ts=ts)
        for itile, mtile in zip(imgen, maskgen):
            yield itile, mtile


class ImageMaskGenerator(object):

    @classmethod
    def __init__(self, dataset, ts=256):

        self.dataset = dataset
        self.ts = ts

        self.tgen = dataset_tile_generator(dataset, ts)

    def __len__(self):

        count = 0
        for imid in identifiers_where_overlay_is_true(self.dataset, "is_image"):
            im = imread(self.dataset.item_content_abspath(imid))
            rows, cols = im.shape[0], im.shape[1]

            nr = rows//self.ts
            nc = cols//self.ts

            count += nr * nc

        return count

    def __next__(self):

        try:
            itile, mtile =  next(self.tgen)

        except StopIteration:
            self.tgen = dataset_tile_generator(self.dataset, self.ts)
            itile, mtile = next(self.tgen)

        X = itile.reshape(1, self.ts, self.ts, 3)
        Y = mtile.reshape(1, self.ts, self.ts, 1)

        return X, Y