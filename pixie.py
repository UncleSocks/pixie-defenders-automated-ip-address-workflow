from parsers import organization_parser
from output import run_pixie
from init import arguments, ip_wordlist, ip_init, organization_keyword


output_dict = organization_parser(ip_init(), organization_keyword(), ip_wordlist(arguments()))
run_pixie(output_dict)

