from requests import get
from bs4 import BeautifulSoup as bs
import re
import os


url_season = "https://genius.com/albums/How-i-met-your-mother/Season-1"
response_season = get(url_season)

url_whole = "https://genius.com/artists/How-i-met-your-mother"
response_whole = get(url_whole)

#Try to get the whole show urls now
soup_whole = bs(response_whole.text,"html.parser")
url_whole = soup_whole.find_all('div', class_ = "modal_window-content modal_window-content--narrow_width modal_window-content--white_background")
lnk = str(soup_whole).strip(",")
links = [i for i in lnk if "href" in i]
#links[7] contains the urls
#https://genius.com/albums/How-i-met-your-mother/Season-(number)
#except for S08 for some reason
whole_links = ["https://genius.com/albums/How-i-met-your-mother/Season-{}".format(i) for i in range(1, 9)]

soup_season = bs(response_season.text, 'html.parser')
link_season = soup_season.find_all('div', class_ = 'column_layout-column_span column_layout-column_span--primary')
#len(ly_season = 47) from 3, every other item
ep_content = []
for x in link_season: 
    ep_content.append(x)
#something[3] is the pilot stuff, look at 
ep_content = str(ep_content[1]).split("\n")
link_location = [i for i in ep_content if "href" in i]

# All season 1 links
season_one = []
for class_ in link_location:
     season_one.append(re.search(r"(?<=href=\").*?(?=\">)", class_).group(0))

#[0] #all episodes here

barney_lines = []
for url in season_one:
    response = get(url)

    html_soup = bs(response.text, 'html.parser')
    # maybe .text
    lyrics_cont = html_soup.find_all('div', class_ = 'song_body-lyrics')
    lyrics = str(lyrics_cont[0]).split("\n")
    barney_lines.append([x for x in lyrics if "Barney:" in x])

html_items = r"<.*>"
click_item = r"ng-click.*\)\""
rando = r"pending.*\">"

clean = re.compile(r"{}|{}|{}".format(html_items, click_item, rando))

for i, line in enumerate(barney_lines):
    #barney_lines[i] = re.sub(clean, '', line)
    print(barney_lines[i])
print(len(barney_lines))




#lyrics 
print(type(lyrics_cont))
print(len(lyrics_cont))