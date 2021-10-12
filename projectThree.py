import re
import urllib.request
import calendar

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

#for request couting
threeX = 0
fourX = 0
total = 0

#variables for figuring out requests in the past six months
jan = 0
feb = 0
mar = 0
may = 0
apr = 0
jun = 0
jul = 0
aug = 0
sep = 0
octo = 0
nov = 0
dec = 0

month = 0

#reads file and splits it by line
#Content = file.read()
#CoList = Content.split('\n')


for line in file:
    total+=1
    try:
        decoded_line = line.decode("utf-8")
        parts = regex.split(decoded_line)
        
        #print(parts[1])
        #print(parts[2])
        #print(parts[3])
        #print(parts[4])

        if parts[2] == "Aug":
            aug+=1
            month = 8
        if parts[2] == "Sep":
            sep+=1
            month = 9
        if parts[2] == "Oct":
            octo+=1
            month = 10
        if parts[2] == "Nov":
            nov+=1
            month = 11
        if parts[2] == "Dec":
            dec+=1
            month = 12
        if parts[2] == "Jan":
            jan+=1
            month = 1
        if parts[2] == "Feb":
            feb+=1
            month = 2
        if parts[2] == "Mar":
            mar+=1
            month = 3
        if parts[2] == "Apr":
            apr+=1
            month = 4
        if parts[2] == "May":
            may+=1
            month = 5
        if parts[2] == "Jun":
            jun+=1
            month = 6
        if parts[2] == "Jul":
            jul+=1
            month = 7

        if calendar.weekday(int(parts[3]),month,int(parts[1])) == 0:
            mon+=1
        if calendar.weekday(int(parts[3]),month,int(parts[1])) == 1:
            tues+=1
        if calendar.weekday(int(parts[3]),month,int(parts[1])) == 2:
            wed+=1
        if calendar.weekday(int(parts[3]),month,int(parts[1])) == 3:
            thurs+=1
        if calendar.weekday(int(parts[3]),month,int(parts[1])) == 4:
            fri+=1
        if calendar.weekday(int(parts[3]),month,int(parts[1])) == 5:
            sat+=1
        if calendar.weekday(int(parts[3]),month,int(parts[1])) == 6:
            sun+=1

        month = 0
        #for 3xx and 4xx requests
        if parts[7] == "300" or parts[7] == "301" or parts[7] == "302" or parts[7] == "303" or parts[7] == "304":
            threeX+=1
        if parts[7] == "400" or parts[7] == "401" or parts[7] == "402" or parts[7] == "403" or parts[7] == "404":
            fourX+=1
    except IndexError:
        print("Index Error Reached")

print("")
print("redirects were " + str(round(threeX/total, 2)))
print("unsuccessful were " + str(round(fourX/total,2)))
print("")
print("monday: " + str(mon))
print("tuesday: " + str(tues))
print("wednesday: " + str(wed))
print("thursday: " + str(thurs))
print("friday: " + str(fri))
print("saturday: " + str(sat))
print("sunday: " + str(sun))
print("")
print("requests in august: " + str(aug))
print("requests in september: " + str(sep))
print("requests in october: " + str(octo))
print("requests in november: " + str(nov))
print("requests in december: " + str(dec))
print("requests in january: " + str(jan))
print("requests in february: " + str(feb))
print("requests in march: " + str(mar))
print("requests in april: " + str(apr))
print("requests in may: " + str(may))
print("requests in june: " + str(jun))
print("requests in july: " + str(jul))
print("total requests: " + str(total))


    







