from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from datetime import date
import requests
import time
import re
import pandas as pd
import csv

driver = webdriver.Chrome(r'C:\Users\zonkb\Desktop\airbnb\chromedriver.exe')

# driver = webdriver.Chrome(executable_path='C:\Users\zonkb\Desktop\airbnb\chromedriver.exe')
driver.implicitly_wait(5)

urls = ["https://www.airbnb.com/s/United-States/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJCzYy5IS16lQRQrfeQ5K5Oxw&query=United%20States&click_referer=t%3ASEE_ALL%7Csid%3Abbc20157-93f5-4a50-abb8-5c8b5d8f6be3%7Cst%3ALANDING_PAGE_HOMES&title_type=LANDING_PAGE_HOMES&allow_override%5B%5D=&s_tag=-i1FRqbo&section_offset=0",
"https://www.airbnb.com/s/United-States/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJCzYy5IS16lQRQrfeQ5K5Oxw&query=United%20States&click_referer=t%3ASEE_ALL%7Csid%3Abbc20157-93f5-4a50-abb8-5c8b5d8f6be3%7Cst%3ALANDING_PAGE_HOMES&title_type=LANDING_PAGE_HOMES&allow_override%5B%5D=&s_tag=-i1FRqbo&section_offset=1",
"https://www.airbnb.com/s/United-States/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJCzYy5IS16lQRQrfeQ5K5Oxw&query=United%20States&click_referer=t%3ASEE_ALL%7Csid%3Abbc20157-93f5-4a50-abb8-5c8b5d8f6be3%7Cst%3ALANDING_PAGE_HOMES&title_type=LANDING_PAGE_HOMES&allow_override%5B%5D=&s_tag=-i1FRqbo&section_offset=2",
"https://www.airbnb.com/s/United-States/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJCzYy5IS16lQRQrfeQ5K5Oxw&query=United%20States&click_referer=t%3ASEE_ALL%7Csid%3Abbc20157-93f5-4a50-abb8-5c8b5d8f6be3%7Cst%3ALANDING_PAGE_HOMES&title_type=LANDING_PAGE_HOMES&allow_override%5B%5D=&s_tag=-i1FRqbo&section_offset=3",
"https://www.airbnb.com/s/United-States/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJCzYy5IS16lQRQrfeQ5K5Oxw&query=United%20States&click_referer=t%3ASEE_ALL%7Csid%3Abbc20157-93f5-4a50-abb8-5c8b5d8f6be3%7Cst%3ALANDING_PAGE_HOMES&title_type=LANDING_PAGE_HOMES&allow_override%5B%5D=&s_tag=-i1FRqbo&section_offset=4",
"https://www.airbnb.com/s/United-States/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJCzYy5IS16lQRQrfeQ5K5Oxw&query=United%20States&click_referer=t%3ASEE_ALL%7Csid%3Abbc20157-93f5-4a50-abb8-5c8b5d8f6be3%7Cst%3ALANDING_PAGE_HOMES&title_type=LANDING_PAGE_HOMES&allow_override%5B%5D=&s_tag=-i1FRqbo&section_offset=5",
"https://www.airbnb.com/s/United-States/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJCzYy5IS16lQRQrfeQ5K5Oxw&query=United%20States&click_referer=t%3ASEE_ALL%7Csid%3Abbc20157-93f5-4a50-abb8-5c8b5d8f6be3%7Cst%3ALANDING_PAGE_HOMES&title_type=LANDING_PAGE_HOMES&allow_override%5B%5D=&s_tag=-i1FRqbo&section_offset=6",
"https://www.airbnb.com/s/United-States/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJCzYy5IS16lQRQrfeQ5K5Oxw&query=United%20States&click_referer=t%3ASEE_ALL%7Csid%3Abbc20157-93f5-4a50-abb8-5c8b5d8f6be3%7Cst%3ALANDING_PAGE_HOMES&title_type=LANDING_PAGE_HOMES&allow_override%5B%5D=&s_tag=-i1FRqbo&section_offset=7",
"https://www.airbnb.com/s/United-States/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJCzYy5IS16lQRQrfeQ5K5Oxw&query=United%20States&click_referer=t%3ASEE_ALL%7Csid%3Abbc20157-93f5-4a50-abb8-5c8b5d8f6be3%7Cst%3ALANDING_PAGE_HOMES&title_type=LANDING_PAGE_HOMES&allow_override%5B%5D=&s_tag=-i1FRqbo&section_offset=8",
"https://www.airbnb.com/s/United-States/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJCzYy5IS16lQRQrfeQ5K5Oxw&query=United%20States&click_referer=t%3ASEE_ALL%7Csid%3Abbc20157-93f5-4a50-abb8-5c8b5d8f6be3%7Cst%3ALANDING_PAGE_HOMES&title_type=LANDING_PAGE_HOMES&allow_override%5B%5D=&s_tag=-i1FRqbo&section_offset=9",
"https://www.airbnb.com/s/United-States/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJCzYy5IS16lQRQrfeQ5K5Oxw&query=United%20States&click_referer=t%3ASEE_ALL%7Csid%3Abbc20157-93f5-4a50-abb8-5c8b5d8f6be3%7Cst%3ALANDING_PAGE_HOMES&title_type=LANDING_PAGE_HOMES&allow_override%5B%5D=&s_tag=-i1FRqbo&section_offset=10",
"https://www.airbnb.com/s/United-States/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJCzYy5IS16lQRQrfeQ5K5Oxw&query=United%20States&click_referer=t%3ASEE_ALL%7Csid%3Abbc20157-93f5-4a50-abb8-5c8b5d8f6be3%7Cst%3ALANDING_PAGE_HOMES&title_type=LANDING_PAGE_HOMES&allow_override%5B%5D=&s_tag=-i1FRqbo&section_offset=11",
"https://www.airbnb.com/s/United-States/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJCzYy5IS16lQRQrfeQ5K5Oxw&query=United%20States&click_referer=t%3ASEE_ALL%7Csid%3Abbc20157-93f5-4a50-abb8-5c8b5d8f6be3%7Cst%3ALANDING_PAGE_HOMES&title_type=LANDING_PAGE_HOMES&allow_override%5B%5D=&s_tag=-i1FRqbo&section_offset=12",
"https://www.airbnb.com/s/United-States/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJCzYy5IS16lQRQrfeQ5K5Oxw&query=United%20States&click_referer=t%3ASEE_ALL%7Csid%3Abbc20157-93f5-4a50-abb8-5c8b5d8f6be3%7Cst%3ALANDING_PAGE_HOMES&title_type=LANDING_PAGE_HOMES&allow_override%5B%5D=&s_tag=-i1FRqbo&section_offset=13",
"https://www.airbnb.com/s/United-States/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJCzYy5IS16lQRQrfeQ5K5Oxw&query=United%20States&click_referer=t%3ASEE_ALL%7Csid%3Abbc20157-93f5-4a50-abb8-5c8b5d8f6be3%7Cst%3ALANDING_PAGE_HOMES&title_type=LANDING_PAGE_HOMES&allow_override%5B%5D=&s_tag=-i1FRqbo&section_offset=14",
"https://www.airbnb.com/s/United-States/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJCzYy5IS16lQRQrfeQ5K5Oxw&query=United%20States&click_referer=t%3ASEE_ALL%7Csid%3Abbc20157-93f5-4a50-abb8-5c8b5d8f6be3%7Cst%3ALANDING_PAGE_HOMES&title_type=LANDING_PAGE_HOMES&allow_override%5B%5D=&s_tag=-i1FRqbo&section_offset=15",
"https://www.airbnb.com/s/United-States/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJCzYy5IS16lQRQrfeQ5K5Oxw&query=United%20States&click_referer=t%3ASEE_ALL%7Csid%3Abbc20157-93f5-4a50-abb8-5c8b5d8f6be3%7Cst%3ALANDING_PAGE_HOMES&title_type=LANDING_PAGE_HOMES&allow_override%5B%5D=&s_tag=-i1FRqbo&section_offset=16"]

