![Pixie](https://github.com/UncleSocks/pixie-automated-ipinfo-address-lookup/assets/79778613/d130d9b8-191e-4199-a22e-dea6c77071b5)

# Pixie: Automated IPInfo Address Lookup
A Python 3 script that automates IP address lookup on IPInfo and displays the output in IPADDRESS[COUNTRY:ORGANIZATION] format. The script accepts IP address organization keyword/s and outputs the addresses matching the keyword/s (it is also capable of negating your searches). 

**NOTE:** You will need to sign up for IPInfo (FREE) to get your access token.

As a SOC Analyst, we are often task to look up the hundreds of IP addresses, provide their country of origin and organization, and verify if the user is connecting to suspicious or unsanctioned addresses. This tool aims to address the slow process of manually inputting hundreds of IP addresses into an OSINT lookup tool, such as IPInfo.

## Usage

Run the `pixie.py` Python3 script on your machine; use the `-i` or `--ip_list` option and specify the file location of the text file containing the list of IP addresses you want to look up. Please note that the text file must be in a format that each IP address takes up one line, and no non-IP address content must be present. A samplelist.txt is available in the repository for your reference.

**Example:** `pixie.py -i C:\Users\$Username\Documents\List_of_IP_Addresses.txt`


When running the command, the script will ask for your IPInfo access token and your desired IP address organization keyword/s for searching. 

**NOTE:** When pasting the IPInfo token, use the right-click button of your mouse.

Use a space to separate multiple keywords (e.g., AMAZON MICROSOFT GOOGLE). The script will look up each IP address in your text file list using the IPInfo API and will only output the addresses that match ANY of the provided organization keywords. In short, the script will show you the list of addresses belonging to the organization/s in your search.


If you want to negate your search, prepend a `NOT` keyword on your search (e.g., NOT AMAZON MICROSOFT GOOGLE). Similarly, the script will still look up each IP address inside the list using the IPInfo API but will only output the IP address that does not belong to the organization/s in your search.


If you want to simply look up all IP addresses in your list, use the `-` key.


## Output

The script will display the result in IPADDRESS[COUNTRY:ORGANIZAITON] format. 
