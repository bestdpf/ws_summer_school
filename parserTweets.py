import json
import nltk
from bs4 import BeautifulSoup

f_in = open('tweets.txt','r')
f_usr = open('tweet_processed.txt','w')

for line in f_in.readlines():
    js_data = json.loads(line)
    usr_id = js_data['id']
    html_data = BeautifulSoup(js_data['content'])
    raw_data = html_data.get_text()
    #print usr_id,raw_data
    f_usr.write('{0}\n{1}\n'.format(usr_id,raw_data.encode('utf-8')))

f_usr.close()
