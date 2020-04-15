import urllib
import urllib.request
from bs4 import BeautifulSoup
import openpyxl

theurl = 'https://twitter.com/realDonaldTrump'
thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage,'html.parser')

wb = openpyxl.Workbook()
sheet = wb.active
i=1
for tweets in soup.findAll('div',{"class":"content"}):
    print(i)
    print(tweets.find('p').text)
    c1 = sheet.cell(row=i, column=1)
    i= i+1
    c1.value = tweets.find('p').text
    wb.save("C:\\Users\\Tong\\Desktop\\python\\DonaldTrumpRecentTweets.xlsx")



