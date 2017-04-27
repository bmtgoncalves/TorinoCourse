import gzip

header = {}
line_count = 0

for line in gzip.open("data/enwiki-20170420-geo_tags.csv.gz", "rt"):
	fields = line.strip().split(',')

	if line_count == 0:
		header = dict(zip(fields, range(len(fields))))

	line_count += 1

	if(fields[header["gt_globe"]] == "earth"):
		print(fields[header["gt_lat"]], fields[header["gt_lon"]])
