from selenium import webdriver
from espeak import espeak
import time
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
deadline_elements = driver.find_elements_by_class_name('deadline-item')
deadline_counter = driver.find_elements_by_class_name('deadline-counter')
l1=len(deadline_elements)
l2=len(deadline_counter)
if(l1==1):
	espeak.synth('Vishaal, you have '+str(l1)+' deadline')
	time.sleep(4)
else:
	espeak.synth('Vishaal, you have '+str(l1)+' deadlines')
	time.sleep(4)
count = 0
for i in deadline_elements:
	#deadline = i.get_attribute('innerHTML')
	#rint (deadline)
	#espeak.synth(deadline)
	#time.sleep(5)
	count += 1

for j in range(count):
	i = deadline_counter[j]
	d= i.get_attribute('innerHTML')
	deadline=deadline_elements[j].get_attribute('innerHTML')
	print(deadline)
	print (d)
	espeak.synth(deadline)
	time.sleep(3)
	espeak.synth(d)
	time.sleep(5)
