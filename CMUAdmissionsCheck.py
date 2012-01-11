#! /usr/bin/env python
# Sumukh Sridhara - SumukhSridhara.com - You may use this for non profit/personal users. All I request is that you leave the credit in here. 

from time import sleep
import urllib, urllib2
import smtplib
import string
import smtplib

from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders

#CHANGE THESE VARIABLES, 
admissionID = "1234567"
lastName = "MyLastName"
birthdate = "01/01/1900"
update_interval=60 #in seconds, it will take 1 minute for the first run. You can change it to be as frequent as you want. Make sure you give it at least 10-45 seconds between requests
gmail_user = 'YOUR_GMAIL_Username@gmail.com'
gmail_pwd = 'YOUR GMAIL PASSWORD'
gmail_to = 'email@email.com'

#Don't alter anything below this line.
def mail(to, subject, text):
	msg = MIMEMultipart()
	msg['From'] = gmail_user
	msg['To'] = gmail_to
	msg['Subject'] = subject
	msg.attach(MIMEText(text))

	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(gmail_user, gmail_pwd)
	server.sendmail(gmail_user, to, msg.as_string())
	server.close()
	print ("Sent off an email:",subject)
	
if __name__ == "__main__":
  old_html = ""
  while not sleep(update_interval):
    try:
      post_values = urllib.urlencode({"VAR1":admissionID, "VAR2":lastName, "VAR3":birthdate})
      request = urllib2.urlopen('https://www.as.cmu.edu/application/display.formproc?FUNCNAME=now_enrolling&ARGNUM=3',post_values)
      html = request.read()
      if html != old_html and old_html != "":
        print "Online App Changed: YES"   
        mail(gmail_user, "CMU Status Change", "Your status has changed on the CMU site. https://www.as.cmu.edu/application//display.html )
        old_html = html
      elif old_html == "": 
      	print "First Time Checking"
       # for debugging purposes.
       # print html
       # mail(gmail_user, "First Check", "The script has started. <br> Direct Link: https://www.as.cmu.edu/application//display.html")
      	old_html = html
      else:
      	print "Online App Changed: NO"
      	old_html = html
    except:
      print 'Error! Retrying now.'


