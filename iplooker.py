import ipinfo
import maskpass
import argparse
from collections import Counter


accessToken = maskpass.askpass("Enter IPInfo Token: ")
handler = ipinfo.getHandler(accessToken)
orgKeyword = input("Enter organization keyword (e.g., Microsoft): ").lower()

negCheck = orgKeyword.split(' ')
print(negCheck)

parser = argparse.ArgumentParser(description="IP address checker for Microsoft and Amazon addresses")
parser.add_argument("-i","--ipList")
args = parser.parse_args()

ipList = []
with open(args.ipList) as list:
    for ip in list:
        ip = ip.strip()
        ipList.append(ip)

listOfList = []
listcount = 0

if negCheck[0] == "-":
    for ip in ipList:
        details = handler.getDetails(ip)
        ipOutput = str(details.ip + "[" + details.country + ":" + details.org.split(' ',1)[1].upper() + "]")
        listOfList.append(ipOutput)
    listcount = listcount + 1        
elif negCheck[0] == "not":
    for check in negCheck[1:]:
        for ip in ipList:
            details = handler.getDetails(ip)
            ipOrg = str(details.org.lower())
            if check not in ipOrg:
                ipOutput = str(details.ip + "[" + details.country + ":" + details.org.split(' ',1)[1].upper() + "]")
                listOfList.append(ipOutput)
        listcount = listcount+1
elif negCheck[0] != "not":
    for check in negCheck[0:]:
        for ip in ipList:
            details = handler.getDetails(ip)
            ipOrg = str(details.org.lower())
            if check in ipOrg:
                ipOutput = str(details.ip + "[" + details.country + ":" + details.org.split(' ',1)[1].upper() + "]")
                listOfList.append(ipOutput)
        listcount = listcount+1
else:
    print("ERROR BOGO")

if listcount == 1:
    for entry in listOfList:
        print(entry, end="\n")
elif listcount > 1 and negCheck[0] == "not": 
    counter = Counter(listOfList)
    string_duplicates = [item for item, count in counter.items() if count > 1]
    for entry in string_duplicates:
        print(entry, end="/n")
elif listcount > 1 and negCheck[0] != "not":
    uniqueValue = set(listOfList)
    print(uniqueValue)
else:
    print("ERROR!")

