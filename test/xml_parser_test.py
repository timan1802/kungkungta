from bs4 import BeautifulSoup
import os

fp = open("../dict_xml/951730_5000.xml", "r",  encoding='UTF8')
soup = BeautifulSoup(fp, "lxml")

# findAll로 해당되는 TAG를 검색
for songElement in soup.findAll('item'):
    # 해당 TAG안의 Attribute(속성) 값을 가져올때는 아래와 같이 사용
    print(songElement['word_info'])

    # Tag 아래에 있는 다른 Tag를 가져올경우 아래와 같이 사용
    print(songElement.title.string, songElement.length.string)