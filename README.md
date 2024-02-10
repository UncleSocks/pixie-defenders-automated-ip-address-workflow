![Pixie](https://github.com/UncleSocks/pixie-automated-ipinfo-address-lookup/assets/79778613/1a47e09c-6643-4696-8022-a74b9c04e503)

# Pixie: Automated IPInfo Address Lookup
![Static Badge](https://img.shields.io/badge/License%20-%20MIT%20-%20brown) ![Static Badge](https://img.shields.io/badge/Release%20-%202024.2.0%20-%20orange)

A Python 3 script, named after my Mini Pinscher, that automates IP address lookup on IPInfo and displays the output in IPADDRESS[COUNTRY:ORGANIZATION] format. The script accepts IP address organization keyword/s and outputs the addresses matching the keyword/s (it is also capable of negating your searches). 

**NOTE:** You will need to sign up for IPInfo (FREE) to get your access token.

As a SOC Analyst, we are often task to look up the hundreds of IP addresses, provide their country of origin and organization, and verify if the user is connecting to suspicious or unsanctioned addresses. This tool aims to address the slow process of manually inputting hundreds of IP addresses into an OSINT lookup tool, such as IPInfo.

## Usage

Run the `pixie.py` Python3 script on your machine; use the `-i` or `--ip_list` option and specify the file location of the text file containing the list of IP addresses you want to look up. 

Please note that the text file must be in a format that each IP address takes up one line, and no non-IP address content must be present. A samplelist.txt is available in the repository for your reference.

**Example:** `pixie.py -i C:\Users\$Username\Documents\List_of_IP_Addresses.txt`

```
C:\Users\Pixie>pixie.py -i samplelist.txt

=============================================================================================
=============================================================================================
                     _____
               \/_  | Awo |
              ..     -----
           +++xX:  /
          ;;;+XX;                                      ^^
        ++++++++:                   ^^
       :x++;++++.                                                 ^^
          ;++;;::                                 ^^
         .+++;:::              ^^
        .;;;;++;::
       ;+;;;;::;;;:.   ;&&&&&&&&&&&&+ ;&&&&&; x&&&&&&&&+&&&&&&.:&&&&&:
      :++;;;:::;++:;    :&&&&x  $&&&&::&$;     :&&&&&&.&&$     :&$;
      :+;;;;;+;;x+ +;.  X&&&&:  &&&&X:&&&&&:    ;&&&&&&$      :&&&&&:   X&&&&&&:
      +++++xX++XX:  ;;:;&&&&$:$&&&&+.$&&&&+      +&&&&&X      $&&&&+ .$&&X  X&&$
     :;X;;++XXXXx     :+;+&&&&&$X.  .$&&&$      +&&&&&&&;     $&&&$ ;&&&&&&&&&&+
     ;+:   ;;+;++;    X&$+;+.       +&&&&:    x&&+.&&&&&&;   +&&&&: $&&&$
    :+:     :;;xx+  :X&&&&$:      .X&&&&&:;+$&&&: :$&&&&&&;:x&&&&&: X&&&&&$&&X
    .+       .+;+; .X$&&&Xx:      +$&&&$x:X&&&$x. X$&&&$$x;+$&&&$+.  ;X&&$x;
    :;        :;:;.
    ;:            ;;               Automated IP(Info) Lookup
   .;:            .::

    In loving memory of my dog, Pixie.


Created by Tyrone Kevin Ilisan (@unclesocks)
2024.2.0

[+] Automatically queries the IP addresses in the wordlist on IPInfo.
[+] Accepts organization keywords for filtering.
[+] Outputs the results in IPADDRESS[COUNTRY:ORG] format.
[-] Known Issue: Bogon and missing-ASN-addresses will result in an error.

Note: The tool requires the IPInfo token to connection to IPInfo.

=============================================================================================

Enter token: ***************
```

When running the command, the script will ask for your IPInfo access token and your desired IP address organization keyword/s for searching. 

**NOTE:** When pasting the IPInfo token, use the right-click button of your mouse.

### Organization Keyword Search

Use a space to separate multiple keywords (e.g., AMAZON MICROSOFT). The script will look up each IP address in your text file list using the IPInfo API and will only output the addresses that match ANY of the provided organization keywords. In short, the script will show you the list of addresses belonging to the organization/s in your search.

```
Enter organization keyword (e.g., Microsoft): AMAZON MICROSOFT
Processing wordlist...
Performing keyword parsing...
```

### Negating Organization Keyword Search

If you want to negate your search, prepend a `NOT` keyword on your search (e.g., NOT AMAZON MICROSOFT GOOGLE). Similarly, the script will still look up each IP address inside the list using the IPInfo API but will only output the IP address that does not belong to the organization/s in your search.
```
Enter organization keyword (e.g., Microsoft): NOT AMAZON MICROSOFT
Processing wordlist...
Performing keyword parsing...
```

### Lookup All IP Address In The Wordlist
If you want to simply look up all IP addresses in your list, use the `-` key.
```
Enter organization keyword (e.g., Microsoft): -
Processing wordlist...
Performing keyword parsing...
```

### Automated Blacklist Check
Pixie now features an automated blacklist check against the Cisco Talos Intelligence IP Blacklist:
```
https://www.talosintelligence.com/documents/ip-blacklist
```
The IP blacklist is updated every time you run Pixie. If an IP address in your wordlist matches an address in the blacklist, it will be displayed in the BLACKLISTED IPs section in the output.


## Output

The script will display a list of output in IPADDRESS[COUNTRY:ORGANIZAITON] format.
```
                                          OUTPUT
---------------------------------------------------------------------------------------------

136.226.170.4[DE:ZSCALER, INC.]
8.8.4.4[US:GOOGLE LLC]
147.161.132.5[NL:ZSCALER SWITZERLAND GMBH]
13.107.6.153[US:MICROSOFT CORPORATION]
165.225.74.32[DE:ZSCALER SWITZERLAND GMBH]
165.225.72.20[DE:ZSCALER SWITZERLAND GMBH]
204.79.197.215[US:MICROSOFT CORPORATION]
136.226.170.25[DE:ZSCALER, INC.]
52.68.0.1[JP:AMAZON.COM, INC.]
52.68.1.90[JP:AMAZON.COM, INC.]
8.8.8.8[US:GOOGLE LLC]

=============================================================================================
```
