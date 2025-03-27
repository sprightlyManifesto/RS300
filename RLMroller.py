from cadquery import Workplane as WP
from math import sin, pi
import cadquery as cq

OD = 65
LOA = 82
L1 = 80
mastD = 78
slotRad = 2
slotD = 50 
ID = 8.3
D1 = 30
slotIncludedAngle = 40
slotPitch = 35

#turned form
a = WP().moveTo(LOA/2,ID/2).lineTo(LOA/2,D1/2).lineTo(L1/2,D1/2)\
    .lineTo(L1/2,OD/2).lineTo(-L1/2,OD/2)\
    .lineTo(-L1/2,D1/2).lineTo(-LOA/2,D1/2).lineTo(-LOA/2,ID/2)\
    .close()
a = a.revolve(360,(0,0,0),(1,0,0))

#mast form
a = a.cut(WP().moveTo(0,57).circle(mastD/2).revolve(360,(0,0,0),(1,0,0)))
#slots
y = 20
for x  in  (slotPitch,-slotPitch):
    dx = y*sin(slotIncludedAngle*pi/180/2)
    if slotIncludedAngle != 0:
        a = a.cut(WP().moveTo(x,slotD/2+slotRad)\
                  .lineTo(x+dx,slotD/2+slotRad+y).lineTo(x-dx,slotD/2+slotRad+y)\
                  .close().offset2D(slotRad).revolve(360,(0,0,0),(1,0,0)))
    else:
        a = a.cut(WP().moveTo(x,slotD/2+slotRad).lineTo(x+dx,slotD/2+slotRad+y).close()\
                  .offset2D(slotRad).revolve(360,(0,0,0),(1,0,0)))

SECTION = True
if SECTION:
    a = a.cut(WP().rect(100,100).extrude(100))

cq.exporters.export(a,"RLMroller.stl")
cq.exporters.export(a,"RLMroller.step")