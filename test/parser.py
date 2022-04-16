import requests
from bs4 import BeautifulSoup as bs
data="word_no=0&searchKeywordTo=3&spCodeList=&dialectRegionCodeList=&techTermList=&spCodeAll=-1&dialectRegionCodeAll=-1&techTermAll=-1&spCode=&dialectRegionCode=&techTerm=&fileType=&fileField=&fileUseType=&fileUseContent=&searchFlag=Y&searchBoxFlag=Y&pageSize=10&searchSpType=or&_searchWordKindCode_all=on&searchWordKindCode=0&_searchWordKindCode=on&_searchWordKindCode=on&_searchWordKindCode=on&_searchWordKindCode=on&searchWordKind_all=-1&_searchWordKind_all=on&searchWordKind=1&_searchWordKind=on&searchWordKind=2&_searchWordKind=on&searchWordKind=3&_searchWordKind=on&searchWordKind=0&_searchWordKind=on&searchSyllableStart=3&searchSyllableEnd=3&searchMultimediaCode_all=-1&_searchMultimediaCode_all=on&searchMultimediaCode=N&_searchMultimediaCode=on&searchMultimediaCode=P&_searchMultimediaCode=on&searchMultimediaCode=I&_searchMultimediaCode=on&searchMultimediaCode=V&_searchMultimediaCode=on&searchMultimediaCode=A&_searchMultimediaCode=on&searchMultimediaCode=S&_searchMultimediaCode=on&searchUpdatedStartDate=&searchUpdatedEndDate=&searchType=1&searchOp=AND&searchTargets=WORD&searchTargetsOrgLanguage=-1&searchConditions=start&searchKeywords=%EC%9D%B4&syllablePosition=F&syllableFirst1=&syllableFirst2=&syllableFirst3=&syllableSecond1=&syllableSecond2=&syllableSecond3=&syllableThird1=&syllableThird2=&syllableThird3=&syllableFourth1=&syllableFourth2=&syllableFourth3=&pageUnit=10&pageIndex=1"
page = requests.post("https://stdict.korean.go.kr/search/searchDetailWords.do", data=data, verify=False)
soup = bs(page.text, "html.parser")

elements = soup.select('#content > ul')

for index, element in enumerate(elements, 1):
		print("{} 번째 게시글의 제목: {}".format(index, element.text))