csv_file = open('airbnb.csv', 'w')

writer = csv.writer(csv_file)

writer.writerow(['Name','Location','Hometype','Max_guest','Home_summary','Price','Amenities','Reviewnumber','Reviewstar'])



for url in urls:
	driver.get(url)
	# xpath for all the rooms
	room = driver.find_elements_by_xpath('//div[@class = "_1szwzht"]/a')
	# href attribute to get the url for each room
	rooms = [x.get_attribute("href") for x in room]

	
	# loop through every url in rooms
	for each in rooms:
		try:
			driver.get(each)
			airbnb_dict = {}
			Name = driver.find_element_by_xpath('//div[@itemprop = "name"]').text
			Hometype = driver.find_element_by_xpath('//div[@id = "summary"]//div[@class = "_4efw5a"]//span[@class = "_1hh2h7tb"]/span').text
			Location = driver.find_element_by_xpath('//a[@class = "_1biqilc"]/div[@class = "_ncwphzu"]').text
			summary = driver.find_elements_by_xpath('//div[@class = "_2h22gn"]//div[@class = "_qtix31"]//span[@class = "_fgdupie"]')
			Summary = [x.text for x in summary]
			Max_guest = Summary[0]
			Home_summary = Summary[1:4]
			price = driver.find_element_by_xpath('//div[@class = "_12cv0xt"]//span[@class = "_doc79r"]/span').text
			pernight = driver.find_element_by_xpath('//div[@class = "_12cv0xt"]//span[@class = "_p1g77r"]/span').text
			Price = price + " " + pernight
			amenities = driver.find_elements_by_xpath('//div[@class = "_2h22gn"]//div[@class = "_iq8x9is"]//div[@class = "_qtix31"]//div[@class = "_ncwphzu"]')
			Amenities = [x.text for x in amenities]
			Reviewnumber = driver.find_element_by_xpath('//button[@class = "_ff6jfq"]//span[@class = "_p1g77r"]/span').text
			reviewstar = driver.find_element_by_xpath('//button[@class = "_ff6jfq"]//span[@role = "img"]')
			Reviewstar = reviewstar.get_attribute("aria-label")

			airbnb_dict['Name']=Name
			airbnb_dict['Location']=Location
			airbnb_dict['Hometype']=Hometype
			airbnb_dict['Max_guest']=Max_guest
			airbnb_dict['Home_summary']=Home_summary
			airbnb_dict['Price']=Price
			airbnb_dict['Amenities']=Amenities
			airbnb_dict['Reviewnumber']=Reviewnumber
			airbnb_dict['Reviewstar']=Reviewstar
			writer.writerow(airbnb_dict.values())
			# writer.save()
		except Exception as e:
			print(e)
		


