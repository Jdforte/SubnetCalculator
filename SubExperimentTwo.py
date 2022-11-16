#need a separate program for regular class bound submasks for all private classes

import re


def classAA(ipadd, submask):

    sec_one = "[0-1]{2}[.][0-9]{1}[.][0-9]{1,3}[.][0-9]{1,3}"
    sec_two = "[0-1]{2}[.][0-9]{2}[.][0-9]{1,3}[.][0-9]{1,3}"
    sec_three = "[0-1]{2}[.][0-9]{3}[.][0-9]{1,3}[.][0-9]{1,3}"
    match_one = re.findall(sec_one, ipadd)
    match_two = re.findall(sec_two, ipadd)
    match_three = re.findall(sec_three, ipadd)
    make_list = []
    make_list.append(ipadd)
    broad_add = '.255.255'
    last_add = '.255.254'
    first_add= '.0.1'
    net_add = '.0.0'
    cl = "10."
    blsz_find = 0 
    oct_bound = 0 
    sub_aa = "255.128.0.0"
    sub_ab = "255.192.0.0"
    sub_ac = "255.224.0.0"
    sub_ad = "255.240.0.0"
    sub_ae = "255.248.0.0"
    sub_af = "255.252.0.0"
    sub_ag = "255.254.0.0"
     

    
    if match_one == make_list: 
        blsz_find = int(ipadd[3:4])
    elif match_two == make_list:
        blsz_find = int(ipadd[3:5]) 
    elif match_three == make_list: 
        blsz_find = int(ipadd[3:6])
        
    else:
        print("Please enter a valid ip address and/or submask.")
    if submask == sub_aa:
        oct_bound = 128
    elif submask == sub_ab:
        oct_bound = 64
    elif submask == sub_ac:
        oct_bound = 32
    elif submask == sub_ad:
        oct_bound = 16
    elif submask == sub_ae:
        oct_bound = 8
    elif submask == sub_af:
        oct_bound = 4
    elif submask == sub_ag:
        oct_bound = 2
    else:
        print("Please enter a valid submask")
    
    if blsz_find // oct_bound == 0:
        begin_octet = str(blsz_find // oct_bound)
        end_octet = str((blsz_find // oct_bound) + oct_bound - 1)
        broad_octet = end_octet
    else:
        octet_count = blsz_find // oct_bound + 1
        begin_octet = str(blsz_find // oct_bound * oct_bound)   
        end_octet = str((octet_count * oct_bound) -1)
        broad_octet = end_octet
    
 
    
    print(oct_bound)
    print(submask)       
    print(ipadd + " belongs to a class A private address space ranging from " + cl + begin_octet + first_add + " to " + cl + end_octet + last_add + " with a Network address of " + cl + begin_octet + net_add + " and a broadcast address of " + cl + broad_octet + broad_add +".")


#classAA('10.2.3.4','255.128.0.0')
#classAA('10.234.4.16','255.192.0.0')
#classAA('10.55.12.188','255.224.0.0')
#classAA('10.0.245.34','255.240.0.0')
#classAA('10.240.78.1', '255.248.0.0')
#classAA('10.45.80.90', '255.254.0.0')
#classAA('10.78.90.23', 'not a valid submask')
#classAA('not a valid ip', '255.240.0.0')
