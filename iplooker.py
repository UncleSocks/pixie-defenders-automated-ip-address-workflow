import ipinfo
import maskpass
import argparse
from collections import Counter

parser = argparse.ArgumentParser(description="IP address checker using IPInfo API. Enter the organization keyword/s for searching, use space as a separator for multiple keywords; prepend the 'NOT' keyword to negate the search. The '-' character will process all IP addresses in the list without any keyword.")
parser.add_argument("-i","--ipList",help="Specify the location of the text file containing the IP addresses to be processed.")
args = parser.parse_args()
ipList = []
with open(args.ipList) as list:
    for ip in list:
        ip = ip.strip()
        ipList.append(ip)

accessToken = maskpass.askpass("Enter token: ")
handler = ipinfo.getHandler(accessToken)
orgKeyword = input("Enter organization keyword (e.g., Microsoft): ").lower()
keywordList = orgKeyword.split(' ')

output = []
keywordCount = 0

if keywordList[0] == "-":
    for ip in ipList:
        details = handler.getDetails(ip)
        ipOutput = str(details.ip + "[" + details.country + ":" + details.org.split(' ',1)[1].upper() + "]")
        output.append(ipOutput)
    keywordCount = keywordCount + 1        
elif keywordList[0] == "not":
    for keyword in keywordList[1:]:
        for ip in ipList:
            details = handler.getDetails(ip)
            ipOrg = str(details.org.lower())
            if keyword not in ipOrg:
                ipOutput = str(details.ip + "[" + details.country + ":" + details.org.split(' ',1)[1].upper() + "]")
                output.append(ipOutput)
        keywordCount = keywordCount + 1
elif keywordList[0] != "not":
    for keyword in keywordList[0:]:
        for ip in ipList:
            details = handler.getDetails(ip)
            ipOrg = str(details.org.lower())
            if keyword in ipOrg:
                ipOutput = str(details.ip + "[" + details.country + ":" + details.org.split(' ',1)[1].upper() + "]")
                output.append(ipOutput)
        keywordCount = keywordCount + 1
else:
    print("ERROR! Use the '-h' for information on how to use the tool.")


if keywordCount == 1:
    for entry in output:
        print(entry, end="\n")
elif keywordCount > 1 and keywordList[0] == "not": 
    counter = Counter(output)
    duplicates = [item for item, count in counter.items() if count > (keywordCount - 1)]
    for entry in duplicates:
        print(entry, end="\n")
elif keywordCount > 1 and keywordList[0] != "not":
    uniques = set(output)
    for entry in uniques:
        print(entry)
else:
    print("ERROR! Use the '-h' for information on how to use the tool.")
