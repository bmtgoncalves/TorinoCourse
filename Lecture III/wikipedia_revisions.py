import sys
import gzip
from xml.parsers import expat

isContributor = False
isArticle = False
isPage = False
isData = False
buffer = u""
page_id = None
timestamp = None
revision_id = None
title = None

fields = set(["timestamp", "page", "id", "ns", "revision", "contributor", "title"])


def start_element(name, attrs):
    global buffer, isData, isPage, isContributor

    if name in fields:
        buffer = ""

        if name == "page":
            isPage = True
        elif name == "revision":
            isPage = False
        elif name == "contributor":
            isContributor = True
        else:
            isData = True
            buffer = ""

def end_element(name):
    global buffer, isData, isPage, isArticle, isContributor, timestamp, page_id, revision_id, title

    if name in fields:
        if name == "ns":
            if int(buffer) == 0:
                isArticle = True
            else:
                isArticle = False
        elif name == "timestamp":
            timestamp = buffer
        elif name == "id":
            if isPage:
                page_id = buffer
                isPage = False
            elif not isContributor:
                revision_id = buffer
        elif name == "revision":
            if isArticle:
                print(",".join([page_id, revision_id, timestamp, title]))
        elif name == "page":
            isArticle = False
        elif name == "contributor":
            isContributor = False
        elif name == "title":
            title = buffer

    buffer = u""
    isData = False

def char_data(data):
    global isData, buffer

    if isData:
        buffer += data

if __name__ == "__main__":
    p = expat.ParserCreate()

    p.StartElementHandler = start_element
    p.EndElementHandler = end_element
    p.CharacterDataHandler = char_data

    print(",".join(["page_id", "revision_id", "timestamp", "title"]))

    try:
        p.ParseFile(gzip.open(sys.argv[1]))
    except Exception as e:
        print(e, file=sys.stderr)
