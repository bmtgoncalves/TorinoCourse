from pyquery import PyQuery as pq

url = "http://scholar.google.com/citations?hl=en&user=B7vSqZsAAAAJ&view_op=list_works&pagesize=100"

doc = pq(url=url)

table = doc("table#gsc_a_t")

for row in table("td.gsc_a_t").items():
    print(row("a").text())