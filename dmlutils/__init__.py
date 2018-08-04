

def tile_generator(im, ts=256):

    xdim, ydim, _ = im.shape
    nx = xdim//ts
    ny = ydim//ts

    for x in range(nx):
        for y in range(ny):
            itile = im[x*ts:(x+1)*ts,y*ts:(y+1)*ts]
            yield itile