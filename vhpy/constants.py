import math


TRANSV = 6363.235
TRANSH = 2250.700

EX = 0.40426992
EY = 0.68210848
EZ = 0.60933887

WX = 0.65517646
WY = 0.37733790
WZ = 0.65449210

PX = -0.555977821730048699
PY = -0.345728488161089920
PZ = 0.755883902605524030

RADIUS = 12481.103

rot = math.radians(76.597497064)
ROTC = math.cos(rot)
ROTS = math.sin(rot)

GX = 0.216507961908834992
GY = -0.134633014879368199

A = 0.151646645621077297

Q = -0.294355056616412800
Q2 = 0.0866448993556515751
EPSILON = 0.0000001

K1 = 0.99435487
K2 = 0.00336523
K3 = -0.00065596
K4 = 0.00005606
K5 = -0.00000188

M_PI_2 = math.pi / 2.0

K9 = RADIUS * ROTC
K10 = RADIUS * ROTS