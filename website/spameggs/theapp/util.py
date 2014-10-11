from math import sin, cos, sqrt, atan2, radians

R = 6373.0


def lat_long_distance(lon_a, lat_a, lon_b, lat_b):
    lon_a, lat_a, lon_b, lat_b = [
        radians(i) for i in (lon_a, lat_a, lon_b, lat_b)]

    dlon = lon_b - lon_a
    dlat = lat_b - lat_a
    a = (sin(dlat / 2)) ** 2 + cos(lat_a) * cos(lat_b) * (sin(dlon / 2)) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c

    return distance
