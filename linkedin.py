from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome("chromedriver.exe")

browser.get("https://www.linkedin.com/")

browser.fullscreen_window()
time.sleep(5)

login = browser.find_element_by_xpath("/html/body/nav/a[3]")
login.click()
time.sleep(5)

email = browser.find_element_by_xpath("//*[@id='username']")
password = browser.find_element_by_xpath("//*[@id='password']")

email.send_keys("***@hotmail.com")
password.send_keys("***")

login_button = browser.find_element_by_css_selector("#app__container > main > div:nth-child(2) > form > div.login__form_action_container > button")
login_button.click()

time.sleep(5)

search_bar = browser.find_element_by_xpath("//*[@id='ember29']/input")
search_bar.send_keys("#python")
search_bar.send_keys(Keys.RETURN)
time.sleep(10)

contacts = browser.find_element_by_xpath("//*[@id='mynetwork-tab-icon']")
contacts.click()
time.sleep(5)

contact_button = browser.find_element_by_class_name("mn-community-summary__entity-info")
contact_button.click()
time.sleep(5)
#aşşagı kaydırma
for i in range(1,3):
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)

followers = browser.find_elements_by_class_name("mn-connection-card__details")
fallowerList=[]

for follower in followers:
    fallowerList.append(follower.text)

with open ("jobdetail.txt","w",encoding = "UTF-8") as file:
    for follower in fallowerList:
        file.write(follower + "/n")
time.sleep(5)



#mail işlemleri

user = 'i*****@gmail.com'
app_password = '*****'
to = '***2@hotmail.com'

subject = '****'


content = ['','','jobdetail.txt']

with yagmail.SMTP(user, app_password) as yag:
    yag.send(to, subject, content)
    print('Sent email successfully')

browser.quit()
















