from bs4 import BeautifulSoup
import requests

html = requests.get("https://punchng.com/").text

soup = BeautifulSoup(html, "html.parser")

just_in = soup.findAll("li", {"class": "new-item"})

# print(link)
# print(time)

def get_post_content(link):

    news_html = requests.get(link).text
    soup2 = BeautifulSoup(news_html, "html.parser")

    heading = soup2.find("article", class_="single-article").find("h1").string
    body = soup2.find("article", class_="single-article").find("div", class_="post-content").findAll("p")

    print(heading.strip())
    for p in body:
        print(p.text.strip().strip('NAN'))


for idx, news in enumerate(just_in):
    link = news.find("a")["href"]
    #print(link)
    time = news.find("div", class_="meta-time").find("span").string
    print("\nNEWS {}".format(idx))
    get_post_content(link)

#get_post_content("https://punchng.com/no-justification-for-suicide-psychiatrists-warn-nigerians/")


# https://punchng.com/no-justification-for-suicide-psychiatrists-warn-nigerians/
# https://punchng.com/family-discovers-decomposing-body-of-retired-benue-judge/
# https://punchng.com/reps-to-get-n54bn-for-constituency-projects/




