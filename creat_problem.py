import requests
import json
import csv

#payload  = {"description": "Test Problem Ticket", "short_description":"Test Problem Ticket","priority":"2","urgency":"1"} 

def create_problem(payload):
 url = 'https://dev247022.service-now.com/api/now/table/problem'

 headers= { 
     "Accept": "application/json",
     "Content-Type": "application/json"
 } 

# payload = { 
#   "description":"Test Problem Ticket", "short_description":"Test Problem Ticket","priority":2,"urgency":"1"
# }


 res=requests.post(url,auth=("test_integ","1Jcithof!"), headers=headers, data= json.dumps(payload))
 print(res.text)

filename ="CiscoReport.csv"

with open(filename, 'r') as data:
  for line in csv.DictReader(data):
      print(line)
      create_problem(line)


