from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import keyboard



driver = webdriver.Chrome()
driver.get('https://moltke.nccu.edu.tw/SSO/startApplication?name=inccustucmt')

id_box = driver.find_element_by_name('captcha$Login1$UserName')
id_box.send_keys('')
pass_box = driver.find_element_by_name('captcha$Login1$Password')
pass_box.send_keys('')

login_button = driver.find_element_by_id('captcha_Login1_LoginButton')
login_button.click()


main = WebDriverWait(driver, 10).until(lambda d: d.find_elements_by_tag_name('frame[id^="mainFrame"]'))
driver.switch_to.frame(main[0])
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "btnclose"))).click()


count = 0
print("Calculating Number of Courses...")
while count == 0:
    x = BeautifulSoup(driver.page_source, 'lxml')
    count=len(x.select('.container > div[class="row"] > div:nth-of-type(3) > h4'))
    print("Number of Courses: " + str(count))

for i in range(6,6):
    y = str(95+90*i)
    for t in range(2):
        time.sleep(2)
        driver.execute_script('window.scrollTo(0,'+ y +')')
        try:
            WebDriverWait(driver, 10).until(lambda d: d.find_element_by_xpath('//*[contains(concat(" ", @class, " "), "container")]/div[' +str(i+2)+ ']/div[5]/div[1]/a['+str(t+1)+']')).click()
        except:
            continue
        if t == 0:
            print("Filling Course Number " + str(i+1))
            driver.switch_to.default_content()
            driver.switch_to.frame(WebDriverWait(driver, 10).until(lambda d: d.find_elements_by_tag_name('frame')[3]))
        
            client = WebDriverWait(driver, 10).until(lambda d: d.find_elements_by_css_selector('input[value="2"]'))
            for button in client:
                try:
                    button.click()
                except:
                    print('Already Clicked')
                    pass

            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='agree']"))))
            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#save"))))
            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='#']"))))
        elif t == 1:
            print("Filling Core Shit Number " + str(i+1))
            driver.switch_to.default_content()
            driver.switch_to.frame(WebDriverWait(driver, 10).until(lambda d: d.find_elements_by_css_selector('frame')[3]))
            driver.switch_to.frame(WebDriverWait(driver, 10).until(lambda d: d.find_element_by_css_selector('iframe')))
            second = WebDriverWait(driver, 10).until(lambda d: d.find_elements_by_css_selector('option[value="3"]'))
            for x in second:
                x.click()
            WebDriverWait(driver, 10).until(lambda d: d.find_element_by_css_selector('input[type="submit"]')).click()
            driver.switch_to.parent_frame()
            WebDriverWait(driver, 10).until(lambda d: d.find_element_by_css_selector('#backurl')).click()

#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "btnclose"))).click()


time.sleep(10)
#element = driver.find_element_by_xpath("")
#driver.execute_script("arguments[0].click();", element)

#actions = ActionChains(driver)
#actions.click(elem).perform()

#bb = driver.find_element_by_id("btnclose")
#bb.click()


#driver.find_element_by_css_selector("a[href*='#'").click()

#driver.find_element_by_partial_link_text('教師').click()


