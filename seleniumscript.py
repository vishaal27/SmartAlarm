from selenium import webdriver
driver=webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("https://www.usebackpack.com/")
driver.maximize_window()
#driver.implicitly_wait(5)
driver.find_element_by_id("loginButton").click()
username=driver.find_element_by_id("user_email")
username.send_keys("vishaal16119@iiitd.ac.in")
password=driver.find_element_by_id("user_password")
password.send_keys("")
username.submit()


