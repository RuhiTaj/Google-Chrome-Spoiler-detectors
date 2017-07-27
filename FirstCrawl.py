from bs4 import BeautifulSoup
import requests
import json
import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter
import pickle

simplejson = json
url= 'http://tvtropes.org/pmwiki/pmwiki.php/Main/FilmSeries'
r=requests.get(url)
#data=json.loads(r.content)
data=r.content
soup=BeautifulSoup(data)
co=0
z= open("C:\Users\Hai\Desktop\spoiler1k.txt","w+")

spoilers=[]
f = open("data.p","wb")
for divs in soup.find_all("div", {"class","page-content"}):
	for lis in divs.find_all('li'):
		co=co+1
		for em in lis.find_all('em'):	
			#print "this is em list : "+str(em)
			try:
				url2=em.find('a')['href']
				r2=requests.get(url2)
				data2=r2.content
				soup2=BeautifulSoup(data2)
				for sentence in soup2.find_all('span',{'class':'spoiler'}):
					print sentence.get_text()
					word= sentence.get_text()
					z.write(word)
					spoilers.append(sentence.get_text())
			except:
				pass
			break
		if co==20:
				break
print spoilers
z.close
pickle.dump(spoilers,f)

f.close()
	

