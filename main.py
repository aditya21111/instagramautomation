from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.chrome.options import Options
import os

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--remote-debugging-port=9222')
driver = webdriver.Chrome(executable_path=r"chromedriver.exe",options=options)
driver.get("https://www.instagram.com/")
time.sleep(5)

def login(username,password):
    user_enter=driver.find_element_by_xpath("//input[@name=\"username\"]")
    pass_enter=driver.find_element_by_xpath("//input[@name=\"password\"]")
    user_enter.send_keys(username)
    pass_enter.send_keys(password)
    login_btn=driver.find_element_by_css_selector('.sqdOP.L3NKy.y3zKF')
    login_btn.click()

def like_spam(account):
    searchbox=driver.find_element_by_class_name('XTCLo')
    searchbox.send_keys(account)
    time.sleep(6)
    acc=driver.find_elements_by_class_name('-qQT3')[0]
    acc.click()
    time.sleep(6)
    total_posts=driver.find_elements_by_class_name('g47SY')[0].text
    print(total_posts)
    first_post=driver.find_elements_by_css_selector('.Nnq7C.weEfm')[0]
    first_post.click()
    time.sleep(5)
    
    for i in range(0,int(total_posts)):
        time.sleep(2)
        like_btn_box=driver.find_element_by_xpath("//article[1]//div[3]//section[1]//span[1]//button[1]")
        time.sleep(1)
        like_btn_box.click()
        nxt_btn=driver.find_element_by_link_text('Next')
        time.sleep(3)
        print(nxt_btn) 
        nxt_btn.click()

def following(username):
    time.sleep(5)
    driver.find_element_by_css_selector('._2dbep.qNELH').click()
    time.sleep(2)
    driver.find_element_by_css_selector('._7UhW9.xLCgt.MMzan.KV-D4.fDxYl').click()
    time.sleep(5)
    following_link=driver.find_elements_by_tag_name('a')[2]
    following_link.click()
    time.sleep(6)
    following_box=driver.find_elements_by_class_name('PZuss')   
    for elements in following_box:
        following_link=elements.find_elements_by_tag_name('a')
        # print(list(follower_link))
    following_list=[]    
    for following in following_link:
        following_name=following.text
        if following_name!="":
            following_list.append(following_name)
    driver.find_elements_by_class_name('wpO6b   ')[1].click()
    return following_list

def followers(username):    
    time.sleep(5)
    #reason (try block) - sometimes we may not at the homepage 
    try:
        driver.find_element_by_css_selector('._2dbep.qNELH').click()
        time.sleep(5)
        driver.find_element_by_css_selector('._7UhW9.xLCgt.MMzan.KV-D4.fDxYl').click()    
    except Exception as e:
        print(e)
    time.sleep(5)
    followers_link=driver.find_elements_by_tag_name('a')[1]
    followers_link.click()
    time.sleep(5)
    folow_box=driver.find_elements_by_class_name('PZuss')
    time.sleep(5)
    for elements in folow_box:
        follower_link=elements.find_elements_by_tag_name('a')
    time.sleep(5)
    followers_list=[]
    for followers in follower_link:
        followers_name=followers.text
        if followers_name!="":

            followers_list.append(followers_name)
            now = datetime.now()
            dt_string = now.strftime("%d%m%Y%H%M%S")
            f = open('{}{}.txt'.format(username,dt_string),'a')
            f.write(f'{followers_name}\n')
            f.close()
    driver.find_elements_by_class_name('wpO6b')[1].click()
        
    return followers_list

def not_follow(following_name,followers_name):
    whonotfollow = []
    l1=following_name
    l2=followers_name
    for ele in l1:
        if not ele in l2:
            whonotfollow.append(ele)
    for stupid_people in whonotfollow:
        now = datetime.now()
        dt_string = now.strftime("%d%m%Y%H%M%S")
        f = open('nofollowers{}{}.txt'.format(username,dt_string),'a')
        f.write(f'{stupid_people}\n')
        f.close()
    print(whonotfollow) 

    



username=input('Enter your username :')
password=input('Enter password :')
choice=input('Enter the number according to choice :\n 0- Spam the account\n 1 - Find who not follows you 😡 \n 2 - get follower list\n 3-get following list\n   ')

if choice=="2":
    login(username,password)
    followers(username)
    driver.quit()

if choice=="3":
    login(username,password)
    following(username)
    driver.quit()

if choice=="1":
    login(username,password)
    time.sleep(2)
    following_name=following(username)
    time.sleep(2)
    print(following_name)
    followers_name=followers(username)
    time.sleep(2)
    not_follow(following_name,followers_name)
    driver.quit()

if choice=='0':
    account=input("Enter the name of user 😁\n")
    login(username,password)
    time.sleep(5)
    like_spam(account)
    driver.quit()