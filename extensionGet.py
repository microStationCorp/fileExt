from bs4 import BeautifulSoup
import requests
import os


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
                # text = '.' + span.text.lower()
                if span.text.find(' ') == -1:
                    text = '.' + span.text.lower()
                    extList.add(text)
                else:
                    minilist = span.text.split(' ')
                    for i in minilist:
                        if i.endswith(','):
                            i = i[:-1]
                        elif i.endswith('..') or i == '':
                            continue
                        text = '.' + i
                        extList.add(text)

    return list(extList)


urlsym = 'https://en.wikipedia.org/wiki/List_of_filename_extensions'
urlae = "https://en.wikipedia.org/wiki/List_of_filename_extensions_(A%E2%80%93E)"
urlfl = "https://en.wikipedia.org/wiki/List_of_filename_extensions_(F%E2%80%93L)"
urlmr = "https://en.wikipedia.org/wiki/List_of_filename_extensions_(M%E2%80%93R)"
urlsz = "https://en.wikipedia.org/wiki/List_of_filename_extensions_(S%E2%80%93Z)"
ext = getExtList(urlsym, urlae, urlfl, urlmr, urlsz)
ext.sort()
print(len(ext))
try:
    file = open('extension.txt', 'x')
except:
    os.remove('extension.txt')

with open('extension.txt', 'a') as file:
    for i in ext:
        file.write(f'{i}\n')

file.close()