from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome('chromedriver_linux64/chromedriver')
driver.get('https://www.google.com/') #orange coat fashion

box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys("orange coat fashion") # sửa tên ở đây 
box.send_keys(Keys.ENTER)

driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()


#Will keep scrolling down the webpage until it cannot scroll no more
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    try:
        driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input').click()
        driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
        time.sleep(2)
    except:
        pass
    if new_height == last_height:
        break
    last_height = new_height


i = 0
while True:
    try:
        img = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img')
        src = img.get_attribute('src') 
        urllib.request.urlretrieve(src, "image_person/"+str(i+2283)+".jpg")
        # driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot('images/'+str(i)+'.png')
    except:
        pass
    i = i + 1
    print(i)
    # if i == 10:
    #     break

driver.close()