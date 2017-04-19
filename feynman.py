import requests
from bs4 import BeautifulSoup

url = "http://scholar.google.com/citations?hl=en&user=B7vSqZsAAAAJ&view_op=list_works&pagesize=100"

request = requests.get(url)
soup = BeautifulSoup(request.text, 'lxml')

table = soup.find("table", attrs={"id" : "gsc_a_t"})

for paper in table.findAll("td", attrs={"class": "gsc_a_t"}):
    print(paper.a.string)
