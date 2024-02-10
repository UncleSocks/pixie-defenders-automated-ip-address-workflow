from collections import Counter
from parsers import ip_blacklist


def run_pixie(output_dict):

    def parsed_output(output_dict):
        output = output_dict
        output_list = []
        
        print("""
+==================================================================================================================+
                                                       OUTPUT                                                      
+==================================================================================================================+
        """)

        if output['Keyword Counter'] == 1:

            for entry in output['Output List']:
                #print(entry, end="\n")
                output_list.append(entry)

        elif output['Keyword Counter'] > 1 and output['Keyword List'][0] == "not": 
            output_counter = Counter(output['Output List'])
            output_duplicates = [item for item, count in output_counter.items() if count > (output['Keyword Counter'] - 1)]

            for duplicate in output_duplicates:
                output_list.append(duplicate)

        elif output['Keyword Counter'] > 1 and output['Keyword List'][0] != "not":
            output_uniques = set(output['Output List'])

            for unique in output_uniques:
                output_list.append(unique)

        else:
            print("ERROR! Use the '-h' for information on how to use the tool.")

        for entry in output_list:
            print(entry)

        return blacklist_check(output_list)
    

    def blacklist_check(output_list):

        print("""
+==================================================================================================================+
                                                    BLACKLISTED IPs                                                
+==================================================================================================================+
        """)

        blacklist = ip_blacklist()
        blacklisted_ips_list = []

        for entry in output_list:
            ip_address = entry.split("[")[0]

            if ip_address in blacklist:
                blacklisted_ips_list.append(entry)

        if not blacklisted_ips_list:
            print("No IP address are found in the blacklist.")
        else:
            for blacklisted_ip in blacklisted_ips_list:
                print(blacklisted_ip)

    parsed_output(output_dict)