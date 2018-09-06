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

urls =["https://www.airbnb.com/s/France/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJMVd4MymgVA0R99lHx5Y__Ws&adults=1&children=0&infants=0&query=France&click_referer=t%3ASEE_ALL%7Csid%3Accae9e9d-eb42-4b90-9f6e-a5a33cba5e43%7Cst%3ALANDING_PAGE_MARQUEE&title_type=LANDING_PAGE_MARQUEE&allow_override%5B%5D=&s_tag=tvnQik4w&section_offset=0",
"https://www.airbnb.com/s/France/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJMVd4MymgVA0R99lHx5Y__Ws&adults=1&children=0&infants=0&query=France&click_referer=t%3ASEE_ALL%7Csid%3Accae9e9d-eb42-4b90-9f6e-a5a33cba5e43%7Cst%3ALANDING_PAGE_MARQUEE&title_type=LANDING_PAGE_MARQUEE&allow_override%5B%5D=&s_tag=tvnQik4w&section_offset=1",
"https://www.airbnb.com/s/France/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJMVd4MymgVA0R99lHx5Y__Ws&adults=1&children=0&infants=0&query=France&click_referer=t%3ASEE_ALL%7Csid%3Accae9e9d-eb42-4b90-9f6e-a5a33cba5e43%7Cst%3ALANDING_PAGE_MARQUEE&title_type=LANDING_PAGE_MARQUEE&allow_override%5B%5D=&s_tag=tvnQik4w&section_offset=2",
"https://www.airbnb.com/s/France/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJMVd4MymgVA0R99lHx5Y__Ws&adults=1&children=0&infants=0&query=France&click_referer=t%3ASEE_ALL%7Csid%3Accae9e9d-eb42-4b90-9f6e-a5a33cba5e43%7Cst%3ALANDING_PAGE_MARQUEE&title_type=LANDING_PAGE_MARQUEE&allow_override%5B%5D=&s_tag=tvnQik4w&section_offset=3",
"https://www.airbnb.com/s/France/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJMVd4MymgVA0R99lHx5Y__Ws&adults=1&children=0&infants=0&query=France&click_referer=t%3ASEE_ALL%7Csid%3Accae9e9d-eb42-4b90-9f6e-a5a33cba5e43%7Cst%3ALANDING_PAGE_MARQUEE&title_type=LANDING_PAGE_MARQUEE&allow_override%5B%5D=&s_tag=tvnQik4w&section_offset=4",
"https://www.airbnb.com/s/France/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJMVd4MymgVA0R99lHx5Y__Ws&adults=1&children=0&infants=0&query=France&click_referer=t%3ASEE_ALL%7Csid%3Accae9e9d-eb42-4b90-9f6e-a5a33cba5e43%7Cst%3ALANDING_PAGE_MARQUEE&title_type=LANDING_PAGE_MARQUEE&allow_override%5B%5D=&s_tag=tvnQik4w&section_offset=5",
"https://www.airbnb.com/s/France/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJMVd4MymgVA0R99lHx5Y__Ws&adults=1&children=0&infants=0&query=France&click_referer=t%3ASEE_ALL%7Csid%3Accae9e9d-eb42-4b90-9f6e-a5a33cba5e43%7Cst%3ALANDING_PAGE_MARQUEE&title_type=LANDING_PAGE_MARQUEE&allow_override%5B%5D=&s_tag=tvnQik4w&section_offset=6",
"https://www.airbnb.com/s/France/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJMVd4MymgVA0R99lHx5Y__Ws&adults=1&children=0&infants=0&query=France&click_referer=t%3ASEE_ALL%7Csid%3Accae9e9d-eb42-4b90-9f6e-a5a33cba5e43%7Cst%3ALANDING_PAGE_MARQUEE&title_type=LANDING_PAGE_MARQUEE&allow_override%5B%5D=&s_tag=tvnQik4w&section_offset=7",
"https://www.airbnb.com/s/France/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJMVd4MymgVA0R99lHx5Y__Ws&adults=1&children=0&infants=0&query=France&click_referer=t%3ASEE_ALL%7Csid%3Accae9e9d-eb42-4b90-9f6e-a5a33cba5e43%7Cst%3ALANDING_PAGE_MARQUEE&title_type=LANDING_PAGE_MARQUEE&allow_override%5B%5D=&s_tag=tvnQik4w&section_offset=8",
"https://www.airbnb.com/s/France/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJMVd4MymgVA0R99lHx5Y__Ws&adults=1&children=0&infants=0&query=France&click_referer=t%3ASEE_ALL%7Csid%3Accae9e9d-eb42-4b90-9f6e-a5a33cba5e43%7Cst%3ALANDING_PAGE_MARQUEE&title_type=LANDING_PAGE_MARQUEE&allow_override%5B%5D=&s_tag=tvnQik4w&section_offset=9",
"https://www.airbnb.com/s/France/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJMVd4MymgVA0R99lHx5Y__Ws&adults=1&children=0&infants=0&query=France&click_referer=t%3ASEE_ALL%7Csid%3Accae9e9d-eb42-4b90-9f6e-a5a33cba5e43%7Cst%3ALANDING_PAGE_MARQUEE&title_type=LANDING_PAGE_MARQUEE&allow_override%5B%5D=&s_tag=tvnQik4w&section_offset=10",
"https://www.airbnb.com/s/France/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJMVd4MymgVA0R99lHx5Y__Ws&adults=1&children=0&infants=0&query=France&click_referer=t%3ASEE_ALL%7Csid%3Accae9e9d-eb42-4b90-9f6e-a5a33cba5e43%7Cst%3ALANDING_PAGE_MARQUEE&title_type=LANDING_PAGE_MARQUEE&allow_override%5B%5D=&s_tag=tvnQik4w&section_offset=11",
"https://www.airbnb.com/s/France/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJMVd4MymgVA0R99lHx5Y__Ws&adults=1&children=0&infants=0&query=France&click_referer=t%3ASEE_ALL%7Csid%3Accae9e9d-eb42-4b90-9f6e-a5a33cba5e43%7Cst%3ALANDING_PAGE_MARQUEE&title_type=LANDING_PAGE_MARQUEE&allow_override%5B%5D=&s_tag=tvnQik4w&section_offset=12",
"https://www.airbnb.com/s/France/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJMVd4MymgVA0R99lHx5Y__Ws&adults=1&children=0&infants=0&query=France&click_referer=t%3ASEE_ALL%7Csid%3Accae9e9d-eb42-4b90-9f6e-a5a33cba5e43%7Cst%3ALANDING_PAGE_MARQUEE&title_type=LANDING_PAGE_MARQUEE&allow_override%5B%5D=&s_tag=tvnQik4w&section_offset=13",
"https://www.airbnb.com/s/France/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJMVd4MymgVA0R99lHx5Y__Ws&adults=1&children=0&infants=0&query=France&click_referer=t%3ASEE_ALL%7Csid%3Accae9e9d-eb42-4b90-9f6e-a5a33cba5e43%7Cst%3ALANDING_PAGE_MARQUEE&title_type=LANDING_PAGE_MARQUEE&allow_override%5B%5D=&s_tag=tvnQik4w&section_offset=14",
"https://www.airbnb.com/s/France/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJMVd4MymgVA0R99lHx5Y__Ws&adults=1&children=0&infants=0&query=France&click_referer=t%3ASEE_ALL%7Csid%3Accae9e9d-eb42-4b90-9f6e-a5a33cba5e43%7Cst%3ALANDING_PAGE_MARQUEE&title_type=LANDING_PAGE_MARQUEE&allow_override%5B%5D=&s_tag=tvnQik4w&section_offset=15",
"https://www.airbnb.com/s/France/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJMVd4MymgVA0R99lHx5Y__Ws&adults=1&children=0&infants=0&query=France&click_referer=t%3ASEE_ALL%7Csid%3Accae9e9d-eb42-4b90-9f6e-a5a33cba5e43%7Cst%3ALANDING_PAGE_MARQUEE&title_type=LANDING_PAGE_MARQUEE&allow_override%5B%5D=&s_tag=tvnQik4w&section_offset=16"]

csv_file = open('airbnb_fr.csv', 'w')

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