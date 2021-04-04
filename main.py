from selenium import webdriver
from selenium.webdriver.common.keys import keys
from time import sleep

driver = webdriver.Chrome(executable_path="Path to the chrome driver executable")
driver.gey("twitter website")

sleep(3)

driver.find_element_by_name('session[username_or_email]').send_keys('Your twitter username')
driver.find_element_by_name('session[password]').send_keys('Your twitter password')
driver.find_element_by_name('session[password]').send_keys(Keys.RETURN)
sleep(3)

l = open("The text file ")

for word in l:
    if word == "\n":
        continue
    driver.find_element_by_xpath("//a[@data-testid='SideNav_NewTweet_Button']").click()
    sleep(1)
    driver.find_element_by_class_name("notranslate").click()
    driver.find_element_by_class_name("notranslate").send_keys(word)
    driver.find_element_by_xpath("//div[@data-testid='tweetButton']").click()
    sleep(5)
