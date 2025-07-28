import requests
import re


def domen_extract(string):
    if not len(string):
        return None
    if "//" in string:
        search = re.search(r".*?//(.*)", string)
        if search:
            string = search.group(1)
    if "/" in string:
        search = re.search(r"(.*?)/", string)
        if search:
            string = search.group(1)
    return string


lst = []
content = requests.get(input()).text
lst.extend(
    map(lambda x: x[1], re.findall(r"<a.*?href=[\"'](.*?://)?(\w.*?)[\"'/:]", content))
)
lst = sorted(list(set(map(domen_extract, lst))))
for url in lst:
    if url != "":
        print(url)