csv_file.close()
driver.close()

		
		# wait_button = WebDriverWait(driver, 10)
		# next_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,
		# 							'//li[@class = "_b8vexar"]//svg[@aria-label = "Next"]')))
		# next_button.click()
	# except Exception as e:
	# 	print(e)
	# 	csv_file.close()
	# 	driver.close	
	# 	break

# driver.get("https://www.airbnb.com/s/United-States/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJCzYy5IS16lQRQrfeQ5K5Oxw&query=United%20States&click_referer=t%3ASEE_ALL%7Csid%3Abb46c3c0-de40-4e3d-aa0a-e078ea80a5c4%7Cst%3ALANDING_PAGE_HOMES&title_type=LANDING_PAGE_HOMES&allow_override%5B%5D=&s_tag=0FWf6hTu")
# xpath for all the rooms
# room = driver.find_elements_by_xpath('//div[@class = "_1szwzht"]/a')
# # href attribute to get the url for each room
# rooms = [x.get_attribute("href") for x in room]

# csv_file = open('airbnb.csv', 'w')

# writer = csv.writer(csv_file)

# writer.writerow(['Name','Location','Hometype','Max_guest','Home_summary','Price','Amenities','Reviewnumber','Reviewstar'])



# index = 0
# while index <= 16:
# 	try:
# 		print('page number' + str(index))
# 		index = index + 1
# 		# xpath for all the rooms
# 		room = driver.find_elements_by_xpath('//div[@class = "_1szwzht"]/a')
# 		# href attribute to get the url for each room
# 		rooms = [x.get_attribute("href") for x in room]

