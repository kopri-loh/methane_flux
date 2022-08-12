from pyproj import Transformer as trf

ll_proj = "epsg:4326"
co_proj = "epsg:3857"

trf_c2ll = trf.from_crs(co_proj, ll_proj)
trf_ll2c = trf.from_crs(ll_proj, co_proj)


def c2ll(x, y):
    return trf_c2ll.transform(x, y)


def ll2c(x, y):
    return trf_ll2c.transform(x, y)
