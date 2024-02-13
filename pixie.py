from parsers import organization_parser, netstat
from output import run_pixie
from init import arguments, ip_wordlist, ip_init, organization_keyword


if __name__ == "__main__":

    if arguments().wordlist and not arguments().netstat:
        output_dict = organization_parser(ip_init(), organization_keyword(), ip_wordlist(arguments()))
        run_pixie(output_dict)

    elif arguments().netstat and not arguments().wordlist:
        output_dict = organization_parser(ip_init(), organization_keyword(), netstat())
        run_pixie(output_dict)

    else:
        print("ERROR-001: Inclusion of both arguments not allowed.")