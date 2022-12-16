def test_original():
    """Adapted from original source code: http://www.burgerbum.com/python/testVH.py"""
    from vhpy.VH import VH

    # Starting with v,h = 7000, 3000
    vh = VH(7000, 3000)

    # Distance to 2001,3001 should be 1613.5873078330778 miles
    assert vh.distance(2001, 3001) == 1613.710289983924

    # Distance to 2001,3001 should be 2596.817052337317 kilometers
    assert vh.miles2km(vh.distance(2001, 3001)) == 2597.0149729238883

    # Distance to 2001,3001 (through converter twice) should be 1613.5873078322106 miles
    assert vh.km2miles(vh.miles2km(vh.distance(2001, 3001))) == 1613.7102899830568

    # Algorithm #2 Distance to 2001,3001 should be 1580.8099264048478 miles
    assert vh.distance_algorithm2(2001, 3001) == 1580.8099264048478

    # Convert VH to Lat Lon
    # Lat Lon should be (36.82549281982578, -88.20724414805579)
    assert vh.vh2ll() == (36.82549281982578, -88.20724414805579)

    # Convert Lat, Lon back to VH
    # VH should be (6999.999503500015, 3000.0002577874247)
    assert vh.ll2vh(vh.vh2ll()) == (6999.999503500015, 3000.0002577874247)
