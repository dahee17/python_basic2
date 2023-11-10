# Daum News Collector ver 1.0
# - 작성일자 : 2023년 11월 08dlf
# - 작성자 :
# - 내용: 사용자가 수집하고 싶은 뉴스 카테고릴를 설정하면 해당 카테고리로 이동
# - 라이브러리 : requests, beautifulsoup4, pynmogo

# 프로세스
# 1) 사용자로부터 뉴스 카테고리를 입력
# 2) 해당 카테고리의 실시간 다음뉴스를 수집(제목, 본문)
# 3) 수집 한 기사를 데이터베이스(MongoDB)

import requests  # 전체 소스코드
from bs4 import BeautifulSoup  # 원하는 정보 SELECT
from service.service_news import get_news

count = 0  # 전체 기사수
page = 1   # 시작 페이지 1로 고정

print("=" * 150)
print("MSG : 수집하고 싶은 뉴스 카테고리를 입력해주세요.")
print("= 뉴스 카테고리 목록")
print("= 1. 사회")
print("= 2. 정치")
print("= 3. 경제")
print("= 4. 국제")
print("= 5. 문화")
print("= 6. 연예")
print("= 7. 스포츠")
print("= 8. IT")

dict_news = {
    "사회" : "society",
    "정치" : "politics",
    "경제" : "economic",
    "국제" : "foreign",
    "문화" : "culture",
    "연예" : "entertain",
    "스포츠" : "sports",
    "IT" : "digital"
}
while True:
    category = input("> 카테고리: ")
    if category in list(dict_news.keys()) :
        break
    else :
        print("= MSG : 올바른 카테고리를 입력해주세요.")




# print(f"replace : {dict_news[category]}")

while True :
    url = f"https://news.daum.net/breakingnews/{dict_news[category]}?page={page}"
    result = requests.get(url)

    if result.status_code == 200 :
        print(result, "접속 성공 -> 접속데이터를 수집합니다.")  # 200 성공

        doc = BeautifulSoup(result.text, "html.parser")
        url_list = doc.select("ul.list_news2 a.link_txt")

        if len(url_list) == 0:
            break

        for url in url_list:
            print(f"{count+1}", "=" * 100)
            # get_news() : 기사 제목, 본문, 날짜 수집
            get_news(url["href"])
            count += 1
    else :
        print("URL 경로가 잘못됐습니다. 확인부탁드립니다.")
    print(result)  # 200(성공)

    page += 1