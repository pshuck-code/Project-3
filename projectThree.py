file = open('http_access_log.txt','r') #opens log file
count = 0 #counts amount of requests total
sixMonth = 0 #counts requests in past six months

#variables for figuring out requests in the past six months
may = "May"
jun = "Jun"
jul = "Jul"
aug = "Aug"
sep = "Sep"
octo = "Oct"
date = "1995"

#reads file and splits it by line
Content = file.read()
CoList = Content.split('\n')


#for loop that loops through each line of the request 
for lines in CoList:
    if lines:
        #checks for past six months requests
        if may in CoList[count]:
            sixMonth +=1
        if jun in CoList[count]:
            sixMonth +=1
        if jul in CoList[count]:
            sixMonth +=1
        if aug in CoList[count]:
            sixMonth +=1
        if sep in CoList[count]:
            sixMonth +=1
        if octo in CoList[count]:
            if date in CoList[count]:
                sixMonth +=1
    #adds total requests
    count +=1

#outputs both requests
print("There were " + str(count) + " total requests") 
print("There were " + str(sixMonth) + " in the past six months")

#close log file
file.close()