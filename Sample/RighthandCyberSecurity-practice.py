from selenium import webdriver

driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')

driver.get('https://cyberready.right-hand.ai/auth/signin-1')
driver.implicitly_wait(30)

logo = driver.find_element_by_xpath('//img[@src="/static/media/logo.e5050a14.svg"]')

logoImage = driver.find_element_by_xpath('//img[@src="/static/media/logo.e5050a14.svg"]').get_attribute('src')
print(logoImage)
logoImageTobe = "https://cyberready.right-hand.ai/static/media/logo.e5050a14.svg"
assert logoImage == logoImageTobe

logoClass = driver.find_element_by_xpath('//img[@src="/static/media/logo.e5050a14.svg"]').get_attribute('class')
logoClassTobe = "w-150 mb-5"
assert logoClass == logoClassTobe

email = "notfound"
print(email)
email = driver.find_element_by_name('email')
print(email)
assert email != "notfound"
#assert if email == "notfound"


y = driver.get

#Assert.assertEquals(true,)

print(driver.title)
print(driver.current_url)

disc = driver.find_element_by_class_name('text-darkest')
print(disc.text)


#x = driver.find_element_by_link_text('Terms & Privacy').get_attribute('href')
#print(x)


title = driver.title
assert title == "Welcome | Right-Hand Cybersecurity"

#driver.find_element_by_link_text("Enter Password").click()
#driver.find_element_by_xpath('//button[@class="min-wid-100 m-0 px-0 f-12 text-left btn btn-link"]').click()


#x = driver.find_element_by_link_text("Terms & Privacy")
#print (x)