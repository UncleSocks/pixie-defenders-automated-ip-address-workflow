from parser_modules.parsers import ip_address_search_engine, netstat
from parser_modules.stager import staged_output, blacklist_check, export_parser, export_blacklist_parser
from init import arguments, ip_wordlist, ip_init, organization_keyword
from output import cli_output, csv_ouput


if __name__ == "__main__":

    if arguments().wordlist and not arguments().netstat and not arguments().ioc:
        output_dict = ip_address_search_engine(ip_init(), organization_keyword(), ip_wordlist(arguments()))
        blacklist_file = False

        output_list = staged_output(output_dict)
        blacklist = blacklist_check(output_list, blacklist_file)
        cli_output(output_list, blacklist)

        if arguments().output:

            print("Exporting to a CSV file...")
            parsed_output_list = export_parser(output_list)
            parsed_blacklist_list = export_blacklist_parser(blacklist)

            print(f"CSV file exported as {arguments().output}")
            csv_ouput(parsed_output_list, parsed_blacklist_list, arguments().output)


    elif arguments().netstat and not arguments().wordlist and not arguments().ioc:
        output_dict = ip_address_search_engine(ip_init(), organization_keyword(), netstat())
        blacklist_file = False
        
        output_list = staged_output(output_dict)
        blacklist = blacklist_check(output_list, blacklist_file)
        cli_output(output_list, blacklist)

        if arguments().output:

            print("Exporting to a CSV file...")
            parsed_output_list = export_parser(output_list)
            parsed_blacklist_list = export_blacklist_parser(blacklist)

            print(f"CSV file exported as {arguments().output}")
            csv_ouput(parsed_output_list, parsed_blacklist_list, arguments().output)

    elif arguments().wordlist and not arguments().netstat and arguments().ioc:
        output_dict = ip_address_search_engine(ip_init(), organization_keyword(), ip_wordlist(arguments()))
        blacklist_file = True
        
        output_list = staged_output(output_dict)
        blacklist = blacklist_check(output_list, blacklist_file)
        cli_output(output_list, blacklist)

        if arguments().output:

            print("Exporting to a CSV file...")
            parsed_output_list = export_parser(output_list)
            parsed_blacklist_list = export_blacklist_parser(blacklist)

            print(f"CSV file exported as {arguments().output}")
            csv_ouput(parsed_output_list, parsed_blacklist_list, arguments().output)

    elif arguments().netstat and not arguments().wordlist and arguments().ioc:
        output_dict = ip_address_search_engine(ip_init(), organization_keyword(), netstat())
        blacklist_file = True

        output_list = staged_output(output_dict)
        blacklist = blacklist_check(output_list, blacklist_file)
        cli_output(output_list, blacklist)

        if arguments().output:

            print("Exporting to a CSV file...")
            parsed_output_list = export_parser(output_list)
            parsed_blacklist_list = export_blacklist_parser(blacklist)

            print(f"CSV file exported as {arguments().output}")
            csv_ouput(parsed_output_list, parsed_blacklist_list, arguments().output)

    else:
        print("ERROR-001: Specify either the '-w' or '-n' argument; inclusion of both arguments are not allowed. Use the '-h' option for more information.")