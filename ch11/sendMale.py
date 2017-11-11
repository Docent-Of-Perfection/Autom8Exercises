#!/usr/bin/env python3
#This script will paste into the body of an email
from selenium import webdriver
import re, argparse, sys, time, pyperclip
from info import myEmail, myPass

parser = argparse.ArgumentParser()
parser.add_argument("-r","--recipient", help="who to send the email message to")
parser.add_argument("-s","--subject", help="email subject line (optional)")
args = parser.parse_args()

emailRegex = re.compile(r'\w+@\w+\.\w')
if args.recipient:
	if emailRegex.search(args.recipient):
		print("email valid")
	else:
		print("ruh roh")
		sys.exit()
else:
	print("Please provide a valid email address to send to")
	response = input()
	if emailRegex.search(response):
		args.recipient = response
		print(args.recipient + " is the value of args.recipient")
	else:
		print("Really?")
		sys.exit()


#https://www.guru99.com/xpath-selenium.html
#Wow, google is tricky with the dynamically generated classes and such
firefox = webdriver.Firefox()
firefox.get("http://gmail.com")
firefox.find_element_by_id('identifierId').send_keys(myEmail)
firefox.find_element_by_id('identifierNext').click()
time.sleep(2)
firefox.find_element_by_css_selector('#password input').send_keys(myPass)
firefox.find_element_by_id('passwordNext').click()
time.sleep(2)
firefox.find_element_by_xpath("//*[contains(text(), 'COMPOSE')]").click()
time.sleep(1)
firefox.find_element_by_xpath("//*[@name='to']").send_keys(args.recipient)
time.sleep(1)
if args.subject:
	firefox.find_element_by_xpath("//*[@name='subjectbox']").send_keys(args.subject)
firefox.find_element_by_css_selector("#\:ma").click()
time.sleep(1)
firefox.find_element_by_css_selector("#\:ma").send_keys(pyperclip.paste())
