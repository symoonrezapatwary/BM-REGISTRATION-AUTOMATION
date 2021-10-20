from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.breakingmars.com/registration')
# f ='David'
# l = 'malan'
# e = 'davidmalan@gmail.com'
# p = '123456'
# create_account = driver.find_element_by_xpath('//*[@id="__next"]/main/div/div/div/div[1]/div/div[2]/div/div[3]/div[2]/span')
# create_account.click()
time.sleep(3)
def regi(f, l, e, p):
    first_name = driver.find_element_by_xpath('//*[@id="basic"]/div/div/div/div[1]/div[1]/div/div/div[1]/div/input')
    #first_name.send_keys("")
    first_name.send_keys(f)
    last_name = driver.find_element_by_xpath('//*[@id="basic"]/div/div/div/div[1]/div[2]/div/div/div[1]/div/input')

    last_name.send_keys(l)
    email = driver.find_element_by_xpath('//*[@id="basic"]/div/div/div/div[2]/div/div/div[1]/div/input')
    #email.send_keys("")
    email.send_keys(e)
    password =driver.find_element_by_xpath('//*[@id="basic"]/div/div/div/div[3]/div/div/div[1]/div/span/input')
    password.send_keys(p)
    checkbox = driver.find_element_by_xpath('//*[@id="basic"]/div/div/div/div[4]/div[1]/label/span/input')
    checkbox.click()
    start_button = driver.find_element_by_xpath('//*[@id="basic"]/div/div/div/div[5]/button')
    start_button.click()
    time.sleep(5)
    count = driver.find_element_by_xpath('//*[@id="__next"]/main/div/div/div/div[1]/div/div[2]/div/div[2]')
    countText = count.text
    if countText:
        print(countText)
        time.sleep(3)

        reloadRegPage()
        drive('Symoon', 'malan', 'test46@gmail.com', '1234567')
        time.sleep(2)
    companyName = driver.find_element_by_xpath('//*[@id="basic"]/div[2]/div/div/div[1]/div/input')
    companyName.send_keys('6sense')
    time.sleep(2)
    elementsdrp =driver.find_element_by_xpath('//*[@id="basic"]/div[3]/div/div/div[1]/div/div/div/span[2]')
    elementsdrp.click()
    time.sleep(5)
    option_sel = driver.find_element_by_name('5-20 people')
    option_sel.click()
    time.sleep()


    #slectinon_of_value = drp.select_by_visible_text('5-20 people')




def drive(fName, lName, email, password):
    regi(fName, lName, email, password)
def reloadRegPage():
    driver.get('https://www.breakingmars.com/registration')
drive('David','malan','test36@gmail.com','123456')
