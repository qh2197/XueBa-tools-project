
# coding: utf-8

# 


import requests 
from bs4 import BeautifulSoup 

def start_requests(url):
    r = requests.get(url)
    return r.content

movie_Dict = {'Movies Name':[],'Release Year':[], 'Genre':[]}

def parse(text):
    soup = BeautifulSoup(text, 'html.parser')
    movie_list = soup.find_all('div', class_ = 'lister-item-content') # 'div class' list all info. of each movie
    for movie in movie_list:
        movies_Name = movie.find_all('a')[0].text
        movies_ReleaseYear = movie.find_all('span')[1].text
        movies_Genre = movie.find_all('span', class_ = 'genre')[0].text.strip()
        movie_Dict['Movies Name'].append(movies_Name)
        movie_Dict['Release Year'].append(movies_ReleaseYear)
        movie_Dict['Genre'].append(movies_Genre)
    return print(movie_Dict)

def main():
    for i in range(1):
        x = 1 + i * 50
        url = f'https://www.imdb.com/search/title?title_type=feature&start={x}&ref_=adv_nxt'
        text = start_requests(url)
        parse(text)

if __name__ == '__main__':
    main()

    
