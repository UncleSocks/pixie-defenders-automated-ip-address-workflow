import re
import time
import requests
import json
import csv



def banner():
    
    banner = """
        ____  _      _      
        |  _ \(_)_  _(_) ___ 
        | |_) | \ \/ / |/ _ \\
        |  __/| |>  <| |  __/
        |_|   |_/_/\_\_|\___|lite
        Abuse IP Reputation

    """

    return print(banner)


def public_address_parser(ip_address):
    private_match = re.compile(r'((^127\.)|(^192\.168\.)|(^10\.)|(^172\.1[6-9]\.)|(^172\.2[0-9]\.)|(^172\.3[0-1]\.)|(^::1$)|(^[fF][cCdD])/)|([a-zA-Z])').match(ip_address)
    if private_match:
        return True
    else:
        return False
    

def wordlist_process():
    
    print("Parsing IP wordlist...")
    
    ip_list = []
    with open("ip.txt") as ip_wordlist:
        for ip in ip_wordlist:
            ip = ip.strip()
            if public_address_parser(ip) == False:
                ip_list.append(ip)

    return ip_list


def api_process():
    
    with open("api.txt") as api:
        api_key = api.read().strip()
    
    return api_key


def abuse_ip_lookup(api_key, ip_list):
    print("Performing Abuse IP lookup...")
    processed_ip_list = []
    total_ips = len(ip_list)

    start_time = time.time()
    
    url = 'https://api.abuseipdb.com/api/v2/check'
    headers = {
        'Accept':'application/json',
        'Key':api_key
    }

    for index, ip in enumerate(ip_list, start=1):
        
        querystring = {
            'ipAddress':ip,
            'maxAgeInDays':'30'
        }

        response = requests.request(method='GET', url=url, headers=headers, params=querystring)
        decodedResponse = json.loads(response.text)

        ipAddress = decodedResponse['data']['ipAddress']
        
        try:
            country = decodedResponse['data']['countryCode']
        except:
            country = "NONE"

        try:
            isp = decodedResponse['data']['isp']
        except:
            isp = "NONE"

        abuseScoreRaw = decodedResponse['data']['abuseConfidenceScore']
        abuseScore = str(abuseScoreRaw) + "%"
        totalReports = decodedResponse['data']['totalReports']

        processed_ip = [str(ipAddress), str(country), str(isp), str(abuseScore), str(totalReports)]
        processed_ip_list.append(processed_ip)

        print(f"\rProcessing {index}/{total_ips} IP addresses", end="", flush=True)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nLookup complete. Elapsed time: {elapsed_time:.2f} seconds.\n")

    return processed_ip_list


def csv_output(processed_ip_list):
    
    with open(f'./output.csv', 'w', newline='') as csv_export:
        csv_writer = csv.writer(csv_export)
        csv_writer.writerow(['IP ADDRESS', 'COUNTRY', 'ISP', 'ABUSE SCORE', 'TOTAL REPORTS'])
        csv_writer.writerows(processed_ip_list)

    print("Successfully exported to a CSV file.")

    return


if __name__ == "__main__":

    banner()

    api_key = api_process()
    ip_list = wordlist_process()
    processed_ip_list = abuse_ip_lookup(api_key, ip_list)

    csv_output(processed_ip_list)
    print("Done")
    time.sleep(5)