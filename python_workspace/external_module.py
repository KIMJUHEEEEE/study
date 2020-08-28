# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <h1>1.Hello External Module 수프 </h1>
# <h1>2.Hello External Module 수프 </h1>
# <p class="title"><b>The Dormouse's story</b></p>

# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>

# <p class="story">...</p>
# </body>
# </html>
# """

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html_doc, 'html.parser') #beautifulSoup 객체 생성

# print(soup.prettify())


# print(soup.find_all('h1'))
# print(soup.title)
# # <title>The Dormouse's story</title>

# print(soup.title.name)
# # u'title'

# print(soup.title.string)
# # u'The Dormouse's story'

# print(soup.title.parent.name)
# # u'head'

# soup.p
# # <p class="title"><b>The Dormouse's story</b></p>

# soup.p['class']
# # u'title'

# soup.a
# # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

# soup.find_all('a')
# # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# soup.find(id="link3")
# # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
from urllib import request
from bs4 import BeautifulSoup

target=request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")

soup=BeautifulSoup(target,"html.parser")

for location in soup.select("location"):
    print("도시:",location.select_one("city").string)
    print("날씨:",location.select_one("wf").string)
    print("최저기온:",location.select_one("tmn").string)
    print("최고기온:",location.select_one("tmx").string)
    print()