# 		csv_file = open('airbnb.csv', 'w')

# 		writer = csv.writer(csv_file)

# 		writer.writerow(['Name','Location','Hometype','Max_guest','Home_summary','Price','Amenities','Reviewnumber','Reviewstar'])


# 		# loop through every url in rooms
# 		for each in rooms:
# 			driver.get(each)
# 			airbnb_dict = {}
# 			Name = driver.find_element_by_xpath('//div[@itemprop = "name"]').text
# 			Hometype = driver.find_element_by_xpath('//div[@id = "summary"]//div[@class = "_4efw5a"]//span[@class = "_1hh2h7tb"]/span').text
# 			Location = driver.find_element_by_xpath('//a[@class = "_1biqilc"]/div[@class = "_ncwphzu"]').text
# 			summary = driver.find_elements_by_xpath('//div[@class = "_2h22gn"]//div[@class = "_qtix31"]//span[@class = "_fgdupie"]')
# 			Summary = [x.text for x in summary]
# 			Max_guest = Summary[0]
# 			Home_summary = Summary[1:4]
# 			price = driver.find_element_by_xpath('//div[@class = "_12cv0xt"]//span[@class = "_doc79r"]/span').text
# 			pernight = driver.find_element_by_xpath('//div[@class = "_12cv0xt"]//span[@class = "_p1g77r"]/span').text
# 			Price = price + " " + pernight
# 			amenities = driver.find_elements_by_xpath('//div[@class = "_2h22gn"]//div[@class = "_iq8x9is"]//div[@class = "_qtix31"]//div[@class = "_ncwphzu"]')
# 			Amenities = [x.text for x in amenities]
# 			Reviewnumber = driver.find_element_by_xpath('//button[@class = "_ff6jfq"]//span[@class = "_p1g77r"]/span').text
# 			reviewstar = driver.find_element_by_xpath('//button[@class = "_ff6jfq"]//span[@role = "img"]')
# 			Reviewstar = reviewstar.get_attribute("aria-label")

# 			airbnb_dict['Name']=Name
# 			airbnb_dict['Location']=Location
# 			airbnb_dict['Hometype']=Hometype
# 			airbnb_dict['Max_guest']=Max_guest
# 			airbnb_dict['Home_summary']=Home_summary
# 			airbnb_dict['Price']=Price
# 			airbnb_dict['Amenities']=Amenities
# 			airbnb_dict['Reviewnumber']=Reviewnumber
# 			airbnb_dict['Reviewstar']=Reviewstar
# 			writer.writerow(airbnb_dict.values())
# 			# writer.save()
		
# 		wait_button = WebDriverWait(driver, 10)
# 		next_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,
# 									'//li[@class = "_b8vexar"]//svg[@aria-label = "Next"]')))
# 		next_button.click()
# 	except Exception as e:
# 		print(e)
# 		csv_file.close()
# 		driver.close	
# 		break
	

# # csv_file.close()

# # driver.close()

#     # print("-"*50)
#     # print(Name)
#     # print(Hometype)
#     # print(Location)
#     # print(Max_guest)
#     # print(Home_summary)
#     # print(Price)
#     # print(Amenities)
#     # print(Reviewnumber)
#     # print(Reviewstar)