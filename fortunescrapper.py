import requests
import json
import time
from random import randint

while 1: #Keeps running always
  url="http://dojodevopschallenge.s3-website-eu-west-1.amazonaws.com/fortune_of_the_day.json"
  response=requests.get(url)
  responseJson=json.loads(response.content)
  #Get a random message from the json
  messageID = (randint(1,99))
  currentMessage = responseJson[messageID].get("message")
  print(currentMessage)
  #Writing the message to a html file
  f = open('fortuneMessage.html','w')
  message = """<html><head></head><body><p>"""+ currentMessage +"""!</p></body></html>"""
  f.write(message)
  f.close()
  #To Test File content
  #file = open('fortuneMessage.html','r')
  #for line in file:
  #  print (line)
  time.sleep(10)
