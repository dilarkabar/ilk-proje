import requests as rqst
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
pages = np.arange(1,51)
for page in pages:
    url="https://www.kitapsec.com/Products/Edebiyat/Cok-Satan-Kitaplar/1-6-0a0-0-0-0-0-0.xhtml"+str(page)+".html"
    a=rqst.get(url)
    soup = bs(a.content,"html.parser")
print(soup.prettify())
pages = np.arange(1,51)
kitap_adı=[]
for i in soup.find_all("a",{'class':"text"}):
    for y in i.find_all("span",{"itemprop":"name"}):
        kitap_adı.append(y.text)
print(kitap_adı)

fiyatpiyasa=[]
for t in soup.find_all("span",{"class":"fiyat"}):
    for f in t.find_all("font",{"class":"piyasa"}):
        fiyatpiyasa.append(f.text)
print(fiyatpiyasa)

fiyatsatiş=[]
for t in soup.find_all("span",{"class":"fiyat"}):
    for f in t.find_all("font",{"class":"satis"}):
        fiyatsatiş.append(f.text)
print(fiyatsatiş)

yayınevi=[]
for j in soup.find_all("div",{"itemprop":"publisher"}):
    for s in j.find_all("a"):
        yayınevi.append(s.text)
print(yayınevi)

link = []
for ğ in soup.find_all("div", {"class": "Ks_UrunSatir", "itemtype": "http://schema.org/Book"}):
    for w in ğ.find_all('a', {"class": "text", "itemprop": "url"}):
        link.append(w["href"])
print(link)

ata = {'Kitap_Adı':kitap_adı,'Piyasa_fiyatı':fiyatpiyasa,'Satış_Fiyatı':fiyatsatiş,"Link":link}

book_data = pd.DataFrame(ata)
book_data.to_excel("kitapsec.xlsx",index=False)