# XueBa-tools-project


## What is it?
We built a **web crawler** to get the information on IMDB.com. 
Movies take an important role of our daily life and there are more and more good movies nowadays. However, it is too hard to find the information you want efficiently from such a large amount of data. 
Web Crawler is a very flexible way to get data. We can basically crawl all the webpages we can see on the web and crawl the data we need in the format we want. After we get all these data, we can use these information to do further analysis and research such as customers’ behaviors.

**Xueba web crawler** is a tool to find data from all the feature films on **IMDB.com**, which is sorted by popularity ascending. It aims to catrgorize top 500 feature films into different film genres. We are using practical, **real world** data analysis in Python. Additionally, it has the broader goal to graphically display the rating, frenquency and scores of the top 500 outstanding movies. It is already well on its way towards this goal and we want to develop and add more functions of this tool accourding to practical needs. 


## Who contribute it?
Group Members: Qinming Hu(qh2197);
               Shuning Liu(sl4439);
               Xinyi Zhou(xz2771);
               Yijian Pang(yp2496).
               

## Before we run, what should we have?

**Installation instructions**

To use this tools, we need import several packages:
1. Use HTTP library,
```shell
$ python
```
```python
>>> import requests 
>>>
```
2. Fine data from library,
```python
>>> from bs4 import BeautifulSoup
```
3. Display data graphically,
```python
>>> pip install pyecharts
>>> from pyecharts import Page, Pie, Bar
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
```
4. Data Analytics,
```python
>>> import numpy as np
>>> import pandas as pd
```
5. Regular Expression,
```python
>>> import re
```

## How to play this tool?

**Run instructions**
Under ‘Getting Data’ section, users need to enter a number between 0 to 8048, which will decide how many urls to crawl and use these data to do further analysis. 
The total number of movies is 402450 and each url lists 50 movies, so users can crawl up to 8048 urls. 

