import gzip

header = {}
line_count = 0

ll_from = {}
for line in gzip.open("data/acewiki-20170420-langlinks.csv.gz", "rt"):
	fields = line.strip().split(',')

	if line_count == 0:
		header = dict(zip(fields, range(len(fields))))

	line_count += 1

	if fields[header["ll_lang"]] == "ab":
		key = fields[header["ll_title"]]

		ll_from[key] = fields[header["ll_from"]]

header = {}
line_count = 0

for line in gzip.open("data/abwiki-20170420-stub-meta-current.csv.gz", "rt"):
	fields = line.strip().split(',')

	if line_count == 0:
		header = dict(zip(fields, range(len(fields))))

	line_count += 1

	title = fields[header["title"]]

	if title in ll_from:
		print("ace", ll_from[title], "ab", fields[header["page_id"]])