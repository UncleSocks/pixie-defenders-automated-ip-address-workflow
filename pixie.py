from parsers import organization_parser, netstat
from output import run_pixie
from init import arguments, ip_wordlist, ip_init, organization_keyword


if __name__ == "__main__":

    if arguments().wordlist and not arguments().netstat and not arguments().ioc:
        output_dict = organization_parser(ip_init(), organization_keyword(), ip_wordlist(arguments()))
        blacklist_file = False
        run_pixie(output_dict, blacklist_file)

    elif arguments().netstat and not arguments().wordlist and not arguments().ioc:
        output_dict = organization_parser(ip_init(), organization_keyword(), netstat())
        blacklist_file = False
        run_pixie(output_dict, blacklist_file)

    elif arguments().wordlist and not arguments().netstat and arguments().ioc:
        output_dict = organization_parser(ip_init(), organization_keyword(), ip_wordlist(arguments()))
        blacklist_file = True
        run_pixie(output_dict, blacklist_file)

    elif arguments().netstat and not arguments().wordlist and arguments().ioc:
        output_dict = organization_parser(ip_init(), organization_keyword(), netstat())
        blacklist_file = True
        run_pixie(output_dict, blacklist_file)

    else:
        print("ERROR-001: Specify either the '-w' or '-n' argument; inclusion of both arguments are not allowed. Use the '-h' option for more information.")