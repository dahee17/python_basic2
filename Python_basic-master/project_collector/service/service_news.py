import requests
from bs4 import BeautifulSoup
from db.news_dao import add_news


# URL -> 기사(제목, 본문, 날짜) 수집
def get_news(url : str):  # str : 힌트 url이 string type 이다.
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    reg_date = doc.select("span.num_date")[0].get_text()
    print(f"날짜 : {reg_date}")

    title = doc.select("h3.tit_view")[0].get_text()
    print(f"제목: {title}")

    content_list = doc.select("div.article_view p")
    content = ""
    for p in content_list:
        content += p.get_text()
    print(f"본문: {content}")

    data = {
        "title": title,
        "content": content,
        "date": reg_date
    }
    add_news(data)

