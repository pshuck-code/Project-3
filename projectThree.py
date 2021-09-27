file = open('http_access_log.txt','r')
count = 0
sixMonth = 0

may = "May"
jun = "Jun"
jul = "Jul"
aug = "Aug"
sep = "Sep"
octo = "Oct"
date = "1995"

Content = file.read()
CoList = Content.split('\n')

for lines in CoList:
    if lines:
        
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

    count +=1

print("There were " + str(count) + " total requests") 
print("There were " + str(sixMonth) + " in the past six months")

file.close()