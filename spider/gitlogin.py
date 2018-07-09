# -*-coding=utf-8-*-
import requests
from bs4 import BeautifulSoup  # standard library for parsing html page
from lxml import etree
# header for simulating the browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
}

# creare a session to hold all browser information
gitSession = requests.Session()

# get the auth token from github login page
soup = BeautifulSoup(gitSession.get('https://github.com/login',
                                    headers=headers).text,
                     'html.parser')
# find the element containing the auth_token by selector
auth_token = soup.find("input", {"name": "authenticity_token"}).attrs['value']
print('auth_token: {}'.format(auth_token))

# prepare the login data using the auth token we got
payload = {
    "commit": "Sign in",
    "authenticity_token": auth_token,
    "login": "@gmail.com",  # fill your username
    "password": ""  # fill your password
}

# send a post request to session page to login
# we will need the session as Github request enable cookie and the session can
# help us to keep the cookie for different requests
login = gitSession.post('https://github.com/session',
                        data=payload)

# find my repo names by css selector
repro_link = 'https://github.com/dashboard/ajax_repositories?button=&utf8=%E2%9C%93&repos_cursor=Nw%3D%3D'
headers = {'x-requested-with': 'XMLHttpRequest',
           'Host': 'github.com'}
repo_text = gitSession.get(repro_link, headers = headers).text
tree = etree.HTML(repo_text)
for i in tree.xpath('//li//span[2]/text()'):
    print(i)