import requests
from BeautifulSoup import BeautifulSoup

url = "http://scholar.google.com/citations?hl=en&user=B7vSqZsAAAAJ&view_op=list_works&pagesize=100"

request = requests.get(url)
soup = BeautifulSoup(request.text)

table = soup.find("table", attrs={"class" : "cit-table"})

for paper in table.findAll("td", attrs={"id": "col-title"}):
    print paper.a.string
