
from imageio import imread


def identifiers_where_overlay_is_true(dataset, overlay_name):

    overlay = dataset.get_overlay(overlay_name)

    selected = [identifier
                for identifier in dataset.identifiers
                if overlay[identifier]]

    return selected


def tile_generator(im, ts=256):

    xdim, ydim = im.shape[0], im.shape[1]

    nx = xdim//ts
    ny = ydim//ts

    for x in range(nx):
        for y in range(ny):
            itile = im[x*ts:(x+1)*ts,y*ts:(y+1)*ts]
            yield itile


def dataset_tile_generator(dataset, ts=256):

    mask_ids = dataset.get_overlay("mask_ids")
    for imid in identifiers_where_overlay_is_true(dataset, "is_image"):
        im = imread(dataset.item_content_abspath(imid))
        mask = imread(dataset.item_content_abspath(mask_ids[imid]))

        imgen = tile_generator(im, ts=ts)
        maskgen = tile_generator(mask, ts=ts)
        for itile, mtile in zip(imgen, maskgen):
            yield itile, mtile