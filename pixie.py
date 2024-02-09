from collections import Counter
from parsers import organization_parser
from init import arguments, ip_wordlist, ip_init, organization_keyword


output = organization_parser(ip_init(), organization_keyword(), ip_wordlist(arguments()))

print("                                      OUTPUT")
print("---------------------------------------------------------------------------------------------\n")

if output['Keyword Counter'] == 1:

    for entry in output['Output List']:
        print(entry, end="\n")

elif output['Keyword Counter'] > 1 and output['Keyword List'][0] == "not": 
    output_counter = Counter(output['Output List'])
    output_duplicates = [item for item, count in output_counter.items() if count > (output['Keyword Counter'] - 1)]

    for duplicate in output_duplicates:
        print(duplicate, end="\n")

elif output['Keyword Counter'] > 1 and output['Keyword List'][0] != "not":
    output_uniques = set(output['Output List'])

    for unique in output_uniques:
        print(unique)

else:
    print("ERROR! Use the '-h' for information on how to use the tool.")

print("\n=============================================================================================")