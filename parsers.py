import re
import urllib.request


def organization_parser(handler, organization_keyword, ip_list):

    print("Performing keyword parsing...")

    organization_keyword_list = organization_keyword.split(' ')
    output_list = []
    organization_keyword_counter = 0

    if organization_keyword_list[0] == "-":

        for ip in ip_list:
            ip_info = handler.getDetails(ip)

            try:
                country = ip_info.country
            except:
                country = "NONE"

            try:
                organization = ip_info.org.split(' ',1)[1].upper()
            except:
                organization = "NONE"

            try:
                hostname = ip_info.hostname
            except:
                hostname = "NONE"

            ip_output = str(ip_info.ip + "[" + country + ":" + organization + ":" + hostname + "]")
            output_list.append(ip_output)
        
        organization_keyword_counter += 1

    elif organization_keyword_list[0] == "not":

        for keyword in organization_keyword_list[1:]:

            for ip in ip_list:
                ip_info = handler.getDetails(ip)

                try:
                    country = ip_info.country
                except:
                    country = "NONE"  

                try:
                    organization = ip_info.org.split(' ',1)[1].upper()
                    ip_organization = str(ip_info.org.lower())
                except:
                    organization = "NONE"
                    ip_organization = "NONE"

                try:
                    hostname = ip_info.hostname
                except:
                    hostname = "NONE"                    

                if keyword not in ip_organization:
                    ip_output = str(ip_info.ip + "[" + country + ":" + organization + ":" + hostname + "]")
                    output_list.append(ip_output)
            
            organization_keyword_counter += 1
    
    elif organization_keyword_list[0] != "not":

        for keyword in organization_keyword_list[0:]:

            for ip in ip_list:
                ip_info = handler.getDetails(ip)

                try:
                    country = ip_info.country
                except:
                    country = "NONE"

                try:
                    organization = ip_info.org.split(' ',1)[1].upper()
                    ip_organization = str(ip_info.org.lower())
                except:
                    organization = "NONE"
                    ip_organization = "NONE"  

                try:
                    hostname = ip_info.hostname
                except:
                    hostname = "NONE"

                if keyword in ip_organization:
                    ip_output = str(ip_info.ip + "[" + country + ":" + organization + ":" + hostname + "]")
                    output_list.append(ip_output)
            
            organization_keyword_counter += 1
    
    else:
        print("ERROR! Use the '-h' for information on how to use the tool.")

    output_dict = {'Keyword List': organization_keyword_list, 'Keyword Counter':organization_keyword_counter, 'Output List':output_list}
    return output_dict


def public_address_parser(ip_address):
    match = re.compile(r'((^127\.)|(^192\.168\.)|(^10\.)|(^172\.1[6-9]\.)|(^172\.2[0-9]\.)|(^172\.3[0-1]\.)|(^::1$)|(^[fF][cCdD])/)|([a-zA-Z])').match(ip_address)
    if match:
        return True
    else:
        return False
    

def ip_blacklist():

    print("\nUpdating IP address blacklist... ")

    blacklist_url = "https://snort-org-site.s3.amazonaws.com/production/document_files/files/000/028/652/original/ip-filter.blf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAU7AK5ITMJQBJPARJ%2F20240210%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240210T121755Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=93bcc076536d07affb75fe58156d281d86a0b87cba30e4033241397a43c64c1c"

    try:
        get_blacklist = urllib.request.urlopen(blacklist_url).read().decode('utf-8')
        parsed_blacklist = get_blacklist.strip().split("\n")
        print("IP address blacklist updated.\n")
    except:
        print("Failed to update blacklist IP")

    return parsed_blacklist