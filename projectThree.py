import re
import urllib.request

count = 0 #counts amount of requests total
sixMonth = 0 #counts requests in past six months

regex = re.compile('\[(\d{2})/([A-Za-z]{3,4})/(\d{4}):(\d{2}:\d{2}:\d{2}).+\] \"([A-Z]{3,6}) (.+) HTTP/1.0\" (\d{3}) .*')

url = "https://s3.amazonaws.com/tcmg476/http_access_log"
file = urllib.request.urlopen(url)
print(str(file.getcode()))
#variables for amount of access requests each day
mon = 0
tues = 0
wed = 0
thurs = 0
fri = 0
sat = 0
sun = 0

#variables for figuring out requests in the past six months
may = "May"
jun = "Jun"
jul = "Jul"
aug = "Aug"
sep = "Sep"
octo = "Oct"
date = "1995"

#reads file and splits it by line
#Content = file.read()
#CoList = Content.split('\n')




#for loop that loops through each line of the request 
#for lines in CoList:
 #   if lines:
        #checks for past six months requests
     #   if may in CoList[count]:
    #        sixMonth +=1
   #     if jun in CoList[count]:
  #          sixMonth +=1
      #  if jul in CoList[count]:
     #       sixMonth +=1
    #    if aug in CoList[count]:
   #         sixMonth +=1
  #      if sep in CoList[count]:
        #    sixMonth +=1
       # if octo in CoList[count]:
      #      if date in CoList[count]:
     #           sixMonth +=1
    #adds total requests
    #count +=1

#outputs both requests
#print("There were " + str(count) + " total requests") 
#print("There were " + str(sixMonth) + " in the past six months")

