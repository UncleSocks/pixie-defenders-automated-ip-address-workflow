from parser_modules.parsers import ipinfo_lookup, xforce_lookup, organization_parser, netstat
from parser_modules.stager import staged_output, blacklist_check, export_parser, export_blacklist_parser
from init import arguments, ip_wordlist, ip_init, xforce_init, organization_keyword
from output import cli_output, csv_ouput


if __name__ == "__main__":

    if arguments().source == "i" or arguments().source is None: #Use IPInfo as OSINT source.
        handler = ip_init()
        organization_keywords = organization_keyword()
        if arguments().wordlist and not arguments().netstat and not arguments().ioc:
            ip_list = ip_wordlist(arguments())
            processed_ip_list = ipinfo_lookup(handler, ip_list)
            output_dict = organization_parser(processed_ip_list, organization_keywords)
            output_list = staged_output(output_dict)

            blacklist_file = False
            blacklist = blacklist_check(output_list, blacklist_file)
            cli_output(output_list, blacklist)

        elif arguments().netstat and not arguments().wordlist and not arguments().ioc:
            ip_list =  netstat()
            processed_ip_list = ipinfo_lookup(handler, ip_list)
            output_dict = organization_parser(processed_ip_list, organization_keywords)
            output_list = staged_output(output_dict)
            
            blacklist_file = False
            blacklist = blacklist_check(output_list, blacklist_file)
            cli_output(output_list, blacklist)

        elif arguments().wordlist and not arguments().netstat and arguments().ioc:
            ip_list = ip_wordlist(arguments())
            processed_ip_list = ipinfo_lookup(handler, ip_list)
            output_dict = organization_parser(processed_ip_list, organization_keywords)
            output_list = staged_output(output_dict)

            blacklist_file = True
            blacklist = blacklist_check(output_list, blacklist_file)
            cli_output(output_list, blacklist)

        elif arguments().netstat and not arguments().wordlist and arguments().ioc:
            ip_list =  netstat()
            processed_ip_list = ipinfo_lookup(handler, ip_list)
            output_dict = organization_parser(processed_ip_list, organization_keywords)
            output_list = staged_output(output_dict)

            blacklist_file = True
            blacklist = blacklist_check(output_list, blacklist_file)
            cli_output(output_list, blacklist)

        else:
            print("ERROR-001: Specify either the '-w' or '-n' argument; inclusion of both arguments are not allowed. Use the '-h' option for more information.")

        if arguments().output:

            print("Exporting to a CSV file...")
            parsed_output_list = export_parser(output_list)
            parsed_blacklist_list = export_blacklist_parser(blacklist)

            print(f"CSV file exported as {arguments().output}")
            csv_ouput(parsed_output_list, parsed_blacklist_list, arguments().output)


    elif arguments().source == "x": #Use IBM X-Force as OSINT source.

        api_url, api_key, api_pw = xforce_init()
        organization_keywords = organization_keyword()       
        
        if arguments().wordlist and not arguments().netstat and not arguments().ioc:
            ip_list = ip_wordlist(arguments())
            processed_ip_list = xforce_lookup(api_url, api_key, api_pw, ip_list)

            output_dict = organization_parser(processed_ip_list, organization_keywords)
            output_list = staged_output(output_dict)

            blacklist_file = False
            blacklist = blacklist_check(output_list, blacklist_file)
            cli_output(output_list, blacklist)

        elif arguments().netstat and not arguments().wordlist and not arguments().ioc:
            ip_list = netstat()
            processed_ip_list = xforce_lookup(api_url, api_key, api_pw, ip_list)

            output_dict = organization_parser(processed_ip_list, organization_keywords)
            output_list = staged_output(output_dict)

            blacklist_file = False
            blacklist = blacklist_check(output_list, blacklist_file)
            cli_output(output_list, blacklist)

        elif arguments().wordlist and not arguments().netstat and arguments().ioc:

            ip_list = ip_wordlist(arguments())
            processed_ip_list = xforce_lookup(api_url, api_key, api_pw, ip_list)

            output_dict = organization_parser(processed_ip_list, organization_keywords)
            output_list = staged_output(output_dict)

            blacklist_file = True
            blacklist = blacklist_check(output_list, blacklist_file)
            cli_output(output_list, blacklist)

        elif arguments().netstat and not arguments().wordlist and arguments().ioc:
            ip_list = netstat()
            processed_ip_list = xforce_lookup(api_url, api_key, api_pw, ip_list)

            output_dict = organization_parser(processed_ip_list, organization_keywords)
            output_list = staged_output(output_dict)

            blacklist_file = True
            blacklist = blacklist_check(output_list, blacklist_file)
            cli_output(output_list, blacklist)

        else:
            print("ERROR-001: Specify either the '-w' or '-n' argument; inclusion of both arguments are not allowed. Use the '-h' option for more information.")

        
        if arguments().output:

            print("Exporting to a CSV file...")
            parsed_output_list = export_parser(output_list)
            parsed_blacklist_list = export_blacklist_parser(blacklist)

            print(f"CSV file exported as {arguments().output}")
            csv_ouput(parsed_output_list, parsed_blacklist_list, arguments().output)

    else:
        print("ERROR-005: Invalid source argument. Use the '-h' option for more information.")

