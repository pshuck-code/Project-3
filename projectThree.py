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

threeX = 0
fourX = 0
total = 0

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


for line in file:
    total+=1
    try:
        decoded_line = line.decode("utf-8")
        parts = regex.split(decoded_line)
        
        if parts[7] == "300" or parts[7] == "301" or parts[7] == "302" or parts[7] == "303" or parts[7] == "304":
            threeX+=1
        if parts[7] == "400" or parts[7] == "401" or parts[7] == "402" or parts[7] == "403" or parts[7] == "404":
            fourX+=1
    except IndexError:
        print("Index Error Reached")


print("redirects were " + str(round(threeX/total, 2)))
print("unsuccessful were " + str(round(fourX/total,2)))
#print(parts[9])
    


    







