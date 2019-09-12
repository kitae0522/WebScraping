import requests
import urllib.parse
import re
from bs4 import BeautifulSoup

while True:
    answer = input("가사를 알고 싶은 노래 이름을 입력해주세요 : ")
    url = urllib.parse.quote(answer)

    html = requests.get('https://search.naver.com/search.naver?query=' + url).text
    soup = BeautifulSoup(html, 'html.parser')

    song_name = str(soup.select('.api_title_area h3[class*=api_title]'))
    song_lyrics = str(soup.select('.lyrics_area span[class*=_text]'))

    cleaned_name = re.sub('(<([^>]+)>)', '', song_name, 0).strip()
    cleaned_lyrics = re.sub('(<([^>]+)>)', '\n', song_lyrics, 0).strip()

    print("노래 이름 : " + cleaned_name + "\n" +
          "노래 가사 : " + cleaned_lyrics + "\n" + "------------------------")
    continue
