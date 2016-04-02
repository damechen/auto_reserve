"""
TODO:
1. check if there is a room available
2. setup email server to send email automatically
"""

import time
# Import smtplib for the actual sending function
import smtplib
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
# Import the email modules we'll need
from email.mime.text import MIMEText

url = 'https://reservations.foreverresorts.com/ReservationCalendar.do?propertyKey=181'
browser = webdriver.Firefox()
browser.get(url)

def sendemail():
	from_addr = 'mr.chenxianming@gmail.com'
	to_addr_list = ['mr.chenxianming@gmail.com', 'hanguiyuan@gmail.com']
	message  = 'From: %s\n' % from_addr
	message += 'To: %s\n' % ','.join(to_addr_list)
	message += 'Subject: %s\n\n' % 'Grand Canyon: ROOM!!'

	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login('mr.chenxianming@gmail.com',
    			 'cXm8809252011')
	problems = server.sendmail(from_addr, to_addr_list, message)
	server.quit()

def makeselection():
	month = browser.find_element_by_xpath(".//a[contains(@onclick, 'jmpto1605')]")
	month.send_keys("\n")
	time.sleep(5) # delays for 5 seconds
	sectionDatesOfStay = browser.find_element_by_id('sectionDatesOfStay')
	containerDatesOfStay = sectionDatesOfStay.find_element_by_id('containerDatesOfStay')
	calCell = containerDatesOfStay.find_element_by_class_name('calCell')
	cal1 = calCell.find_element_by_id('cal1')
	calTable1605 = cal1.find_element_by_id('calTable1605')

	# Select May 28 as the arrival day
	date_28 = calTable1605.find_element_by_id('160528')
	date_28.send_keys("\n")
	time.sleep(5) # delays for 5 seconds

	# Select May 29 as the departure day
	date_29 = calTable1605.find_element_by_id('160529')
	date_29.send_keys("\n")
	time.sleep(5) # delays for 5 seconds

	# Select the adults number
	frmNumAdults = browser.find_element_by_id('frmNumAdults')
	adultNo = Select(frmNumAdults)
	adultNo.select_by_visible_text('2')

	# Check the room status
	time.sleep(5)
	suiteTypes = browser.find_element_by_id('suiteTypes')
	sendemail()

def auto_check(): 
	while True:
		browser.refresh()
		time.sleep(10)
		try:
			makeselection()
		except:
			pass
		time.sleep(30)

auto_check()