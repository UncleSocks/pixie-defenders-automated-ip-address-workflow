import csv

def cli_output(output_list, blacklist_list):

    cli_report = """
===================================================================================================
                                                OUTPUT
===================================================================================================

"""
    
    for output in output_list:
        cli_report += f"{output}\n"

    cli_report += """
===================================================================================================
                                                BLACKLIST
===================================================================================================

"""
    
    if blacklist_list:
        for blacklist in blacklist_list:
            cli_report += f"{blacklist}\n"
    
    else:
        cli_report += "No IP address found in the blacklist."

    return print(cli_report)


def csv_ouput(parsed_output_list, parsed_blacklist_list, filename):

    with open(f'./reports/{filename}', 'w', newline='') as csv_export:
        csv_writer = csv.writer(csv_export)
        csv_writer.writerow(['IP ADDRESS', 'COUNTRY', 'ORGANIZATION', 'HOSTNAME'])
        csv_writer.writerows(parsed_output_list)
        csv_writer.writerow([])
        csv_writer.writerow(['BLACKLIST IPs'])
        csv_writer.writerows(parsed_blacklist_list)

    return