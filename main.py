import selenium
import behave
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com.br")

#

vInput = driver.find_element_by_xpath("//*[@id=\"tsf\"]/div[2]/div[1]/div[1]/div/div[2]/input")
vInput.send_keys("Speed test by Ookla")
vInput.send_keys(Keys.ENTER)

vSpeedTest = driver.find_element_by_xpath("//*[@id=\"rso\"]/div[1]/div/div/div[1]/a/h3")
vSpeedTest.click()

#
vStartTest = driver.find_element_by_xpath("//*[@id=\"container\"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
vStartTest.click()

vTestResult = driver.find_element_by_xpath("//*[@id=\"container\"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]")



driver.quit