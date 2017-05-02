from geopy import distance

p1 = (41.49008, -71.312796)
p2 = (41.499498, -81.695391)

dist_vincenty = distance.vincenty(p1, p2).meters
dist_great = distance.great_circle(p1, p2).meters

print("Vincenty:", dist_vincenty)
print("Great Circles:", dist_great)