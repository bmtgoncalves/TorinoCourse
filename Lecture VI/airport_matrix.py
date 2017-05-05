from geopy import distance

airports = {}

for line in open("airport_gps.dat"):
	fields = line.strip().split()

	airport_id = int(fields[0])
	lat = float(fields[1])
	lon = float(fields[2])

	airports[airport_id] = (lat, lon)

airport_list = airports.keys()

for airport_i in airport_list:
	for airport_j in airport_list:
		try:
			if airport_i != airport_j:
				dist = distance.distance(airports[airport_i], airports[airport_j]).km

				if dist < 20:
					print(airport_i, airport_j, dist)
		except:
			pass
