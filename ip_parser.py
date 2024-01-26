import ipinfo
import re


def organization_parser(handler, organization_keyword, ip_list):

    print("Performing keyword parsing...")

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

    output_dict = {'Keyword List': organization_keyword_list, 'Keyword Counter':organization_keyword_counter, 'Output List':output_list}
    return output_dict


def public_address_parser(ip_address):
    match = re.compile(r'((^127\.)|(^192\.168\.)|(^10\.)|(^172\.1[6-9]\.)|(^172\.2[0-9]\.)|(^172\.3[0-1]\.)|(^::1$)|(^[fF][cCdD])/)|([a-zA-Z])').match(ip_address)
    if match:
        return True
    else:
        return False