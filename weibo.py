import requests
from pyquery import PyQuery as pq
import os
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time


path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver'
option=ChromeOptions()
option.set_headless()
option.add_experimental_option('excludeSwitches',['enable-automation'])
browser=webdriver.Chrome(executable_path=path,options=option)

url='https://weibo.com/zhudeyongblog?topnav=1&wvr=6&topsug=1'
headers={
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
        }
def search(data):
    print('please input search element:')
    data=str(input())
browser.get(url)
time.sleep(10)
browser.implicitly_wait(10)


for i in range(1):
    js="var q=document.documentElement.scrollTop=100000"  
    browser.execute_script(js)  
    time.sleep(3)

aaa=browser.find_elements_by_css_selector('div.WB_cardwrap.WB_feed_type.S_bg2.WB_feed_like')
dic={
    'author':'1',
    'time':'1',
    'detail':'1',
    'media':'1',
    'share':'1',
    'comment':'1',
    'thumb':'1'
    }
ls=[]
tempurl=[]
def getone(item):
    bbb=item.find_elements_by_css_selector('em')
    
    dic['share']=bbb[4].text
    dic['comment']=bbb[7].text
    dic['thumb']=bbb[10].text
   
    
    dic['author']=item.find_element_by_css_selector('a.W_f14.W_fb.S_txt1').text
    dic['time']=item.find_element_by_css_selector('a.S_txt2').text
    dic['detail']=item.find_element_by_css_selector('div.WB_text.W_f14').text
    
    img=item.find_elements_by_css_selector('img')
    del img[0]
    for item in img:
        tempurl.append(item.get_attribute('src'))
    
    dic['media']=tempurl
    print(len(img)+'aaaaaaa222222222222222222222222\n\n')
   
def main():
    aaa=browser.find_elements_by_css_selector('div.WB_cardwrap.WB_feed_type.S_bg2.WB_feed_like')
    
    for item in aaa:
        getone(item)
        print(dic)
        print('\n')
    tempurl.clear()
    print(tempurl+'aaaaaaaaaaaaaaaaaaaaaaaa22222222222\n\n')
main()
browser.close()
