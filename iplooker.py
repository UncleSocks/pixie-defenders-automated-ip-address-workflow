import ipinfo
import maskpass
import argparse
from collections import Counter

argument_parser = argparse.ArgumentParser(description="IP address checker using IPInfo API. Enter the organization keyword/s for searching, use space as a separator for multiple keywords; prepend the 'NOT' keyword to negate the search. The '-' character will process all IP addresses in the list without any keyword.")
argument_parser.add_argument("-i","--ip_list",help="Specify the location of the text file containing the IP addresses to be processed.")
argument = argument_parser.parse_args()
ip_list = []

with open(argument.ip_list) as ip_wordlist:
    for ip in ip_wordlist:
        ip = ip.strip()
        ip_list.append(ip)

access_token = maskpass.askpass("Enter token: ")
handler = ipinfo.getHandler(access_token)
organization_keyword = input("Enter organization keyword (e.g., Microsoft): ").lower()
organization_keyword_list = organization_keyword.split(' ')

output_list = []
organization_keyword_counter = 0

if organization_keyword_list[0] == "-":

    for ip in ip_list:
        ip_info = handler.getDetails(ip)
        ip_output = str(ip_info.ip + "[" + ip_info.country + ":" + ip_info.org.split(' ',1)[1].upper() + "]")
        output_list.append(ip_output)

    organization_keyword_counter += 1       

elif organization_keyword_list[0] == "not":

    for keyword in organization_keyword_list[1:]:

        for ip in ip_list:
            ip_info = handler.getDetails(ip)
            ip_organization = str(ip_info.org.lower())

            if keyword not in ip_organization:
                ip_output = str(ip_info.ip + "[" + ip_info.country + ":" + ip_info.org.split(' ',1)[1].upper() + "]")
                output_list.append(ip_output)

        organization_keyword_counter += 1

elif organization_keyword_list[0] != "not":

    for keyword in organization_keyword_list[0:]:

        for ip in ip_list:
            ip_info = handler.getDetails(ip)
            ip_organization = str(ip_info.org.lower())
            
            if keyword in ip_organization:
                ip_output = str(ip_info.ip + "[" + ip_info.country + ":" + ip_info.org.split(' ',1)[1].upper() + "]")
                output_list.append(ip_output)
        organization_keyword_counter += 1

else:
    print("ERROR! Use the '-h' for information on how to use the tool.")

if organization_keyword_counter == 1:

    for entry in output_list:
        print(entry, end="\n")

elif organization_keyword_counter > 1 and organization_keyword_list[0] == "not": 
    output_counter = Counter(output_list)
    output_duplicates = [item for item, count in output_counter.items() if count > (organization_keyword_counter - 1)]

    for duplicate in output_duplicates:
        print(duplicate, end="\n")

elif organization_keyword_counter > 1 and organization_keyword_list[0] != "not":
    output_uniques = set(output_list)

    for unique in output_uniques:
        print(unique)

else:
    print("ERROR! Use the '-h' for information on how to use the tool.")
