from geojson import Polygon

# no hole within polygon
# Polygon([[(2.38, 57.322), (23.194, -20.28), (-120.43, 19.15), (2.38, 57.322)]])  # doctest: +ELLIPSIS
{"coordinates": [[[2.3..., 57.32...], [23.19..., -20.2...], [-120.4..., 19.1...]]], "type": "Polygon"}

# hole within polygon
Polygon([
    [(2.38, 57.322), (23.194, -20.28), (-120.43, 19.15), (2.38, 57.322)],
     [(-5.21, 23.51), (15.21, -10.81), (-20.51, 1.51), (-5.21, 23.51)]
 ])  # doctest: +ELLIPSIS
{"coordinates": [[[2.3..., 57.32...], [23.19..., -20.2...], [-120.4..., 19.1...]], [[-5.2..., 23.5...], [15.2..., -10.8...], [-20.5..., 1.5...], [-5.2..., 23.5...]]], "type": "Polygon"}

