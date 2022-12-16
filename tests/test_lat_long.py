import pytest

from vhpy import get_lat_long


def _normalize(ll: (float, float)) -> (str, str):
    fmt = "{:0.12f}"
    lat = fmt.format(ll[0])
    lon = fmt.format(ll[1])
    return lat, lon


@pytest.mark.parametrize(
    "v, h, expected",
    [
        # (0, 0, (50.7305527204251, -42.80542199513297)),
        (0, 10000, (75.7219237114612, -140.78132538587545)),
        (10000, 0, (18.014218111556353, -81.93468837339516)),
        (10000, 10000, (31.33343084347239, -130.14529211618458)),
    ],
)
def test_lat_long(v, h, expected):
    coords = get_lat_long(v, h)
    assert isinstance(coords, tuple)
    assert len(coords) == 2
    assert isinstance(coords[0], float)
    assert isinstance(coords[1], float)

    fmt_coords = _normalize(coords)
    expected = _normalize(expected)
    assert fmt_coords == expected, f"Expected: {expected} Got: {coords}"
