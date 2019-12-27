from bs4 import BeautifulSoup
import requests


def getExtList(*url):
    extList = set()
    for i in url:
        res = requests.get(i)
        htmlContent = res.content
        soup = BeautifulSoup(htmlContent, 'html.parser')
        tableList = soup.find_all('table', class_='wikitable')
        for table in tableList:
            spanList = table.find_all('span')
            for span in spanList:
                text = '.' + span.text.lower()
                extList.add(text)

    return list(extList)

urlsym='https://en.wikipedia.org/wiki/List_of_filename_extensions'
urlae = "https://en.wikipedia.org/wiki/List_of_filename_extensions_(A%E2%80%93E)"
urlfl = "https://en.wikipedia.org/wiki/List_of_filename_extensions_(F%E2%80%93L)"
urlmr = "https://en.wikipedia.org/wiki/List_of_filename_extensions_(M%E2%80%93R)"
urlsz = "https://en.wikipedia.org/wiki/List_of_filename_extensions_(S%E2%80%93Z)"
ext=getExtList(urlsym, urlae, urlfl, urlmr, urlsz)
ext.sort()
print(type(ext),len(ext))
