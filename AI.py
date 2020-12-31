from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import os
import random

quotes_list = []
names_list = []
with open ("quotes/quotes.txt") as quotes :
    for quote in quotes :
        stripped_quote = quote.strip()
        quotes_list.append(stripped_quote)

dir_list = os.listdir("names-west/batches_copy/")
for txt in dir_list :
    if txt == '.DS_Store' :
        continue
    with open ("names-west/batches_copy/"+txt, "r") as names :
        for name in names :
            stripped_name = name.strip()
            names_list.append(stripped_name)

list_file = open ("1.txt","x")

for name in names_list :
    list_file.write(name+"\n")

driver = webdriver.Chrome(executable_path='/Users/aniket/Desktop/sele/chromedriver')
driver.implicitly_wait(30)
driver.get('https://www.instagram.com/')
sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input').send_keys('saveairrack9')  # username
driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').send_keys('mesohorny')  # password
driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div').click()  # login_button
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()  # NOT NOW BUTTION
driver.find_element_by_css_selector('button.aOOlW.HoLwm').click()
a = 0
b=1
for name in names_list :
    try :
        if a==0 :
            driver.find_element_by_css_selector('div.pbgfb.Di7vw').click()  # search
            driver.find_element_by_css_selector('input.XTCLo.x3qfX.focus-visible').send_keys(name)  # input
            driver.find_element_by_css_selector('div.z556c').click()  # click on ananya
            a = a + 1
        else:
            driver.find_element_by_css_selector('div.pbgfb.Di7vw').click()  # search
            driver.find_element_by_css_selector('input.XTCLo.x3qfX.focus-visible').send_keys(name)
            driver.find_element_by_css_selector('div.z556c').click()  # click on ananya
        sleep(2)
        driver.find_element_by_css_selector('button._5f5mN.jIbKX._6VtSN.yZn4P').click()  # FOLLOW
        driver.find_element_by_css_selector('button.sqdOP.L3NKy._4pI4F._8A5w5').click()  # MESSAGE
        driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').click()  # TEXT
        driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys('Hey! there is this youtuber duo named AIRRACK ( Eric and Mack ) who are currently stranded on an island until they hit 1 million subscribers. You can google it, its pretty interesting !  This referral link which will send you to the AIRRACK channel || subto.saveairrack.com/sagesy_46046643 || if this seems interesting maybe go subscribe to the channel *wink wink*'+quotes_list[random.randint(0,390)])  # TEXT
        driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()  # SEND TEXT BUTTON
    except :
        print(name + " is not public \n")
        continue
    os.remove(str(b)+".txt")
    b = b + 1
    list_file = open (str(b)+".txt","x")
    for name_ception in names_list :
        if name_ception != name :
            list_file.write(name_ception+"\n")


print("FINISHED")

# driver.find_element(By.__class__, "_8-yf5 ").click()
# driver.find_element_by_class_name("_8-yf5 ").click()
"""driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/a/svg').click()
sleep(2)

if driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').size()!=0 :
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[9]/a/div')"""

"""
menu = driver.find_element_by_xpath('//*[@id="main"]/header')
menu.click()

time.sleep(5)
media_gen = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[2]/div[1]/div/div/div[1]/span')
media_gen.click()

photo = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div[2]/span/div/div/div/div[1]/div[2]/div/div[2]/div/div')
photo.click()
previous = driver.find_element_by_xpath('//*[@id="app"]/div/span[3]/div/div/div[2]/div[2]/div[1]/div')
could_not_donwload = 1
while previous.get_attribute("aria-disabled")=='false':
    try :
        download = driver.find_element_by_xpath('//*[@id="app"]/div/span[3]/div/div/div[2]/div[1]/div[2]/div/div[4]/div')
        download.click()
    except NoSuchElementException:
        print("we had exception at "+ str(could_not_donwload))
        could_not_donwload=could_not_donwload+1
    if download.get_attribute('aria-disabled')=='true':
        a=0
        b=0
        while a==0:
            if download.get_attribute('aria-disabled')=='true' and b<120:
                time.sleep(1)
                b=b+1
            elif b==120 :
                print("ERROR could not download "+could_not_donwload+" from the first element")
                could_not_donwload=could_not_donwload+1
                a=1
            else :
                download.click()
                previous = driver.find_element_by_xpath('//*[@id="app"]/div/span[3]/div/div/div[2]/div[2]/div[1]/div')
                previous.click()
                a=1
    else :
        download.click()
        previous = driver.find_element_by_xpath('//*[@id="app"]/div/span[3]/div/div/div[2]/div[2]/div[1]/div')
        previous.click()
    previous = driver.find_element_by_xpath('//*[@id="app"]/div/span[3]/div/div/div[2]/div[2]/div[1]/div')
    previous.click()
    time.sleep(2)
    #previous = driver.find_element_by_xpath('//*[@id="app"]/div/span[3]/div/div/div[2]/div[2]/div[1]/div')

print('done')
"""

# MESSAGE - div.pbgfb.Di7vw  or div.eyXLr.wUAXj
# acc page - div.pbgfb.Di7vw  or div.eyXLr.wUAXj
